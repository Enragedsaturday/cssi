#!/usr/bin/env python3
"""
LINT-5 — link every named case + wikilink resolution.  Enforces S1 N7 + D13.

Two checks, using a page+anchor index built from the WHOLE corpus (so
resolution is correct even when this lint is scoped to a subset of files):

  (a) Bare case names: any party-v-party case name (e.g. "Foo v. Bar") in
      prose/tables that is NOT wrapped in a [[wikilink]] is flagged MEDIUM
      (it should link to its case page). Names inside [[...]] or code are
      ignored. A Markdown link to CourtListener does NOT satisfy N7 (the case
      must wikilink to its case PAGE), so CL link text is still bare.
  (b) Wikilink resolution: every [[Page]] / [[Page#anchor]] / [[Page#^block]]
      target must resolve to an existing page (broken page target = HIGH) and,
      where an anchor is given, the anchor must exist on that page (broken
      anchor = MEDIUM).

Usage: python3 lint5_link_every_case.py [glob ...]
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _common as c  # noqa: E402

LINT = "LINT-5"

# words that, as a left "party", indicate this is NOT a case (defensive)
_NON_CASE_LEFT = {"see", "cf", "e.g", "id", "compare", "accord", "but"}


def check_file(path, idx):
    out = []
    text = c.read_text(path)
    fm, body, start = c.split_frontmatter(text)
    body_lines = body.split("\n")
    fenced = c.fenced_line_numbers(body_lines)
    this_stem = os.path.splitext(os.path.basename(path))[0]

    for i, line in enumerate(body_lines):
        if i in fenced:
            continue
        lineno = start + i

        # (b) wikilink resolution
        for m in c.WIKILINK_RE.finditer(line):
            inner = m.group(1).strip()
            inner = inner.split("|", 1)[0].strip()      # drop |display
            page, _, anchor = inner.partition("#")
            page = page.strip()
            anchor = anchor.strip()
            if page == "":
                # same-page anchor [[#anchor]]
                if anchor and not idx.has_anchor(this_stem, anchor):
                    out.append(c.make_violation(
                        LINT, path, lineno, c.MEDIUM,
                        "broken same-page anchor [[#%s]] [D13]" % anchor))
                continue
            stem = idx.resolve(page)
            if stem is None:
                out.append(c.make_violation(
                    LINT, path, lineno, c.HIGH,
                    "broken wikilink: [[%s]] does not resolve to a page "
                    "[N7/D13]" % page))
                continue
            if anchor and not idx.has_anchor(stem, anchor):
                out.append(c.make_violation(
                    LINT, path, lineno, c.MEDIUM,
                    "broken anchor: [[%s#%s]] — anchor not found on target "
                    "[N7/D13]" % (page, anchor)))

        # (a) bare case names (mask out wikilinks + code so linked names skip)
        masked = c.mask_links_and_code(line)
        for m in c.CASE_RE.finditer(masked):
            left = m.group(1).strip()
            if left.lower().rstrip(".") in _NON_CASE_LEFT:
                continue
            name = m.group(0).strip()
            out.append(c.make_violation(
                LINT, path, lineno, c.MEDIUM,
                "bare case name '%s' is not a [[wikilink]] to its case page "
                "[N7/D13]" % (name[:80])))
    return out


def run(paths=None):
    idx = c.build_corpus_index()
    out = []
    for path in c.iter_markdown_files(paths):
        out.extend(check_file(path, idx))
    return out


if __name__ == "__main__":
    c.cli_main(run, LINT)
