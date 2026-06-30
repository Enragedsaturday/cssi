# Interview S6 — Doctrine & Page Re-format (brief-first)

**You are conducting the design interview for Spec S6.** Output: the brief-first page
template for every doctrine page (and the other narrative pages), plus the per-page
change-list that clears the instructor's quick-fix register. You design the template +
change-list; you do not rewrite pages now.

## Required reading
1. `_overhaul/00-CONTEXT-PACK.md` — esp. N1–N10 and the **quick-fix register** (in the
   roadmap brief at `/Users/johngalt/briefs/2026-06-27-cssi-overhaul-spec-roadmap.html`).
2. `_overhaul/specs/S1-standards.spec.md`, `S2-information-architecture.spec.md`,
   `S4-case-data-model.spec.md` (case links/format), `S5-case-ingest.spec.md` (full corpus).
3. Pull the CURRENT text of the pages named in the register so the change-list is concrete:
   `Abandonment`, `CREW`, `Consent Searches`, `Curtilage`, `Knock and Talk`,
   `Community Caretaking and Emergency Aid`, `Collective Knowledge and the Fellow-Officer
   Rule`, `Exigent Circumstances and Hot Pursuit`, `Common Law Origins`.

## Part A — Ask the user (AskUserQuestion, recommend first)
1. **The brief-first template.** Present the proposed section order and get sign-off:
   **Brief** (rule + elements/tests stated up front per N3 + limits + nuance + pitfalls,
   integrated as one teaching read) → **Key cases** → **Related cases across doctrines** →
   **Recent developments & subsequent treatment** (circuit/state only, N5) → **Sources**.
   Ask specifically: do Nuances and Pitfalls **fold into the brief narrative** (recommended,
   matches "read the brief in its entirety first") or remain as labeled subsections after it?
2. **Exhaustive-treatment pages.** Knock-and-Talk is flagged for deep, exhaustive treatment.
   Ask which *other* topics deserve the same depth (candidates: consent scope, curtilage,
   community caretaking, exigency). Confirm the list.
3. **Flashcard regeneration.** When a page is rewritten, regenerate its deck from the new
   text (preserving ids) or leave decks alone this pass? *Recommend regenerate-preserving-ids.*

## Part B — Self-interview and propose
- The **template** in full, annotated with which S1 rules apply where (lexicon in the Weight
  column; tests-up-front; link-every-case; "limited by" inline).
- The **per-page change-list**: for every page, the specific edits — drawn from the
  quick-fix register (CREW "R"→"RE"; promote *Herring*; move *Riley* to Related; *Santana*
  "limited by"; *Dunn* factors into the Rule; the knock-and-talk reframe around lawful
  presence / implied-license scope incl. front-vs-other-public-doors, time/reasonableness,
  the hard line to leave, Jardines-to-no-"talk"-purpose, plain-view limits; consent three
  prongs bulleted + scope-exceeded pitfall with a real illustrative case; the Bandiero
  "hot on the tail / fresh on the trail" line + hot-vs-fresh discussion + *Newman v.
  Underhill* as fresh-pursuit; re-home *Case v. Montana* to Key cases; persuasive-language
  sweep). Mark each item with the L#/N# it enforces.
- The **non-doctrine narrative pages** in scope for reformat (excluding Legal Research, which
  is S8): home, framework/checklist pages, Three Golden Rules, Instructor Development, etc.
- The execution **find→adjudicate→fix gate** per page.

## Research to run as needed (web + serial CL)
- Resolve the **horizontal-pooling vs *Maryland v. Pringle*** contradiction the instructor
  flagged on Collective Knowledge (is *Pringle* truly a horizontal-pooling example, or
  vertical/aggregate-PC?). Resolve the **knock-and-talk** open questions with authority
  (*Jardines*, *Carloss*, circuit split on scope of license). Cite findings into the change-list.

## Deliverable
Write `_overhaul/specs/S6-doctrine-reformat.spec.md`. Section 6 = the template + the
per-page change-list table (Page · Change · Lesson · Cases affected). Section 8 = the gate.

## Handoff
Update `_overhaul/README.md` (S6 → ✅). Recap. Hand the user `_overhaul/wrappers/S7.wrapper.md`.
