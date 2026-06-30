#!/usr/bin/env python3
"""
LINT-8 — guardrails.   Enforces S1 D6.

Three deterministic guardrails:
  (a) The apocryphal Holiday / McCall / Smith training "trio" must never be
      asserted. The REAL United States v. Smith (5th Cir. 2024 geofence case)
      is legitimate and is NOT flagged — only the apocryphal pattern is. The
      tell-tale of the fabricated trio is its other two members (Holiday and
      McCall) appearing as cases; a page that names a "Holiday" case AND a
      "McCall" case is flagged HIGH. (A bare "Smith" is never flagged.)
  (b) Mnemonics carry no citation: a mnemonic line (or a few lines around a
      "mnemonic" cue) that contains a reporter cite or a CourtListener link is
      flagged MEDIUM (a mnemonic is a teaching device, not a holding).
  (c) No inline "## Flashcards" heading on any page (decks live in the deck
      pipeline, never inline) — flagged HIGH.

Usage: python3 lint8_guardrails.py [glob ...]
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _common as c  # noqa: E402

LINT = "LINT-8"

# apocryphal-trio party markers (case-name patterns), excluding the real Smith
HOLIDAY_CASE_RE = re.compile(
    r"\b(?:v\.\s*Holiday|Holiday\s+v\.)", re.IGNORECASE)
MCCALL_CASE_RE = re.compile(
    r"\b(?:v\.\s*McCall|McCall\s+v\.)", re.IGNORECASE)

MNEMONIC_CUE_RE = re.compile(r"\bmnemonic", re.IGNORECASE)
FLASHCARDS_HEADING_RE = re.compile(r"^#{1,6}\s*flashcards\b", re.IGNORECASE)


def check_file(path):
    out = []
    text = c.read_text(path)
    fm, body, start = c.split_frontmatter(text)
    body_lines = body.split("\n")
    fenced = c.fenced_line_numbers(body_lines)

    # (a) apocryphal trio: Holiday + McCall both present as cases on a page
    holiday_line = None
    mccall_line = None
    for i, line in enumerate(body_lines):
        if i in fenced:
            continue
        if holiday_line is None and HOLIDAY_CASE_RE.search(line):
            holiday_line = start + i
        if mccall_line is None and MCCALL_CASE_RE.search(line):
            mccall_line = start + i
    if holiday_line is not None and mccall_line is not None:
        out.append(c.make_violation(
            LINT, path, min(holiday_line, mccall_line), c.HIGH,
            "apocryphal Holiday/McCall(/Smith) case trio asserted "
            "(Holiday@%d, McCall@%d) — fabricated cases [D6]"
            % (holiday_line, mccall_line)))

    # (b)/(c) per-line checks
    for i, line in enumerate(body_lines):
        if i in fenced:
            continue
        lineno = start + i

        if FLASHCARDS_HEADING_RE.match(line.strip()):
            out.append(c.make_violation(
                LINT, path, lineno, c.HIGH,
                "inline '## Flashcards' heading — decks are generated, never "
                "inline [D6]"))

        if MNEMONIC_CUE_RE.search(line):
            lo, hi = i, min(len(body_lines), i + 3)
            window = " ".join(body_lines[lo:hi])
            if c.REPORTER_RE.search(window) or c.CL_ANY_URL_RE.search(window):
                out.append(c.make_violation(
                    LINT, path, lineno, c.MEDIUM,
                    "mnemonic appears with a citation/CL link nearby — "
                    "mnemonics carry no citation [D6]"))
    return out


def run(paths=None):
    out = []
    for path in c.iter_markdown_files(paths):
        out.extend(check_file(path))
    return out


if __name__ == "__main__":
    c.cli_main(run, LINT)
