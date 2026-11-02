"""Extract the set texts for the Plato journey.

Sources (all in .cache/texts, headers checked):
  1497.txt  Plato, The Republic, tr. Benjamin Jowett (Gutenberg #1497; Jowett 1817-1893; 1st ed. 1871, 3rd ed. 1888)
  1658.txt  Plato, Phaedo, tr. Benjamin Jowett (Gutenberg #1658)
  8438.txt  Aristotle, Nicomachean Ethics, tr. D. P. Chase (1847, rev. 1861; Everyman text, Gutenberg #8438; Chase d. 1902)
  3296.txt  Augustine, Confessions, tr. E. B. Pusey (1838; Gutenberg #3296; Pusey d. 1882)
McMahon's Metaphysics (archive.org) was not fetched (the search returned nothing), so session 6 reads
Aristotle's other attack on the Form of the Good, Nicomachean Ethics I.6 (Bekker numbering; Chase's chapter III).
Jowett's Gutenberg text has no Stephanus numbers: the ranges in the refs were matched to his paragraphs by content.
Paragraphs are split on blank lines, never on line ends. Chase's footnote markers ('[11]') are removed and listed.
Run: python3 tools/journeys/src/plato/extract.py
"""
import re, json, os
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..'))
T = os.path.join(ROOT, '.cache', 'texts')

def read(n):
    t = open(os.path.join(T, f'{n}.txt'), encoding='utf-8').read()
    return t[t.index('*** START'):t.index('*** END')]

def blocks(t): return [re.sub(r'\s+', ' ', b.strip()) for b in re.split(r'\n\s*\n', t) if b.strip()]

FOOT = []
def pick(bl, idxs, where, starts):
    out = []
    for i in idxs:
        if i == '…': out.append('…'); continue
        p = bl[i]
        p2 = re.sub(r'\[(\d{1,3})\]', lambda m: FOOT.append((where, m.group(1), p[max(0, m.start() - 30):m.start()])) or '', p)
        out.append(p2)
    real = [x for x in out if x != '…']
    got = [p[:len(s)] for p, s in zip(real, starts)]
    assert got == starts, (where, got, starts)
    return out

def rng(a, b): return list(range(a, b + 1))

# Republic: the dialogue text begins after the translator's introduction (second 'PERSONS OF THE DIALOGUE')
P = read(1497); D = P[P.index('PERSONS OF THE DIALOGUE.', P.index('PERSONS OF THE DIALOGUE.') + 10):]
names = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X']
pos = [D.index(f'\n BOOK {n}.\n') for n in names] + [len(D)]
B = {n: blocks(D[pos[k]:pos[k + 1]])[1:] for k, n in enumerate(names)}   # [1:] drops the 'BOOK n.' heading
R = {}

# Session 1: Republic VII.514a–519b (the cave, and education as turning)
R['cave'] = pick(B['VII'], rng(0, 53), 'Republic VII',
    ['And now, I said, let me show in a figure', 'I see.', 'And do you see, I said, men passing', 'You have shown me a strange image'])
# Session 2: Phaedo 72e–77a (recollection and equality itself); Republic V.475e–476d (lovers of sights, dreamers and the awake)
PH = read(1658); PD = blocks(PH[PH.rindex('PERSONS OF THE DIALOGUE'):])
s = next(k for k, b in enumerate(PD) if b.startswith('Cebes added: Your favorite doctrine'))
R['phaedo'] = pick(PD, rng(s, s + 86), 'Phaedo', ['Cebes added: Your favorite doctrine', 'But tell me, Cebes, said Simmias'])
assert R['phaedo'][-1].startswith('Yes, Socrates; I am convinced'), R['phaedo'][-1][:40]
R['rep5sights'] = pick(B['V'], rng(448, 470), 'Republic V', ['He said: Who then are the true philosophers?'])
assert R['rep5sights'][-1] == 'Certainly.'
# Session 3: Republic IV.434d–436b; 436b; 439a–441c; 441d–442d; 443c–444a (the three parts of the soul)
R['rep4'] = pick(B['IV'], rng(257, 266) + ['…'] + rng(277, 281) + ['…'] + rng(329, 368) + ['…'] + rng(375, 392) + ['…'] + rng(413, 416), 'Republic IV',
    ['We will not, I said, be over-positive', 'That will be in regular course'])
assert R['rep4'][-1].startswith('You have said the exact truth')
# Session 4: Republic VI.506b–509c (the sun and the Good) and 509d–511e (the divided line)
R['sun'] = pick(B['VI'], rng(313, 385), 'Republic VI', ['Of course, he replied; but I wish that you would tell me'])
assert R['sun'][-1] == 'I hope not, he said.'
R['line'] = pick(B['VI'], rng(386, 407), 'Republic VI', ['You have to imagine, then, that there are two ruling powers'])
# Session 5: Republic III.414b–415d (the noble lie), 416d–417b (no property), V.473b–e (philosopher-kings), VII.519b–521b (the return)
R['lie'] = pick(B['III'], rng(469, 479) + ['…'] + rng(493, 496), 'Republic III', ['How then may we devise one of those needful falsehoods'])
R['kings'] = pick(B['V'], rng(419, 427), 'Republic V', ['I think, I said, that there might be a reform'])
R['return'] = pick(B['VII'], rng(54, 73), 'Republic VII', ['Yes, I said; and there is another thing which is likely'])
assert R['return'][-1].startswith('They are the men, and I will choose them')
# Session 6 compare: Republic IX.591c–592b (the pattern laid up in heaven)
R['pattern'] = pick(B['IX'], rng(391, 404), 'Republic IX', ['To this nobler purpose the man of understanding'])
# Session 7 compare: Republic X.617d–619b, 619b–620d, 621b–d (the myth of Er: the choice of lives, and the ending)
R['er'] = pick(B['X'], [314, 315, '…', 317], 'Republic X', ['When Er and the spirits arrived', 'And according to the report of the messenger', 'And thus, Glaucon, the tale has been saved'])
R['er-start'] = pick(B['X'], [312], 'Republic X', ['Well, I said, I will tell you a tale'])

# Session 6: Aristotle, Nicomachean Ethics I.6 (Chase's ch. III, from 'Again, the notion of one Universal Good')
NE = read(8438); NB = blocks(NE[NE.index('\nBOOK I\n', NE.index('Contents') + 400):])
a = next(k for k, b in enumerate(NB) if b.startswith('Again, the notion of one Universal Good'))
b = next(k for k, b in enumerate(NB) if b.endswith('—Thus much on these points.'))
R['ne'] = pick(NB, rng(a, b), 'Nicomachean Ethics I', ['Again, the notion of one Universal Good', 'In the next place, since good is predicated'])

# Session 7: Augustine, Confessions VII.9, VII.10, VII.20, VII.21 (Pusey's Gutenberg text has no chapter numbers)
A = read(3296); AB = blocks(A[A.index('\nBOOK VII\n'):A.index('\nBOOK VIII\n')])
def find(bl, start):
    hits = [k for k, x in enumerate(bl) if x.startswith(start)]; assert len(hits) == 1, (start, hits); return hits[0]
i9 = find(AB, 'And Thou, willing first to show me'); i10 = find(AB, 'And being thence admonished'); i20 = find(AB, 'But having then read those books')
R['conf'] = pick(AB, [i9, i9 + 1, i9 + 2, i10, '…', i20, i20 + 1], 'Confessions VII',
    ['And Thou, willing first to show me', 'Again I read there, that God the Word', 'And therefore did I read there also', 'And being thence admonished', 'But having then read those books', 'Most eagerly then did I seize'])

for k, v in R.items(): print(k, len(' '.join(v).split()), 'words', len(v), 'paras')
for w, n, ctx in FOOT: print('footnote removed:', w, n, 'after', repr(ctx))
json.dump(R, open(os.path.join(HERE, 'raw.json'), 'w'), ensure_ascii=False, indent=1)
json.dump([{'where': w, 'number': n, 'after': ctx} for w, n, ctx in FOOT], open(os.path.join(HERE, 'footnotes.json'), 'w'), ensure_ascii=False, indent=1)
