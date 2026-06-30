#!/usr/bin/env python3
"""
LINT-6 — treatment status presence.   Enforces S1 N13 + D3.

Two checks:
  (a) Every case page (frontmatter type: case) must carry a non-blank
      treatment.status AND a non-blank treatment.as_of (S4 Appendix B,
      N13/SR-1). Missing either = HIGH. (Pre-overhaul there are zero case
      pages, so this branch reports nothing until S5 generates them.)
  (b) Every Case-Index row must carry a non-blank treatment cell. The Case
      Index is detected by frontmatter type: index (or filename "Case Index"),
      and its treatment column by a header matching Treatment / Good law /
      Status. A blank treatment cell = MEDIUM (the current index uses a
      "blank == presumed good" convention, which N13 disallows).

Usage: python3 lint6_treatment_status.py [glob ...]
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _common as c  # noqa: E402

LINT = "LINT-6"

TREATMENT_HEADER_RE = re.compile(
    r"\b(treatment|good\s*law|good-law|status)\b", re.IGNORECASE)


def _is_case_index(fm, path):
    if fm.get("type") == "index":
        return True
    stem = os.path.splitext(os.path.basename(path))[0].lower()
    title = (fm.get("title") or "").lower() if isinstance(fm.get("title"), str) \
        else ""
    return stem == "case index" or title == "case index"


def _check_case_page(path, fm, start, out):
    status = c.fm_get(fm, "treatment", "status")
    as_of = c.fm_get(fm, "treatment", "as_of")
    if not status or (isinstance(status, str) and not status.strip()):
        out.append(c.make_violation(
            LINT, path, start, c.HIGH,
            "case page missing non-blank treatment.status [N13]"))
    if not as_of or (isinstance(as_of, str) and not str(as_of).strip()):
        out.append(c.make_violation(
            LINT, path, start, c.HIGH,
            "case page missing treatment.as_of check date [N13]"))


def _check_case_index(path, body, start, out):
    body_lines = body.split("\n")
    n = len(body_lines)
    i = 0
    while i < n:
        line = body_lines[i]
        if "|" in line and i + 1 < n and re.match(
                r"^\s*\|?[\s:|\-]+\|?\s*$", body_lines[i + 1]):
            header = [x.strip() for x in line.strip().strip("|").split("|")]
            tidx = None
            for k, h in enumerate(header):
                if TREATMENT_HEADER_RE.search(h):
                    tidx = k
                    break
            j = i + 2
            while j < n and "|" in body_lines[j] and body_lines[j].strip():
                if tidx is not None:
                    cells = [x.strip() for x in
                             body_lines[j].strip().strip("|").split("|")]
                    cell = cells[tidx] if tidx < len(cells) else ""
                    if not cell:
                        out.append(c.make_violation(
                            LINT, path, start + j, c.MEDIUM,
                            "Case-Index row has a blank treatment cell "
                            "[N13/D3]"))
                j += 1
            i = j
        else:
            i += 1


def check_file(path):
    out = []
    text = c.read_text(path)
    fm, body, start = c.split_frontmatter(text)
    if fm.get("type") == "case":
        _check_case_page(path, fm, start, out)
    if _is_case_index(fm, path):
        _check_case_index(path, body, start, out)
    return out


def run(paths=None):
    out = []
    for path in c.iter_markdown_files(paths):
        out.extend(check_file(path))
    return out


if __name__ == "__main__":
    c.cli_main(run, LINT)
