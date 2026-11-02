"""Extract the set texts for Number and nature from the cached texts in .cache/texts.

Paragraphs are split on blank lines, never on line ends. Footnote and endnote markers are removed (listed in notes.json).
Run: python3 tools/journeys/src/number-and-nature/extract.py

Sources (all checked against the file headers):
  57342.txt  Diogenes Laertius, Lives and Opinions of Eminent Philosophers, tr. C. D. Yonge (Bohn, 1853; Yonge d. 1891)
  2707.txt   Herodotus, History, vol. 1, tr. G. C. Macaulay (1890; d. 1915)
  1497.txt   Plato, Republic, tr. Benjamin Jowett (d. 1893)
  59.txt     Descartes, Discourse on Method, tr. John Veitch (1850; d. 1894)
  44125.txt  Polybius, Histories, vol. 1, tr. Evelyn S. Shuckburgh (1889; d. 1906)
  14988.txt  Cicero, Tusculan Disputations and On the Commonwealth, tr. C. D. Yonge (Republic revised from Francis Barham, 1841), Harper 1877
  url/number-and-nature-hippocrates-sacred.txt, -oath.txt  Hippocrates, tr. Francis Adams (1849; d. 1861), MIT Internet Classics Archive
  25717.txt  Gibbon, Decline and Fall (1776-89), with Milman's notes
  url/number-and-nature-socrates-scholasticus-7.txt  Socrates Scholasticus, Church History VII, tr. A. C. Zenos, NPNF II.2 (1890)
  1572.txt   Plato, Timaeus, tr. Benjamin Jowett
"""
import re, json, os, html
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..'))
T = os.path.join(ROOT, '.cache', 'texts')
def read(p): return open(os.path.join(T, p), encoding='utf-8', errors='ignore').read().replace('\r', '')
def blocks(t): return [re.sub(r'\s+', ' ', b).strip() for b in re.split(r'\n\s*\n', t) if b.strip()]
def vblocks(t): return ['\n'.join(l.strip() for l in b.split('\n') if l.strip()) for b in re.split(r'\n\s*\n', t) if b.strip()]
def one(bl, start):
    hits = [b for b in bl if b.startswith(start)]
    assert len(hits) == 1, (start, len(hits))
    return hits[0]
def upto(s, end):
    i = s.index(end) + len(end); return s[:i]
def fromw(s, start):
    return s[s.index(start):]
nofn = lambda s: re.sub(r'^[IVXL]+\. ', '', re.sub(r'\[\d+\]', '', s).replace(' ,', ',').strip())  # footnote numbers and Yonge's section numerals
R = {}

# Diogenes Laertius, tr. Yonge. Yonge's section numbers (I., II. ...) are his own, not the standard numbering;
# the standard references are given in the session refs (see notes.json).
DL = read('57342.txt')
th = blocks(DL[DL.index('LIFE OF THALES.'):DL.index('LIFE OF SOLON.')])
R['thales'] = [nofn(one(th, 'II. After having been immersed')).split(' But Callimachus')[0],   # I.23 (cut before the verses)
               nofn(one(th, 'According to others he wrote two books')),                      # I.23
               nofn(upto(one(th, 'III. Some again'), 'that he sacrificed an ox in honour of his discovery.')),  # I.24
               nofn(one(th, 'VI. He asserted water')),                                        # I.27
               nofn(one(th, 'VIII. It is said that once he was led out')).split(' Timon also')[0],  # I.34
               nofn(upto(one(th, 'And the following are quoted as sayings of his'), 'for it finds out everything.”'))]  # I.35
an = blocks(DL[DL.index('LIFE OF ANAXIMANDER.'):DL.index('LIFE OF ANAXAGORAS.')])
he = blocks(DL[DL.index('LIFE OF HERACLITUS.'):DL.index('LIFE OF XENOPHANES.')])
R['ionians'] = [nofn(one(an, 'II. He used to assert')),                    # II.1
                nofn(one(an, 'III. He also was the first discoverer')),    # II.1-2
                nofn(upto(one(an, 'I. Anaximenes, the son of Eurystratus'), 'around the earth.')),  # II.3
                nofn(upto(one(he, 'II. He was above all men'), 'which by itself will govern everything on every occasion.”')),  # IX.1
                nofn(upto(one(he, 'In particulars, his doctrines are of this kind'), 'and that the whole world exists according to it.'))]  # IX.8
# Herodotus I.74, tr. Macaulay: footnote numbers 88, 89 removed
H = blocks(read('2707.txt'))
R['herodotus'] = [re.sub(r'^74\. ', '', re.sub(r' \d{2}(?=[: ])', '', upto(one(H, '74. After this, seeing that Alyattes'), 'that peace should be made between them.')))]

py = DL[DL.index('LIFE OF PYTHAGORAS.'):DL.index('LIFE OF EMPEDOCLES.')]
pb = blocks(py); pv = vblocks(py)
R['pythagoras'] = [nofn(upto(one(pb, 'VI. And Sosicrates'), 'but philosophers are seekers after truth.”')),  # VIII.8
                   nofn(one(pb, 'VIII. He was the first person, as Timæus says')),                   # VIII.10
                   nofn(upto(one(pb, 'XI. It was Pythagoras also who carried geometry'), 'the sides containing the right angle.')),                 # VIII.11-12
                   nofn(one(pb, 'XIII. He was also the first person who introduced measures')),       # VIII.14
                   nofn(one(pb, 'That the monad was the beginning of everything')),                   # VIII.25
                   nofn(upto(one(pb, 'They also say, that the most important privilege'), 'Also, that friendship is a harmonious equality.')),  # VIII.32-33
                   nofn(upto(one(pb, 'Another of his doctrines was, that of all solid figures'), 'and disease the destruction of it.')),  # VIII.35
                   nofn(one(pb, 'And respecting his having been different people')),                # VIII.36
                   one(pv, 'They say that once, as passing by he saw')]                              # VIII.36 (Xenophanes)

# Plato, Republic VI.510b-511e and VII.526c-527c, tr. Jowett
RP = read('1497.txt')
a = RP.index('Thus:—There are two subdivisions'); b = RP.index('I understand, he replied, and give my assent')
R['divided'] = blocks(RP[a:b])
a = RP.index('Yes, I said, but for that purpose a very little of either geometry'); b = RP.index('Then nothing should be more sternly laid down')
R['geometry'] = blocks(RP[a:b])

# Descartes, Discourse on Method, Part II, tr. Veitch
D = blocks(read('59.txt'))
R['descartes'] = [one(D, 'The first was never to accept anything for true'), one(D, 'The second, to divide each of the difficulties'),
                  one(D, 'The third, to conduct my thoughts in such order'), one(D, 'And the _last_, in every case').replace('_last_', 'last'),
                  upto(one(D, 'The long chains of simple and easy reasonings'), 'such must have been the rule of their investigations.')]

# Polybius VIII.5-9, tr. Shuckburgh: the bold section numbers (+5.+) and footnote numbers removed; VIII.6 (the sambuca) left out
P = blocks(read('44125.txt'))
sec = lambda s: nofn(re.sub(r'^\+\d+\.\+ ', '', s))
R['polybius'] = [sec(one(P, '+5.+ When Epicydes and Hippocrates had occupied Syracuse')), '…',
                 sec(one(P, '+7.+ With such contrivances')), sec(one(P, '+8.+ Other machines which he invented')),
                 sec(upto(one(P, '+9.+ Nor was Appius Claudius more successful'), 'which made it possible for Archimedes to oppose them.'))]

# Cicero, On the Commonwealth I.14 and Tusculan Disputations V.23 (V.64-66), tr. Yonge/Barham
C = blocks(read('14988.txt'))
R['cicero_sphere'] = [nofn(upto(fromw(one(C, 'XIV. Then Philus said'), 'XIV. Then Philus said: ')[len('XIV. Then Philus said: '):], 'at the instant the sun appears opposite.'))]
R['cicero_tomb'] = [upto(one(C, 'I will present you with an humble and obscure mathematician'), 'in constant fears by night and by day.')]

# Cicero, Tusculan Disputations I.25 (I.62-63), tr. Yonge: Archimedes' sphere and Plato's God
cg = one(C, next(b for b in C if 'when Archimedes described in a sphere' in b)[:40])
R['cicero_god'] = [upto(fromw(cg, 'For we have provided great entertainments'), 'without a divine soul.')]

# Hippocrates, tr. Adams (MIT Internet Classics Archive). The MIT transcription has some garbled words; they are kept and flagged in notes.json.
S = blocks(read('url/number-and-nature-hippocrates-sacred.txt'))
R['sacred'] = [one(S, 'It is thus with regard to the disease called Sacred'),
               one(S, 'Thus, they who try to cure these maladies in this way'), '…',
               upto(one(S, 'But this disease seems to me to be no more divine than others'), 'like that of other diseases.'), '…',
               one(S, 'Men ought to know that from nothing else but the brain'), '…',
               one(S, 'And the disease called the Sacred arises from causes as the others')]
O = one(blocks(read('url/number-and-nature-hippocrates-oath.txt')), 'I SWEAR by Apollo')
# The Oath is one paragraph in the source; it is shown in five pieces, split only at sentence ends (no word changed).
cuts = ['I will follow that system of regimen', 'With purity and with holiness', 'Into whatever houses I enter', 'While I continue to keep this Oath']
pieces = []; rest = O
for c in cuts:
    i = rest.index(c); pieces.append(rest[:i].strip()); rest = rest[i:]
pieces.append(rest.strip())
assert ' '.join(pieces) == O
R['oath'] = pieces

# Gibbon, Decline and Fall, ch. XXVIII (the Serapeum, 391) and ch. LI (the Arab conquest and the library story).
# Footnote numbers (35, 41, 4411, 4711 ...) removed.
G = blocks(read('25717.txt'))
gfn = lambda s: re.sub(r' \d{2,4}(?=[ ,.;:]|$)', '', s)
g1 = gfn(one(G, 'In this wide and various prospect of devastation'))
g2 = gfn(one(G, 'At that time 43 the archiepiscopal throne'))
R['gibbon'] = [g1,
               upto(g2, 'which were the reward of his victory.'), '…',
               upto(fromw(g2, 'The colossal statue of Serapis'), 'the object, and the folly, of his superstitious attachment.')]
l1 = gfn(one(G, 'I should deceive the expectation of the reader'))
l2 = gfn(one(G, 'Amrou was inclined to gratify the wish of the grammarian'))
R['gibbon51'] = [l1, upto(l2, 'our treasures, rather than our losses, are the objects of my surprise.')]

# Socrates Scholasticus VII.15, tr. Zenos (New Advent). HTML entities turned into letters (&aelig; -> æ).
SS = blocks(read('url/number-and-nature-socrates-scholasticus-7.txt'))
R['hypatia'] = [html.unescape(one(SS, 'There was a woman at Alexandria named Hypatia'))]

# Plato, Timaeus 27c-30c, tr. Jowett
TM = read('1572.txt')
a = TM.index('TIMAEUS: All men, Socrates, who have any degree'); b = TM.index('This being supposed, let us proceed to the next stage')
R['timaeus'] = blocks(TM[a:b])

# Wisdom of Solomon 11:17-26, World English Bible (Classic, ecumenical edition), from ebible.org (web.py has no deuterocanon).
# Each verse is a paragraph, with its number and its line breaks; the one footnote marker (11:4) lies outside this passage.
W = read('url/web-wisdom-11.txt')
W = W[W.index('\n17 For your all-powerful hand'):W.index('\nWisdom of Solomon\n', W.index('26 But you spare'))]
vs = re.split(r'\n\s*\n(?=\d+ )', W.strip())
R['wisdom'] = ['\n'.join(l.strip() for l in v.split('\n') if l.strip()) for v in vs]
assert R['wisdom'][0].startswith('17 ') and R['wisdom'][-1].startswith('26 ') and len(R['wisdom']) == 10

# Mark the cuts between passages that are not continuous in the source.
def gaps(lst, keep_together=()):
    out = []
    for i, x in enumerate(lst):
        if i and i not in keep_together: out.append('…')
        out.append(x)
    return out
R['thales'] = gaps(R['thales'], keep_together=(2,))
R['pythagoras'] = gaps(R['pythagoras'])
R['ionians'] = R['ionians'][:3] + ['…'] + R['ionians'][3:4] + ['…'] + R['ionians'][4:]   # Heraclitus IX.1, cut, IX.8
for k, v in R.items(): print(k, [len(x.split()) for x in v])
json.dump(R, open(os.path.join(HERE, 'raw.json'), 'w'), ensure_ascii=False, indent=1)
