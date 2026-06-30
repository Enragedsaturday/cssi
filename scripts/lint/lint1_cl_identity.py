#!/usr/bin/env python3
"""
LINT-1 — CourtListener URL identity check.   Enforces S1 L3 + D7.

############################################################################
#  RUN ONLY THROUGH THE SINGLE SERIAL CL LANE AT THE GATE.                  #
#  NEVER run this in parallel, and never alongside any other CL caller (L4).#
#  ALL CourtListener traffic in the project is concurrency-1, always.       #
#  This file is WRITE-ONLY in the lint-authoring unit: it is built here but  #
#  executed later, exactly once, by the serial CL lane at the publish gate.  #
############################################################################

What it does
------------
For every CourtListener reference in the corpus it confirms BOTH halves of L3:
  1. the URL/opinion id RESOLVES (HTTP 200), and
  2. the returned record displays the NAMED case (identity, not just status) —
     i.e. cluster-id != opinion-id; a 200 alone is never enough.

References checked:
  - case-page frontmatter  courtlistener.opinion_url + courtlistener.opinion_id
    (paired with the page `title` as the expected case name), and
  - any CourtListener opinion URL appearing in prose/tables (paired with the
    nearest party-v-party case name on the same line, when present).

Discipline (L4)
---------------
  - Uses the no-auth public REST API:  /api/rest/v4/opinions/<id>/  and the
    linked cluster for the canonical case name.
  - SERIAL pacing: sleeps MIN_INTERVAL_SECONDS between every call so the rate
    stays well under 20/min (default 15/min). Honors STOP-on-5/min-tier:
    if the tier regresses, RUNBOOK §3 STOP-and-notify governs — raise the
    interval or stop; never parallelize to "catch up".
  - Checkpointable: resumable via a JSON ledger so a long run can resume.

It is importable (functions below) and has a CLI, but the CLI REFUSES to make
any network call unless the operator passes the explicit serial-lane
confirmation flag --i-am-the-serial-cl-lane. Importing this module performs no
I/O. Do NOT execute it from the lint-authoring unit.
"""

import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _common as c  # noqa: E402

LINT = "LINT-1"

API_BASE = "https://www.courtlistener.com/api/rest/v4"
USER_AGENT = "CSSI-LINT-1/1.0 (serial CL lane; +https://courtlistener.com)"

# --- serial pacing (L4) ---------------------------------------------------
MAX_CALLS_PER_MIN = 15            # target rate; keep well under 20/min
MIN_INTERVAL_SECONDS = 60.0 / MAX_CALLS_PER_MIN
REQUEST_TIMEOUT = 30


# --------------------------------------------------------------------------
# reference collection (no network)
# --------------------------------------------------------------------------

def collect_references(paths=None):
    """Return a list of reference dicts to verify:
       {file, line, opinion_id, url, expected_name, source}
    `source` is 'frontmatter' or 'prose'. No network I/O here."""
    refs = []
    for path in c.iter_markdown_files(paths):
        text = c.read_text(path)
        fm, body, start = c.split_frontmatter(text)

        if fm.get("type") == "case":
            oid = c.fm_get(fm, "courtlistener", "opinion_id")
            url = c.fm_get(fm, "courtlistener", "opinion_url")
            title = fm.get("title") if isinstance(fm.get("title"), str) else ""
            if oid or url:
                if not oid and url:
                    m = c.CL_OPINION_URL_RE.search(str(url))
                    oid = int(m.group(1)) if m else None
                refs.append({
                    "file": c.relpath(path), "line": 1,
                    "opinion_id": int(oid) if oid else None,
                    "url": url or "",
                    "expected_name": title,
                    "source": "frontmatter",
                })

        body_lines = body.split("\n")
        fenced = c.fenced_line_numbers(body_lines)
        for i, line in enumerate(body_lines):
            if i in fenced:
                continue
            for m in c.CL_OPINION_URL_RE.finditer(line):
                oid = int(m.group(1))
                nm = c.CASE_RE.search(c.mask_links_and_code(line))
                refs.append({
                    "file": c.relpath(path), "line": start + i,
                    "opinion_id": oid, "url": m.group(0),
                    "expected_name": nm.group(0) if nm else "",
                    "source": "prose",
                })
    return refs


# --------------------------------------------------------------------------
# CL fetch (network — serial lane only)
# --------------------------------------------------------------------------

def _get_json(url):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT,
                                               "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=REQUEST_TIMEOUT) as resp:
        return resp.getcode(), json.loads(resp.read().decode("utf-8"))


def _name_tokens(name):
    """Significant party tokens for fuzzy identity matching (drops reporter
    cites, years, punctuation, and common stopwords)."""
    name = re.sub(r"\d.*$", "", name)            # drop trailing cite/year
    name = name.replace("’", "'")
    toks = re.findall(r"[A-Za-z]{3,}", name.lower())
    stop = {"the", "and", "for", "united", "states", "city", "county",
            "people", "commonwealth", "state", "ex", "rel"}
    return [t for t in toks if t not in stop]


def verify_reference(ref):
    """Verify a single reference (one or two CL calls). Returns a violation
    dict on failure, or None on success. MUST be called only from the serial
    lane (it makes live HTTP calls)."""
    oid = ref.get("opinion_id")
    if not oid:
        return c.make_violation(
            LINT, ref["file"], ref["line"], c.HIGH,
            "CL reference has no resolvable opinion id: %s [L3]"
            % (ref.get("url") or "<none>"))
    try:
        code, op = _get_json("%s/opinions/%d/" % (API_BASE, oid))
    except urllib.error.HTTPError as e:
        return c.make_violation(
            LINT, ref["file"], ref["line"], c.HIGH,
            "CL opinion %d did not resolve (HTTP %d) [L3]" % (oid, e.code))
    except Exception as e:  # noqa: BLE001 - network/parse errors are failures
        return c.make_violation(
            LINT, ref["file"], ref["line"], c.HIGH,
            "CL opinion %d fetch error: %s [L3]" % (oid, e))
    if code != 200:
        return c.make_violation(
            LINT, ref["file"], ref["line"], c.HIGH,
            "CL opinion %d returned HTTP %d [L3]" % (oid, code))

    # identity: resolve cluster -> canonical case name (cluster-id != opinion-id)
    case_name = ""
    cluster_url = op.get("cluster")
    if cluster_url:
        time.sleep(MIN_INTERVAL_SECONDS)   # serial pacing between calls (L4)
        try:
            ccode, cl = _get_json(cluster_url)
            if ccode == 200:
                case_name = (cl.get("case_name") or cl.get("case_name_full")
                             or cl.get("case_name_short") or "")
        except Exception:  # noqa: BLE001
            case_name = ""

    expected = ref.get("expected_name") or ""
    if not expected:
        return None  # resolved 200; no expected name to identity-check against
    want = _name_tokens(expected)
    have = set(_name_tokens(case_name)) if case_name else set()
    matched = [t for t in want if t in have]
    if want and not matched:
        return c.make_violation(
            LINT, ref["file"], ref["line"], c.HIGH,
            "CL identity mismatch for opinion %d: expected '%s' but cluster "
            "names '%s' (cluster-id != opinion-id?) [L3]"
            % (oid, expected, case_name))
    return None


def run(paths=None, ledger_path=None, confirmed=False):
    """Run the full identity sweep. SERIAL ONLY. Refuses to make network calls
    unless `confirmed=True` (set by the CLI serial-lane flag). Returns the list
    of violations."""
    refs = collect_references(paths)
    if not confirmed:
        raise RuntimeError(
            "LINT-1 is serial-CL-gate-only. Refusing to make CL calls without "
            "explicit serial-lane confirmation (pass confirmed=True / "
            "--i-am-the-serial-cl-lane). Collected %d references." % len(refs))

    done = {}
    if ledger_path and os.path.exists(ledger_path):
        with open(ledger_path, "r", encoding="utf-8") as fh:
            done = json.load(fh)

    violations = []
    for n, ref in enumerate(refs):
        key = "%s::%s::%s" % (ref["file"], ref["line"], ref.get("opinion_id"))
        if key in done:
            if done[key]:
                violations.append(done[key])
            continue
        v = verify_reference(ref)
        done[key] = v
        if v:
            violations.append(v)
        if ledger_path:
            with open(ledger_path, "w", encoding="utf-8") as fh:
                json.dump(done, fh)
        if n + 1 < len(refs):
            time.sleep(MIN_INTERVAL_SECONDS)   # serial pacing (L4)
    return violations


def main():
    args = sys.argv[1:]
    confirmed = "--i-am-the-serial-cl-lane" in args
    paths = [a for a in args if not a.startswith("-")] or None
    ledger = None
    for a in args:
        if a.startswith("--ledger="):
            ledger = a.split("=", 1)[1]

    if not confirmed:
        refs = collect_references(paths)
        sys.stderr.write(
            "LINT-1 is WRITE-ONLY / serial-CL-gate-only. NOT running.\n"
            "RUN ONLY THROUGH THE SINGLE SERIAL CL LANE AT THE GATE (L4).\n"
            "Collected %d CL reference(s) that WOULD be verified.\n"
            "To actually run (serial lane only): "
            "python3 lint1_cl_identity.py --i-am-the-serial-cl-lane "
            "[--ledger=cl-ledger.json] [glob ...]\n" % len(refs))
        sys.exit(2)

    violations = run(paths, ledger_path=ledger, confirmed=True)
    c.emit(violations)
    sys.exit(c.exit_code_for(violations))


if __name__ == "__main__":
    main()
