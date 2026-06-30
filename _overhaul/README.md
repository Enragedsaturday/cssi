# CSSI Overhaul — Spec-Driven Development Kit

This directory drives the CSSI rebuild as **spec-driven development**: one design
**interview** per spec → a written **spec** → (after all specs) one **autonomous
execution run**. Each interview is meant to run in its own fresh context thread.

## The loop

1. Paste a **wrapper** (`wrappers/SN.wrapper.md`) into a new thread.
2. The thread reads `00-CONTEXT-PACK.md` + `interviews/SN-*.md`, conducts the interview
   with you, and writes `specs/SN-<slug>.spec.md`.
3. It hands you the **next** wrapper. Repeat.
4. After S9, paste `wrappers/EXECUTE.wrapper.md` to launch the autonomous build.

Start here → `wrappers/S1.wrapper.md`.

## Files
- `00-CONTEXT-PACK.md` — shared grounding (read first in every thread).
- `interviews/SN-*.md` — the detailed interview agenda for each spec.
- `wrappers/SN.wrapper.md` — short paste-able launchers (one per spec + EXECUTE).
- `specs/SN-*.spec.md` — interview outputs (the approved specs). Empty until written.

## Status

| Spec | Title | Wave | Depends on | Interview | Spec written |
|---|---|---|---|---|---|
| S1 | Standards & Self-Improvement | A | — | `interviews/S1-standards.md` | ✅ |
| S2 | Information Architecture & Categories | A | S1 | `interviews/S2-information-architecture.md` | ✅ |
| S3 | Platform & Nav/UX | B | S2 | `interviews/S3-platform-nav.md` | ✅ |
| S4 | Case Data Model & Per-Case Pages | B | S1–S3 | `interviews/S4-case-data-model.md` | ✅ |
| S5 | Case Ingest / Coverage Completion | C | S2, S4 | `interviews/S5-case-ingest.md` | ✅ |
| S6 | Doctrine & Page Re-format (brief-first) | C | S1,S2,S4,S5 | `interviews/S6-doctrine-reformat.md` | ✅ |
| S7 | Legal-Term Linking | C | S3, S6 | `interviews/S7-legal-term-linking.md` | ✅ |
| S8 | Legal-Research & Citations Pages | C | S1 | `interviews/S8-legal-research-pages.md` | ✅ |
| S9 | Full Independent Verification & Adjudication | D | all | `interviews/S9-verification.md` | ✅ |

> Recommended order: S1 → S2 → S3 → S4 → S5 → S6 → S7 → S9, with S8 slotted any time
> after S1. The interview thread updates this table (☐ → ✅) when it writes a spec.

## Cross-spec coherence pass — ✅ 2026-06-30

All nine specs were verified **in conjunction** (conflicts, interface mismatches, missing context).
Verdict: **GO — execution-ready.** Findings + resolutions are in **`COHERENCE-REPORT.md`**. Amendments
applied (all additive, recorded in each spec's Appendix A): **U5-S9** flashcards out of scope (frozen
through the overhaul; rebuilt in a **separate later run**) · **U6-S9** `content/` is canonical (vault→content
sync retired) · **D3-S2** Garrity promoted OPTIONAL→CORE · deck-id supersession forward-pointers ·
TreatmentBadge values aligned to S1 §3.D · EXECUTE corrected (mechanics in load order; S7+S8 anchorize-then-wire;
mandatory human pauses; `content/`-canonical publish). **Next: paste `wrappers/EXECUTE.wrapper.md`** for the
full autonomous build (content-only; the flashcard rebuild is a separate run afterward).
