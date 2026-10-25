"""Check the journey specs as a set before any drafting.

Finds: Bible passages read twice (across specs and against finished journeys), other set texts listed twice,
memory and music ids that do not exist (unless marked new), 'before' ids that point nowhere, specs without
an objection, and specs whose sessions are not seven. Writes a report to stdout.
Run: python3 tools/journeys/specs_check.py"""
import json, os, re, glob, sys
from collections import defaultdict
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
C = lambda f: json.load(open(os.path.join(ROOT, 'content', f)))
journeys, halls = C('journeys.json'), C('halls.json')
mem = {m['id'] for m in C('memory.json')}
music = {m['id'] for m in C('music.json')}
done = {j['id'] for j in journeys}

def front(text):
    m = re.match(r'---\n(.*?)\n---\n', text, re.S); d, key = {}, None
    for line in m.group(1).split('\n'):
        line = re.sub(r'\s+#.*$', '', line)
        if re.match(r'^\s+- ', line): d.setdefault(key, []).append(line.strip()[2:].strip())
        elif ':' in line:
            key, v = line.split(':', 1); key = key.strip(); v = v.strip()
            d[key] = [x.strip() for x in v.strip('[]').split(',') if x.strip()] if v.startswith('[') else (v if v else [])
    return d, text[m.end():]

BOOKS = ['Genesis','Exodus','Leviticus','Numbers','Deuteronomy','Joshua','Judges','Ruth','1 Samuel','2 Samuel','1 Kings','2 Kings','1 Chronicles','2 Chronicles','Ezra','Nehemiah','Esther','Job','Psalm','Psalms','Proverbs','Ecclesiastes','Song of Songs','Isaiah','Jeremiah','Lamentations','Ezekiel','Daniel','Hosea','Joel','Amos','Obadiah','Jonah','Micah','Nahum','Habakkuk','Zephaniah','Haggai','Zechariah','Malachi','Matthew','Mark','Luke','John','Acts','Romans','1 Corinthians','2 Corinthians','Galatians','Ephesians','Philippians','Colossians','1 Thessalonians','2 Thessalonians','1 Timothy','2 Timothy','Titus','Philemon','Hebrews','James','1 Peter','2 Peter','1 John','2 John','3 John','Jude','Revelation','Wisdom of Solomon']
BRE = re.compile(r'^(' + '|'.join(sorted(map(re.escape, BOOKS), key=len, reverse=True)) + r')\s+(\d+)(?::(\d+))?(?:\s*[–-]\s*(\d+)(?::(\d+))?)?')

def bible(ref):
    """'Mark 14:1–31' -> (book, (c1,v1), (c2,v2)); chapters only -> whole chapters."""
    m = BRE.match(ref.strip())
    if not m: return None
    b, c1, v1, x, y = m.groups(); b = 'Psalm' if b == 'Psalms' else b
    c1 = int(c1)
    if v1 is None:  # chapters
        c2 = int(x) if x else c1
        return b, (c1, 0), (c2, 999)
    v1 = int(v1)
    if y: return b, (c1, v1), (int(x), int(y))
    if x: return b, (c1, v1), (c1, int(x))
    return b, (c1, v1), (c1, v1)

def overlap(a, b):
    return a[0] == b[0] and not (a[2] < b[1] or b[2] < a[1])

# Bible passages already read in finished journeys (read parts, compare parts)
read_done = []
for j in journeys:
    for s in j['sessions']:
        for k in ('read', 'compare'):
            r = s.get(k) or {}
            refs = [p.get('ref') or p.get('bible') or '' for p in (r.get('parts') or [])] or [r.get('ref') or '']
            for ref in refs:
                for piece in re.split(r';\s*', ref or ''):
                    p = bible(piece)
                    if p: read_done.append((p, j['id'], s['title']))

specs = {}
for f in sorted(glob.glob(os.path.join(ROOT, 'specs', 'journeys', '*.md'))):
    if f.endswith('TEMPLATE.md'): continue
    d, body = front(open(f).read()); d['body'] = body; specs[d['id']] = d

problems, notes = [], []
newids = set()
for d in specs.values(): newids |= set(re.findall(r'new\s+`([a-z0-9-]+)`', d['body']))
bible_specs = defaultdict(list); text_specs = defaultdict(list)
for i, d in specs.items():
    rw = d.get('kind') == 'rewrite'
    for r in d.get('reads', []):
        pb = 'point back only' in r or 'point to' in r
        moved = {j['id'] for j in journeys if ('moved from ' + j['title']) in r}
        piece = re.sub(r'\s*\(.*$', '', r)
        p = bible(piece)
        if p:
            if pb: continue
            kept = rw and any(overlap(p, q) for q, jid, _ in read_done if jid == i)  # a rewrite keeping a passage it already reads
            for q, jid, st in ([] if kept else read_done):
                if overlap(p, q) and jid != i and jid not in moved: problems.append(f'{i}: {piece} is already read in {jid} ("{st}"): point back or choose another passage')
            bible_specs[p[0]].append((p, i, piece))
        elif not pb and 'our own words' not in r:
            key = re.sub(r'[^a-z0-9 ]', '', piece.lower())[:60]
            text_specs[key].append(i)
    if not rw:
        n = len(re.findall(r'^\d+\. \*\*', d['body'], re.M))
        if n != 7: problems.append(f'{i}: {n} sessions (expected 7)')
        if '**Objection:**' not in d['body']: problems.append(f'{i}: no objection named')
    for b in d.get('before', []):
        if b and b not in done and b not in specs: problems.append(f'{i}: before "{b}" is neither a journey nor a spec')
    for kind, ids_ in (('Learn', mem), ('Music', music)):
        for line in re.findall(r'\*' + kind + r':\*\s*([^*]+?)(?:\*|$)', d['body'], re.M):
            for tok in re.findall(r'(new\s+)?`([a-z0-9-]+)`', line):
                if not tok[0] and tok[1] not in ids_ and not (kind == 'Learn' and tok[1] in newids): problems.append(f'{i}: {kind.lower()} id `{tok[1]}` does not exist (mark it new or choose another)')

for b, lst in bible_specs.items():
    for x in range(len(lst)):
        for y in range(x + 1, len(lst)):
            if lst[x][1] != lst[y][1] and overlap(lst[x][0], lst[y][0]):
                problems.append(f'{lst[x][1]} and {lst[y][1]} both read {lst[x][2]} / {lst[y][2]}: give it to one, point back from the other')
for k, lst in text_specs.items():
    if len(set(lst)) > 1: notes.append(f'set text listed by several specs: "{k}" in {", ".join(sorted(set(lst)))} (check the sections differ)')

# hall walk: every planned (later) title has a spec
for h in halls:
    for l in h.get('later', []):
        t = l['title'].lower()
        if not any(d['title'].lower().startswith(t[:18]) or t.startswith(d['title'].lower()[:18]) for d in specs.values()):
            problems.append(f'hall {h["id"]}: planned "{l["title"]}" has no spec')

flags = sum(1 for d in specs.values() if '**Flags:**' in d['body'])
print(f'{len(specs)} specs ({sum(1 for d in specs.values() if d.get("kind") == "rewrite")} rewrites), {flags} with flags')
print(f'\n{len(problems)} problems:'); [print(' -', p) for p in problems]
print(f'\n{len(notes)} notes:'); [print(' -', n) for n in notes]
sys.exit(1 if problems else 0)
