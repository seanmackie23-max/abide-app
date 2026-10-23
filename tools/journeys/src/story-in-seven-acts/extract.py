"""Set texts for The story in seven acts. Augustine (Dods) from .cache/books/cityofgod (Gutenberg #45305, via the
texts-cache branch), Paine from .cache/books/paine (#3743). Milton XII and Augustine XXII.30 are kept from the
first version of this journey (already in raw.json)."""
import re, json, os
HERE = os.path.dirname(os.path.abspath(__file__)); B = os.path.join(HERE, '..', '..', '..', '..', '.cache', 'books')
def read(p): return open(os.path.join(B, p), encoding='utf-8', errors='ignore').read().replace('\r', '')
def blocks(t): return [re.sub(r'\s+', ' ', b).strip() for b in re.split(r'\n\s*\n', t) if b.strip()]
def para(bl, start): return next(b for b in bl if b.startswith(start))
clean = lambda s: re.sub(r'\[\d+\]', '', s).replace('_', '')
R = json.load(open(os.path.join(HERE, 'raw.json')))
C = blocks(read('cityofgod/45305.txt'))
p28 = clean(para(C, 'Accordingly, two cities have been formed by two loves'))
p15 = clean(para(C, 'OF the bliss of Paradise'))
i = p15.index('This race we have distributed into two parts')
R['augustine14'] = [p28, '…', p15[i:]]
P = blocks(read('paine/3743.txt'))
R['paine'] = [para(P, 'When we see the studied craft of the scripture-makers'), para(P, 'Behold a virgin shall conceive, and bear a son (Isa. vii. I4)'), para(P, 'Whether Isaiah was playing a trick with Ahaz'), para(P, 'The king of Syria and the king of Israel'), para(P, 'In this situation of things, Isaiah addresses himself to Ahaz')]
for k, v in R.items(): print(k, [len(x.split()) for x in v])
json.dump(R, open(os.path.join(HERE, 'raw.json'), 'w'), ensure_ascii=False, indent=1)
