#!/usr/bin/env python3
"""Build the Anki .apkg from the published flashcards.json. Topic subdecks, stable GUIDs.
Needs genanki:  python3 -m venv .venv && .venv/bin/pip install genanki && .venv/bin/python flashcard-src/make_apkg.py"""
import json, html, re, zlib, os, genanki

HERE = os.path.dirname(os.path.abspath(__file__))
DECK = os.path.normpath(os.path.join(HERE, "..", "quartz", "static", "flashcards", "flashcards.json"))
OUT = os.path.normpath(os.path.join(HERE, "..", "quartz", "static", "flashcards", "cssi-search-and-seizure.apkg"))


def stable_id(s):
    return (zlib.crc32(s.encode("utf-8")) & 0x7FFFFFFF) | 0x10000000


MODEL = genanki.Model(
    stable_id("cssi-model-v1"), "CSSI Q&A",
    fields=[{"name": "Front"}, {"name": "Back"}, {"name": "Citation"}, {"name": "Source"}],
    templates=[{"name": "Card 1",
        "qfmt": '<div class="front">{{Front}}</div>',
        "afmt": '{{FrontSide}}<hr id="answer"><div class="back">{{Back}}</div>'
                '{{#Citation}}<div class="cite">{{Citation}}</div>{{/Citation}}'
                '{{#Source}}<div class="src">{{Source}}</div>{{/Source}}'}],
    css=""".card{font-family:Georgia,serif;font-size:19px;line-height:1.5;color:#222;background:#faf8f8;text-align:left;padding:18px;max-width:680px;margin:0 auto}
.front{font-weight:600}.back{margin-top:6px}hr#answer{border:0;border-top:1px solid #ccc;margin:14px 0}
.cite{font-family:'IBM Plex Mono',Menlo,monospace;font-size:13px;color:#555;margin-top:10px}
.src{font-size:13px;margin-top:4px}.src a{color:#284b63}""")


def fmt(s):
    s = html.escape(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"<i>\1</i>", s)
    s = re.sub(r"`(.+?)`", r"<code>\1</code>", s)
    return s.replace("\n", "<br>")


data = json.load(open(DECK, encoding="utf-8"))
by_topic = {}
for c in data["cards"]:
    by_topic.setdefault(c["topic"], []).append(c)
decks = []
for topic, items in sorted(by_topic.items()):
    d = genanki.Deck(stable_id("cssi::" + topic), f"CSSI — Search & Seizure::{topic}")
    for c in items:
        src = c.get("source", "")
        src_html = f'<a href="{html.escape(src)}">View on CourtListener ↗</a>' if src else ""
        d.add_note(genanki.Note(model=MODEL,
            fields=[fmt(c["front"]), fmt(c["back"]), html.escape(c.get("cite", "")), src_html],
            tags=[c["page"], c["type"]] + [re.sub(r"\s+", "-", t) for t in c.get("tags", [])],
            guid=genanki.guid_for(c["id"])))
    decks.append(d)
genanki.Package(decks).write_to_file(OUT)
print(f"wrote {OUT}: {len(data['cards'])} notes / {len(decks)} subdecks")
