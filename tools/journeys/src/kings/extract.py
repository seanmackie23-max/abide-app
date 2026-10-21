"""Extract the set texts for Kings and prophets from the Gutenberg files (GITenberg clones in .cache/books)."""
import re, json, os
HERE = os.path.dirname(os.path.abspath(__file__)); B = os.path.join(HERE, '..', '..', '..', '..', '.cache', 'books')
def read(p): return open(os.path.join(B, p), encoding='utf-8', errors='ignore').read().replace('\r', '')
def blocks(t): return [re.sub(r'\s+', ' ', b).strip() for b in re.split(r'\n\s*\n', t) if b.strip()]
def para(bl, start): return next(b for b in bl if b.startswith(start))
R = {}
P = blocks(read('politics/6762.txt'))
p37 = para(P, 'Now the corruptions attending each of these governments are these')
p510 = para(P, 'It now remains that we speak of monarchies')
i = p510.index('A kingdom, as we have said, partakes much')
R['aristotle'] = [p37, '…', p510[i:]]
RP = blocks(read('republic/1497.txt'))
g1 = para(RP, 'Now that those who practise justice do so involuntarily')
R['gyges'] = [g1]
H = blocks(read('hesiod/348.txt'))
strip = lambda s: re.sub(r'^\(ll\. [\d-]+\)\s*', '', s)
R['hesiod'] = [strip(para(H, '(ll. 202-211)')), strip(para(H, '(ll. 212-224)')), strip(para(H, '(ll. 225-237)')), strip(para(H, '(ll. 248-264)'))]
PA = blocks(read('paine/3743.txt'))
R['paine'] = [para(PA, 'There are matters in that book, said to be done by the express command'), para(PA, 'To charger the commission of things upon the Almighty')]
for k, v in R.items(): print(k, [len(x.split()) for x in v])
json.dump(R, open(os.path.join(HERE, 'raw.json'), 'w'), ensure_ascii=False, indent=1)
