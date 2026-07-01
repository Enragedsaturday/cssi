# S7 — Term → Pages Occurrence Map (glossary wiring)

status: BUILT (anchorize + author half of S7)
depends-on: [S6 finalized page text, S7 anchorized glossary]
gates: [Phase-2 wiring sweep (R8/R11)]
last-updated: 2026-06-30
scope: R6 audit run against the finalized S6 doctrine/narrative prose — all 58 in-scope
       `content/**/*.md` pages **except** `content/cases/*`, the S8 pages (`Reading and Citing
       Cases`, `Legal Research Tools`, `Verifying Good Law`), the `Case Index`, `flashcards.md`,
       and the glossary itself.

> **What this file is.** The term→pages occurrence map (S7 §6.2) the Phase-2 sweep applies without
> re-deciding. Each row fixes the **destination** (glossary `#anchor` per R2/R7, doctrine `[[Page]]`
> per R2, or S8 `[[Reading and Citing Cases#slug]]` per §9), whether the term is **in the glossary**,
> the **pages where it occurs** (first-occurrence-per-page gets the link, R8/U3), and the **routing
> rationale**. This half does **not** wire any links into doctrine pages — that is Phase 2.
>
> **Anchor slugs** are Quartz auto-slugs of the `### Term` headings now in `Common Legal Terms.md`
> (lowercase, spaces→`-`, punctuation dropped). **Index pages** (`index.md` section landings) are
> omitted from "pages to wire" (nav landings, not prose); noted where a term appears only there.

---

## A. Glossary-wired terms (in glossary → `[[Common Legal Terms#anchor]]`)

Term-of-art, no page home, not R3-vernacular, not the page's own subject. First qualifying
occurrence per page is wired to the anchor.

| Term | Destination | In glossary? | Pages to wire (first occurrence each) | Notes |
|---|---|---|---|---|
| totality of the circumstances | `[[Common Legal Terms#totality-of-the-circumstances]]` | **add** (authored) | Probable Cause and Reasonable Suspicion · Use of Force · Section 1983 Liability and Qualified Immunity · Seizure of the Person · Traffic Stops · Terry Stops and Reasonable Suspicion · The Warrant Requirement · CREW · Miranda Waiver and Invocation · Eyewitness Identification · Due-Process Voluntariness of Confessions · Knock and Talk · Consent Searches · Exigent Circumstances and Hot Pursuit | Cross-cutting standard, no page home; R3 counter-note keeps it **included**. High-value add. |
| de novo | `[[Common Legal Terms#de-novo]]` | **add** (authored) | Probable Cause and Reasonable Suspicion · Brady and Giglio · Section 1983 Liability and Qualified Immunity · Standing to Challenge a Search · The Exclusionary Rule · Arrest in the Home · Collective Knowledge and the Fellow-Officer Rule · Seizure of the Person · Traffic Stops · Terry Stops and Reasonable Suspicion · The Warrant Requirement · The Third-Party Doctrine and Digital Surveillance · Two Definitions of Search · Abandonment · Curtilage · Tents · Miranda and Custodial Interrogation · Sixth Amendment Right to Counsel · Eyewitness Identification · Border Searches · Search Incident to Arrest · Securing the Scene · Knock and Talk · Special Needs and Administrative Searches · Consent Searches · Plain View Doctrine · Exigent Circumstances and Hot Pursuit · Automobile Exception | Appellate standard of review; page-less. Wire in each page's "Burden · standard of review" line. |
| clear error | `[[Common Legal Terms#clear-error]]` | **add** (authored) | Probable Cause and Reasonable Suspicion · Brady and Giglio · Standing to Challenge a Search · The Exclusionary Rule · Arrest in the Home · Collective Knowledge and the Fellow-Officer Rule · Seizure of the Person · Traffic Stops · The Warrant Requirement · The Third-Party Doctrine and Digital Surveillance · Two Definitions of Search · Abandonment · Curtilage · Tents · Sixth Amendment Right to Counsel · Eyewitness Identification · Border Searches · Securing the Scene · Knock and Talk · Special Needs and Administrative Searches · Consent Searches · Plain View Doctrine · Exigent Circumstances and Hot Pursuit · Automobile Exception | Pairs with *de novo* in the standard-of-review lines; page-less. Distinct anchor so both get wired. |
| per se | `[[Common Legal Terms#per-se]]` | **add** (authored) | Sixth Amendment Right to Counsel · Eyewitness Identification · Due-Process Voluntariness of Confessions · Consent Searches · Plain View Doctrine | Legal "per se rule/exclusion" sense (categorical, no balancing). Borderline vs. lay adverb (R4) — wire only the *per se rule* usage; instructor may drop. |
| respondeat superior | `[[Common Legal Terms#respondeat-superior]]` | **add** (authored) | Section 1983 Liability and Qualified Immunity | Opaque Latin term of art; page assumes the meaning. Definition is generic; the *Monell* case-tied limit stays on the page (R9 — no holding restated in glossary). |
| stare decisis | `[[Common Legal Terms#stare-decisis]]` | yes | The Federal Court System | Also on `index.md`. The Federal Court System is its natural first prose home (not its subject). |
| holding | `[[Common Legal Terms#holding]]` | yes | (occurs on ~30 doctrine pages) Probable Cause and Reasonable Suspicion · The Federal Court System · Brady and Giglio · … · Automobile Exception | **Flag for R3 review:** very high frequency; instructor may deem it audience-vernacular. Default = wire first-occurrence; low priority. |
| per curiam | `[[Common Legal Terms#per-curiam]]` | yes | Brady and Giglio · Use of Force · Section 1983 Liability and Qualified Immunity · Arrest in the Home · Securing the Scene · Plain View Doctrine · Exigent Circumstances and Hot Pursuit · Emergency Aid · Automobile Exception | Not one of the 10 S8 citation-mechanics terms — stays a glossary entry. |
| fruit of the poisonous tree | `[[Common Legal Terms#fruit-of-the-poisonous-tree]]` | yes | Abandonment | On **The Exclusionary Rule** it is core-doctrine/subject → skip glossary-link there (route to page). Wire only where it's an incidental mention (Abandonment). |
| suppression hearing | `[[Common Legal Terms#suppression-hearing]]` | yes | Standing to Challenge a Search | Single prose occurrence in scope. |
| habeas corpus | `[[Common Legal Terms#habeas-corpus]]` | yes | Section 1983 Liability and Qualified Immunity | Also `index.md`. |
| ex parte | `[[Common Legal Terms#ex-parte]]` | yes | Seizure of the Person | — |
| de minimis | `[[Common Legal Terms#de-minimis]]` | yes | Traffic Stops | — |
| de facto | `[[Common Legal Terms#de-facto]]` | yes | Seizure of the Person · Terry Stops and Reasonable Suspicion | Split from the former paired *De facto vs. de jure* entry (R7). |
| de jure | `[[Common Legal Terms#de-jure]]` | yes | *(no non-index prose occurrence in scope)* | Reference-only anchor; split from the paired entry. Wire if a future page uses it. |
| dicta | `[[Common Legal Terms#dicta]]` | yes | Entrapment | Also `index.md`. Canonical lemma; *obiter dictum*/`dictum` noted in the entry body. |
| mens rea | `[[Common Legal Terms#mens-rea]]` | yes | Standing to Challenge a Search | Also `index.md`. |
| concurring opinion | `[[Common Legal Terms#concurring-opinion]]` | yes | Standing to Challenge a Search · Two Definitions of Search · Fourth Amendment Recalibration · Tents · Miranda and Custodial Interrogation · Miranda Waiver and Invocation · Entrapment · Search Incident to Arrest · Special Needs and Administrative Searches · Plain View Doctrine | Prose uses inflected "concurrence/concurring" → pipe display text. Low priority; instructor may treat as vernacular. |
| dissenting opinion | `[[Common Legal Terms#dissenting-opinion]]` | yes | Section 1983 Liability and Qualified Immunity · The Exclusionary Rule · Traffic Stops · Fourth Amendment Framework · Fourth Amendment Recalibration · Knock and Talk | Inflected "dissent/dissenting" → pipe display text. Low priority. |
| voir dire | `[[Common Legal Terms#voir-dire]]` | yes | *(index.md only in scope)* | Reference-only in current corpus. |
| prima facie | `[[Common Legal Terms#prima-facie]]` | yes | *(index.md only in scope)* | Reference-only in current corpus. |

**Glossary entries with no in-scope prose occurrence** (reference-only anchors; wired if future pages use them): actus reus · corpus delicti · modus operandi · motion in limine · statement of facts · subpoena duces tecum · subpoena ad testificandum · in forma pauperis · statute of limitations · majority opinion · plurality opinion · pro bono · pro se · inter alia.

---

## B. New glossary entries authored (R9) — the additions list

All 5 are pure definitions (no citation); **zero case-tied propositions** → **no CL gate**. Wiring
destinations/pages are in table A above.

| Term | Category slotted into | Two-key (case-tied)? | Rationale |
|---|---|---|---|
| totality of the circumstances | Evidence & procedure | no | Cross-cutting standard; page-less; explicitly R3-included. |
| de novo | Opinions & precedent | no | Appellate standard of review; page-less; recurs in every SoR line. |
| clear error | Opinions & precedent | no | Deferential fact-finding review; pairs with *de novo*; page-less. |
| per se | Latin shorthand | no | "Per se rule" = categorical/no-balancing; page-less Latin term of art. |
| respondeat superior | Latin shorthand | no | Vicarious-liability principle; page-less; *Monell* limit left to the page (R9). |

---

## C. Route-to-doctrine-page terms (R2) — **NOT** glossary-wired

Term-of-art **with a page home** → link the owning page (S6 already doctrine-links these; the sweep
routes any remaining first-occurrence to the page, not the glossary). No glossary entry added.

| Term | Destination | In glossary? | Pages where it occurs | Notes |
|---|---|---|---|---|
| attenuation | `[[The Exclusionary Rule]]` | n/a | The Exclusionary Rule · Collective Knowledge and the Fellow-Officer Rule · Seizure of the Person · Traffic Stops · Miranda and Custodial Interrogation | Sub-doctrine of the Exclusionary Rule (page has no `#attenuation` section anchor → route to the page, R2). |
| inevitable discovery | `[[The Exclusionary Rule]]` | n/a | The Exclusionary Rule · Search Incident to Arrest | Sub-doctrine → route to page. |
| independent source | `[[The Exclusionary Rule]]` | n/a | The Exclusionary Rule · Securing the Scene · Sixth Amendment Right to Counsel · Eyewitness Identification | Exclusionary-rule sub-doctrine; on 6A/Eyewitness it is the *Wade* lineup independent-source → route those to `[[Eyewitness Identification]]`. |
| good-faith exception | `[[The Exclusionary Rule]]` | n/a | The Exclusionary Rule (+ generic "good faith" on many pages — not the term) | Wire only the *good-faith exception* doctrine mention; skip generic "good faith." |
| taint | `[[The Exclusionary Rule]]` | n/a | The Exclusionary Rule · Standing to Challenge a Search · Collective Knowledge · Seizure of the Person · Traffic Stops · Abandonment · Miranda (×2) · Eyewitness Identification · Due-Process Voluntariness · Securing the Scene · Knock and Talk · Consent Searches | Tied to fruit-of-the-tree/attenuation; conceptually covered by `#fruit-of-the-poisonous-tree`. Route doctrine mentions to the Exclusionary Rule; low priority. |
| standing | `[[Standing to Challenge a Search]]` | n/a | Standing to Challenge a Search (subject) + Section 1983 · Seizure of the Person · Traffic Stops · Two Definitions of Search · Border Searches · Automobile Exception · … | Has its own page. **R4 caution:** exclude ordinary-English "standing" (e.g., "standing in the doorway") — wire only the 4A-standing sense. |
| particularity | `[[The Warrant Requirement]]` | n/a | The Warrant Requirement · CREW · The Third-Party Doctrine and Digital Surveillance · Two Definitions of Search · Common Law Origins · Border Searches · Plain View Doctrine · Use of Force | The particularity requirement is core content of the Warrant Requirement page → route there. |
| curtilage | `[[Curtilage]]` | n/a | Curtilage (subject) + Arrest in the Home · CREW · Abandonment · Tents · Knock and Talk · Plain View Doctrine · Automobile Exception · Two Definitions of Search · Fourth Amendment Framework · Securing the Scene · Standing · The Third-Party Doctrine · Fourth Amendment Analysis Checklist | Has its own page (S6 doctrine link). Not glossary-wired. |
| reasonable expectation of privacy | `[[Two Definitions of Search]]` | n/a | (18 pages) Two Definitions of Search · Fourth Amendment Framework · Fourth Amendment Recalibration · Curtilage · Abandonment · Tents · The Third-Party Doctrine · Standing · The Exclusionary Rule · Arrest in the Home · Traffic Stops · The Warrant Requirement · Special Needs · Consent Searches · Plain View Doctrine · Automobile Exception · Fourth Amendment Analysis Checklist | The *Katz* REP test; its doctrinal home is the search-definition pages. Route to page; also near-vernacular for this audience. |
| color of law | `[[Section 1983 Liability and Qualified Immunity]]` | n/a | Section 1983 Liability and Qualified Immunity (subject) | Element 1 of a § 1983 claim, defined on the page (its subject). Not glossary-wired. |
| probable cause | `[[Probable Cause and Reasonable Suspicion]]` | yes (def-only anchor) | (site-wide) | R3 officer-vernacular **and** has a page. Glossary keeps a definitional anchor (`#probable-cause`) for reference; **prose mentions route to the page** (§9/R2), not the glossary. |
| reasonable suspicion | `[[Probable Cause and Reasonable Suspicion]]` | yes (def-only anchor) | (site-wide) | Same as probable cause: definitional glossary anchor retained; prose routes to the page. |
| exigent circumstances | `[[Exigent Circumstances and Hot Pursuit]]` | n/a | (12 pages) | R3 vernacular **and** has a page → route to page; not glossary-wired. |

---

## D. S8 citation-mechanics terms (§9) — route to `[[Reading and Citing Cases#slug]]`, **do NOT define in glossary**

The 10 terms homed on the S8 **Reading & Citing Cases** page. S8 has landed (page exists with the
`### Term`→auto-slug convention). These are **left unwired for the S8 sweep to claim** and are **not**
glossary entries. None is currently a glossary term (confirmed).

| Term | Destination (S8) | In glossary? | Occurs in doctrine prose? | Notes |
|---|---|---|---|---|
| supra | `[[Reading and Citing Cases#supra]]` | n/a (S8) | no | No in-scope prose occurrence. Route/reference only. |
| id. | `[[Reading and Citing Cases#id]]` | n/a (S8) | citation usage only | Appears as the `Id.` short-form inside cites, not as a wireable prose term — do not wire. |
| pinpoint cite | `[[Reading and Citing Cases#pinpoint-cite-pin-cite]]` | n/a (S8) | no | Confirm exact S8 slug at wire time (heading may be "Pinpoint cite (pin cite)"). |
| reporter | `[[Reading and Citing Cases#reporter]]` | n/a (S8) | The Federal Court System (weight/level context) | Route to S8; leave unwired. |
| parallel citation | `[[Reading and Citing Cases#parallel-citation]]` | n/a (S8) | no | Route/reference only. |
| en banc | `[[Reading and Citing Cases#en-banc]]` | n/a (S8) | (14 pages) The Federal Court System · Brady and Giglio · Standing · The Exclusionary Rule · Traffic Stops · Terry Stops · The Warrant Requirement · The Third-Party Doctrine · Fourth Amendment Framework · Two Definitions of Search · Curtilage · Border Searches · Plain View Doctrine · Community Caretaking | Leave unwired — S8 sweep claims it. |
| certiorari | `[[Reading and Citing Cases#certiorari]]` | n/a (S8) | The Federal Court System · Brady and Giglio (+ index) | Leave unwired. |
| slip opinion | `[[Reading and Citing Cases#slip-opinion]]` | n/a (S8) | "slip op." appears inside cites (Eyewitness Id) | Citation usage, not prose term — do not wire. |
| on remand | `[[Reading and Citing Cases#on-remand]]` | n/a (S8) | "remand/remanded" on Use of Force · The Exclusionary Rule · Seizure of the Person · The Warrant Requirement · Fourth Amendment Framework · Due-Process Voluntariness · Entrapment · Special Needs · Community Caretaking | Leave unwired — S8 claims it. |
| vacated | `[[Reading and Citing Cases#vacated]]` | n/a (S8) | Use of Force · Seizure of the Person · The Warrant Requirement · Fourth Amendment Framework · Abandonment · Due-Process Voluntariness · Entrapment · Special Needs | Leave unwired — S8 claims it. |

---

## E. Skipped candidates — vernacular (R3), plain-English (R4), or deferred fuzzy (R6 #2)

| Term / set | Disposition | Rationale |
|---|---|---|
| probable cause · reasonable suspicion · exigent circumstances · custody · detention · arrest · stop · frisk / pat-down · search · seizure · consent · warrant · plain view · contraband · Miranda · suspect · officer · evidence | **skip (R3 officer-vernacular)** | Field-operational vocabulary this audience knows cold; most also have doctrine pages (routed by R2 — see C). Instructor-editable seed set. |
| car · house · night · money · door · knock · statement · question · mistake | **skip (R4 plain-English)** | Lay meaning matches; not terms of art. |
| color of law | **route to page (C)** | Subject of the § 1983 page, not glossary. |
| prophylactic | **skip / route to `[[Miranda and Custodial Interrogation]]`** | Adjective describing the Miranda rule; not a standalone glossary lemma. Occurs on the Miranda/voluntariness pages. |
| nexus | **skip (near-plain) / route to `[[The Warrant Requirement]]`** | "Connection/link"; borderline lay. Occurs Three Golden Rules · Miranda Waiver · Border Searches. |
| exculpatory | **defer (fuzzy) → route to `[[Brady and Giglio]]`** | Term of art but taught on the Brady page (its home). Fuzzy-pass candidate for instructor review; not added this pass. |
| affirmative defense | **defer (fuzzy)** | Genuine term of art but only 1–2 occurrences (Section 1983 · Entrapment); low value. Flag for next continuous-audit cycle (N11). |
| fair probability · articulable · mixed question of law and fact · interlocutory appeal | **skip / component-of-doctrine** | Sub-phrases of PC/RS or SoR paragraphs; route to their owning doctrine pages, not the glossary. |

---

## Summary

- **In-scope pages audited:** 58 (all `content/**/*.md` minus cases, the 3 S8 pages, Case Index, flashcards, glossary).
- **Glossary anchorized (R7):** 30 existing entries → `### Term` anchors; **2 paired entries split** (*Probable cause vs. reasonable suspicion* → `#probable-cause` + `#reasonable-suspicion`; *De facto vs. de jure* → `#de-facto` + `#de-jure`). Parentheticals kept as canonical lemma + body note (*Dicta*, *Modus operandi*, *In forma pauperis*). Final glossary = **37 `### Term` anchors**.
- **Additions authored (R9):** 5 — totality of the circumstances · de novo · clear error · per se · respondeat superior. All pure definitions, **no citations, no case-tied propositions → 0 CL-gate items.**
- **S8 routing (§9):** all 10 citation-mechanics terms routed to `[[Reading and Citing Cases#…]]`, **left unwired** for the S8 sweep, **not** defined in the glossary. Confirmed none is a glossary entry.
- **Map rows:** 21 glossary-wired (incl. 5 additions) · 13 route-to-page · 10 S8-routed · skip/defer sets. Phase-2 sweep wires first-occurrence-per-page (R8/U3) through the R11 gate.
