CSSI — FINAL QA & HARDENING PASS (autonomous, spec-driven, orchestrator-led)

You are the ORCHESTRATOR for an exhaustive final QA pass over the CSSI wiki (CSSI =
Certified Search & Seizure Instructor; FEDERAL criminal-suppression 4A/5A/6A course for
police instructors). The wiki is already built + published (commit 496c225: 42 pages incl.
Case Index; deck v2026-06-25.2 @ 1643 cards). This pass HARDENS it to a finished product.

>> READ FIRST, in order:
   1. ~/Projects/cssi-quartz/docs/FINAL-QA-SPEC.md  ← THE GOVERNING SPEC. Follow it exactly:
      §0 (process shortfalls this pass must catch), §2 (the find→adjudicate→fix layer),
      §3 (the 12 check dimensions D1–D12), §4 (phases P0–P5), §5 (CL protocol), §6 (scope),
      §7 (artifacts), §8 (definition of done).
   2. ~/Projects/cssi-quartz/docs/RUNBOOK.md  ← §3 CourtListener rate-limit, §3a misspelling/
      cluster-id≠opinion-id gotcha, §5 guardrails.
   3. The vault rulebook: "~/Library/Mobile Documents/com~apple~CloudDocs/Main/CSSI/_conventions.md".

RUN AUTONOMOUSLY TO COMPLETION. Do NOT interview me — where you'd ask, run a structured
self-interview (red-team / steel-man / adjudicate, written to the ledger) and proceed; the
timestamped backup makes it reversible. Surface every consequential call in the final report.

NON-NEGOTIABLES (full detail in the spec):
- BACKUP the vault first (timestamped cp -R to scratch).
- ORCHESTRATOR = THIN. All work in fresh sub-agents; hand off via small files on disk; never
  load the whole vault into one context. PARALLELIZE the free phases (review, fix, sweeps)
  with the Workflow tool — one well-scoped fan-out per phase, read results, adjudicate, then
  launch the next.
- ALL CourtListener through ONE SERIAL LANE (concurrency-1). NEVER fan out CL — not in review,
  not in adjudication. Re-probe the tier; STOP + tell me on the old 5/min tier. Log every call.
- ADJUDICATION LAYER: REVIEW (no CL) → ADJUDICATE (serial CL for legal findings; free editor
  for the rest) → FIX (apply only adjudicated fixes). Never change a legal assertion without
  CL evidence. Log dismissed false-positives. EXHAUSTIVE via an assertion inventory (every
  case/quote/pinpoint/CL-URL/framing/diagram is a tracked item with a verdict) — not sampled.
- TWO-KEY rule + GUARDRAILS (federal binding · circuits persuasive+labeled · state illustrative+
  paired; never blur fed/state; English/colonial = history; NEVER assert the apocryphal
  Holiday/McCall/Smith — but the real US v. Smith geofence case IS legitimate; mnemonics verbatim
  + uncited; NO inline ## Flashcards on pages).
- REUSE prior verification (the _staging manifests + ~506 CL calls of confirmed data). Target
  fresh CL at: good-law currency on every asserted case (batch via analyze_citations), every
  unconfirmed quote/pinpoint, every CL-URL's correctness, and the D3 new-frontier research
  (issues of first impression / splits beyond SCOTUS — ok to expand outside SCOTUS).
- DECK STAYS UNCHANGED (1643 cards): do NOT add cards for recent-application circuit cases
  (user decision). DO regenerate the Case Index from the updated manifests (D12).
- iCloud EPERM: the Read tool fails on the vault path — cp vault files to scratch to read,
  write in scratch + cp back. Files under ~/Projects/cssi-quartz/ read fine.
- Loop cap 3 per item → escalate to _review-needed/<slug>.md. Checkpoint a resumable QA-LEDGER
  after every sub-phase.

ARTIFACTS (in vault _run/, mirror durable): QA-LEDGER.json, qa-findings.json,
qa-adjudications.json, assertion-inventory.json, FINAL-QA-REPORT.md.

FINISH: render + visually inspect EVERY Mermaid; verify every wikilink + every CL URL resolves
to the correct case; cross-page consistency audit; completeness sign-off vs the inventory;
regenerate Case Index. Then PUBLISH (sync vault→content via redeploy.sh which validates the
build; commit + push origin main → Vercel auto-deploys https://cssi-search-and-seizure.vercel.app;
GH noreply identity) and VERIFY live (pages 200, internal dirs _run/_staging/_raw/_inbox/
_conventions NOT published, Mermaid renders, CL links resolve, deck version intact). Then a
SHORT report (accuracy summary; every negatively-treated case; every split/frontier surfaced;
completeness sign-off; anything in _review-needed/) and offer a /brief.
