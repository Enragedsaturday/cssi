# CORRECTION / POST-CAPTURE INGEST — *Chatrie v. United States* (SCOTUS, June 29, 2026)

> **Feed this to the CSSI overhaul build after the current run completes and commits.**
> It is a single-finding correction + ingest order. It supersedes the "pending before the
> Supreme Court / unresolved circuit split" framing for geofence / Google Location History
> everywhere it appears. Slot it into S5 (post-capture ingest) and flag the page-body edits
> for S6; it does **not** require restarting the in-flight run.

- **Finding owner:** out-of-band (human + research pass, 2026-06-30)
- **Diagnostic class:** **6 (too-recent / post-capture)** + **7 (frontier-not-run, now *resolved*)** — see S5 · R4.
- **R6 inclusion verdict:** new **Binding — SCOTUS** anchor on a live, taught question → **earns a standalone BIRAC page** + reframes existing doctrine pages. Not annotation-only.

---

## 1. The finding (what changed)

On **June 29, 2026** the Supreme Court decided ***Chatrie v. United States*, No. 25-112, 609 U.S. ___ (2026)** (argued Apr. 27, 2026). The build currently has this case **only as "pending / argued / not yet decided,"** because the decision landed one day after the last research pass on the digital-frontier pages. It is now decided and must be ingested.

**Holding (web-sourced — confirm verbatim against the slip op before authoring quotes/pincites):**
- Acquiring a cell-phone user's **Google Location History (geofence) data *is* a Fourth Amendment search.** A person has a **reasonable expectation of privacy in records of his phone's location**, and police intrude on it when they demand that data — **even for a short time** (~2 hours here) and **even though held by a third party** (rejecting the Fourth Circuit panel's "voluntarily shared / opt-in / third-party doctrine" rationale; applying/extending *Carpenter*).
- The Court **did NOT hold geofence warrants categorically unconstitutional.** It **expressly declined** to decide whether *this* geofence warrant satisfied the Fourth Amendment's **probable-cause and particularity** requirements.
- **Disposition: vacated and remanded to the Fourth Circuit** for the PC/particularity question.
- Reported **6–3, Kagan, J.** (majority). *Vote split, authorship of any concurrences/dissents, and whether the Court touched good-faith — CONFIRM against the slip op.*
- Decision below: **136 F.4th 100 (4th Cir. en banc)** (the 7–7 equally-divided affirmance on whether a search occurred).

**Net doctrinal effect:** the threshold "is obtaining geofence Location History a *search*?" question — which the pages frame as an **open circuit split now before SCOTUS** (5th Cir. *Smith* = yes vs. 4th Cir. en banc *Chatrie* = fractured) — is **RESOLVED: it is a search.** The **new open question** is the one SCOTUS remanded: **probable cause + particularity of geofence warrants.**

---

## 2. VERIFICATION STATUS — read before ingesting

- **L2 (web discovers): DONE.** Sources at the bottom of this file.
- **PRIMARY SOURCE for authoring = the slip opinion**, not CourtListener:
  `https://www.supremecourt.gov/opinions/25pdf/25-112_0am4.pdf`
  Pull the holding statement, disposition, vote, and any verbatim quotes + pin cites from the slip op. Cite as slip op. until a reporter/CL cite is clean.
- **L3 / L4 (CourtListener confirm): BLOCKED — do not trust CL for this case yet.**
  - CourtListener has **no clean SCOTUS *Chatrie* object.** A docket search for *Chatrie* at `scotus` returns **zero**.
  - ⚠️ **DO NOT INGEST CL opinion `10881683`.** Its search-index entry is **corrupted**: it displays as "Chatrie v. United States / SCOTUS / 2026-06-29 / 25-112" but the underlying opinion → cluster `10415095` → docket `68534185` actually resolves to ***Harmon v. ABC 2 News Station*, E.D. Wis., 2:24-cv-00600** (a 2024 civil case). It is the wrong object.
  - **Action:** mark every new/edited Chatrie reference `CL-confirm: pending (slip-op sourced)`. Re-poll CL in a few days; when a clean cluster appears (verify `case_name` contains "Chatrie," `court = scotus`, `docket = 25-112` **before** trusting it), backfill the CL permalink and run the normal good-law check. The existing CL links to the **4th Cir.** opinions (`10265776`, and the 2025-04-30 en banc `10443725`, 136 F.4th 100) and the **5th Cir.** *Smith* (`10036119`, 110 F.4th 817) remain valid for those lower-court entries.

---

## 3. Action A — create the case page

**File:** `content/cases/Chatrie v. United States.md` (none exists yet; the three existing `Smith v. *` pages are unrelated). Author via the **S4 BIRAC generator**, with:

- **Treatment line:** `*609 U.S. ___ (2026)* (No. 25-112) · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*`
- **Frontmatter:** `as_of: 2026-06-30`; `holding:` one-liner =
  *"Acquiring a cell-phone user's Google Location History (geofence) data is a Fourth Amendment search — there is a reasonable expectation of privacy in records of one's phone's location, even for a short period and even when held by a third party; the Court did not decide whether geofence warrants satisfy probable cause and particularity, vacating and remanding."*
- **BIRAC body:** Background (Midlothian, VA credit-union robbery, May 20, 2019; June 14 geofence warrant to Google, 150-meter radius) · Issue (is executing a geofence warrant for Location History a 4A search?) · Rule (REP in phone-location records; third-party/opt-in rationale rejected; *Carpenter* applied) · Application · Conclusion (vacated & remanded; PC/particularity left open).
- **Cross-links / homes:** anchor on `[[Two Definitions of Search]]`; also `[[The Third-Party Doctrine and Digital Surveillance]]`, `[[The Warrant Requirement]]`, `[[Plain View Doctrine]]`, `[[Standing to Challenge a Search]]`, `[[The Exclusionary Rule]]`, `[[Fourth Amendment Framework]]`. Companion: `[[Carpenter v. United States]]` (Anchor/Progeny). Cross-reference the 4th Cir. en banc below (superseded) and 5th Cir. *Smith* (search-question result now confirmed; categorical-unconstitutionality holding **not** adopted).
- Quotes/pincites: **slip op only**, `CL-confirm: pending`. Do not fabricate a U.S. Reports page number.

---

## 4. Action B — reframe the doctrine pages (S6 edits)

Each page currently treats the geofence **search** question as an **open split pending at SCOTUS**. Change all of them to: **RESOLVED — *Chatrie* (2026) holds it is a search; geofence warrants NOT categorically unconstitutional; PC/particularity remanded.** Re-tier the controlling authority from "persuasive circuit law" to **Binding — SCOTUS** (the *4th Cir. opinions stay persuasive/superseded*; the new SCOTUS opinion is the binding anchor). Keep the `⚖` marker but relabel the search-question split **"resolved (Chatrie 2026)"**; the live `⚖` split is now **PC/particularity on remand**.

| # | File | Stale anchors |
|---|------|---------------|
| 1 | `content/3-what-is-a-search/Fourth Amendment Framework.md` | intro "…now before the Supreme Court, with the circuits split…" (~L77); "Chatrie v. United States — *pending before the Supreme Court*" bullet (~L79); 4th/5th Cir. bullets (~L80–81). **Moore-Bush (pole-camera, ~L82) is NOT disturbed by Chatrie — leave, but note it remains the open pole-camera question.** |
| 2 | `content/3-what-is-a-search/Two Definitions of Search.md` | "Chatrie — *pending before the Supreme Court*" bullet (~L67); panel bullet (~L68); "*(cert. granted, No. 25-112)*" source line (~L83). **This is Chatrie's anchor doctrine page** — add the holding here in full. |
| 3 | `content/6-warrant-requirement/The Warrant Requirement.md` | "Chatrie — *pending before the Supreme Court*" bullet (~L93); 4th/5th Cir. bullets (~L95). Frame the **remanded PC/particularity** question as the live warrant-law issue. |
| 4 | `content/7-exceptions-warrant/7a-pc-needed/Plain View Doctrine.md` | intro "…the geofence question they split on is now squarely before the Supreme Court" (~L95); Chatrie/Smith bullets (~L97–98); source lines (~L111, L115). |
| 5 | `content/8-exclusionary-rule-remedies/Standing to Challenge a Search.md` | intro "…the Supreme Court has now stepped in" (~L70); the *Smith/Chatrie* threshold note (~L70); Chatrie/Smith bullets (~L73–74). |
| 6 | `content/8-exclusionary-rule-remedies/The Exclusionary Rule.md` | intro "…that split is now before the Supreme Court" (~L95); Chatrie/Smith bullets (~L97–98). Note the **good-faith** angle: confirm whether Chatrie addressed *Leon* on remand framing. |

**Also check (re-grep, don't trust this list alone):** `content/cases/Carpenter v. United States.md` and `content/7-exceptions-warrant/.../The Third-Party Doctrine and Digital Surveillance.md` for any "split pending / before SCOTUS" geofence language.

Exhaustiveness sweep:
```
grep -rniE "geofence|location history|chatrie|25-112|pending before the supreme court|now before the supreme court|teed up|squarely before" content/
```

**Smith (5th Cir., 110 F.4th 817) — re-tier decision (R6 gate / USER):** its "is it a search" holding is now **confirmed/subsumed** by *Chatrie*; its **"geofence warrants are modern-day general warrants / categorically unconstitutional"** holding was **NOT adopted** by SCOTUS and is now the persuasive minority position feeding the **remand** question. Recommend Smith **stays a doctrine-page mention/foil** (reframed), not a standalone page — but flag for the R6 gate rather than deciding unilaterally.

---

## 5. Action C — update S5 coverage + ledger artifacts

- **`_overhaul/coverage/annotate-queue.md` — Cluster 1 (geofence/pole-camera):** rewrite. The **Smith ↔ Chatrie search-question split is RESOLVED by SCOTUS** → promote *Chatrie* out of the annotate-only cluster into a **full page** (Action A). **Moore-Bush (long-term pole-camera) stays** as an open-question annotation (Chatrie did not reach it). New open frontier to annotate = **geofence-warrant PC/particularity on remand.**
- **`_overhaul/coverage/borderline.md` / `missed-cases.md`:** update the geofence-cluster lines to reflect "Chatrie = SCOTUS, ingested as page (post-capture, class 6/7)."
- **`_overhaul/coverage/omissions.md`:** add an entry — *Chatrie* SCOTUS (2026-06-29) ingested post-capture as a new Binding-SCOTUS anchor; CL-confirm pending; nothing dropped.
- **`_overhaul/ledger/ORCHESTRATION.md` — S5 tracker:** log a "post-capture SCOTUS ingest: Chatrie 25-112" line; carry an **S6 flag** for the six page reframes; carry an **S9 flag** for the CL-confirm backfill + good-law recheck.

---

## 6. Acceptance checks

- [ ] No remaining `pending before the Supreme Court` / `not yet decided` / `now before the Supreme Court` for Chatrie/geofence anywhere in `content/` (re-grep).
- [ ] Every geofence **search-question** `⚖ Circuit split` reframed as **resolved (Chatrie 2026)**; remaining live split = **PC/particularity on remand**.
- [ ] `content/cases/Chatrie v. United States.md` exists, **Binding — SCOTUS**, BIRAC-complete, slip-op-sourced, `CL-confirm: pending`, passes S4 lint (treatment line + `holding:` + pinpoint discipline).
- [ ] Case Index regenerated to include the Chatrie row (LINT-6 clean).
- [ ] `npx quartz build` succeeds; no broken inbound links/aliases to the new page; all six reframed pages still resolve their `[[...]]` anchors.
- [ ] CL backfill ticket recorded for S9 (re-poll CourtListener; verify a clean `scotus / 25-112 / Chatrie` object before trusting; **never** ingest opinion `10881683`).

---

## 7. Secondary watch-item (UNVERIFIED by this finding — re-check, do not assume)

The same stale-able "pending before the Supreme Court" pattern appears for at least one other case:
- **`content/4-what-is-a-seizure/Seizure of the Person.md` (~L61): *United States v. Carter* — "pending before the Supreme Court (cert petition No. 25-885)."** I did **not** verify Carter's status. While correcting Chatrie, re-poll every `pending before the Supreme Court` marker (`grep -rni "pending before the supreme court" content/`) against current SCOTUS data and update any that have since been decided or denied.

---

## Sources

- **Slip opinion (PRIMARY):** <https://www.supremecourt.gov/opinions/25pdf/25-112_0am4.pdf>
- SCOTUSblog case page: <https://www.scotusblog.com/cases/chatrie-v-united-states/>
- Justia, *Chatrie v. United States*, 609 U.S. ___ (2026): <https://supreme.justia.com/cases/federal/us/609/25-112/>
- Faegre Drinker, "Supreme Court Decides *Chatrie v. United States*": <https://www.faegredrinker.com/en/insights/publications/2026/6/supreme-court-decides-chatrie-v-united-states>
- Question presented / decision below (136 F.4th 100): <https://www.supremecourt.gov/qp/25-00112qp.pdf>
