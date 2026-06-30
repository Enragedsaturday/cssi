#!/usr/bin/env python3
"""
LINT-7-AUTO — glossary wiring (the automatable half).  Enforces S1 N11 + D13.

This is the deterministic subset of S7·R10 (a–d):
  (a) [[Common Legal Terms#x]] anchor targets resolve.
  (b) [[Reading and Citing Cases#x]] anchor targets resolve (the current
      corpus page is "Legal Research and Case Citations"; both names are
      accepted as the citing-cases glossary until the S2 rename).
  (c) No glossary term is linked more than once per page (link the first
      occurrence only) — the 2nd+ link to the same glossary anchor on a page
      is flagged LOW.

NOT automatable (CHECKLIST-only — S1 §9): novel-term discovery (is every
non-vernacular term wired at all?) and definition accuracy. This lint only
verifies the wiring that already exists; it does not judge coverage or meaning.

Usage: python3 lint7_glossary.py [glob ...]
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _common as c  # noqa: E402

LINT = "LINT-7"

# the glossary pages this lint audits (normalized names)
GLOSSARY_NAMES = {
    "common legal terms",
    "reading and citing cases",
    "legal research and case citations",
}


def _is_glossary_target(page):
    return c.CorpusIndex.norm(page) in GLOSSARY_NAMES


def check_file(path, idx):
    out = []
    text = c.read_text(path)
    fm, body, start = c.split_frontmatter(text)
    body_lines = body.split("\n")
    fenced = c.fenced_line_numbers(body_lines)
    seen_targets = {}   # (stem, anchor) -> first lineno

    for i, line in enumerate(body_lines):
        if i in fenced:
            continue
        lineno = start + i
        for m in c.WIKILINK_RE.finditer(line):
            inner = m.group(1).strip().split("|", 1)[0].strip()
            page, _, anchor = inner.partition("#")
            page = page.strip()
            anchor = anchor.strip()
            if not _is_glossary_target(page):
                continue
            stem = idx.resolve(page)
            # (a)/(b) anchor resolution
            if anchor:
                if stem is None or not idx.has_anchor(stem, anchor):
                    out.append(c.make_violation(
                        LINT, path, lineno, c.MEDIUM,
                        "glossary anchor does not resolve: [[%s#%s]] [N11/D13]"
                        % (page, anchor)))
            # (c) term linked more than once per page
            key = (c.CorpusIndex.norm(page), anchor.lower())
            if key in seen_targets:
                out.append(c.make_violation(
                    LINT, path, lineno, c.LOW,
                    "glossary term linked more than once on this page "
                    "(first at line %d): [[%s%s]] [N11]" % (
                        seen_targets[key], page,
                        "#" + anchor if anchor else "")))
            else:
                seen_targets[key] = lineno
    return out


def run(paths=None):
    idx = c.build_corpus_index()
    out = []
    for path in c.iter_markdown_files(paths):
        out.extend(check_file(path, idx))
    return out


if __name__ == "__main__":
    c.cli_main(run, LINT)
