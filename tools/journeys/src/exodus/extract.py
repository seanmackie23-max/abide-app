"""Extract the set texts for Exodus and the law from the Gutenberg and Perseus files."""
import re, json, os
HERE = os.path.dirname(os.path.abspath(__file__)); B = os.path.join(HERE, '..', '..', '..', '..', '.cache', 'books')
TAC = '/tmp/claude-0/-home-claude/a89da40b-1fd7-57c8-a14f-13683ecac49a/scratchpad/tac/canonical-latinLit/data/phi1351/phi004/phi1351.phi004.perseus-eng1.xml'
def read(p): return open(os.path.join(B, p), encoding='utf-8', errors='ignore').read().replace('\r', '')
def blocks(t): return [re.sub(r'\s+', ' ', b).strip() for b in re.split(r'\n\s*\n', t) if b.strip()]
def para(bl, start): return next(b for b in bl if b.startswith(start))
fn = lambda s: re.sub(r'\s*\[\d+\]', '', s)
R = {}
L2 = blocks(read('legends2/1494.txt'))
R['midwives'] = [fn(para(L2, 'The two Hebrew midwives were Jochebed')), fn(para(L2, 'The king used all sorts of devices'))]
R['shepherd'] = [fn(para(L2, 'Moses watched over the flocks with loving care')), fn(para(L2, 'Once a kid escaped from the flock')), '…', fn(para(L2, 'There were good reasons for selecting the thorn-bush'))]
HB = blocks(read('hebraic/14368.txt'))
R['talmud'] = [next(b for b in HB if 'Akiva was apprehended' in b), para(HB, 'Once a Gentile came to Shamai, and said, "Proselytize me')]
D = blocks(read('bondage/202.txt'))
i = next(k for k, b in enumerate(D) if b.startswith('I am the more inclined to think that he suspected us'))
dq = [re.sub(r'\{\d+\}', '', b).replace('_', '') for b in D[i:i + 6]]
R['douglass'] = dq
H = blocks(read('hammurabi/17150.txt'))
sec = lambda n: para(H, f'section {n}.')
R['hammurabi'] = [sec(15), sec(16), sec(117), sec(196), sec(197), sec(198), sec(199), sec(200), sec(201), sec(282)]
t = open(TAC, encoding='utf-8').read(); j = t.find('Most writers, however, agree'); k = t.find('Moyses, wishing to secure', j)
s = re.sub(r'<note.*?</note>', '', t[j:k], flags=re.S); s = re.sub(r'<[^>]+>', '', s); s = s.replace('&aelig;', 'æ')
R['tacitus'] = [re.sub(r'\s+', ' ', s).strip()]
for k, v in R.items(): print(k, [len(x.split()) for x in v])
json.dump(R, open(os.path.join(HERE, 'raw.json'), 'w'), ensure_ascii=False, indent=1)
