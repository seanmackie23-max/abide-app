"""Extract the set texts for 'Rome: Cicero, Virgil and the law' from the Gutenberg files in .cache/texts.

Every passage is copied from the file. Paragraphs are split on blank lines, never on line ends.
Editorial marks removed (listed in notes.json): Mackail's line-number brackets such as [255-289];
footnote markers such as [344], [114] and Gibbon's ' 59'; Shuckburgh's chapter numbers '+12.+';
Moyle's section numbers at the start of paragraphs; Tacitus's chapter number '30.'.
"""
import re, json, os
HERE = os.path.dirname(os.path.abspath(__file__))
T = os.path.join(HERE, '..', '..', '..', '..', '.cache', 'texts')
def read(f): return open(os.path.join(T, f), encoding='utf-8', errors='ignore').read().replace('\r', '')
def blocks(t): return [re.sub(r'\s+', ' ', b).strip() for b in re.split(r'\n\s*\n', t) if b.strip()]
def para(bl, start):
    return next(b for b in bl if b.startswith(start))
def after(bl, start, n):
    i = next(k for k, b in enumerate(bl) if b.startswith(start)); return bl[i:i + n]
def cut(p, a=None, b=None):
    """Slice a paragraph from the words a (inclusive) to the words b (inclusive)."""
    i = p.index(a) if a else 0
    j = p.index(b, i) + len(b) if b else len(p)
    return p[i:j]
def lines(s): return re.sub(r' {2,}', ' ', re.sub(r'\[\d+-\d+\]', ' ', s)).strip()
def notes(s): return re.sub(r'\[\d+\]', '', s).replace(' ,', ',').replace(' .', '.')
R = {}

# Virgil, Aeneid, tr. J. W. Mackail (1885), Gutenberg #22456
A = blocks(read('22456.txt'))
R['aen-proem'] = [lines(para(A, 'I sing of arms and the man')), lines(para(A, 'Muse, tell me why'))]
R['aen-1'] = [lines(para(A, 'Smiling on her with that look')), lines(para(A, "'Spare thy fear, Cytherean"))]
R['aen-4'] = [lines(p) for p in after(A, 'But Aeneas in truth gazed in dumb amazement', 8)]
R['aen-4'].append(lines(cut(para(A, 'But good Aeneas, though he would fain soothe'), None, 'returns to his fleet.')))
R['aen-6'] = [lines(para(A, 'Anchises ceased, and leads his son')), lines(para(A, "'Now come, the glory hereafter"))]
R['aen-1-33'] = [cut(para(A, 'There was a city of ancient days'), 'and many a year were they wandering', 'Such work was it to found the Roman people.')]

# Polybius, Histories VI.11-18, tr. Evelyn S. Shuckburgh (1889), Gutenberg #44125
P = blocks(read('44125.txt'))
num = lambda s: re.sub(r'^\+\d+\.\+ ', '', notes(s))
R['polybius'] = [num(para(P, '+11.+ I have given an account of the constitution of Lycurgus')), '…',
 num(para(P, 'As for the Roman constitution, it had three elements')),
 num(para(P, '+12.+ The Consuls, before leading out the legions')),
 num(para(P, '+13.+ The Senate has first of all the control')),
 num(para(P, '+14.+ After this one would naturally be inclined')),
 num(para(P, 'Again, it is the people who bestow offices')),
 num(para(P, 'These considerations again would lead one to say')),
 num(para(P, '+15.+ Such, then, is the distribution of power')),
 num(para(P, 'The Consul, then, when he has started on an expedition')),
 num(para(P, 'But these triumphs the commanders cannot celebrate')),
 num(para(P, '+16.+ As for the Senate, which possesses the immense power')),
 num(para(P, '+17.+ In like manner the people on its part')),
 num(para(P, '+18.+ The result of this power of the several estates'))]

# Cicero, On the Commonwealth, tr. Francis Barham (1841) revised by C. D. Yonge (1853), Gutenberg #14988
C = blocks(read('14988.txt'))
R['scipio'] = [notes(para(C, 'XIII. Now, in order to encourage you')),
 notes(para(C, 'That, replied he, is impossible')),
 notes(para(C, 'Men are likewise endowed with a soul')),
 notes(para(C, 'But rather follow the examples of your grandfather')),
 notes(cut(para(C, 'From thence, as I took a view of the universe'), None, None)),
 notes(para(C, 'XIX. On which Africanus said')),
 '…',
 notes(para(C, 'XXIII. Wherefore, if you have no hopes'))]
R['cic-3-law'] = [notes(cut(para(C, 'VIII. * * * Both to discover and maintain'), 'But the weakness of their cause', None)),
 notes(cut(para(C, 'XI. * * * [If this justice were natural'), 'The laws are, therefore, based', None)),
 '…',
 notes(para(C, 'XXI. _Scipio._ I might reply')),
 notes(para(C, '_Lælius._ This Carneades ought not')),
 notes(para(C, 'XXII.[344] True law is right reason'))]
R['cic-3-empire'] = [notes(para(C, 'XII. For when he[339] inquired of a pirate')),
 notes(para(C, 'Wisdom and prudence instruct us by all means')),
 notes(para(C, 'But justice commands us to have mercy upon all men')),
 notes(para(C, 'XIII. How far utility is at variance with justice')),
 notes(para(C, "What is the advantage of one's own country")),
 notes(para(C, 'XV. This was the sum of the argument of Carneades'))]

# Tacitus, Agricola 30, the Oxford translation revised (Gutenberg #7524)
G = blocks(read('7524.txt'))
R['agricola'] = [re.sub(r'^30\. ', '', notes(para(G, '30. "When I reflect on the causes of the war'))).strip()]

# Augustine, The City of God, tr. Marcus Dods (1871), Gutenberg #45304
D = blocks(read('45304.txt'))
v12 = after(D, 'Wherefore let us go on to consider what virtues of the Romans', 7)
v13 = after(D, 'Wherefore, when the kingdoms of the East had been illustrious', 5)
R['cog-5'] = [notes(cut(v12[0], None, 'thirst for glory did.')), '…'] + [notes(p) for p in v12[2:7]] + [notes(p) for p in v13[:4]] + [notes(cut(v13[4], None, 'beneficial to the republic.'))]
R['cog-10'] = [notes(cut(next(b for b in D if 'It is of Him, too, that the most famous poet speaks' in b), 'It is of Him, too, that the most famous poet speaks', 'dictated by the Cumæan sibyl.'))]

# Gibbon, Decline and Fall, ch. XX (1776-1789), Gutenberg #25717
GB = blocks(read('25717.txt'))
g = next(b for b in GB if 'Forty years before the birth of Christ, the' in b)
g = cut(g, 'Forty years before the birth of Christ', 'missionaries of the gospel.')
R['gibbon'] = [re.sub(r' (6[0-2])(?=[ ,;.]|$)', '', g).replace(', 61 but', ', but').replace(' 61 ', ' ')]

# Justinian, Institutes, tr. J. B. Moyle (5th ed. 1913; 1st ed. 1883), Gutenberg #5983
J = blocks(read('5983.txt'))
sec = lambda s: re.sub(r'^\d+ ', '', s)
R['justinian'] = [para(J, 'The imperial majesty should be armed with laws'),
 '…',
 para(J, 'Justice is the set and constant purpose'),
 sec(para(J, '1 Jurisprudence is the knowledge')),
 sec(para(J, '3 The precepts of the law are these')),
 sec(para(J, '4 The study of law consists of two branches')),
 sec(para(J, '1 The law of nature is that which she has taught')),
 sec(para(J, '2 Civil law takes its name from the state')),
 '…',
 sec(para(J, '11 But the laws of nature, which are observed')),
 para(J, 'In the law of persons, then, the first division'),
 sec(para(J, '1 Freedom, from which men are called free')),
 sec(para(J, '2 slavery is an institution of the law of nations'))]

for k, v in R.items(): print(k, [len(x.split()) for x in v], sum(len(x.split()) for x in v))
json.dump(R, open(os.path.join(HERE, 'raw.json'), 'w'), ensure_ascii=False, indent=1)
