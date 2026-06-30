# Wrapper — EXECUTE the CSSI Overhaul (full autonomous build)

Use this only after **all** specs `_overhaul/specs/S1…S9` are written (check
`_overhaul/README.md` shows every row ✅). Paste everything below the line into a fresh
Claude Code thread opened in the CSSI repo (`/Users/johngalt/Projects/cssi-quartz`). This is
the full autonomous bound: you execute the approved specs end-to-end.

---

You are executing the **CSSI overhaul** autonomously from its approved specs. The interviews
are done; the specs are law. Build the product.

## Load order
1. Read `/Users/johngalt/Projects/cssi-quartz/_overhaul/00-CONTEXT-PACK.md`.
2. Read **every** spec in `/Users/johngalt/Projects/cssi-quartz/_overhaul/specs/` (S1…S9).
3. `_overhaul/specs/S1-standards.spec.md` is the **governing contract** — it outranks your
   defaults. Obey it throughout.
4. Read `docs/RUNBOOK.md` for **operational mechanics** — the **CourtListener tier-probe + serial-lane
   + STOP-on-old-5/min-tier protocol (§3)**, the **misspelling-tolerant ID + cluster-id≠opinion-id
   gotcha (§3a)**, and the **iCloud EPERM** read/write workaround — and `docs/FINAL-QA-SPEC.md`
   **Key-paths** for the **Mermaid render command** (`mmdc` + `pptr.json`). These are the executable
   mechanics the specs reference but don't restate.

## Execution order (respect the dependency graph)
1. **S1** — author `docs/STANDARDS.md` from the spec; stand up the automated checks
   (CL-identity link-checker per L3; two-key/quote linter; "no SCOTUS in recent-developments"
   structural lint; no-blank-treatment-status check).
2. **S2** — apply the taxonomy: folder/category restructure + page splits/merges/creates.
   **No deck work** — decks are frozen for the entire overhaul (S4·R11 / U5-S9). Keep **file stems
   stable** so `[[wikilinks]]` resolve after the folder move, and add `aliases:` on any path-changed or
   split page. *(The Garrity cluster is **CORE** — S2 §2.0 amendment / D3-S2 — homed to a new doctrine
   page authored in S6.)*
3. **S3** — apply the platform/nav/UX changes (the decided direction).
4. **S4** — build the case data model + generate a per-case page for every case; wire
   universal linking + pinpoint deep-links; complete the treatment-status sweep (no blanks).
5. **S5** — run the missed-case ingest (diff → diagnose → generalized search → verify →
   author → home).
6. **S6** — re-format every doctrine + narrative page brief-first; clear the quick-fix register.
7. **S7 + S8 — coordinate (mutual term-anchor dependency).** S7 wires doctrine-prose citation-mechanics
   terms to **S8's** `### Term` anchors, and S8 routes its page-less terms to **S7's** glossary anchors.
   So **anchorize first, then wire:** (a) S8 authors the 3 legal-research pages + creates its ten
   citation-term anchors (tools vetted live, sources cited); (b) S7 anchorizes the glossary; (c) **then**
   run the term-wiring sweep across the doctrine pages, pointing each term at the right (now-existing)
   anchor. S9·R9 re-audits term wiring against final text as a back-fill safety net.
8. **S9** — run the full independent verification & adjudication pass; reconcile the ledger.
   **No deck rebuild here** — decks stay frozen; the page-derived rebuild is a **separate later run**.

## Non-negotiable guardrails (from the standard)
- **Two-key rule**: every holding/quote/pinpoint traces to the primary opinion. Web
  **discovers**; CourtListener **confirms**. Never assert from memory or paraphrase.
- **One serial CourtListener lane.** Never hit CL from parallel agents (L4). Verify each CL
  URL resolves AND shows the named case (L3). "Not found" ≠ "doesn't exist" — escalate (L6).
- **find → adjudicate → fix** separation (L5): reviewers never self-edit; adjudicators rule;
  fixers apply verbatim. Cap 3 attempts/fix → escalate to `_review-needed/`. Never guess.
- **Orchestration is mandatory, not optional** — see the next section. (Serial-CL, role separation,
  and the loop cap are part of it.)

## Orchestration model (MANDATORY — this is *how* you run, not a suggestion)

The project pattern is a **thin orchestrator + fresh sub-agents + small on-disk hand-offs** (RUNBOOK §1 ·
FINAL-QA-SPEC §1 · S1 §3.G). It is **non-negotiable** — the build is large, heavy-CL, and multi-session;
running it inline in one context will blow the context, lose resumability, and break the serial-CL
discipline. Obey all of the following:

- **Thin orchestrator.** The main thread is a **coordinator only**: it holds the **ledger, the specs,
  and per-unit statuses** — nothing else. It **must NOT** pull the full corpus, whole pages in bulk, or
  long sub-agent transcripts into its own context. *If you find yourself reading content in the main
  thread in order to **do work**, stop — that work belongs in a sub-agent.* Never load the whole vault /
  corpus into one agent.
- **Delegate all substantive work to fresh sub-agents.** Writing, verifying, reviewing, adjudicating,
  fixing, researching — each runs in its **own fresh sub-agent**, **one unit = one job** (one page, or
  one role on one page: writer / verifier / reviewer / adjudicator / fixer), fed **only its inputs**.
  Fan out in parallel for independent units.
- **Hand-offs are small files on disk.** Sub-agents return **small JSON/MD artifacts** (findings,
  adjudications, statuses, manifests) — never long prose the orchestrator must hold. The orchestrator
  reads the small hand-off, updates the ledger, dispatches the next unit. Hand-offs go on disk, not
  through context.
- **The single serial bottleneck is CourtListener** (the guardrail above): **concurrency-1, one lane,
  always.** Reviewers/writers fan out wide **because they are free / no-CL**; the instant a step needs
  CL it **queues on the one lane**. **Never** fan CL out across agents — re-probe the tier first and
  STOP on the old 5/min tier (RUNBOOK §3).
- **find → adjudicate → fix stays role-separated** (L5): a **reviewer** emits findings and **never
  edits**; an **adjudicator** rules (legal verdicts must cite CL evidence); a **fixer** applies only
  UPHELD/MODIFIED verbatim and introduces no new content. DISMISSED findings are logged with a reason.
  **Loop cap 3** → escalate to `_review-needed/`. Never guess.
- **Checkpoint after every sub-phase.** Write the ledger to disk after each unit/sub-phase so the run is
  **resumable from the ledger, not from scratch** — assume the run *will* be interrupted across sessions.
- **Decision framework for consequential calls** (naming, a close structural call): draft → a sub-agent
  red-teams → a sub-agent steel-mans → the orchestrator adjudicates and writes a one-paragraph rationale
  to disk → execution agents follow it (RUNBOOK §1). Cap any build↔fix loop at 3, then escalate.

## Process & safety
- Work on a **new git branch** (e.g. `overhaul/build`). Commit progressively, one logical
  unit per commit, with clear messages. Do **not** force-push or rewrite history.
- Validate with `npx quartz build` locally after major phases. **`content/` is the canonical source
  (U6-S9) — do NOT run `redeploy.sh`** for build *or* publish: its **vault→content** sync would
  **overwrite the rebuilt `content/`** with the stale iCloud vault. The vault→content sync is retired.
- **Do NOT touch the flashcards** — decks are frozen for the whole overhaul (U5-S9); the page-derived
  purge + regenerate is a **separate later run** after the full content corpus is final. Run no
  `merge.py` / `make_apkg.py`.
- **Mandatory human pauses** (the run is autonomous *between* these, not through them): (a) **S5
  borderline sign-off** — park ambiguous-relevance cases in `_overhaul/coverage/borderline.md` and
  **surface them for my disposition** before ingesting/dropping (don't auto-decide; you may proceed with
  the clear-ingest cases and apply borderline dispositions in a short follow-up); (b) the **final publish
  go-ahead** below.
- **Stop before any outward-facing step.** Do NOT push to `main` or trigger a Vercel
  production deploy on your own — prepare everything (commit/push to the **branch**, not `main`), then
  surface it for my go-ahead.
- Keep a running ledger on disk (findings → adjudications → applied fixes → escalations).

## Done
When S9's release-gate checklist passes, produce a **served HTML brief** (per my `/brief`
flow) summarizing: what changed, the verification ledger, anything parked in
`_review-needed/`, **the reminder that the page-derived flashcard rebuild is a still-owed separate
run**, and the exact commands to review the branch + deploy. Publish = **commit + push `content/`**
(Vercel builds the repo) — **not** `redeploy.sh`. Hand me the link. Then wait for my go-ahead on
push/deploy to `main`.
