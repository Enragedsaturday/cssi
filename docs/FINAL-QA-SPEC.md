> ## ⊘ SUPERSEDED — authority transferred to `docs/STANDARDS.md`
>
> **This document is superseded by [`docs/STANDARDS.md`](./STANDARDS.md)** (SR-3 supremacy).
> Its authority has been **absorbed** into STANDARDS.md: the §0 adversarial self-critique and
> the §3 **D1–D12** reviewer dimensions are carried forward there (now extended to **D1–D14**),
> and the §2 find→adjudicate→fix machine is adopted there verbatim.
>
> This file is **retained for historical reference only.** On any conflict,
> **`docs/STANDARDS.md` governs.** Do not treat anything below as current authority —
> consult STANDARDS.md instead.

---

# CSSI — Final QA & Hardening Pass (SPEC)

*A definitive, exhaustive accuracy + completeness + framing + shepardize pass over the whole CSSI wiki, run in a fresh context. Spec-driven, orchestrator-led, serial-CL, with a true adjudication layer. Author: prior build orchestrator. The build that produced the current state shipped at commit `496c225` (42 pages incl. Case Index; deck v2026-06-25.2 @ 1643 cards; ~506 CL calls to date).*

---

## §0. Adversarial review of the CURRENT process — shortfalls this pass must catch
*(This is the "why" of the spec. The build was good but fast; here is where it can be wrong. Each shortfall maps to a check below.)*

1. **Holdings stated from deck-derived paraphrase, not freshly quote-verified.** Many cases on the new pages were asserted by a *holding written in the writer's words*, derived from "Name That Case" deck holdings verified at NTC-time — not re-confirmed verbatim against the opinion when the doctrine page was written. → **Paraphrase drift risk.** Re-verify every stated proposition against the opinion. (D1)
2. **Cross-list framings came from WEB scouts, not verified holdings.** The "Related cases across doctrines" relevance lines were authored by web-discovery agents and only spot-checked against the one-line Case Index. → Framing imprecision / overstatement risk. Re-check each framing against the actual holding. (D2)
3. **Web-discovery had a real error rate.** The shepardize scouts produced a backwards holding (*Moore-Bush*), invented frameworks (*Mayville/Lyle/Small*), garbled cites, and 4 non-existent cases — caught only because serial CL re-checked them. → **Treat ALL non-CL-verified content as suspect.** Anything not confirmed by the single CL lane is unverified.
4. **Pinpoints not all independently re-confirmed.** A wrong pinpoint (e.g., "469 U.S. at 341") is an instructor-credibility killer. → Confirm every pinpoint that accompanies a quote. (D7)
5. **CL opinion URLs vs cluster/slug + cluster≠opinion gotcha.** Some links were corrected mid-run; the 2026 cases hit CL ID mismatches. → Confirm every CL URL resolves AND points to the *named* case. (D7)
6. **Mermaid only partially visually inspected.** 15/15 new diagrams rendered; only ~3 were eyeballed for doctrinal accuracy; the 25 pre-existing diagrams were not re-inspected this run. → Render + visually inspect EVERY diagram; cross-check each node against the page's stated rule. (D8)
7. **Cross-page inconsistency risk (new with cross-listing).** The same case now appears on multiple pages with different framings. → Shared cases must be framed consistently, good-law treatment stated consistently, and overruled cases (*Aguilar/Spinelli, Jones-1960, Michigan v. Jackson*) shown as history EVERYWHERE they appear. (D5)
8. **Good-law currency.** Confirmed at build/shepardize time; law moves (esp. the 2024–2026 and pending items). → Re-confirm current validity for every asserted case. (D3)
9. **Completeness was IA-time, not page-time.** The completeness critic proposed *cases* to add; it did not audit whether each page explains the doctrine's *elements, burden, standard of review, remedy, and operational application*. → Per-doctrine completeness against a checklist. (D4)
10. **Sampling, not exhaustiveness.** Phase 8 re-verified a 31-case sample. The user now wants EVERY asserted case/fact/statement reviewed. → This pass is **exhaustive**, tracked by an assertion inventory.
11. **Reviewers fixed in place with no separate adjudication.** A reviewer could over-correct (false positive) or a fixer could mis-apply. → Separate **find → adjudicate → fix**; never change a legal assertion on a reviewer's say-so without CL evidence.
12. **A parallel-CL leak occurred** (enrichment reviewers each hit CL). → Re-assert: ALL CL through ONE serial lane, always.
13. **The 8 practical/reference/history pages** (CREW, Three Golden Rules, Instructor Development, Common Law Origins, Common Legal Terms, Analysis Checklist, Federal Court System, Legal Research) were not re-touched. → Sanity-check them (mnemonic verbatim, glossary accuracy, no rot, guardrails). (D11)
14. **Deck/Case Index drift.** Pages changed; the deck and the generated Case Index did not. → Verify deck↔page integrity and **regenerate the Case Index**. (D12)
15. **Pedagogy not separately audited.** This is an *instructor* course; legal accuracy ≠ teachability. → A teachability dimension. (D9)

---

## §1. Operating principles (carry-over + hardening)
- **Backup FIRST**: timestamped `cp -R` of the vault to scratch before any edit. Everything reversible.
- **Orchestrator = thin.** Main thread holds the ledger/specs/statuses only. All work in fresh sub-agents; handoffs are small files on disk. Never load the whole vault into one context.
- **ALL CourtListener through ONE serial lane** (concurrency-1). NEVER fan out CL — not in review, not in adjudication. Re-probe the tier first (§3 of `docs/RUNBOOK.md`); STOP + notify on the old 5/min tier. Log every call to `scratch/cl/cl-calls.log`.
- **Reuse prior verification.** 19 staging manifests + 15 final manifests + the enrichment results are manifest-grade ground truth. Do NOT re-verify what is already confirmed unless a finding flags it. Target fresh CL at: good-law currency, unconfirmed quotes/pinpoints, flagged propositions, CL-URL correctness, and new-frontier research.
- **Two-key rule** still governs every asserted case (existence + proposition + verbatim pinpoint where quoted, AND good-law). **Never change a legal statement without CL evidence.**
- **Guardrails (D6).** Federal criminal-suppression focus; SCOTUS binding · circuits persuasive (label the circuit, flag splits) · state illustrative-only + paired with federal authority; never blur fed/state; English/colonial = non-binding history; **NEVER assert Holiday/McCall/Smith** (the apocryphal trio — but the real *United States v. Smith* geofence case is legitimate); mnemonics (C.R.E.W., Strive for Five, 3 Golden Rules) verbatim + uncited; **no inline `## Flashcards` on pages** (deck-only now).
- **Additive to verified substance**; do not delete confirmed prose/quotes without an adjudicated reason. Preserve flashcard ids.
- **Loop cap 3**, then escalate to `_review-needed/<slug>.md` with the open issue. Checkpoint the ledger after every sub-phase (resumable). Surface consequential calls in the final report.
- **iCloud EPERM:** the Read tool fails on the vault path → `cp` vault files to scratch to read, write in scratch + `cp` back. Files under `~/Projects/cssi-quartz/` read fine.

---

## §2. The review → adjudicate → fix model (the adjudication layer)
The defining upgrade. Three separated roles; a legal assertion never changes on a reviewer's opinion alone.

1. **REVIEW (parallel, free, NO CL).** Per page, dimensional reviewers emit structured FINDINGS. A finding =
   `{id, page, dimension(D1–D12), locator(section + the verbatim text), problem, severity(high|med|low), proposed_fix, needs_cl(bool), confidence}`.
   Reviewers may NOT edit pages. They surface, they don't decide.
2. **ADJUDICATE.** Every finding is adjudicated to `UPHELD | MODIFIED | DISMISSED | ESCALATE` with `adjudicated_fix` + `evidence`.
   - Findings with `needs_cl=true` (good-law, proposition, quote/pinpoint, case existence, CL-URL, new-frontier) → adjudicated by the **SINGLE serial CL lane**, and the verdict MUST cite CL evidence (a confirmed pinpoint/quote or treatment). No CL evidence → cannot UPHOLD a change to a legal assertion (→ DISMISS or ESCALATE).
   - Findings that are non-legal (formatting, structure, missing cross-link, internal contradiction, pedagogy, completeness-gap that the corpus already supports) → adjudicated by a free editor-adjudicator.
   - **DISMISSED findings are logged with the reason** (defends against over-correction; a dismissed false-positive is a successful outcome).
3. **FIX (parallel, free).** Per page, a fixer applies ONLY `UPHELD`/`MODIFIED` adjudicated fixes, verbatim from the adjudication. `ESCALATE` → `_review-needed/`. The fixer introduces no new content of its own.

---

## §3. Check dimensions (each finding is tagged with one)
- **D1 — Accuracy / two-key (exhaustive).** Every asserted case, holding, fact, statement, quote, and pinpoint must trace to the opinion/manifest. Re-confirm each stated proposition matches the case (catches paraphrase drift). Every quotation must be verbatim with a correct pinpoint or be de-quoted. *Acceptance:* every assertion in the inventory has a verdict; zero unverified legal claims asserted as settled.
- **D2 — Framing.** Is each case framed correctly *for the doctrine of THIS page* (especially cross-listed cases)? Are the doctrine's relevant **details, nuances, and pitfalls** actually explained (not just named)? *Acceptance:* no framing contradicts/overstates the real holding; nuances & pitfalls are substantive and doctrine-specific.
- **D3 — Shepardize + new frontier (may expand beyond SCOTUS).** Still valid law? Has it been overruled/abrogated/limited/criticized? Have lower courts split, narrowed, or extended it? Are there **issues of first impression** in the doctrine that no SCOTUS case resolves but circuits/states are grappling with (or have not yet reached) — the live frontier? *Acceptance:* current good-law status recorded for every case; genuine splits/restrictions/frontiers surfaced and labeled (circuit = persuasive); nothing stale asserted as current.
- **D4 — Completeness.** Is the doctrine FULLY explained for an instructor? Per-doctrine checklist: black-letter rule · its elements/prongs · burden of proof + who bears it · standard of review · the controlling SCOTUS authority + significant progeny by role · limits/exceptions · nuances · common pitfalls · recent developments · cross-links · the operational "apply it" angle. *Acceptance:* no checklist item missing without a logged reason; gaps the corpus can fill are filled (verified).
- **D5 — Internal consistency & cross-page coherence.** Shared/cross-listed cases framed consistently across pages; good-law treatment stated consistently; overruled cases shown as history everywhere; no contradictory statements between pages; boundary sentences where pages overlap. *Acceptance:* a shared-case audit shows no conflicts.
- **D6 — Guardrails.** (See §1.) *Acceptance:* federal/state never blurred; every circuit case labeled persuasive; no apocryphal trio; mnemonics uncited; no inline flashcards.
- **D7 — Citation hygiene.** Bluebook consistency; pinpoint present wherever a quote appears; every CourtListener URL **resolves (200) AND shows the named case** (guards cluster≠opinion). *Acceptance:* all cites Bluebook-consistent; all CL URLs correct.
- **D8 — Visual accuracy.** Render EVERY Mermaid diagram (mermaid-cli + system Chrome → PNG) and **visually inspect each**; every node/branch matches the page's stated rule; correct cases labeled; compact/legible. *Acceptance:* all diagrams render, inspected, and doctrinally faithful.
- **D9 — Pedagogy / teachability.** Rule-first clarity; the "why"; operational application; instructor pitfalls; the "change the facts, change the outcome" habit where apt. Instructor voice; digestible (≈½–1 page core, recent-developments may extend). *Acceptance:* each page teaches, not just states.
- **D10 — Structure / spec compliance.** Template sections present + ordered (Rule · Key cases · Related cases across doctrines · Nuances & limits · Common pitfalls · Visual · Recent developments · Sources); frontmatter correct (single controlling amendment; aliases for renamed pages); in the MOC. *Acceptance:* structurally uniform.
- **D11 — Practical/reference/history pages.** The 8 non-case pages: mnemonics verbatim, glossary terms accurate, court-system/research facts correct, English/colonial framed as history, no rot. *Acceptance:* accurate + guardrail-clean.
- **D12 — Deck ↔ page ↔ index integrity.** No orphaned deck cards (page/source pointing to removed content); card `page`/`source` valid; **regenerate the Case Index** from the (now-updated) manifests; Case Index links resolve to correct cases + home pages. *Acceptance:* deck consistent; Case Index regenerated + correct. (Do NOT add cards for recent-application circuit cases — user decision: keep them out of the deck.)

---

## §4. Execution phases (each ends with a gate + ledger checkpoint)
- **P0 — Bootstrap & assertion inventory.** Backup the vault. Re-probe CL tier (STOP on old). Load prior LEDGER/manifests/Case Index/this spec. **Build the assertion inventory** (deterministic, free): extract from every page every (case-cite, quoted passage + pinpoint, CL URL, cross-list framing, mermaid block). This is the exhaustive target list and the completeness gate. *Gate:* inventory built; tier OK.
- **P1 — Dimensional review (parallel fan-out, free).** Per page (tiered: full on the 33 case-bearing doctrine pages incl. Exigent; sanity on the 8 practical/reference/history pages; + Case Index + MOC), reviewers across D1–D12 emit findings. *Gate:* every page reviewed; findings collected.
- **P2 — Adjudication.** (a) Serial-CL adjudication of all `needs_cl` findings + the PROACTIVE CL sweeps that run regardless of findings: good-law re-confirm on every asserted case (batch via `analyze_citations`), confirm every unconfirmed quote/pinpoint, confirm every CL-URL resolves to the right case, and the **new-frontier research** (D3). (b) Free editor-adjudication of non-legal findings. *Gate:* every finding has a verdict + evidence; CL log shows no old-tier throttle.
- **P3 — Fix (parallel fan-out, free).** Apply adjudicated fixes per page; escalate unresolved to `_review-needed/`. Loop cap 3. *Gate:* all UPHELD/MODIFIED applied; escalations logged.
- **P4 — Final sweeps.** Render + visually inspect ALL Mermaid (D8); link-check all wikilinks + verify all CL URLs (D7); shared-case cross-page consistency audit (D5); completeness sign-off vs the assertion inventory (every item has a verdict); regenerate Case Index + deck-integrity check (D12). *Gate:* all sweeps pass or escalate.
- **P5 — Publish & verify & report.** Sync vault→content (`redeploy.sh`), commit + push origin main (Vercel), verify live (pages 200, no internal 404s, internal dirs unpublished, Mermaid renders, CL links resolve, deck version intact). Short report + offer a `/brief`.

---

## §5. CourtListener protocol & budget
Serial lane only; `docs/RUNBOOK.md` §3 (tier probe, pace <20/min, STOP on old tier) + §3a (misspelling-tolerant ID, cluster-id≠opinion-id — confirm the case NAME in returned text before trusting any quote; resolve cluster→lead opinion id for post-2015 cases). If the MCP OAuth token expires, fall back to the no-auth REST API `https://www.courtlistener.com/api/rest/v4/search/?type=o&q=...`. **Minimize calls:** reuse manifest-grade data; batch good-law checks via `analyze_citations`; only read opinions for unconfirmed quotes/propositions/frontiers. Budget expectation: this is the heaviest pass — possibly several hundred calls — so run it patiently in serial batches and checkpoint continually.

## §6. Scope & tiering
- **Full depth:** the 33 case-bearing doctrine pages (the 32 enriched + any case page missed). All D1–D10.
- **Sanity depth:** the 8 practical/reference/history pages (D11 + D1 accuracy + D6 guardrails).
- **Generated:** Case Index (regenerate, verify) + `index.md` MOC (accurate, all links resolve).
- New pages may be added only if completeness reveals a genuinely missing doctrine — adjudicate + verify like everything else; rare.

## §7. Artifacts (in `_run/`, mirrored durably)
- `QA-LEDGER.json` — per page: dimension verdicts, findings, adjudications, fixes, escalations, status. Resumable.
- `qa-findings.json` / `qa-adjudications.json` — the full find→adjudicate trail (incl. DISMISSED + reasons).
- `assertion-inventory.json` — every tracked assertion + its final verdict (the exhaustiveness proof).
- `FINAL-QA-REPORT.md` — accuracy summary, every negatively-treated case, every split/frontier surfaced, completeness sign-off, escalations.

## §8. Definition of done
Every asserted case/fact/quote/pinpoint in the inventory is adjudicated with a verdict; no legal assertion changed without CL evidence; every page passes D1–D12 (tiered) or has a logged `_review-needed` escalation; every Mermaid inspected + faithful; every CL URL resolves to the correct case; shared cases consistent across pages; each doctrine completeness-signed-off; Case Index regenerated; deck integrity confirmed (no new cards); published + verified live; report delivered. Anything unresolved after 3 passes sits in `_review-needed/` — never silently dropped.

---

## Key paths
- Vault `~/Library/Mobile Documents/com~apple~CloudDocs/Main/CSSI` (pages = root `*.md`; `_conventions.md`; `_run/` ledger+specs; `_staging/` manifests; `_raw/`; `_review-needed/`).
- Project `~/Projects/cssi-quartz` · content `content/` · decks `flashcard-src/decks/` + `merge.py` + `make_apkg.py` (`.venv`) · study app `quartz/static/flashcards/app.js` (IndexedDB) · published deck `…/flashcards.json` · this spec `docs/FINAL-QA-SPEC.md` · runbook `docs/RUNBOOK.md`.
- Mermaid render: write body to `in.mmd`; `npx -y -p @mermaid-js/mermaid-cli mmdc -i in.mmd -o out.png -p pptr.json -b white -w 1000`; `pptr.json` → `executablePath` = chrome-headless-shell under `~/.cache/puppeteer`, `args ["--no-sandbox","--disable-setuid-sandbox"]`; then visually Read the PNG.
- Publish = Vercel CI/CD: commit + push origin main (repo `Enragedsaturday/cssi`) → Vercel builds + deploys https://cssi-search-and-seizure.vercel.app (~2–3 min). GH noreply commit identity. `redeploy.sh` syncs vault→content + builds locally (validates before push) + refreshes the Tailscale site.
