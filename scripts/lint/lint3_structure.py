#!/usr/bin/env python3
"""
LINT-3 — doctrine-page structure.   Enforces S1 N5/N8/D10.

On every doctrine page (frontmatter type: doctrine) checks:
  (a) Section-order presence — a brief-first ordering: an opening brief/rule
      section, then Key cases, Recent developments, and Sources apparatus
      (S1 §3.I). Missing/mis-ordered sections are flagged LOW (the pre-overhaul
      corpus uses slightly different headings; informational).
  (b) NO SCOTUS case in a "Recent developments" section (N5) — flagged HIGH.
      A SCOTUS *case* is detected by a U.S./S.Ct. reporter cite (or an explicit
      "(SCOTUS)"/"U.S. Supreme Court" tag) appearing on a case-name line within
      the Recent-developments section. Passing references to "the Supreme Court"
      with no case cite do NOT trigger (avoids false positives).
  (c) A single controlling amendment in frontmatter (D10) — flagged LOW when
      absent or when more than one distinct amendment is named (pre-overhaul
      pages carry the amendment inside `jurisdiction:`, not a dedicated field).

Usage: python3 lint3_structure.py [glob ...]
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _common as c  # noqa: E402

LINT = "LINT-3"

# tolerant matching of the canonical section roles (substring on the slug)
BRIEF_HINTS = ("rule", "the-brief", "brief", "overview", "black-letter")
KEYCASES_HINTS = ("key-cases", "key-case")
RECENTDEV_HINTS = ("recent-development", "recent-dev")
SOURCES_HINTS = ("sources", "source")

AMENDMENT_TOKEN_RE = re.compile(
    r"\bamend(?:ment)?s?\.?\s*"
    r"((?:[IVXLC]+|\d+)(?:\s*[&/,]\s*(?:[IVXLC]+|\d+))*)", re.IGNORECASE)
# also catch ordinal-word amendments ("Fourth Amendment", "Fifth and Fourteenth")
ORDINAL_AMEND_RE = re.compile(
    r"\b(First|Second|Third|Fourth|Fifth|Sixth|Seventh|Eighth|Ninth|Tenth|"
    r"Eleventh|Twelfth|Thirteenth|Fourteenth)\s+Amendment", re.IGNORECASE)

SCOTUS_TAG_RE = re.compile(r"\(\s*SCOTUS\s*\)|U\.?\s?S\.?\s+Supreme\s+Court|"
                           r"\bSCOTUS\b", re.IGNORECASE)


def _amendments_in(text):
    found = set()
    for m in AMENDMENT_TOKEN_RE.finditer(text or ""):
        for tok in re.split(r"[&/,]", m.group(1)):
            tok = tok.strip()
            if tok:
                found.add(tok.upper())
    for m in ORDINAL_AMEND_RE.finditer(text or ""):
        found.add(m.group(1).capitalize())
    return found


def _has_any(slug, hints):
    return any(h in slug for h in hints)


def check_file(path):
    out = []
    text = c.read_text(path)
    fm, body, start = c.split_frontmatter(text)
    if fm.get("type") != "doctrine":
        return out
    body_lines = body.split("\n")
    secs = c.sections(body_lines)

    # (a) section-order presence
    slugs = [s["slug"] for s in secs]
    if secs:
        first = slugs[0]
        if not _has_any(first, BRIEF_HINTS):
            # brief-first violated only if first section is apparatus
            if _has_any(first, KEYCASES_HINTS) or _has_any(first, RECENTDEV_HINTS):
                out.append(c.make_violation(
                    LINT, path, start + secs[0]["start"], c.LOW,
                    "brief-first violated: first section is '%s' (the teaching "
                    "brief should lead) [N8]" % secs[0]["title"]))
    for label, hints in (("Key cases", KEYCASES_HINTS),
                         ("Sources", SOURCES_HINTS)):
        if not any(_has_any(s, hints) for s in slugs):
            out.append(c.make_violation(
                LINT, path, start, c.LOW,
                "missing expected '%s' section [N8/D10]" % label))

    # (b) no SCOTUS case in Recent developments.
    # Inspect only the window right AFTER the entry's FIRST case name (its own
    # court parenthetical/cite), so a passing cite to a SCOTUS case deeper in a
    # CIRCUIT entry's description is not mistaken for a SCOTUS placement.
    fenced = c.fenced_line_numbers(body_lines)
    for s in secs:
        if not _has_any(s["slug"], RECENTDEV_HINTS):
            continue
        for i in range(s["start"] + 1, s["end"]):
            if i in fenced:
                continue
            line = body_lines[i]
            m = c.CASE_RE.search(line)
            if not m:
                continue
            window = line[m.end():m.end() + 45]
            has_us = bool(c.US_REPORTER_RE.search(window)
                          or c.SCT_REPORTER_RE.search(window))
            has_tag = bool(SCOTUS_TAG_RE.search(window))
            if has_us or has_tag:
                cue = "U.S./S.Ct. reporter cite" if has_us else "SCOTUS tag"
                out.append(c.make_violation(
                    LINT, path, start + i, c.HIGH,
                    "SCOTUS case '%s' in 'Recent developments' (%s) — SCOTUS "
                    "holdings belong in Key cases [N5]"
                    % (m.group(0).strip()[:50], cue)))

    # (c) single controlling amendment in frontmatter
    fm_amend_field = (fm.get("amendment") or fm.get("controlling_amendment")
                      or fm.get("jurisdiction") or "")
    amendments = _amendments_in(fm_amend_field if isinstance(fm_amend_field, str)
                                else str(fm_amend_field))
    if not amendments:
        out.append(c.make_violation(
            LINT, path, start, c.LOW,
            "no controlling amendment found in frontmatter [D10]"))
    elif len(amendments) > 1 and not (fm.get("amendment")
                                      or fm.get("controlling_amendment")):
        out.append(c.make_violation(
            LINT, path, start, c.LOW,
            "multiple amendments named in frontmatter %s; declare a single "
            "controlling amendment [D10]" % sorted(amendments)))
    return out


def run(paths=None):
    out = []
    for path in c.iter_markdown_files(paths):
        out.extend(check_file(path))
    return out


if __name__ == "__main__":
    c.cli_main(run, LINT)
