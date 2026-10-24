"""Assemble drafted journeys into content/: build each (validate, then --write), merge new paintings,
memory pieces and reviewer notes, and set each journey's place in its hall's walk from its spec.

  python3 tools/journeys/assemble.py [id ...]     default: every spec with a src/<id>/journey.py
"""
import json, os, re, subprocess, sys, glob
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
C = lambda f: os.path.join(ROOT, 'content', f)
load = lambda p: json.load(open(p)); dump = lambda p, d: open(p, 'w').write(json.dumps(d, ensure_ascii=False, indent=1) + '\n')

def front(t):
    m = re.match(r'---\n(.*?)\n---\n', t, re.S); d = {}
    for l in m.group(1).split('\n'):
        mm = re.match(r'^(\w+): (.*)$', l)
        if mm: d[mm.group(1)] = re.sub(r'\s+#.*$', '', mm.group(2)).strip()
    return d
specs = {}
for f in glob.glob(os.path.join(ROOT, 'specs', 'journeys', '*.md')):
    if f.endswith('TEMPLATE.md'): continue
    d = front(open(f).read()); specs[d['id']] = d
ids = sys.argv[1:] or sorted((i for i in specs if os.path.exists(os.path.join(HERE, 'src', i, 'journey.py'))), key=lambda i: (specs[i]['hall'], int(specs[i]['order'])))

art = load(C('art.json')); mem = load(C('memory.json')); notes = load(C('review/journeys-notes.json'))
art_ids = {w['id'] for w in art['works']}; art_nga = {w.get('nga'): w['id'] for w in art['works'] if w.get('nga')}; mem_ids = {m['id'] for m in mem}
ok, failed = [], {}
for i in ids:
    src = os.path.join(HERE, 'src', i)
    for w in (load(os.path.join(src, 'art_new.json')) if os.path.exists(os.path.join(src, 'art_new.json')) else []):
        if w['id'] in art_ids: continue
        if w.get('nga') in art_nga: print(f'{i}: painting {w["id"]} is already in art.json as {art_nga[w["nga"]]}'); continue
        art['works'].append(w); art_ids.add(w['id']); art_nga[w.get('nga')] = w['id']
    for m in (load(os.path.join(src, 'memory_new.json')) if os.path.exists(os.path.join(src, 'memory_new.json')) else []):
        if m['id'] not in mem_ids: mem.append(m); mem_ids.add(m['id'])
    dump(C('art.json'), art); dump(C('memory.json'), mem)
    r = subprocess.run([sys.executable, os.path.join(HERE, 'build.py'), i, '--write'], capture_output=True, text=True, cwd=ROOT)
    if r.returncode: failed[i] = r.stdout[-1500:] + r.stderr[-800:]; continue
    ok.append(i)
    n = os.path.join(src, 'notes.json')
    if os.path.exists(n):
        x = load(n); lines = [f"{c['claim']} Source: {c.get('source', '')}" for c in x.get('claims', [])] + list(x.get('flags', [])) + [f"MISSING: {m}" for m in x.get('missing', [])]
        notes[i] = lines
dump(C('review/journeys-notes.json'), notes)

# each hall's walk follows the specs' order (finished journeys not in a spec keep their place after the ones before them)
halls = load(C('halls.json')); built = {j['id'] for j in load(C('journeys.json'))}
for h in halls:
    order = {i: int(specs[i]['order']) for i in h['journeys'] if i in specs}
    if not order: continue
    pos, cur = {}, 0
    for k, i in enumerate(h['journeys']):
        cur = order.get(i, cur + 0.01); pos[i] = (cur, k)
    h['journeys'] = sorted(h['journeys'], key=lambda i: pos[i])
    titles = [specs[i]['title'].lower() for i in h['journeys'] if i in specs]
    h['later'] = [l for l in h.get('later', []) if not any(t.startswith(l['title'].lower()[:18]) or l['title'].lower().startswith(t[:18]) for t in titles)]
dump(C('halls.json'), halls)
print('assembled:', len(ok), ok)
for i, e in failed.items(): print('\nFAILED', i, '\n', e)
