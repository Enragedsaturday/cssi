#!/usr/bin/env python3
"""
S4 · R10 — regenerate `Case Index.md` from case-page frontmatter.

Single source of truth = `content/cases/*.md` frontmatter. This builds the
Case-Index table:

  | Case | Holding | Good law | Home page(s) | CourtListener |

  - Case          [[<title>]] wikilink to the case page
  - Holding       the `holding:` one-line ratio (frontmatter)
  - Good law      treatment.status -> glyph+label (NO blank cells, N13)
  - Home page(s)  the homes[].page links joined by " · "
  - CourtListener [opinion](<courtlistener.opinion_url>)

The 3 flagged caption exception rows (self-help; Cruz/West/Jackson trio;
stolen-vehicle White) are carried forward from the existing index verbatim
(no wikilink; flag note kept) so they never vanish; their previously-blank
Good-law cell is set to "⚠ unverifiable" to satisfy N13/LINT-6.

The human header prose + `type: index` frontmatter above the table are
preserved byte-for-byte (everything before the `| Case |` header). Rows are
sorted alphabetically by case name. Output is idempotent: re-running yields a
byte-identical file.

Stdlib only.  Usage: python3 scripts/build_case_index.py [--check]
  --check : regenerate to a temp string and diff against the on-disk file;
            exit 1 if they differ (does not write).
"""

import glob
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.normpath(os.path.join(HERE, ".."))
sys.path.insert(0, os.path.join(HERE, "lint"))
import _common as c  # noqa: E402

INDEX = os.path.join(REPO, "content", "2-legal-system-research", "Case Index.md")
CASES_GLOB = os.path.join(REPO, "content", "cases", "*.md")

TABLE_HEADER = "| Case | Holding | Good law | Home page(s) | CourtListener |"
TABLE_SEP = "|---|---|---|---|---|"
HEADER_RE = re.compile(r"^\|\s*Case\s*\|")

STATUS_LABEL = {
    "good": "good",
    "criticized": "⚠ criticized",
    "limited": "⚠ limited",
    "abrogated": "⚠ abrogated",
    "overruled": "⛔ overruled",
}
FLAG_LABEL = "⚠ unverifiable"


def sortkey(name):
    k = (name or "").strip().lower().replace("’", "'")
    k = re.sub(r"^[^a-z0-9]+", "", k)   # ignore leading quotes/italics/punct
    k = re.sub(r"\s+", " ", k)
    return k


def read_holding(text):
    """The holding is stored json-encoded; decode it losslessly."""
    for ln in text.split("\n")[1:]:
        if ln.strip() == "---":
            break
        m = re.match(r"^holding:\s*(.*\S)\s*$", ln)
        if m:
            try:
                return json.loads(m.group(1))
            except ValueError:
                return m.group(1)
    return ""


def page_rows():
    rows = []
    for p in sorted(glob.glob(CASES_GLOB)):
        text = c.read_text(p)
        fm, _body, _ = c.split_frontmatter(text)
        title = fm.get("title") or os.path.splitext(os.path.basename(p))[0]
        holding = read_holding(text)
        status = (c.fm_get(fm, "treatment", "status") or "").strip().lower()
        good = STATUS_LABEL.get(status, status or "good")
        homes = fm.get("homes") or []
        pages = [h.get("page", "").strip() for h in homes
                 if isinstance(h, dict) and h.get("page")]
        home = " · ".join(pages)
        opinion = c.fm_get(fm, "courtlistener", "opinion_url") or ""
        cl = "[opinion](%s)" % opinion if opinion else "—"
        case = "[[%s]]" % title
        rows.append((sortkey(title),
                     [case, holding, good, home, cl]))
    return rows


def flagged_rows(existing_lines):
    """Carry forward flagged caption rows from the current table verbatim,
    forcing a non-blank Good-law cell (N13)."""
    out = []
    for ln in existing_lines:
        if not ln.startswith("|") or ln.startswith("|---") or HEADER_RE.match(ln):
            continue
        cells = [x.strip() for x in ln.split("|")[1:-1]]
        if len(cells) != 5:
            continue
        case = cells[0]
        if "UNVERIFIABLE" not in case and "UNCONFIRMED" not in case:
            continue
        name = case.strip().strip("*").strip()
        out.append((sortkey(name),
                    [case, cells[1], FLAG_LABEL, cells[3], cells[4]]))
    return out


def build():
    lines = c.read_text(INDEX).split("\n")
    # preamble = everything before the table header row
    hdr_idx = next((i for i, ln in enumerate(lines) if HEADER_RE.match(ln)),
                   None)
    if hdr_idx is None:
        raise RuntimeError("table header not found in Case Index.md")
    preamble = lines[:hdr_idx]

    rows = page_rows() + flagged_rows(lines)
    rows.sort(key=lambda r: r[0])

    body = [TABLE_HEADER, TABLE_SEP]
    for _key, cells in rows:
        body.append("| %s | %s | %s | %s | %s |" % tuple(cells))

    return "\n".join(preamble + body) + "\n", len(rows), \
        sum(1 for _k, cells in rows if cells[2] == FLAG_LABEL)


def main():
    out, nrows, nflag = build()
    if "--check" in sys.argv[1:]:
        cur = c.read_text(INDEX) if os.path.exists(INDEX) else ""
        if cur == out:
            print("OK: regenerated output is byte-identical (idempotent).")
            sys.exit(0)
        print("DIFF: regenerated output differs from on-disk file.")
        sys.exit(1)
    with open(INDEX, "w", encoding="utf-8") as fh:
        fh.write(out)
    blanks = sum(1 for ln in out.split("\n")
                 if ln.startswith("|") and not ln.startswith("|---")
                 and not HEADER_RE.match(ln)
                 and len(ln.split("|")) == 7
                 and ln.split("|")[3].strip() == "")
    print("wrote %s" % os.path.relpath(INDEX, REPO))
    print("rows: %d  (linked: %d, flagged: %d)" % (nrows, nrows - nflag, nflag))
    print("blank Good-law cells: %d" % blanks)


if __name__ == "__main__":
    main()
