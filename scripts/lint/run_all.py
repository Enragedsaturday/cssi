#!/usr/bin/env python3
"""
Runner for the NON-CL CSSI lints (LINT-2,3,4,5,6,7,8) over content/.

LINT-1 (CourtListener identity) is DELIBERATELY EXCLUDED here: it touches the
network and must run only through the single serial CL lane at the publish gate
(S1 L4). This runner never makes a CL call.

Prints each lint's JSON-line violations (unless --quiet) and a per-lint summary
table. Exits non-zero if any lint reports a high-severity violation.

Usage:
  python3 run_all.py [glob ...]      # scope to a subset (default: all content)
  python3 run_all.py --quiet         # summary only, no per-violation JSON
  python3 run_all.py --summary-json  # emit the summary as one JSON object too
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _common as c  # noqa: E402

import lint2_quote_pinpoint as l2  # noqa: E402
import lint3_structure as l3       # noqa: E402
import lint4_lexicon as l4         # noqa: E402
import lint5_link_every_case as l5  # noqa: E402
import lint6_treatment_status as l6  # noqa: E402
import lint7_glossary as l7        # noqa: E402
import lint8_guardrails as l8      # noqa: E402

LINTS = [
    ("LINT-2", "quote/pinpoint (L1)", l2.run),
    ("LINT-3", "structure / no-SCOTUS-in-recent-dev (N5/N8)", l3.run),
    ("LINT-4", "authority lexicon (N2)", l4.run),
    ("LINT-5", "link-every-case + wikilink resolution (N7)", l5.run),
    ("LINT-6", "treatment-status presence (N13)", l6.run),
    ("LINT-7", "glossary wiring (N11, auto half)", l7.run),
    ("LINT-8", "guardrails (D6)", l8.run),
]


def main():
    args = sys.argv[1:]
    quiet = "--quiet" in args
    summary_json = "--summary-json" in args
    paths = [a for a in args if not a.startswith("-")] or None

    rows = []
    total_high = 0
    for name, desc, run_fn in LINTS:
        violations = run_fn(paths)
        if not quiet:
            c.emit(violations)
        n_high = sum(1 for v in violations if v["severity"] == c.HIGH)
        n_med = sum(1 for v in violations if v["severity"] == c.MEDIUM)
        n_low = sum(1 for v in violations if v["severity"] == c.LOW)
        total_high += n_high
        rows.append((name, desc, len(violations), n_high, n_med, n_low))

    out = sys.stderr
    out.write("\n" + "=" * 78 + "\n")
    out.write("CSSI LINT roster — non-CL dry run (LINT-1 excluded; serial CL "
              "gate only)\n")
    out.write("=" * 78 + "\n")
    out.write("%-8s %-44s %6s %5s %5s %5s\n" %
              ("LINT", "checks", "total", "high", "med", "low"))
    out.write("-" * 78 + "\n")
    for name, desc, total, h, m, lo in rows:
        out.write("%-8s %-44s %6d %5d %5d %5d\n" %
                  (name, desc[:44], total, h, m, lo))
    out.write("-" * 78 + "\n")
    out.write("%-8s %-44s %6d %5d %5d %5d\n" % (
        "TOTAL", "", sum(r[2] for r in rows), sum(r[3] for r in rows),
        sum(r[4] for r in rows), sum(r[5] for r in rows)))
    out.write("=" * 78 + "\n")

    if summary_json:
        import json
        c.emit([])  # no-op spacer
        sys.stdout.write(json.dumps({
            "summary": [
                {"lint": n, "total": t, "high": h, "medium": m, "low": lo}
                for (n, _d, t, h, m, lo) in rows
            ]
        }, ensure_ascii=False) + "\n")

    sys.exit(1 if total_high else 0)


if __name__ == "__main__":
    main()
