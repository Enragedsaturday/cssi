# Brief-Mention Queue — Dead-Letter / Demoted Set (S5 tiering)

> The **no-standalone-page set**. Each case here gets a **Case-Index row** (light CL identity/treatment confirm later) **plus a one-line history note** on its home doctrine page (authored in **S6**) — but **no BIRAC page**.
>
> Two sub-groups:
> - **Demoted overruled minors (4)** — Decision 1 demotion: holding is **dead law** (overruled/abrogated/superseded) **AND** the case is a **minor companion not independently taught** (one of a swept-away line). The teaching value is preserved by the live anchor + a labeled-history note.
> - **Borderline brief-mentions (4)** — Decision 2: field-relevance is too thin for a page; mostly **good law** but niche. Also appended to `omissions.md` with disposition `brief-mention`.
>
> **Size: 8.** Treatments are best-knowledge calls; confirm at the light Case-Index pass.
>
> Columns: Case · Cite · One-line holding · Treatment (best knowledge) · S6 history-note home page · Needs Case-Index row?

## Demoted overruled minors (Decision 1)

| Case | Cite | One-line holding | Treatment | S6 history-note home page | Case-Index row? |
|---|---|---|---|---|---|
| **Trupiano v. United States** | 334 U.S. 699 (1948) | A warrant must be obtained where practicable even incident to a lawful arrest. | **Dead law** — abrogated by *United States v. Rabinowitz* (1950); the SITA framework was then superseded by *Chimel v. California* (1969). A minor stepping-stone; the line is taught through Chimel. | [[Search Incident to Arrest]] | Yes |
| **Frank v. Maryland** | 359 U.S. 360 (1959) | A warrantless administrative health inspection of a dwelling does not violate the 4A. | **Dead law** — overruled by *Camara v. Municipal Court* (1967) and *See v. City of Seattle* (1967), which the corpus ingests as the live anchors. | [[Special Needs and Administrative Searches]] | Yes |
| **Arkansas v. Sanders** | 442 U.S. 753 (1979) | A warrant is required to search luggage taken from a car (the Chadwick-Sanders rule). | **Dead law** — overruled by *California v. Acevedo* (1991), which collapsed the Chadwick-Sanders container distinction. Minor companion of Chadwick (which earns the page). | [[Automobile Exception]] | Yes |
| **Robbins v. California** | 453 U.S. 420 (1981) | A warrant is required for closed containers found in a car. | **Dead law** — overruled by *United States v. Ross* (1982) one year later. A swept-away container-line companion. | [[Automobile Exception]] | Yes |

## Borderline brief-mentions (Decision 2 — applied)

| Case | Cite | One-line holding | Treatment | S6 history-note home page | Case-Index row? |
|---|---|---|---|---|---|
| **United States v. Verdugo-Urquidez** | 494 U.S. 259 (1990) | The 4A does not protect a nonresident alien against a search of property abroad ('the people' = those with a substantial U.S. connection). | **Good law**, but demoted for thin domestic field relevance (foreign-search niche). | [[Fourth Amendment Framework]] (scope of 'the people') | Yes |
| **Wyman v. James** | 400 U.S. 309 (1971) | A caseworker's home visit as a condition of welfare benefits is not a 4A search requiring a warrant. | **Good law**, but demoted — welfare-administration context, not LE field conduct. | [[Special Needs and Administrative Searches]] | Yes |
| **G. M. Leasing Corp. v. United States** | 429 U.S. 338 (1977) | Warrantless entry of business offices to seize property for a tax levy violated the 4A; seizing the taxpayer's cars from public areas did not. | **Good law**, but demoted — IRS tax-collection context; thin street-officer relevance. | [[The Warrant Requirement]] | Yes |
| **A Quantity of Copies of Books v. Kansas** | 378 U.S. 205 (1964) | Seizing allegedly obscene books requires a prior adversarial hearing (heightened procedure for 1A-sensitive seizures). | **Good law**, but demoted — driven by the 1A obscenity overlay; expressive-materials niche. | [[The Warrant Requirement]] (1A-sensitive seizures) | Yes |

---

> **Demotion is reversible.** Any of these may be promoted to a full page if the Case-Index confirm surfaces unexpected current importance or field relevance. Conversely, none of these is *dropped* — each survives as an indexed, doctrine-anchored history note.

---

## ✅ Case-Index confirm — VERIFIED (S5 closeout, 2026-06-30)

Light CourtListener pass (single serial lane; one batched `analyze_citations` call, 14/14 cites verified — the 8 brief-mentions + the 4 live overruling anchors). Identity + cite + treatment confirmed for each; **no `content/cases/` page created** for any (index-row + S6 history-note only). The eyecite name-cross-check WARNINGs were artifacts of inline-prose party attribution; every reporter cite resolved to the correct canonical cluster.

| Case | Cite (confirmed) | CL cluster | Treatment (confirmed) | Overruling / live anchor (verified) | S6 home page | ✅ |
|---|---|---|---|---|---|---|
| **Trupiano v. United States** | 334 U.S. 699 (1948) | 104576 | ⛔ overruled / dead law | abrogated by *Rabinowitz* 339 U.S. 56 (1950); SITA line superseded by *Chimel* 395 U.S. 752 (1969) | [[Search Incident to Arrest]] | ✅ |
| **Frank v. Maryland** | 359 U.S. 360 (1959) | 105880 | ⛔ overruled / dead law | overruled by *Camara* 387 U.S. 523 (1967) + *See v. City of Seattle* 387 U.S. 541 (1967) | [[Special Needs and Administrative Searches]] | ✅ |
| **Arkansas v. Sanders** | 442 U.S. 753 (1979) | 110119 | ⛔ overruled / dead law | overruled by *California v. Acevedo* 500 U.S. 565 (1991) | [[Automobile Exception]] | ✅ |
| **Robbins v. California** | 453 U.S. 420 (1981) | 110558 | ⛔ overruled / dead law | overruled by *United States v. Ross* 456 U.S. 798 (1982) | [[Automobile Exception]] | ✅ |
| **United States v. Verdugo-Urquidez** | 494 U.S. 259 (1990) | 112382 | good (810 citing) | — (good law; foreign-search niche) | [[Fourth Amendment Framework]] | ✅ |
| **Wyman v. James** | 400 U.S. 309 (1971) | 108223 | good (427 citing) | — (good law; welfare-admin niche) | [[Special Needs and Administrative Searches]] | ✅ |
| **G. M. Leasing Corp. v. United States** | 429 U.S. 338 (1977) | 109579 | good (680 citing) | — (good law; IRS tax-levy niche) | [[The Warrant Requirement]] | ✅ |
| **A Quantity of Copies of Books v. Kansas** | 378 U.S. 205 (1964) | 106878 | good (503 citing) | — (good law; 1A obscenity overlay) | [[The Warrant Requirement]] | ✅ |

**S6 handoff:** add a one-line labeled-history sentence on each home doctrine page above (the 4 minors as dead-law-superseded-by-anchor; the 4 borderlines as good-law-but-niche). No BIRAC pages.

<!-- CASE-INDEX-EXPORT (machine-readable; parsed by scripts/build_case_index.py — 5 cols, no pipes inside cells) -->
| Case | Holding | Treatment | Home | CourtListener |
|---|---|---|---|---|
| Trupiano v. United States | A warrant must be obtained where practicable even incident to a lawful arrest (dead law; the SITA line is taught through Chimel). | overruled | [[Search Incident to Arrest]] | https://www.courtlistener.com/opinion/104576/trupiano-v-united-states/ |
| Frank v. Maryland | A warrantless administrative health inspection of a dwelling does not violate the Fourth Amendment (dead law; superseded by Camara/See). | overruled | [[Special Needs and Administrative Searches]] | https://www.courtlistener.com/opinion/105880/frank-v-maryland/ |
| Arkansas v. Sanders | A warrant is required to search luggage taken from a car (the Chadwick-Sanders rule; collapsed for cars by Acevedo). | overruled | [[Automobile Exception]] | https://www.courtlistener.com/opinion/110119/arkansas-v-sanders/ |
| Robbins v. California | A warrant is required for closed containers found in a car (swept away by Ross one year later). | overruled | [[Automobile Exception]] | https://www.courtlistener.com/opinion/110558/robbins-v-california/ |
| United States v. Verdugo-Urquidez | The Fourth Amendment does not protect a nonresident alien against a search of property abroad; 'the people' means those with a substantial connection to the U.S. | good | [[Fourth Amendment Framework]] | https://www.courtlistener.com/opinion/112382/united-states-v-verdugo-urquidez/ |
| Wyman v. James | A caseworker's home visit as a condition of welfare benefits is not a Fourth Amendment search requiring a warrant. | good | [[Special Needs and Administrative Searches]] | https://www.courtlistener.com/opinion/108223/wyman-v-james/ |
| G. M. Leasing Corp. v. United States | Warrantless entry of business offices to seize property for a tax levy violated the Fourth Amendment; seizing the taxpayer's cars from public areas did not. | good | [[The Warrant Requirement]] | https://www.courtlistener.com/opinion/109579/g-m-leasing-corp-v-united-states/ |
| A Quantity of Copies of Books v. Kansas | Seizing allegedly obscene books requires a prior adversarial hearing (heightened procedure for First-Amendment-sensitive seizures). | good | [[The Warrant Requirement]] | https://www.courtlistener.com/opinion/106878/a-quantity-of-copies-of-books-v-kansas/ |
