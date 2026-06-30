# Interview S4 — Case Data Model & Per-Case Pages

**You are conducting the design interview for Spec S4.** This is the biggest structural
change: define what a "case" IS (the case object), the **per-case page format** (improved
IRAC, built for a working officer), universal linking, and comprehensive treatment status.
You design the model + template + migration plan; you do not author all the pages now.

## Required reading
1. `_overhaul/00-CONTEXT-PACK.md` and `_overhaul/specs/S1-standards.spec.md`.
2. `_overhaul/specs/S2-information-architecture.spec.md` (homing + table categories) and
   `_overhaul/specs/S3-platform-nav.spec.md` (deep-link/highlight mechanism, case-card).
3. The **book's case-analysis example**: `/Users/johngalt/.orca/drops/Book Jun 26, 2026 (1).pdf`
   — format is Facts → Issue → Held → Discussion → Citation(topic). We are improving on this.
4. `…/content/Case Index.md` (the ~261–329 cases that need pages + status) and a current
   doctrine page's "Key cases" table for the row format we're replacing/linking.

## Part A — Ask the user (AskUserQuestion, recommend first)
1. **House case-page format.** Present 2–3 concrete options as previews and let the user
   pick: **BIRAC** (Background/Issue/Rule/Application/Conclusion); **CRuPAC**; or a custom
   **"Field-IRAC"** = Background → Issue → Holding/Rule → Reasoning → **Field Application
   (what it means on the street)** → **Bottom line** → Teaching points → Treatment & links.
   *Recommend Field-IRAC* — it foregrounds practical application + a one-line street takeaway,
   which is the stated objective. Show a filled example (use *Brigham City v. Stuart* from the
   book scan) so the choice is concrete.
2. **Treatment-status verification scope.** Re-verify good-law for all ~329 cases now, or
   per S1's gate (catalog-trust + re-verify deltas/quotes)? Confirm consistency with S1.
3. **Case-page flashcards.** Do per-case pages get their own cards, or do existing
   per-doctrine + "Name That Case" decks stay the flashcard home? *Recommend: no new
   per-case decks; keep id stability.* Confirm.

## Part B — Self-interview and propose
- The **case object schema** (frontmatter): canonical name, Bluebook cite, neutral/slip cite,
  court, year, docket, the verified **CourtListener opinion URL** (case-identity-checked per
  L3), **treatment status** (the S1 lexicon + good/limited/abrogated/overruled + "as of"
  date), **home doctrine(s)** + role per page, pinpoint anchors, related cases.
- The **page template** in full (the chosen format), with the two-key rule baked in: every
  quote verbatim + pinpoint; every proposition traceable; the street-application + bottom-line
  blocks; a "limited by / limits" block (N4); a "appears on" backlink list (the doctrine pages).
- **Universal linking + deep-links (N7):** the rule that every case named anywhere resolves to
  its case page; the slug scheme; the pinpoint/highlight mechanism decided in S3.
- The **migration plan**: generate a case page for every Case-Index case; how doctrine-page
  tables link to them; how the Case Index becomes an index *of* pages; the shepardize sweep
  that fills N13's no-blank-status requirement. Define the find→adjudicate→fix gate for it.

## Deliverable
Write `_overhaul/specs/S4-case-data-model.spec.md`. Include the final frontmatter schema and
the page template verbatim in an appendix so execution is unambiguous. Section 7 (Acceptance)
must include "every named case links to a page" and "no blank treatment status."

## Handoff
Update `_overhaul/README.md` (S4 → ✅). Recap. Hand the user `_overhaul/wrappers/S5.wrapper.md`.
