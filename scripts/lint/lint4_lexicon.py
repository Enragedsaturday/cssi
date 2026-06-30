#!/usr/bin/env python3
"""
LINT-4 — authority-weight lexicon.   Enforces S1 N2 + D6.

The only permitted authority labels site-wide are the six S1 §3.D tiers:
   1. Binding — SCOTUS
   2. Binding in-circuit
   3. Persuasive (outside circuit)
   4. Persuasive — state, illustrative
   5. Persuasive only — non-precedential
   6. Historical

Checks:
  (a) The banned phrase "persuasive, not binding" (and kindred: "persuasive
      but not binding", "not binding but persuasive") — flagged HIGH.
  (b) Weight cells in a Key-cases / authority table (a column headed
      Weight / Authority / Precedential...) that are not one of the six tiers
      — flagged MEDIUM.
  (c) A weight label that mentions "circuit" generically without naming the
      circuit (no ordinal / named circuit) — flagged MEDIUM (N2: circuit cases
      name the circuit).

Note: detecting every free-text weight assertion is not deterministic; this
lint targets (a) the banned phrase anywhere, and (b/c) the structured weight
cells in tables. Free-prose weight framing is the reviewer's job (CHECKLIST:D6).

Usage: python3 lint4_lexicon.py [glob ...]
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _common as c  # noqa: E402

LINT = "LINT-4"

# banned phrasings (N2)
BANNED_RE = re.compile(
    r"persuasive\s*,?\s*(?:but\s+)?not\s+binding"
    r"|not\s+binding\s*,?\s*(?:but\s+)?persuasive", re.IGNORECASE)


def _norm_tier(s):
    """Normalize a weight label for tier comparison: lowercase, all dash
    variants -> '-', collapse whitespace, strip emphasis/parens-spacing."""
    t = s.strip().lower()
    t = re.sub(r"[\*_`]", "", t)
    t = t.replace("—", "-").replace("–", "-").replace("‐", "-")
    t = re.sub(r"\s*-\s*", " - ", t)
    t = re.sub(r"\s+", " ", t).strip()
    return t


CANONICAL_TIERS = {
    _norm_tier("Binding — SCOTUS"),
    _norm_tier("Binding in-circuit"),
    _norm_tier("Persuasive (outside circuit)"),
    _norm_tier("Persuasive — state, illustrative"),
    _norm_tier("Persuasive only — non-precedential"),
    _norm_tier("Historical"),
}

WEIGHT_HEADER_RE = re.compile(
    r"\b(weight|authority|precedential|binding)\b", re.IGNORECASE)

CIRCUIT_NAMED_RE = re.compile(
    r"\b(?:1st|2nd|3rd|4th|5th|6th|7th|8th|9th|10th|11th|"
    r"first|second|third|fourth|fifth|sixth|seventh|eighth|ninth|tenth|"
    r"eleventh|d\.?c\.?|federal|fed\.?)\b", re.IGNORECASE)


def _table_rows(body_lines, start):
    """Yield (lineno, cells, header_cells) for GFM table data rows, pairing
    each data row with the header row of its table."""
    i = 0
    n = len(body_lines)
    while i < n:
        line = body_lines[i]
        if "|" in line and i + 1 < n and re.match(
                r"^\s*\|?[\s:|\-]+\|?\s*$", body_lines[i + 1]):
            header = [x.strip() for x in line.strip().strip("|").split("|")]
            j = i + 2
            while j < n and "|" in body_lines[j] and body_lines[j].strip():
                cells = [x.strip() for x in
                         body_lines[j].strip().strip("|").split("|")]
                yield start + j, cells, header
                j += 1
            i = j
        else:
            i += 1


def check_file(path):
    out = []
    text = c.read_text(path)
    fm, body, start = c.split_frontmatter(text)
    body_lines = body.split("\n")
    fenced = c.fenced_line_numbers(body_lines)

    # (a) banned phrase anywhere (skip code fences)
    for i, line in enumerate(body_lines):
        if i in fenced:
            continue
        if BANNED_RE.search(line):
            out.append(c.make_violation(
                LINT, path, start + i, c.HIGH,
                "banned authority phrasing 'persuasive, not binding' — use a "
                "six-tier label (e.g. 'Persuasive (outside circuit)') [N2]"))

    # (b)/(c) weight cells in tables
    for lineno, cells, header in _table_rows(body_lines, start):
        widx = None
        for k, h in enumerate(header):
            if WEIGHT_HEADER_RE.search(h):
                widx = k
                break
        if widx is None or widx >= len(cells):
            continue
        cell = cells[widx]
        if not cell or set(cell) <= set("-: "):
            continue
        norm = _norm_tier(cell)
        if norm not in CANONICAL_TIERS:
            out.append(c.make_violation(
                LINT, path, lineno, c.MEDIUM,
                "authority-weight label '%s' is not one of the six S1 tiers "
                "[N2]" % cell))
        # circuit naming: a binding/in-circuit label must name the circuit
        if "circuit" in norm and not CIRCUIT_NAMED_RE.search(cell):
            out.append(c.make_violation(
                LINT, path, lineno, c.MEDIUM,
                "circuit authority label '%s' does not name the circuit "
                "[N2]" % cell))
    return out


def run(paths=None):
    out = []
    for path in c.iter_markdown_files(paths):
        out.extend(check_file(path))
    return out


if __name__ == "__main__":
    c.cli_main(run, LINT)
