# Wrapper — Cross-Spec Coherence Verification (do this BEFORE EXECUTE)

Use this **after all nine specs `S1…S9` are written** (check `_overhaul/README.md` shows every row ✅)
and **before** `EXECUTE.wrapper.md`. It is a **design-integrity pass over the specs themselves** — not
content work. It reads all nine specs *in conjunction* and surfaces conflicts, interface mismatches,
ambiguities, and missing context, so the autonomous build runs against a coherent, self-consistent
contract. Paste everything below the line into a fresh Claude Code thread opened in the CSSI repo
(`/Users/johngalt/Projects/cssi-quartz`).

---

You are running the **Cross-Spec Coherence Verification** of the CSSI overhaul spec kit. **All nine
specs are written; do not re-run any interview and do not author content.** Your job is to verify the
specs **work together** as one executable contract, fix what you can, and surface what only the user can
decide — then hand off to the autonomous build.

## Load order
1. Read `/Users/johngalt/Projects/cssi-quartz/_overhaul/00-CONTEXT-PACK.md` in full.
2. Read **every** spec `_overhaul/specs/S1…S9` in full (S1 is the governing constitution — SR-3).
3. Read `_overhaul/wrappers/EXECUTE.wrapper.md` (you will audit it for staleness too) and skim
   `docs/FINAL-QA-SPEC.md` (S9's predecessor) + `docs/RUNBOOK.md` (CL/tier/mermaid/redeploy mechanics).

## What to verify (audit these dimensions across all nine specs)

1. **Dependency & ordering coherence.** Walk the dep graph (S1→S2→S3→S4→S5→S6→S7→S9; S8 depends on S1
   only; S9 depends on all). Confirm every spec's inputs exist when it runs. Surface **hidden
   dependencies** the graph omits (e.g. S7's audit needs S6-finalized text *and* S8's term routing; S8
   coordinates with S7; S6 consumes S5's rows; S4 gates S5/S6; S3 gates S4/S7). Flag any **mandatory
   human-in-the-loop pause** the "autonomous" run must expect (S5·R2 borderline sign-off; the final
   publish go-ahead; any irreversible step like S9·R11 the deck purge / FSRS reset).

2. **Interface / handoff coherence.** For each spec-to-spec handoff, confirm the **producer's declared
   output == the consumer's expected input**, concretely (no "TBD" the downstream spec relies on):
   S2 tree/§6.3 crosswalk/§3.3 role set → S3/S4/S5/S6; S4 Appendix-B frontmatter + Appendix-C BIRAC +
   R6 anchors + R9 data convention → S5/S6/S3/S7/S8; S5 rows+homes+Garrity-flag+Thread-P ledgers →
   S6/S9; S6 finalized brief text → S7; S7's ten routed terms → S8; S8 alias + term anchors → S7/S9;
   everything → S9.

3. **Conflict / supersession coherence.** Hunt for two specs asserting contradictory things, and
   confirm every **mid-kit supersession is consistently reflected everywhere it touches** — at minimum:
   - **Garrity OPTIONAL (S2 §2.0) → CORE (S5·R11 / S6·R9).** S2 still tags it OPTIONAL and S5/S6 only
     *recommend a one-line S2 cross-ref "at execution."* Decide whether S2 should be amended now.
   - **Deck-id half of D-3/D-6.** S4·R11 **drops** the deck-id-preserving caretaking-split migration and
     supersedes the FSRS/deck-id half of D-6 (terminal rebuild instead). Check that **S2 §6.2** ("preserve
     deck card ids… re-home emergency-aid cards losslessly") and **S3·R9** ("deck-id preservation is S4's
     mechanism") are not left asserting a superseded mechanism — and that **`EXECUTE.wrapper.md`**'s S2
     guardrail "**Preserve flashcard ids on every rename (deck ids are stable by contract)**" is corrected
     (it now contradicts S4·R11).
   - **L7 / L8 / SR-5** were added to S1 mid-kit (SI-6/SI-7/SI-8). Confirm the downstream specs that rely
     on them reference them correctly and the lessons-count (21 lessons L1–L8+N1–N13; SR-1…SR-5) is
     consistent across S1 and every citing spec.
   - **`The Warrant Requirement` possible split** (S2 WATCH → S6 re-eval → S9 verify) — confirm the
     deferral chain is consistent and nothing assumes it both split and didn't.

4. **Terminology / ID consistency.** Every `L#/N#/SR#/D#/R#` reference resolves to the same thing across
   specs; the **6-tier lexicon**, the **8-role set** (S2·R3), and the **D1–D14** dimension set are
   referenced identically wherever they appear.

5. **Per-spec clarifications & missing context (the heart of this pass).** For each spec, ask: *what
   would an autonomous executor still not know?* Examples to check and fill: the CL tier-probe + serial-
   lane procedure and the **mermaid render command / `pptr.json`** (RUNBOOK / FINAL-QA Key-paths) carried
   forward; the **prior-research corpus location** for SR-5/S5 (the 41 prior per-page specs + manifests
   in the iCloud vault) **and the iCloud EPERM read workaround**; `redeploy.sh` behavior + the publish
   repo/identity (`Enragedsaturday/cssi`, GH noreply); where `docs/STANDARDS.md` is authored and that all
   specs cite it; the component data convention (S3 §9 → S4·R9 — confirm fully closed); the exact
   `_review-needed/` triage owner after S9. Produce a **per-spec "needs-clarification / needs-context"
   list** with a concrete recommended resolution for each.

6. **Coverage gaps.** Anything **no spec owns**? Confirm each known deferral is *consciously* deferred,
   not dropped: Quartz 4→5 upgrade (S3·§9); post-overhaul continuous-glossary cadence (S7·§9 / S9·§9);
   OPTIONAL/SECONDARY promotion-on-request (S2); FSRS-progress preservation re-open window (S9·§9 before
   the purge).

## How to run it
- This is the project's **hybrid** method: **self-interview** every coherence question (Options →
  Red-team → Steel-man → Adjudication); **only** use `AskUserQuestion` for the genuinely **user-owned**
  conflicts you surface (e.g. "amend S2 now to mark Garrity CORE, or leave the execution-time cross-ref?";
  "correct the EXECUTE deck-id guardrail?"), recommendation first.
- **No content work, no CL, no builds.** This is a spec-level reasoning pass.

## Deliverables
1. A **Cross-Spec Coherence Report** — serve it as an HTML brief via the user's `/brief` flow (he is
   remote; hand the Tailscale link) **and** save a copy to `_overhaul/COHERENCE-REPORT.md`. It lists, per
   audit dimension above: findings · severity · recommended resolution · (conflict vs. clarification vs.
   missing-context).
2. **Applied spec amendments.** For every coherence fix the user approves (and every non-user-owned
   clarification), **apply it additively to the relevant spec** — the same way L7/L8/SR-5 were homed into
   S1 (a decision-log entry + the edit), keeping each spec's `status: APPROVED`. Do **not** silently
   rewrite settled decisions; record each amendment in that spec's Appendix A.
3. **A go/no-go line** on whether the spec set is internally coherent and execution-ready.

## Handoff
When the report is delivered, the user-owned conflicts are dispositioned, and the approved amendments are
applied: update `_overhaul/README.md` if any spec changed, give the user a tight recap, and **hand the
user `_overhaul/wrappers/EXECUTE.wrapper.md`** to launch the full autonomous build in a new thread. Begin.
