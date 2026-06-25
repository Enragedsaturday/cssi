# CSSI — Search & Seizure (study wiki + flashcards)

A federal, **criminal-suppression Fourth Amendment** study wiki for the Certified Search & Seizure
Instructor (CSSI) course, built with [Quartz](https://quartz.jzhao.xyz/). Every case is verified
against CourtListener. Ships with a spaced-repetition flashcard deck (FSRS, 1,176 cards) and a
downloadable Anki deck.

- **Live site:** https://cssi-search-and-seizure.vercel.app
- **Flashcards:** https://cssi-search-and-seizure.vercel.app/flashcards
- **Anki deck (.apkg):** https://cssi-search-and-seizure.vercel.app/static/flashcards/cssi-search-and-seizure.apkg

## How it's built
- Wiki pages live in `content/` (synced from an Obsidian vault).
- Flashcard sources in `flashcard-src/decks/*.json` → `flashcard-src/merge.py` builds
  `quartz/static/flashcards/flashcards.json`; `make_apkg.py` (via `flashcard-src/.venv`) builds the `.apkg`.
- Hosted on **Vercel** — `vercel.json` runs `npx quartz build` → `public/`. **Pushing to `main` auto-deploys.**

## Updating
After editing content or decks (an ingest does this for you):

```sh
cd ~/Projects/cssi-quartz
git add -A && git commit -m "update" && git push
```

Vercel rebuilds and republishes automatically in ~2–3 minutes.

---

Built on [jackyzha0/quartz](https://github.com/jackyzha0/quartz) (`upstream` remote) — pull from there for framework updates.
