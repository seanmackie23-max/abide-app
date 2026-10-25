"""Write memory_new.json (verbatim WEB, 'the Lord' for the divine name as the guide asks) and art_new.json (from the NGA records)."""
import json, os, sys, pickle
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'tools', 'journeys'))
from web import passage
def lines(ref):
    out = []
    for p in passage(ref)['paras']:
        for v, t in p: out += [x.strip() for x in t.split('\n') if x.strip()]
    return [x.replace('Yahweh’s', 'the Lord’s').replace('Yahweh', 'the Lord').replace('’', "'") for x in out]
M = [
 {"id": "proverbs-3-5", "title": "Trust in the Lord with all your heart", "kind": "Scripture", "src": "Proverbs 3:5–6 · World English Bible", "author": "Proverbs", "work": "Proverbs 3:5–6", "translator": "World English Bible", "tradition": "jerusalem",
  "lines": lines('Proverbs 3:5-6'), "why": "The heart of Proverbs in two lines: wisdom begins by trusting someone wiser than yourself. Said in the morning, it turns the day's choices into a walk with God.", "source": "https://ebible.org/eng-web/PRO03.htm"},
 {"id": "song-8-6", "title": "Love is strong as death", "kind": "Scripture", "src": "Song of Songs 8:6–7 · World English Bible", "author": "Song of Songs", "work": "Song of Songs 8:6–7", "translator": "World English Bible", "tradition": "jerusalem",
  "lines": lines('Song of Songs 8:6-7'), "why": "The climax of the Bible's love poem, read at weddings and funerals alike: a love that floods cannot drown and money cannot buy.", "source": "https://ebible.org/eng-web/SNG08.htm"},
 {"id": "colossians-1-17", "title": "In him all things are held together", "kind": "Scripture", "src": "Colossians 1:15–17 · World English Bible", "author": "Colossians", "work": "Colossians 1:15–17", "translator": "World English Bible", "tradition": "jerusalem",
  "lines": lines('Colossians 1:15-17'), "why": "Perhaps one of the oldest Christian hymns: what Proverbs said of Wisdom, this letter says of Christ. The last line is a whole way of seeing the world.", "source": "https://ebible.org/eng-web/COL01.htm"},
]
json.dump(M, open(os.path.join(HERE, 'memory_new.json'), 'w'), ensure_ascii=False, indent=1)
imgs, objs = pickle.load(open(os.path.join(ROOT, '.cache', 'nga', 'cache.pkl'), 'rb'))
by = {im['uuid']: (o, im) for o in objs for im in [imgs.get(o['objectid'])] if im}
A = [("dandre-bardon-skulls", "90bcc63f-35ae-4118-96e8-eebc7a3b6e84", "50% 45%"), ("wilson-solitude", "61c5152e-2408-4b5d-8e08-06a837c25b5a", "35% 60%"),
     ("tura-madonna-garden", "86533ed9-1baa-4e29-8f39-5519b461003f", "50% 45%"), ("master-francis-john-evangelist", "1776edff-237b-411e-b28e-940e253398c1", "50% 30%")]
out = []
for aid, u, f in A:
    o, im = by[u]
    out.append({"id": aid, "title": o['title'], "artist": o['attribution'], "date": o['displaydate'], "museum": "National Gallery of Art, Washington", "nga": u,
                "w": int(im['width']), "h": int(im['height']), "focus": f, "alt": im.get('assistivetext'), "kind": "painting"})
json.dump(out, open(os.path.join(HERE, 'art_new.json'), 'w'), ensure_ascii=False, indent=1)
for m in M: print(m['id'], m['lines'])
for a in out: print(a['id'], a['title'], a['artist'], a['date'])
