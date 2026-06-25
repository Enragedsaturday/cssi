# CSSI Build & Ingest — Runbook

*How the CSSI wiki + flashcard site was built and how to re-run an ingest. This is the reference an
ingest session reads before processing new notes. Last updated 2026-06-23 (Day-2 ingest: added §3a —
misspelling-tolerant case identification + research-depth mandate).*

---

## 0. TL;DR — what an ingest does
Take shorthand class notes from the vault `_inbox/`, turn them into clean **citation-verified** wiki
pages (new pages *or* additive appends), refresh the **flashcard deck**, and republish the **live
site** — following `_conventions.md`, with a hard **CourtListener rate-limit guard** (stop + notify
if we're on the old 5/min tier). Trigger: the `/cssi-ingest` command (or the paste-able wrapper).

---

## 1. Operating principles (how the prior run worked)
- **Orchestrator + thin context.** The main thread orchestrates and holds only the index + statuses.
  All heavy lifting happens in **fresh sub-agents**; hand-offs are **small JSON/MD files on disk**,
  never long transcripts. Never load the whole vault into one agent.
- **One sub-agent = one topic or one role** (writer / verifier / reviewer), fed only its inputs.
- **Decision framework for consequential choices** (naming, tech, architecture): draft a proposal →
  a sub-agent red-teams it → a sub-agent steel-mans it → orchestrator adjudicates and writes a
  one-paragraph rationale to disk → execution sub-agents follow it. Cap any build↔fix loop at **3
  passes**, then ship the best working version / escalate to `_review-needed/`. No silent loops.
- **iCloud EPERM gotcha.** The Read tool often fails on the vault path. To read vault files, `cp`
  them to scratch and read the copies; to write back, write in scratch and `cp` into place.
  (`cp`/`rm`/`>>` via Bash work both directions.) Files under `~/Projects/cssi-quartz/` read fine.
- **Everything is verified before it's asserted.** Every case cited is checked on CourtListener
  (existence+name, then proposition). Unverifiable cites are flagged, never stated as settled.

### How Day 1 was actually executed (for reference)
Recon + timestamped vault backup → 3 decision frameworks in parallel (naming / flashcard tech /
hosting) → deterministic **rename** script + link-checker + body-diff verification → **10 writer
sub-agents** (one per page) produced flashcard decks → merge → **10 adversarial reviewer sub-agents**
(many verified cites live against CourtListener) → merge → **Quartz v4.5.2** site (vendored `ts-fsrs`
UMD, static-asset study component, clean-URL Python server, launchd) → **puppeteer dogfood**
(desktop+mobile, Mermaid-as-SVG, flip/grade/persist) → served brief. **The biggest bottleneck was
CourtListener rate-limiting** during the review/verification fan-out — see §3.

---

## 2. The ingest pipeline (stages)
Run in order; cap each build↔fix loop at 3 passes. Full executable detail lives in the
`/cssi-ingest` command (`~/.claude/commands/cssi-ingest.md`).

1. **Snapshot** — timestamped `cp -R` backup of the vault to scratch.
2. **Collect** — `cp` `_inbox/*.md` to scratch, read. Empty → report "nothing to ingest" and stop.
3. **Segment & route** — each `## heading` = one chunk. Honor first-line hints `@new` /
   `@page: <Name>`; else route automatically (append to a matching page vs. propose a new one).
   **Surface every borderline/auto routing call in the report.**
4. **Verify (CourtListener)** — extract citations; verify existence+name + proposition; write/merge
   `_staging/<slug>.citations.json` with verdicts + corrections. **Governed by the rate-limit
   protocol in §3 — this is the throttle-sensitive stage.**
5. **Write / append** — writer sub-agent per target. New page = full conventions template. Append =
   integrate new **verified** material into the right sections, **additive only** (never delete or
   reword existing verified prose or `::` lines). Render + visually inspect any new Mermaid.
6. **Adversarial review** — reviewer sub-agent per target (accuracy/scope/atomicity/guardrails); ≤3
   passes; unresolved → `_review-needed/`.
7. **MOC** — add new pages to `index.md` in house style.
8. **Flashcards** — (re)generate decks for new/changed pages into `flashcard-src/decks/<slug>.json`
   (ids prefixed by page slug, kept stable so study progress survives) → review →
   `python3 flashcard-src/merge.py` (auto-bumps deck version; app migrates by id) → regenerate
   `.apkg` (`flashcard-src/make_apkg.py` via a `genanki` venv).
9. **Archive** — move processed `_inbox/*.md` → `_raw/<YYYY-MM-DD>-<label>.md`.
10. **Publish** — `~/Projects/cssi-quartz/redeploy.sh` (sync vault→content + rebuild; **no server
    restart needed**). Verify pages render, links resolve, internal dirs unpublished.
11. **Report (short)** — new pages; appends (what was added); cases verified + any UNVERIFIABLE;
    cards added (+ new deck version); anything in `_review-needed/`; the live URL; routing calls made.

---

## 3. ⚠ CourtListener rate-limit protocol (HARD RULE)
**CL verification is the run's biggest bottleneck. We must detect which account tier is live and
STOP if we're on the old one.**

- **Tiers:** OLD account = **5 requests/min**; NEW account = **20 requests/min**. (Per-hour ~50 on
  old.) **Cached reads of an already-fetched opinion are FREE** — only *new* lookups count
  (`analyze_citations`, `search`, first `read_document`/`search_document` of a given opinion).
- **Serialize CL calls.** Run all verification through **one serial path** (a single verifier doing
  calls one at a time) — **NOT** parallel verifier sub-agents. Parallel calls just hit the cap faster
  and make pacing/detection impossible. Log every CL call to `scratch/cl-calls.log`
  (epoch-seconds · endpoint · ok|throttled).
- **Tier probe (first ~minute).** Make the first **~8 distinct, uncached** CL calls back-to-back with
  no artificial delay, watching for a throttle (HTTP 429 / `"Request was throttled. Expected
  available in N seconds."`):
  - **Throttle fires with ≤7 calls in the trailing 60 s → OLD 5/min tier.**
    🛑 **STOP all CourtListener work immediately and TELL THE USER** — report calls-before-throttle,
    timestamps, and the throttle message, then await instructions. **Do not grind through a 5/min run.**
  - **≥8 distinct calls succeed in <60 s with no throttle → NEW ≥20/min tier confirmed.** Tell the
    user once ("✅ new tier confirmed — 8 calls in <60 s, no throttle"), then continue.
- **Pacing (new tier):** stay under 20/min — roughly **1 call / 3.2 s**, or bursts of ≤18 then pause
  to the minute boundary. Minimize calls: batch multiple citations into a single `analyze_citations`
  where possible; reuse cached opinion reads.
- **Mid-run throttle:** recompute trailing-60 s count. ~5 → old tier → **STOP + notify**. ~18–20 →
  new ceiling → wait the stated `Retry-After` seconds and continue (mention it; no need to stop).
- **Scope of the stop rule:** stop-and-notify is triggered by the **old 5/min tier only**. Hitting
  the new 20/min ceiling is expected — pace through it automatically.

---

## 3a. Case identification & research depth (HARD RULE — added Day 2)
Class captures are **shorthand and often misspell case names** (e.g., "Anchando" → *United States v. Erick Anchondo*, 156 F.3d 1043 (10th Cir. 1998)). A failed citation-lookup is **not** proof a case doesn't exist — it usually means the name/reporter as typed didn't match.

- **Never declare a case unfindable from one API miss.** Escalate the search: (1) CL `analyze_citations` on any reporter cite; (2) CL `search` by case name **and phonetic/spelling variants** (drop/swap letters, try last-name-only, try the other party); (3) CL `search` by the *proposition* (full-text `q=`) to find the case by what it says; (4) **web search** (Justia, Google Scholar, CourtListener, official court sites) when CL can't surface it — then re-locate the confirmed cite back in CL. Only after all of that may a case be marked `UNVERIFIABLE`, and then it is flagged, never asserted.
- **Research depth — round out each page, don't just transcribe cites.** Captured cases are the *seed*, not the ceiling. For every page the verifier/researcher must add: (a) the **controlling foundational SCOTUS authority** the doctrine rests on even if uncaptured (e.g., *Chimel* for SITA, *Schneckloth* for consent); (b) **significant related and recent cases**, including **weak-but-overused** ones officers rely on in the field (*Anchondo*) and current-term developments (*Lange*, *Caniglia*) — flagged for what they are. Keep the page digestible (½–1 page): add load-bearing authority, cut the rest. **Everything added is CL-verified like everything else.** Circuit splits get flagged; state cases stay illustrative-and-paired.
- This research is **rate-limited CL work** → it runs in the **serialized verifier/researcher path** (§3), not in the parallel writer fan-out. Web search is free/parallel and good for *discovery*; CL remains the *verification* of existence + proposition + verbatim quote.
- **Cluster-id ≠ opinion-id gotcha (recent cases).** `analyze_citations`/`search` return CLUSTER ids; `read_document`/`search_document` take an OPINION id. For post-~2015 cases the cluster id frequently **collides** with an unrelated old opinion id — reading the cluster id as an opinion id silently returns the WRONG case. Always resolve cluster → lead sub-opinion id first (the cluster endpoint via `get_endpoint_item`/`call_endpoint`, or take the opinion id from a `search` result) and **confirm the case name in the returned text before trusting any quote.** (Day-2: hit on Lange, Caniglia, Rodriguez, Gant, Heien, Morley, Collins, Davis, Braxton, and the digital cases.) Note also the new CL account tier (≥20/min) was confirmed live on Day 2.

## 4. Infrastructure & paths
| Thing | Path / value |
|---|---|
| Obsidian vault | `~/Library/Mobile Documents/com~apple~CloudDocs/Main/CSSI` |
| Inbox (captures) | `…/CSSI/_inbox/` · cheat-sheet `_inbox/README.md` |
| Raw archive / staging / escalations | `_raw/` · `_staging/` · `_review-needed/` |
| Rulebook | `…/CSSI/_conventions.md` |
| Quartz project | `~/Projects/cssi-quartz` |
| Site content (copy of vault) | `…/cssi-quartz/content/` |
| Flashcard source + tools | `…/cssi-quartz/flashcard-src/` (`decks/`, `merge.py`, `make_apkg.py`, briefs) |
| Published deck / apkg | `…/cssi-quartz/quartz/static/flashcards/flashcards.json` · `…/cssi-search-and-seizure.apkg` |
| Rebuild | `~/Projects/cssi-quartz/redeploy.sh` |
| Live site (persistent) | `http://johns-mac-studio.tail2e4945.ts.net:8787` (launchd `com.cssi.quartz`) |
| CourtListener tools | `ToolSearch` → `select:mcp__claude_ai_CourtListener__search,…analyze_citations,…read_document,…search_document` |

---

## 5. Guardrails (carried from `_conventions.md`)
Federal, criminal-suppression focus; never blur federal/state law (SCOTUS binding · circuits
persuasive, flag splits · state illustrative-only and paired with federal authority). Back up before
writing. **Additive-only** edits to existing verified pages — never destructive; don't touch existing
`::` flashcards or prose. Never introduce unverified legal content or invent citations; English/
colonial cases stay non-binding history; **never assert Holiday/McCall/Smith**. Mnemonics (C.R.E.W.,
Strive for Five, 3 Golden Rules) are verbatim maxims, never citation-attached. Keep context thin.

---

## 6. Running an ingest
- In-session: `/cssi-ingest [lunch|eod]`.
- Fresh thread: paste the **ingest wrapper** (a self-contained prompt that points a clean context at
  this runbook + the inbox + the §3 rate-limit rule). Using a fresh thread keeps context clean and is
  the recommended way to run lunch/EOD ingests.
