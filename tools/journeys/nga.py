"""Find open-access paintings in the National Gallery of Art's open data, with the gallery's own description.

  python3 tools/journeys/nga.py search "jacob, angel" [--all]   title keywords (comma-separated); --all also searches the descriptions
  python3 tools/journeys/nga.py show <uuid>                     the full record and description
  python3 tools/journeys/nga.py claim <journey-id> <uuid> <art-id>   reserve a painting so parallel drafters don't pick it twice

Uses .cache/nga/cache.pkl (the NGA open-data objects and published images). Paintings already in content/art.json
or claimed by another journey (.cache/nga/claims.jsonl) are marked. Describe a painting only from its 'assistivetext'.
"""
import pickle, json, sys, os
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
imgs, objs = pickle.load(open(os.path.join(ROOT, '.cache', 'nga', 'cache.pkl'), 'rb'))
art = json.load(open(os.path.join(ROOT, 'content', 'art.json')))
used = {w.get('nga'): w['id'] for w in art['works'] if w.get('nga')}
CL = os.path.join(ROOT, '.cache', 'nga', 'claims.jsonl')
claims = {}
if os.path.exists(CL):
    for l in open(CL):
        try: c = json.loads(l); claims[c['uuid']] = c
        except Exception: pass
BAD = ('follower', 'imitator', 'manner', 'after', 'copy', 'circle')

def row(o, im):
    tag = f"USED as {used[im['uuid']]}" if im['uuid'] in used else (f"CLAIMED by {claims[im['uuid']]['journey']}" if im['uuid'] in claims else 'free')
    return f"{tag:28} | {o['attribution'][:32]:32} | {o['title'][:60]:60} | {o['displaydate'][:14]:14} | {im['width']}x{im['height']} | {im['uuid']}"

cmd = sys.argv[1] if len(sys.argv) > 1 else ''
if cmd == 'search':
    kws = [k.strip().lower() for k in sys.argv[2].split(',')]; deep = '--all' in sys.argv
    hits = []
    for o in objs:
        im = imgs.get(o['objectid'])
        if not im or o['attribution'].lower().startswith(BAD): continue
        hay = o['title'].lower() + (' ' + (im.get('assistivetext') or '').lower() if deep else '')
        if any(k in hay for k in kws): hits.append((o, im))
    hits.sort(key=lambda x: -int(x[1]['width'] or 0))
    for o, im in hits[:40]: print(row(o, im))
    if not hits: print('no matches')
elif cmd == 'show':
    u = sys.argv[2]
    for o in objs:
        im = imgs.get(o['objectid'])
        if im and im['uuid'] == u:
            print(row(o, im)); print('medium:', o['medium']); print('description:', im.get('assistivetext')); break
    else: print('not found')
elif cmd == 'claim':
    j, u, aid = sys.argv[2], sys.argv[3], sys.argv[4]
    if u in used: sys.exit(f'already used in art.json as {used[u]}')
    if u in claims and claims[u]['journey'] != j: sys.exit(f"already claimed by {claims[u]['journey']}")
    open(CL, 'a').write(json.dumps({'journey': j, 'uuid': u, 'art': aid}) + '\n'); print('claimed', u, 'for', j)
else:
    print(__doc__)
