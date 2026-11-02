"""Write memory_new.json and art_new.json for The first historians.

Memory lines are cut by script from raw.json (the cached Macaulay, Crawley and Dods texts) and from the WEB via web.py,
so every word is verbatim. Painting alt text is the first sentences of the NGA's own description (nga.py cache).
"""
import json, os, sys, pickle, re
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'tools', 'journeys'))
from web import verse
R = json.load(open(os.path.join(HERE, 'raw.json')))
def cut(text, start, end):
    i = text.index(start); j = text.index(end, i) + len(end); return text[i:j]

proem = cut(R['hdt-proem'][0], 'This is the Showing forth', 'waged war with one another.')
th = R['hdt-thermopylae'][9].strip('"')
poss = cut(R['thuc-method'][2], 'In fine, I have written my work', 'a possession for all time.')
aug = cut(R['augustine'][0], 'Justice being taken away', 'but little kingdoms?')
luke = verse('Luke 12:20').lstrip('“')  # the opening mark of Jesus' story is dropped; the words are verbatim

def lines(t, breaks):
    out = []; rest = t
    for b in breaks:
        i = rest.index(b); out.append(rest[:i].strip()); rest = rest[i:]
    out.append(rest.strip()); return out

M = [
 {"id": "herodotus-1-1", "title": "That the deeds of men may not be forgotten", "kind": "History",
  "src": "Herodotus, Histories I, opening · tr. G. C. Macaulay (1890)", "author": "Herodotus", "work": "Histories I, opening",
  "translator": "G. C. Macaulay (1890)", "tradition": "athens",
  "lines": lines(proem, ['to the end that', 'nor the works', 'which have been produced', 'may lose their renown;', 'and especially that']),
  "why": "The first sentence of the first history book gives the two reasons we study the past: so that what people did is not forgotten, and so that we understand why it happened. Notice that Herodotus promises to remember the enemy's great deeds as well as his own. Say it when you are tempted to tell only your side of a story.",
  "source": "https://www.gutenberg.org/ebooks/2707"},
 {"id": "luke-12-20", "title": "Tonight your soul is required of you", "kind": "Scripture",
  "src": "Luke 12:20 · World English Bible", "author": "Luke", "work": "Luke 12:20", "translator": "World English Bible", "tradition": "jerusalem",
  "lines": lines(luke, ['‘You foolish one,', 'The things which']),
  "why": "God's word to the rich man who planned bigger barns and thought he owned tomorrow. It says what Solon told Croesus, and more: what we keep is not ours, and what matters is being 'rich toward God'. Say it when you catch yourself making plans as if you were sure of the future.",
  "source": "https://ebible.org/eng-web/LUK12.htm"},
 {"id": "tell-the-spartans", "title": "Stranger, report this word to the Spartans", "kind": "History",
  "src": "Herodotus, Histories VII.228 (the epitaph at Thermopylae) · tr. G. C. Macaulay (1890; third edition 1914)", "author": "Herodotus", "work": "Histories VII.228 (the epitaph of the Spartans at Thermopylae)",
  "translator": "G. C. Macaulay (1890; third edition 1914)", "tradition": "athens",
  "lines": lines(th, ['Here in this spot']),
  "why": "The epitaph on the Spartans who died at Thermopylae in 480 BC, often attributed to Simonides. It does not say they died for glory, but 'faithfully keeping their laws': freedom as obedience to a law you share, at any cost. Say it when keeping your word or your duty costs you something.",
  "source": "https://www.gutenberg.org/ebooks/2456"},
 {"id": "possession-for-all-time", "title": "A possession for all time", "kind": "History",
  "src": "Thucydides, History of the Peloponnesian War I.22 · tr. Richard Crawley (1874)", "author": "Thucydides", "work": "History of the Peloponnesian War I.22",
  "translator": "Richard Crawley (1874)", "tradition": "athens",
  "lines": lines(poss, ['not as an essay', 'but as a possession']),
  "why": "Thucydides' reason for writing slowly and checking everything: not to be applauded today, but to be useful for good. It is a test for anything we make or say. Say it before you send the quick, clever reply.",
  "source": "https://www.gutenberg.org/ebooks/7142"},
 {"id": "city-of-god-robberies", "title": "What are kingdoms but great robberies?", "kind": "Church",
  "src": "Augustine, The City of God IV.4 · tr. Marcus Dods (1871)", "author": "Augustine", "work": "The City of God IV.4",
  "translator": "Marcus Dods (1871)", "tradition": "church",
  "lines": lines(aug, ['For what are robberies']),
  "why": "Augustine's two questions, written after the sack of Rome in 410: without justice, the only difference between an empire and a gang is size. It is the best short answer to 'the strong do what they can'. Say it when you are tempted to think that power makes something right.",
  "source": "https://www.newadvent.org/fathers/120104.htm"},
]
json.dump(M, open(os.path.join(HERE, 'memory_new.json'), 'w'), ensure_ascii=False, indent=1)

imgs, objs = pickle.load(open(os.path.join(ROOT, '.cache', 'nga', 'cache.pkl'), 'rb'))
A = [
 ("daellen-vanitas", "ffcbf669-7d12-4f64-a3b2-39f9dc3d5a91", "Vanitas Still Life", "François van Daellen", "c. 1650", "50% 60%"),
 ("moroni-titians-schoolmaster", "ff8661ce-70d8-44e6-9694-a1c953877e69", "\"Titian's Schoolmaster\"", "Giovanni Battista Moroni", "c. 1575", "50% 30%"),
 ("gwen-john-convalescent", "307969c5-6d50-4b3e-af9e-534f42280cee", "The Convalescent", "Gwen John", "c. 1915/1925", "50% 40%"),
 ("michallon-forum-pompeii", "67a40105-e674-472c-999b-06fed2986008", "The Forum at Pompeii", "Achille-Etna Michallon", "1819", "50% 55%"),
 ("remond-ruins-messina", "edc2237a-36a1-471e-aac0-73465c96cfbe", "Ancient Ruins near Messina, Sicily", "Jean-Charles-Joseph Rémond", "1842", "40% 50%"),
]
def find(u):
    return next(x for x in imgs.values() if x['uuid'] == u) if u not in imgs else imgs[u]
out = []
for aid, u, title, artist, date, focus in A:
    im = find(u)
    desc = im.get('assistivetext') or ''
    sents = re.split(r'(?<=\.)\s+', desc)
    out.append({"id": aid, "title": title, "artist": artist, "date": date, "museum": "National Gallery of Art, Washington",
                "nga": u, "w": int(im['width']), "h": int(im['height']), "focus": focus, "alt": ' '.join(sents[:3])})
json.dump(out, open(os.path.join(HERE, 'art_new.json'), 'w'), ensure_ascii=False, indent=1)
for m in M: print(m['id'], m['lines'])
for a in out: print(a['id'], a['w'], a['h'], a['alt'][:80])
