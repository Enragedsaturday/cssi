---
title: "Chatrie v. United States"
type: case
citation: "609 U.S. ___ (2026)"
parallel_cite: ""
neutral_cite: ""
court: "U.S. Supreme Court"
court_level: scotus
circuit: ""
year: 2026
date_decided: 2026-06-29
docket: "25-112"
authority_weight: "Binding — SCOTUS"
treatment:
  status: good
  as_of: 2026-06-30
  note: "New Binding — SCOTUS anchor (decided 2026-06-29, post-capture). Geofence/Google Location History acquisition IS a Fourth Amendment search; the probable-cause/particularity of geofence warrants was left open on remand. Slip-op sourced; CL-confirm pending."
  by: []
courtlistener:
  opinion_url: ""
  opinion_id: null
  identity_checked: false
  note: "CL-confirm PENDING. CourtListener has no clean SCOTUS Chatrie object: its only index entry, opinion 10881683 ('Chatrie v. United States / scotus / 2026-06-29 / 25-112'), is CORRUPTED — the underlying opinion text resolves to *Harmon v. ABC 2 News Station* (E.D. Wis. 24-cv-600). DO NOT ingest 10881683. Re-poll CL; verify case_name contains 'Chatrie', court = scotus, docket = 25-112 before trusting. Holding independently confirmed via primary/secondary web sources (supremecourt.gov slip op. 25-112; SCOTUSblog; Cornell LII; Justia; EPIC) at the S9 serial-CL gate, 2026-06-30. The 4th Cir. opinions (10265776 panel; 10443725 en banc, 136 F.4th 100) and 5th Cir. *Smith* (10036119, 110 F.4th 817) remain valid for those lower-court entries."
homes:
  - page: "[[Two Definitions of Search]]"
    role: "Key — Anchor"
  - page: "[[The Third-Party Doctrine and Digital Surveillance]]"
    role: "Key — Progeny / Refinement"
related: ["[[Carpenter v. United States]]", "[[United States v. Jones]]", "[[Katz v. United States]]", "[[Smith v. Maryland]]", "[[The Warrant Requirement]]", "[[Standing to Challenge a Search]]", "[[The Exclusionary Rule]]"]
aliases: []
tags: ["case", "fourth-amendment", "search", "digital-privacy", "geofence", "location-history", "third-party-doctrine"]
holding: "Acquiring a cell-phone user's Google Location History (geofence) data is a Fourth Amendment search — there is a reasonable expectation of privacy in the record of one's phone's location, even for a short period and even when the data is held by a third party; the Court did not decide whether geofence warrants satisfy probable cause and particularity, vacating and remanding."
---

# Chatrie v. United States

*609 U.S. ___ (2026)* (No. 25-112) · U.S. Supreme Court · **Binding — SCOTUS** · Treatment: **good** *(as of 2026-06-30)*
<!-- header line; TreatmentBadge + weight render here, degrading to the text above. CL-confirm PENDING: slip-op sourced; the only CL object (10881683) is corrupted — see frontmatter/Sources. -->

## Background
Investigating a 2019 armed robbery of a Midlothian, Virginia credit union, police obtained a **geofence warrant** directing Google to disclose **Location History** for every device within a 150-meter radius of the bank during a roughly one-hour window around the robbery. That "reverse-location" process ultimately identified Okello Chatrie. He moved to suppress, arguing that compelling Google to produce his Location History was a warrantless Fourth Amendment search. The Fourth Circuit — on rehearing **en banc**, splitting 7–7 on whether a search occurred — affirmed the denial of suppression (136 F.4th 100), teeing up the threshold question for the Supreme Court.

## Issue
Whether the government conducts a Fourth Amendment "search" when it acquires a person's Google Location History (geofence) data — records of a cell phone's location — held by a third-party provider.

## Rule
Yes. Acquiring a cell-phone user's **Google Location History is a Fourth Amendment search**: a person "maintains a reasonable expectation of privacy in the record of his phone's location," and the government intrudes on it when it compels production of that data — **even for a short period** and **even though the records are held by a third party**. The Court rejected the argument that Location History (off by default / opt-in) is "voluntarily shared" and thus stripped of protection by the third-party doctrine, **applying and extending *[[Carpenter v. United States|Carpenter]]*** to bulk reverse-location data. *Chatrie v. United States*, 609 U.S. ___ (2026) (No. 25-112) (slip op.). ^pin-op

Critically, the Court **did not** hold geofence warrants categorically unconstitutional. It **expressly declined** to decide whether *this* geofence warrant satisfied the Fourth Amendment's **probable-cause and particularity** requirements, leaving that question for remand.

## Application
Police compelled Google to produce Location History for all devices in a geographic area and time window — an "all-encompassing" record of individuals' movements generated automatically and held by a third party. Under *Carpenter*'s logic, that acquisition invaded a reasonable expectation of privacy and was therefore a search; the third-party/opt-in rationale the Fourth Circuit panel had relied on did not defeat that protection.

## Conclusion
Acquiring geofence Location History is a Fourth Amendment search. The judgment was **vacated and remanded** for the lower courts to decide the **probable-cause and particularity** of the geofence warrant — the question the Court left open. Reported **6–3, Kagan, J.**, for the Court *(vote lineup and separate writings per contemporaneous reports — confirm against the slip op.)*.

## Treatment & subsequent history
- **Status:** good *(as of 2026-06-30)* — **Binding — SCOTUS** anchor on the geofence search-threshold question.
- **Doctrinal effect:** **RESOLVES** the former circuit split on whether acquiring geofence Location History is a *search* (5th Cir. *[[The Warrant Requirement|Smith]]* = yes; 4th Cir. en banc *Chatrie* = fractured) — **it is a search**. *Smith*'s further holding that geofence warrants are "modern-day general warrants" and **categorically unconstitutional** was **not** adopted; it is now the persuasive minority position feeding the **remanded** probable-cause/particularity question — the new live frontier.
- **CL-confirm: PENDING (slip-op sourced).** CourtListener has no clean SCOTUS object; its only entry (opinion 10881683) is corrupted (resolves to *Harmon v. ABC 2 News Station*). Do **not** ingest 10881683. Re-poll CL and backfill a verified permalink once a clean `scotus / 25-112 / Chatrie` cluster appears. See Sources.

## Appears on
- [[Two Definitions of Search]] — *Key — Anchor*
- [[The Third-Party Doctrine and Digital Surveillance]] — *Key — Progeny / Refinement*

## Sources
- *Chatrie v. United States*, 609 U.S. ___ (2026) (No. 25-112) — **slip opinion (PRIMARY):** https://www.supremecourt.gov/opinions/25pdf/25-112_0am4.pdf — decided June 29, 2026.
- SCOTUSblog case page — https://www.scotusblog.com/cases/chatrie-v-united-states/
- Justia, *Chatrie v. United States*, 609 U.S. ___ (2026) — https://supreme.justia.com/cases/federal/us/609/25-112/
- Cornell LII (Supreme Court text, No. 25-112) — https://www.law.cornell.edu/supremecourt/text/25-112
- Decision below: *United States v. Chatrie*, 136 F.4th 100 (4th Cir. 2025) (en banc) — https://www.courtlistener.com/opinion/10443725/united-states-v-okello-chatrie/
- **CL-confirm note:** CourtListener opinion `10881683` is **corrupted** (indexed as SCOTUS *Chatrie* but its text is *Harmon v. ABC 2 News Station*, E.D. Wis.) — **do not ingest**; permalink to be backfilled at a later serial-CL gate once CL carries a clean `scotus / 25-112 / Chatrie` cluster.
