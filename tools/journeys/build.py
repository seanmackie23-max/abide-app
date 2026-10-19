"""Build a learning journey from tools/journeys/src/<id>/ and put it into content/.

src/<id>/journey.py must define META (the journey fields), SESSIONS (a list of session dicts in
the playbook's shape, with 'read' and 'compare' as lists of parts) and CLOSING. Bible parts use
{"bible": "Genesis 1:1-2:3" | [refs]}; book parts use {"raw": key, "idx": [i, ...], "author", "work",
"translator", "source"} with the texts in src/<id>/raw.json.

  python3 tools/journeys/build.py <id>            build, validate and print a summary
  python3 tools/journeys/build.py <id> --write    also write content/journeys.json and move the
                                                  journey from its hall's 'later' list
"""
import json, re, sys, os, importlib.util
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, HERE)
from web import passage

jid = sys.argv[1]; SRC = os.path.join(HERE, 'src', jid)
spec = importlib.util.spec_from_file_location('journey', os.path.join(SRC, 'journey.py')); J = importlib.util.module_from_spec(spec); sys.path.insert(0, SRC); spec.loader.exec_module(J)
RAW = json.load(open(os.path.join(SRC, 'raw.json'))) if os.path.exists(os.path.join(SRC, 'raw.json')) else {}
norm = lambda t: re.sub(r'\s+', ' ', t.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"').replace('\n', ' '))
problems = []

def split_long(p, mx=330):
    if p == '…' or len(p.split()) <= mx: return [p]
    marks = [m.start() for m in re.finditer(r' \(\d+\) ', p)] or [m.end() for m in re.finditer(r'[.;:] ', p)]
    cut = min(marks, key=lambda x: abs(x - len(p) // 2))
    return split_long(p[:cut].strip(), mx) + split_long(p[cut:].strip(), mx)

def build(parts, where):
    paras = []; out = []; bible = all('bible' in p for p in parts)
    for p in parts:
        start = len(paras)
        if 'bible' in p:
            refs = p['bible'] if isinstance(p['bible'], list) else [p['bible']]; labs = []
            for r in refs: q = passage(r); paras += q['paras']; labs.append(q['ref'])
            ref = p.get('ref') or '; '.join(labs); text = ' '.join(t for para in paras[start:] for _, t in para)
        else:
            for i in p['idx']: paras += split_long(RAW[p['raw']][i])
            ref = p['ref']; text = ' '.join(paras[start:])
        part = {k: v for k, v in p.items() if k not in ('bible', 'raw', 'idx')}; part['ref'] = ref; part['paras'] = list(range(start, len(paras)))
        for k in ('context', 'commentary'):
            if not part.get(k): problems.append(f'{where} {ref}: needs {k}')
        if 'raw' in p and not part.get('plain'): problems.append(f'{where} {ref}: an old text needs "plain"')
        T = norm(text)
        for c in part.get('commentary', []):
            for seg in norm(c.get('on', '')).split(' ... '):
                if seg and seg not in T: problems.append(f'{where} {ref}: commentary quote not in text: "{seg[:60]}"')
        out.append(part)
    words = sum((len(' '.join(t for _, t in x).split()) if isinstance(x, list) else len(x.split())) for x in paras)
    r = {"paras": paras, "parts": out, "minutes": max(1, round(words / 200))}
    if bible: r.update(bible=True, ref='; '.join(p['ref'] for p in out))
    else:
        f = parts[0]; authors = list(dict.fromkeys(p.get('author') for p in parts))
        r.update(author=' and '.join(a for a in authors if a), work=f.get('work'), ref=out[0]['ref'], translator=f.get('translator'), source=f.get('source'))
    return r

sessions = []
for n, S in enumerate(J.SESSIONS, 1):
    s = dict(S); s['id'] = f"{J.META['id']}-{n}"; W = f'session {n}'
    for k in ('title', 'line', 'plain', 'why', 'answers', 'finding', 'background', 'before', 'readWhy', 'lecture', 'debate', 'look', 'music', 'think', 'check', 'tutorial', 'reading', 'practice', 'reflect', 'takeaways', 'terms'):
        if not S.get(k): problems.append(f'{W}: needs {k}')
    bgmin = max(2, round(sum(len(' '.join(b['paras']).split()) for b in S['background']) / 180))
    s['read'] = build(S['read'], W)
    if not s['read'].get('bible'):
        f = S['read'][0]; s['read'].update(kind=f.get('kind', 'church'), who=f.get('who', ''), when=f.get('when', ''))
    c = S['compare']; cr = build(c['parts'], W + ' compare'); cr['why'] = c['why']; cr['title'] = c['title']; s['compare'] = cr
    lw = sum(len(p.split()) for x in S['lecture']['sections'] for p in x['paras'])
    for x in S['lecture']['sections']:
        if not x.get('key'): problems.append(f'{W}: lecture "{x["h"]}" needs key')
    s['lecture'] = dict(S['lecture'], minutes=max(8, round(lw / 170)))
    s['minutes'] = bgmin + s['read']['minutes'] + cr['minutes'] + s['lecture']['minutes'] + 6 + 4 + 5 + 5 + 15 + 2 + 5
    if len(S['check']) < 5: problems.append(f'{W}: needs five or six check questions')
    for q in S['check']:
        if len(q['options']) != 4: problems.append(f'{W}: check "{q["q"][:40]}" needs four options')
    # no forward references
    blob = json.dumps(dict(S, background=[{k: v for k, v in b.items() if k != 'timeline'} for b in S['background']]), ensure_ascii=False)  # a roadmap timeline may name later sessions
    for sent in re.split(r'(?<=[.?!])\s+|",\s*"', blob):
        for m in re.finditer(r'[Ss]ession (\d)', sent):
            if int(m.group(1)) > n and not re.search(r'\b(will|next|later|come|comes|follow|follows|shortly|ahead)\b', sent): problems.append(f'{W}: refers forward to session {m.group(1)} without saying it is still to come: "{sent[:120]}"')
    print(f"{s['id']}: {s['minutes']} min · read {s['read']['minutes']} · compare {cr['minutes']} · lecture {lw} words in {len(S['lecture']['sections'])} parts · {len(S['check'])} checks")
    sessions.append(s)
if sum(1 for s in sessions if s.get('objection')) != 1: problems.append('exactly one session needs "objection": True')
out = dict(J.META); out['sessions'] = sessions; out['closing'] = J.CLOSING
G = {g['term'].lower() for g in out.get('glossary', [])}
for s in sessions:
    for t in s.get('terms', []):
        if t.lower() not in G: problems.append(f'{s["id"]}: term "{t}" not in glossary')
print('closing synthesis', sum(len(p.split()) for p in J.CLOSING['synthesis']), 'words')
if problems:
    print('PROBLEMS:'); [print('  -', p) for p in problems]; sys.exit(1)
print('No problems.')
if '--write' in sys.argv:
    fj = os.path.join(ROOT, 'content', 'journeys.json'); js = json.load(open(fj))
    i = next((k for k, x in enumerate(js) if x['id'] == out['id']), None)
    if i is None: js.append(out)
    else: js[i] = out
    open(fj, 'w').write(json.dumps(js, ensure_ascii=False, indent=1) + '\n')
    fh = os.path.join(ROOT, 'content', 'halls.json'); hs = json.load(open(fh))
    hall = next(h for h in hs if h['id'] == J.HALL)
    hall['later'] = [x for x in hall['later'] if x['title'] != out['title'] and x['title'] != getattr(J, 'LATER_TITLE', '')]
    if out['id'] not in hall['journeys']:
        after = getattr(J, 'AFTER', None)
        hall['journeys'].insert(hall['journeys'].index(after) + 1 if after in hall['journeys'] else len(hall['journeys']), out['id'])
    open(fh, 'w').write(json.dumps(hs, ensure_ascii=False, indent=1) + '\n')
    print('Written to content/journeys.json and content/halls.json')
