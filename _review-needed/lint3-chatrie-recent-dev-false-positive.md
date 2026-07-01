# ESCALATION (logged) — LINT-3 HIGH ×2: `United States v. Chatrie` "SCOTUS-in-Recent-developments" false-positive

**Type:** lint-heuristic false-positive (verification-tool precision), NOT a content defect
**Class:** analogous to the accepted LINT-4 anti-pattern false-positive on `Verifying Good Law.md:47`
**Raised by:** S9 closeout final lint sweep · 2026-06-30
**Status:** OPEN as a tool-precision ticket · **content verified correct — no legal assertion at issue** (satisfies U4-S9: not a guessed assertion)

## The two flags
```
LINT-3 HIGH  content/8-exclusionary-rule-remedies/Standing to Challenge a Search.md:80
LINT-3 HIGH  content/8-exclusionary-rule-remedies/The Exclusionary Rule.md:129
  → "SCOTUS case 'United States v. Chatrie' in 'Recent developments' (SCOTUS tag) — N5"
```

## Why they are false-positives (content is correct)
Both flagged entries' **subject case is *United States v. Chatrie* (4th Cir. en banc, 136 F.4th 100 (2025))** — a **circuit** case, legitimately placed in a Recent-developments section as a superseded circuit development. The SCOTUS decision *Chatrie v. United States*, 609 U.S. ___ (2026) is **homed in Key cases** on its anchor doctrine page (*Two Definitions of Search*), not in Recent developments.

LINT-3's N5 heuristic (`lint3_structure.py`, `SCOTUS_TAG_RE = …|\bSCOTUS\b`) inspects a 45-char window **after** the first case name on the line and fires HIGH if it sees a SCOTUS tag. On both lines the window contains the **descriptive phrase** "→ superseded by SCOTUS" / "…now RESOLVED by SCOTUS", so the bare word "SCOTUS" (a description of what happened to the circuit case) trips the tag. The lint's own docstring states passing references to the Supreme Court "do NOT trigger (avoids false positives)" — this is exactly such a case, but the bare-token branch is too broad.

This is the same false-positive class already accepted for LINT-4 (the anti-pattern phrase "persuasive, not binding" quoted **as a prohibition** on `Verifying Good Law.md`).

## Recommended follow-on (either, one line of work — deferred, not taken here to stay in write-scope)
1. **Lint precision (preferred):** in `lint3_structure.py`, suppress the SCOTUS-tag branch when the same 45-char window also contains an explicit circuit-court parenthetical (`(\d+(st|nd|rd|th) Cir\.)`) — the "this entry's subject is a circuit case" signal the heuristic currently lacks. Reduces the roster to a true green. OR
2. **Trivial content reword:** change "superseded by SCOTUS" / "RESOLVED by SCOTUS" → "…by the Supreme Court" in the two entry headers (the un-prefixed "the Supreme Court" does not match `SCOTUS_TAG_RE`). Not done here because doctrine-body rewording is outside this run's write-scope (S8-term wiring only) and the Chatrie reframe text was an already-adjudicated CL fix.

## Release-gate disposition
Gate box **"No SCOTUS in Recent-developments (N5/LINT-3)"** → **PASS-with-logged-escalation**. No silent gap; content re-verified correct via the Chatrie serial-CL/L2 adjudication (`_run/s9-adjudications.md` §1).
