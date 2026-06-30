# Interview S5 — Case Ingest / Coverage Completion

**You are conducting the design interview for Spec S5.** Output: the method to find every
case we missed, **diagnose why each was missed**, generalize that failure logic to surface
other relevant cases (including non-book circuit/state cases), and ingest them as case pages
homed per S2. You design the ingest + diagnostic method; you do not ingest now.

## Required reading
1. `_overhaul/00-CONTEXT-PACK.md`; `_overhaul/specs/S1-standards.spec.md`.
2. `_overhaul/specs/S2-information-architecture.spec.md` — **read the scope decision**; it
   defines the universe of "missed."
3. `_overhaul/specs/S4-case-data-model.spec.md` — new cases are authored as case pages in
   that format.
4. The book TOC `/Users/johngalt/.orca/drops/Book Jun 26, 2026.pdf` (the master list to diff
   against) and `…/content/Case Index.md` (what we currently have).

## Part A — Ask the user (AskUserQuestion, recommend first)
1. **Confirm scope** (inherited from S2) — restate it and confirm before defining the diff.
2. **Aggressiveness for non-book cases.** How far do we go beyond the book to add relevant
   circuit/state-high-court cases (novel issues, first impression, circuit splits, digital-
   frontier)? Options: *book-complete only* · *book + clearly-controlling recent SCOTUS/
   circuit (recommended)* · *expansive frontier sweep*. The instructor wants progressive,
   self-expanding research — but bounded. Set the bound.
3. **Handling of cases the book lists but we'd exclude** (e.g. out-of-scope chapters) — note
   them as deliberately-omitted with reason, or drop silently? *Recommend: logged omissions.*

## Part B — Self-interview and propose
- The **diff method**: reconcile the book TOC against the Case Index by holding-identity (not
  just name string), using the misspelling-tolerant ID + serial-CL verification (L6/L4).
  Produce the missed-case list.
- The **"why missed" diagnostic taxonomy**: classify each miss (e.g. *out-of-prior-scope*,
  *keyword-homing failure (N1)*, *de-duped away*, *web-discovery never ran*, *named in prose
  but never tabled (N7)*, *too recent*). For each class, state the **generalized search** it
  implies to catch siblings (this is the instructor's "apply that logic to find others").
- The **progressive research protocol (N12)** specialized for coverage: narrow issue →
  doctrine/keyword expansion → learn → expand, with the recursion bound from S1 and
  web-discovers/CL-confirms.
- The **ingest pipeline**: discover → verify (serial CL) → author case page (S4 format) →
  home per S2 → wire links → find→adjudicate→fix gate → update Case Index.

## Deliverable
Write `_overhaul/specs/S5-case-ingest.spec.md`. Section 6 (Deliverables) = the missed-case
list format + the diagnostic-class → generalized-search table. Section 8 = the verification
gate (no fabricated cases per L2; identity-checked CL links per L3).

## Handoff
Update `_overhaul/README.md` (S5 → ✅). Recap. Hand the user `_overhaul/wrappers/S6.wrapper.md`.
