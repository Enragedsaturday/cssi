# Interview S9 — Full Independent Verification & Adjudication

**You are conducting the design interview for Spec S9.** Output: the design of the final,
whole-product verification pass that makes the deliverable 100%-verified — independent
review → adversarial check → adjudication → fix, over the serial-CL lane, against the
extended dimension set. You design the pass; you do not run it now (it runs in the
autonomous execution after S4–S8's content exists).

## Required reading
1. `_overhaul/00-CONTEXT-PACK.md`; `_overhaul/specs/S1-standards.spec.md` (the methodology
   this pass instantiates).
2. `…/docs/FINAL-QA-SPEC.md` §3–§8 (the prior pass: D1–D12, phases P0–P5, definition of done)
   — S9 is its successor, extended with the N-rules.
3. All written specs `_overhaul/specs/S2…S8` so the pass covers everything they produce.

## Part A — Ask the user (AskUserQuestion, recommend first)
1. **Definition of done / sign-off.** What does "100% verified, complete, and correct" mean
   as a release gate? *Recommend:* zero open UPHELD/MODIFIED findings unapplied; every case
   page two-key'd + CL-identity-checked; no blank treatment status; no SCOTUS-in-recent-
   developments; every named case linked; all tests stated up front; Mermaid visually
   inspected; the ledger reconciles. Confirm/adjust.
2. **Adversarial intensity vs cost.** How many independent reviewers / refutation votes per
   item? *Recommend:* single independent reviewer per page for editorial dimensions; **N-of-3
   adversarial refutation** only for high-stakes legal assertions (holdings, quotes, good-law)
   and any case flagged novel/first-impression. Confirm the tiering.
3. **Escalation policy.** Unresolved items → a `_review-needed/` human queue (as before),
   never guessed (two-key). Confirm.

## Part B — Self-interview and propose
- The **pipeline**: phases (inventory → dimensional review → adjudication (editorial lane +
  serial-CL legal lane) → fix → visual/Mermaid → link-identity check → ledger reconcile),
  each with the find→adjudicate→fix separation (L5) and the single serial CL lane (L4).
- The **extended dimension set**: D1–D12 from the prior pass + the new N-rules mapped to
  dimensions (N1 homing, N5 recent-dev placement, N7 link-every-case, N8 brief-first
  structure, N13 no-blank-status, etc.). Produce the final reviewer checklist.
- **Coverage**: doctrine pages, every case page, glossary + term links, legal-research
  pages, the Case Index, the category nav, flashcards (deck↔page↔index integrity).
- The **ledger + reporting**: structured findings → adjudications → applied-fixes, a final
  report, and the definition-of-done checklist as the literal release gate.

## Deliverable
Write `_overhaul/specs/S9-verification.spec.md`. Section 7 (Acceptance) = the release-gate
checklist. Section 8 = how the verification pass itself is audited (false-positive logging,
sampling re-checks).

## Handoff
Update `_overhaul/README.md` (S9 → ✅). Recap. **All specs now written** — hand the user
`_overhaul/wrappers/EXECUTE.wrapper.md` to launch the autonomous build in a new thread.
