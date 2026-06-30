# Interview S2 — Information Architecture & Category Taxonomy

**You are conducting the design interview for Spec S2.** Output: a parent/child category
tree (ours — informed by the book + current pages + judgment, not ripped from either),
page splits/merges, case-homing rules, the full set of case-table categories, and the
**project scope decision** that gates S5. You design the taxonomy; you do not move files.

## Required reading
1. `_overhaul/00-CONTEXT-PACK.md` (esp. §5 roadmap + the scope question).
2. `_overhaul/specs/S1-standards.spec.md` (the standard you must conform to).
3. The book TOC: `/Users/johngalt/.orca/drops/Book Jun 26, 2026.pdf` — it shows the book's
   own category structure (I. What is a Search? … XIII. Other Cases). Use as input, not gospel.
4. `…/content/index.md` (current narrative grouping) + the vault `…/CSSI/_run/IA-SPEC.md`
   (prior 11-bucket IA). Skim all 43 page titles in `…/content/`.

## Part A — Ask the user (AskUserQuestion, recommend first)
1. **Project scope (THE gating decision).** (a) 4A-complete, (b) **current scope + its
   existing adjacencies — Miranda/5A, 6A, use-of-force, eyewitness ID, Brady, entrapment
   (recommended)**, or (c) whole book I–XIII. This decides what "missed cases" means in S5.
2. **Community Caretaking split.** The current page bundles community caretaking, emergency
   aid, and exigency. Split into distinct pages and/or add a dedicated **Home Entry &
   Search** page? *Before asking, run the research below so you can recommend from fact,
   not vibes.* Present a recommendation with the cases that would re-home.
3. **Category as folders vs tags.** Quartz's left-nav Explorer is folder-driven. Do we adopt
   a real folder hierarchy under `content/` (drives nav + breadcrumbs) or keep flat files +
   a tag/category frontmatter field? *Recommend folders for nav + a `category`/`tags` field
   for cross-cutting* — but flag the flashcard-id-stability constraint (renames must
   preserve deck ids; see DECISIONS D-6 in the vault).
4. **Tree depth.** Confirm a target of 2 levels (parent → child), 3 only where it genuinely
   aids navigation. The user wants "easy to navigate, makes sense at first glance."

## Part B — Self-interview and propose
- The **category tree**: propose the full parent→child structure with page assignments for
  all current pages + obvious gaps. Name categories in our own voice (don't copy the book's
  headings verbatim; don't gratuitously differ either).
- **Case-homing rules (N1):** the algorithm for a case's primary home (the doctrine whose
  rule the case establishes) and the multi-homing rule (N6: a case may be Key on several
  pages if central to each; framing is page-specific).
- **The full case-table category set (N5/N6):** define every table/role a case can occupy on
  a page — e.g. *Key (anchor)*, *Key (progeny/refinement)*, *Related across doctrines*,
  *Illustrates a circuit split*, *Narrows/limits the rule*, *First-impression (circuit/state)*,
  *Historical*. Specify which roles a circuit/state-high-court case may hold (key when novel
  or first-impression; elsewhere when illustrating splits/narrowing) per the instructor's note.
- **Page split/merge list:** every page that should split, merge, or be created, with rationale.

## Research to run first (web + serial CourtListener, per the standard)
- **Community caretaking — does it reach persons, not just vehicles, outside the home?**
  Resolve with authority (*Cady v. Dombrowski*; *Caniglia v. Strom*; circuit treatment of
  caretaking of persons). This directly drives Part A.2. Cite what you find.

## Deliverable
Write `_overhaul/specs/S2-information-architecture.spec.md`. Section 6 (Deliverables) must
include the concrete target tree and the page split/merge/create list so S4–S6 can execute
against it. Record the scope decision prominently (S5 reads it).

## Handoff
Update `_overhaul/README.md` (S2 → ✅). Recap. Hand the user `_overhaul/wrappers/S3.wrapper.md`.
