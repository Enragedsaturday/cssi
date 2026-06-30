# Interview S3 — Platform, Navigation & UX

**You are conducting the design interview for Spec S3.** Output: the keep-tune-vs-fork-vs-
switch decision for the platform, plus the navigation/UX target that S2's taxonomy needs
and that S4's per-case pages must render at scale. You decide direction; you do not rebuild.

## Required reading
1. `_overhaul/00-CONTEXT-PACK.md` (note: popovers already ON; sidebar = 2 SCSS values).
2. `_overhaul/specs/S2-information-architecture.spec.md` (the nav requirements you must serve).
3. `…/quartz.config.ts`, `…/quartz.layout.ts`, `…/quartz/components/Explorer.tsx`,
   `…/quartz/styles/base.scss`, `…/quartz/styles/variables.scss`.

## Part A — Ask the user (AskUserQuestion, recommend first)
1. **Direction.** (a) **Keep & enhance Quartz (recommended)**, (b) formal bake-off against
   ONE alternative before committing, or (c) switch now. Make the case: popovers, search,
   graph already work; sidebar is a trivial fix; content is portable markdown so there's no
   lock-in. The bar for (b)/(c) is "Quartz can't present the category tree or the case
   corpus well." Present that bar honestly.
2. **Nav model.** Do they want a **docs-style left nav grouped by S2 category** (collapsible
   sections), replacing/retuning the file-tree Explorer? Confirm the "not cramped" target
   (spacing, width, grouping, current-section highlighting).
3. **Custom components — how far.** Invest in a few bespoke components (case-card,
   treatment-status badge, legal-term popover styling, a case-table with sort/filter) or stay
   markdown-only? *Recommend a small, surgical set* — name them and their cost.

## Part B — Self-interview and propose
- An **honest alternatives scan** (use web/Context7 for current facts): Astro **Starlight**,
  **Docusaurus**, **MkDocs-Material**, **Obsidian Publish**. For each: does it give better
  category nav / case-corpus handling than tuned Quartz, and what would we lose (graph,
  popovers, the FSRS flashcard app, the existing build)? Recommend with reasons.
- The concrete **Quartz enhancement set** if we keep it: the exact sidebar/spacing changes;
  category-driven Explorer config; how legal-term popovers attach (wikilink → glossary
  anchor; confirm `enablePopovers` covers it); deep-link/highlight support for case pages
  (see below); responsive behavior (TOC currently hidden <1200px).
- **Deep-link / pinpoint highlighting (N7):** determine how "click a case reference → land on
  the highlighted passage" will work. Check whether CourtListener opinion URLs support text-
  fragment/anchor highlighting, and how our own case pages will anchor to pinpoint sections.
  Record the mechanism for S4 to implement.

## Deliverable
Write `_overhaul/specs/S3-platform-nav.spec.md`. Section 5 (Method) = the decided platform +
the ordered list of UX/nav changes. Section 6 = files to change (config, layout, scss,
any new components). Keep content specs (S4–S8) platform-portable regardless of this outcome.

## Handoff
Update `_overhaul/README.md` (S3 → ✅). Recap. Hand the user `_overhaul/wrappers/S4.wrapper.md`.
