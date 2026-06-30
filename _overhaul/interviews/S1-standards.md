# Interview S1 — Standards & the Self-Improvement Pass

**You are conducting the design interview for Spec S1 of the CSSI overhaul.** This is the
constitution: it turns the lessons register into one enforceable standard that every later
spec must obey. You are DESIGNING the standard, not yet applying it. Output is a written
spec (`specs/S1-standards.spec.md`) plus the standard's table of contents — the standard
document itself (`docs/STANDARDS.md`) is authored during execution, not now.

## Required reading (in order)
1. `_overhaul/00-CONTEXT-PACK.md` (the lessons register L1–L6 / N1–N13 and the lexicon).
2. `…/docs/FINAL-QA-SPEC.md` — read **§0** (15-point self-critique) and **§3** (D1–D12)
   in full. This is the existing discipline you are extending, not replacing.
3. `…/docs/RUNBOOK.md` — the CourtListener rate-limit protocol, the cluster-id≠opinion-id
   gotcha, the misspelling-tolerant case-ID escalation.
4. Skim 2–3 of the prior per-page specs in the vault `…/CSSI/_run/spec/*.spec.md` and
   `…/CSSI/_run/DECISIONS.md` so the spec you write matches the house format.

## Part A — Ask the user (use AskUserQuestion, lead with your recommendation)
1. **"100% verified" gate strictness.** Re-verify *every* assertion live against
   CourtListener, or trust the existing ~329-case verified catalog and re-verify only
   (a) anything changed/added and (b) all quotes + pinpoints? *Recommend (b)* — full
   re-verify is enormous and the catalog is already two-key'd. Confirm.
2. **Authority-weight lexicon.** Present the 6-tier lexicon (§4 of the context pack) and ask
   for confirmation / edits to the wording. This becomes mandatory vocabulary site-wide.
3. **Enforcement model.** Should the standard ship as *automated checks where possible*
   (link-checker that verifies CL case-identity per L3; a two-key/quote linter; a
   "no SCOTUS-in-recent-developments" structural lint) plus a reviewer checklist for the
   rest — or reviewer-checklist only? *Recommend automated-where-cheap + checklist.*
4. **Subsequent-treatment depth (N4).** Inline "limited by [cases]" tag everywhere, with a
   1–2 sentence explanation only when it changes field application? Confirm the threshold.
5. **Where the standard lives & supremacy.** `docs/STANDARDS.md` as the single governing
   contract that supersedes/absorbs `FINAL-QA-SPEC.md`? Confirm name + that it's the
   top authority for all later specs.

## Part B — Self-interview and propose (log each in the Decision-log appendix)
- The full **rules catalog**: restate L1–L6 and N1–N13 as numbered, testable standard
  rules. For each, give the *trigger* (when it applies) and the *check* (how a reviewer or
  script verifies it).
- The **research discipline** (N12): define the progressive/recursive web→CL protocol,
  including a recursion-depth bound and a stop condition, and the hard rule "web discovers,
  CourtListener confirms; one serial CL lane (L4)."
- The **verification methodology** (the standing find→adjudicate→fix machine, L5): roles,
  the no-edit rule for reviewers, the adjudication verdict set (uphold/modify/dismiss/
  escalate), the serial-CL lane, the escalation path for unresolved items.
- The **D1–D12 dimensions extended**: map each N-rule to a dimension (add D13+ if needed)
  so the existing reviewer framework absorbs the new rules.
- The **canonical templates' table of contents**: the brief-first doctrine-page template
  (N8) and the officer-IRAC case-page skeleton (defined in detail in S4 — here just
  reference it and state the cross-cutting rules: tests-up-front N3, link-every-case N7).

## Deliverable
Write `_overhaul/specs/S1-standards.spec.md` in the standard format (context pack §7).
Section 3 (Requirements) should be the numbered rules catalog. Section 8 (Verification
plan) should describe how S1 itself is checked (e.g., the rules are internally consistent,
each has a check, none contradicts a prior DECISIONS.md ruling).

## Handoff
Update `_overhaul/README.md` (S1 → ✅). Recap in 5–8 lines. Then paste the user the
contents of `_overhaul/wrappers/S2.wrapper.md` for a new thread.
