"""Extract the set texts for the Aristotle journey from the fetched texts in .cache/texts.

Paragraphs are split on blank lines, never on line ends. Footnote markers such as [8] (Chase's Ethics,
Yonge's Cicero, Darwin) and Bekker page numbers such as [1253a] (Ellis's Politics) are removed and listed
in notes.json. No word is changed. Where only part of a long paragraph is used, the cut is marked with a
paragraph that is just "…".

Sources (all checked against the file headers):
  8438.txt   Aristotle, Nicomachean Ethics, tr. D. P. Chase (1847), Everyman 1911 with J. A. Smith's introduction
  6762.txt   Aristotle, Politics, tr. William Ellis (1776), Everyman 1912
  2009.txt   Darwin, The Origin of Species, 6th edition (1872): the Historical Sketch, footnote 1, quoting
             Physics II.8 in Clair James Grece's translation
  14988.txt  Cicero, Tusculan Disputations, tr. C. D. Yonge, and On the Nature of the Gods (the Francklin
             translation revised for Bohn's Classical Library), Bohn 1853
  url/aristotle-summa-1-2-3.txt  Aquinas, Summa Theologiae I-II q.3, tr. Fathers of the English Dominican
             Province, 2nd ed. 1920 (New Advent)
"""
import re, json, os
HERE = os.path.dirname(os.path.abspath(__file__))
T = os.path.join(HERE, '..', '..', '..', '..', '.cache', 'texts')


def read(p):
    t = open(os.path.join(T, p), encoding='utf-8', errors='ignore').read().replace('\r', '')
    s = t.find('*** START OF'); e = t.find('*** END OF')
    if s >= 0: t = t[t.index('\n', s) + 1:]
    if e >= 0: t = t[:t.find('*** END OF')]
    return t


def blocks(t):
    return [re.sub(r'\s+', ' ', b).strip() for b in re.split(r'\n\s*\n', t) if b.strip()]


def find(bl, start, after=0):
    for i in range(after, len(bl)):
        if bl[i].startswith(start): return i
    raise ValueError('not found: ' + start)


def run(bl, start, end, after=0):
    i = find(bl, start, after); j = find(bl, end, i)
    return bl[i:j + 1]


def sub(p, start, end=None):
    """Part of a paragraph, from `start` to the end of `end` (inclusive)."""
    i = p.index(start)
    if end is None: return p[i:]
    j = p.index(end, i) + len(end)
    return p[i:j]


FOOT = re.compile(r'\[\d{1,3}\]')
BEKKER = re.compile(r' ?\[[1I]\d{3}[ab]\]')
clean = lambda s: re.sub(r'\s+', ' ', BEKKER.sub('', FOOT.sub('', s))).strip()
R = {}

# --- Nicomachean Ethics, Chase -------------------------------------------------------------
E = blocks(read('8438.txt'))
b1 = find(E, 'Every art, and every science reduced to a teachable form')
R['en1'] = [clean(x) for x in E[b1:b1 + 6]]

b2 = find(E, 'Well: human Excellence is of two kinds')
c1 = run(E, 'Well: human Excellence is of two kinds', 'So then, whether we are accustomed this way', b2)
c3 = run(E, 'The facts,[8] it is true', 'We are right then in saying, that these virtues', b2)
c5 = run(E, 'Now what the genus of Virtue is has been said', '“Men may be bad in many ways', b2)
c6 = run(E, 'Virtue then is “a state apt to exercise deliberate choice', 'In these then you never can go right', b2)
R['en2'] = [clean(x) for x in c1] + ['…'] + [clean(x) for x in c3] + ['…'] + [clean(x) for x in c5] + [clean(x) for x in c6]

b6 = find(E, 'As for Practical Wisdom, we shall ascertain its nature')
v5 = run(E, 'As for Practical Wisdom, we shall ascertain its nature', 'For this reason we think Pericles', b6)
v8a = find(E, 'Nor again does Practical Wisdom consist in a knowledge of general', b6)
v8b = find(E, 'A corroboration of what I have said is', b6)
v12 = run(E, 'There is then a certain faculty, commonly named Cleverness', 'From what has been said then it is clear that one cannot be', b6)
R['en6'] = [clean(x) for x in v5] + ['…', clean(E[v8a]), '…', clean(E[v8b]), '…'] + [clean(x) for x in v12]

b10 = find(E, 'Now if Happiness is a Working in the way of Excellence of course')
x6 = E[b10:]
pick = lambda s: clean(x6[find(x6, s)])
R['en10'] = [
    pick('Now if Happiness is a Working in the way of Excellence'),
    pick('That it is Contemplative has been already stated'),
    pick('Next, it is also most Continuous'),
    pick('And the Self-Sufficiency which people speak of'),
    pick('Again, this alone would seem to be rested in for its own sake'),
    pick('Also, Happiness is thought to stand in perfect rest'),
    '…',
    pick('But such a life will be higher than mere human nature'),
    pick('Yet must we not give ear to those who bid one as man'),
    pick('In fact this Principle would seem to constitute each man'),
    pick('And second in degree of Happiness will be that Life'),
    '…',
    pick('And that the perfect Happiness must be a kind of Contemplative Working'),
    pick('Still, every one believes that they live'),
    pick('To the Gods then all their life is blessed'),
    '…',
    pick('Now he that works in accordance with, and pays observance to, Pure'),
]

# --- Politics, Ellis -----------------------------------------------------------------------
P = blocks(read('6762.txt'))
p2 = find(P, 'Now if in this particular science any one would attend to its original')
R['pol2'] = [clean(P[p2])]
p8 = P[find(P, '[1256a] As a slave is a particular species')]
R['pol8'] = ['…', clean(sub(p8, 'It is evident then that we may conclude of those things that are', 'as well for the state as the family.'))]
p12 = find(P, 'There are then three parts of domestic government')
p13 = find(P, 'It is evident then that in the due government of a family')
q13 = P[p13]; r13 = P[p13 + 2]  # the chapter is split by an indented quotation from Sophocles
R['pol12'] = [
    clean(P[p12]),
    clean(sub(q13, 'It is evident then that in the due government of a family', 'how can he be governed well?')),
    clean(sub(q13, 'for he who is intemperate', 'but in a different manner.')),
    clean(sub(q13, 'Thus a slave can have no power of determination', 'the woman\'s in obeying;')),
    '…',
    clean(sub(r13, 'In like manner the virtue of a slave is to be referred to his master', 'neglect his work through idleness or fear:')),
    '…',
    clean(sub(r13, 'It is evident then that a slave ought to be trained to those virtues', 'and thus we determine this matter.')),
    '…',
    clean(sub(r13, 'Since then every family is part of a city', 'the succeeding citizens are to be formed.')),
]

# --- Darwin quoting Physics II.8 (Grece) ---------------------------------------------------
D = blocks(read('2009.txt'))
d = D[find(D, '[1] Aristotle, in his “Physicæ Auscultationes”')]
R['darwin'] = [re.sub(r'^\[1\]\s*', '', d)]

# --- Cicero, Bohn (Yonge) ------------------------------------------------------------------
C = blocks(read('14988.txt'))
tus = next(b for b in C if 'Aristotle, a man superior to all others, both in genius and industry' in b)
R['cicero'] = [
    '…',
    clean(sub(tus, 'Aristotle, a man superior to all others, both in genius and industry')),
    clean(C[find(C, 'As, then, some animals are generated in the earth, some in the water')]),
    clean(C[find(C, 'Aristotle also deserves high commendation for his observation')]),
    clean(C[find(C, 'Well, then, did Aristotle[163] observe')]),
]

# --- Aquinas, Summa Theologiae I-II q.3 a.8 ------------------------------------------------
A = blocks(read('url/aristotle-summa-1-2-3.txt'))
a8 = find(A, 'Article 8. Whether man\'s happiness consists in the vision')
R['aquinas'] = [A[find(A, 'On the contrary, It is written (1 John 3:2)', a8)],
                A[find(A, 'I answer that, Final and perfect happiness', a8)],
                A[find(A, 'If therefore the human intellect, knowing the essence', a8)]]

for k, v in R.items():
    print(k, [len(x.split()) for x in v], sum(len(x.split()) for x in v))
json.dump(R, open(os.path.join(HERE, 'raw.json'), 'w'), ensure_ascii=False, indent=1)
