# Interview S7 — Legal-Term Linking

**You are conducting the design interview for Spec S7.** Output: the method to expand the
glossary and wire non-vernacular legal terms across all pages so a hover gives a preview and
a click goes to the term's page/anchor. You design the inclusion test + wiring method; you
do not perform the sweep now.

## Required reading
1. `_overhaul/00-CONTEXT-PACK.md` (N11; popovers already ON).
2. `_overhaul/specs/S3-platform-nav.spec.md` (the confirmed popover/anchor mechanism).
3. `…/content/Common Legal Terms.md` (current glossary — categories + entries).

## Part A — Ask the user (AskUserQuestion, recommend first)
1. **Inclusion test ("don't go overly broad").** Define what qualifies as a linkable term.
   *Recommend:* a term qualifies only if it's **outside common lay vernacular and primarily
   used by legal professionals** (e.g. *curtilage, attenuation, inevitable discovery, dicta,
   stare decisis*) — exclude plain-English words and terms the page is itself teaching as its
   subject. Get the user's boundary calls on edge cases.
2. **Link density.** Link the **first occurrence per page** (recommended — clean), or every
   occurrence? Confirm.
3. **Glossary granularity.** One glossary page with anchors (hover shows the entry via the
   `.popover-hint`), or a page per term? *Recommend single page + anchors* unless S4's case
   pages set a per-page precedent worth matching.

## Part B — Self-interview and propose
- The **term-audit method**: scan every live page for candidate terms, dedupe against the
  glossary, and produce (a) the add-to-glossary list and (b) the term→pages occurrence map.
- The **wiring mechanism**: how a term becomes a hover-preview link (wikilink to the glossary
  anchor so Quartz's popover fires; confirm the `.popover-hint` target renders the definition).
- **Authoring rule** for new glossary entries: plain-English definition + a concrete
  search-and-seizure example, matching the existing glossary's voice; two-key only where a
  definition asserts a legal proposition tied to a case.
- The execution gate (find→adjudicate→fix): a reviewer checks no over-linking, no broken
  anchors, definitions accurate.

## Deliverable
Write `_overhaul/specs/S7-legal-term-linking.spec.md`. Section 3 = the inclusion test as a
testable rule. Section 6 = the term→pages map format + glossary-additions format.

## Handoff
Update `_overhaul/README.md` (S7 → ✅). Recap. Hand the user `_overhaul/wrappers/S8.wrapper.md`
(or, if S8 is already done, `_overhaul/wrappers/S9.wrapper.md`).
