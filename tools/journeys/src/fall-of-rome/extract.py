"""Extract the set texts for The fall of Rome and what survived from the cached texts (.cache/texts).

Split on blank lines (or, for the Fordham HTML, on <p> elements), never on line ends.
Editorial insertions removed (and listed in notes.json): New Advent's inline Bible references,
Gutenberg footnote markers ([A], [42], ' 511'), and Fordham's bracketed Bible references.
"""
import re, json, os, html
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.join(HERE, '..', '..', '..', '..', '.cache', 'texts')
def read(p): return open(os.path.join(T, p), encoding='utf-8', errors='ignore').read().replace('\r', '')
def blocks(t): return [re.sub(r'\s+', ' ', b).strip() for b in re.split(r'\n\s*\n', t) if b.strip()]
def at(bl, start): return next(i for i, b in enumerate(bl) if b.startswith(start))
def fn(s): return re.sub(r'\[(?:[A-Z]|\d+)\]', '', s)
R = {}

# Jerome, Letter 127.12-14 (Fremantle, NPNF II.6, 1893)
J = blocks(read('url/for-jerome-127.txt')); j = at(J, '12. Whilst these things')
R['jerome'] = [J[j].replace('down. Isaiah 15:1 O God', 'down. O God')] + J[j + 1:j + 7] + [J[j + 7], J[j + 8]]
assert R['jerome'][1].startswith('Who can set forth') and R['jerome'][7].startswith('13.') and R['jerome'][8].startswith('14.')

# Augustine, City of God I.1, I.4, I.7 and V.17-18 (Dods, 1871)
C = blocks(read('45304.txt'))
c1 = at(C, 'For to this earthly city belong'); c4 = at(C, 'In other words, the place consecrated'); c7 = at(C, 'All the spoiling, then')
R['cog1'] = [C[c1], '…', fn(C[c4]), '…', fn(C[c7])]
c17 = at(C, 'For, as far as this life of mortals'); c18 = at(C, 'What great thing, therefore')
R['cog5'] = [fn(C[c17]), fn(C[c18])]

# Ambrose, Letter 18.3, 7-8, 23, 28 (de Romestin, NPNF II.10, 1896)
A = blocks(read('url/for-ambrose-18.txt'))
R['ambrose'] = [A[at(A, '3. The illustrious Prefect')], A[at(A, '7. Let, then, that invidious')], A[at(A, '8. By one road')], '…', A[at(A, '23. But, he says')], A[at(A, '28. Let them say')]]

# Boethius, Consolation I prose 1-4 and V prose 6 (H. R. James, 1897)
B = blocks(read('14328.txt'))
b1 = at(B, 'While I was thus mutely pondering'); b2 = at(B, "'But the time,' said she"); b3 = at(B, 'Even so the clouds of my melancholy')
b4 = at(B, "'Dost thou understand?' she asks"); b4b = at(B, "Then I, gathering together what strength"); b4e = at(B, "'And now methinks I see the villainous")
R['boe1'] = [fn(B[b1]).replace('[Greek: P]', 'Π').replace('[Greek: Th]', 'Θ'), fn(B[b1 + 1]), fn(B[b2]), fn(B[b3]), B[b3 + 1], fn(B[b3 + 2]), '…', B[b4], B[b4 + 1], B[b4 + 2], fn(B[b4b]), '…', fn(B[b4e]), B[at(B, "'Sovereign Ruler, Lord of all!")], B[at(B, "'Virtue cowers in dark retreats")]]
v = at(B, "'God is eternal; in this judgment")
R['boe5'] = [fn(B[v]), fn(B[v + 1]), B[v + 2], fn(B[v + 3]), '…', fn(B[at(B, "'True, for the Divine vision")]), fn(B[at(B, "'And all this being so")])]

# Gibbon, Decline and Fall ch. XXXVIII, General Observations (1781; Gutenberg #25717)
G = blocks(read('25717.txt')); g = at(G, 'The rise of a city, which swelled')
R['gibbon'] = [G[g], G[g + 1], G[g + 2].replace('chastity. 511 Faith', 'chastity. Faith')]
assert G[g + 2].startswith('As the happiness of a future life')

# Gregory the Great, Dialogues II ('P. W.' 1608, ed. Gardner 1911, Saint Pachomius Library 1995; Fordham)
t = read('url/for-gregory-dialogues.html')
D = [re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', '', x))).strip() for _, x in re.findall(r'<(p|h4)[^>]*>(.*?)</\1>', t, re.S)]
D = [d for d in D if d]
d = lambda s: D[at(D, s)]
R['greg5'] = [d('There was a man of venerable life'), d('But Bennet, desiring rather'), d('The man of God, Bennet, coming to this'), '…', d('About the same time likewise, certain shepherds'),
              d('GREGORY: When this great temptation'), d('Having now taken upon him the charge'), '…', d("GREGORY: When as God's servant daily increased"),
              d('On a certain day, as venerable Bennet was'), d('A strange thing, and since the time'), d('Coming back to the father'), '…', d('GREGORY: The holy man, changing his place')]
R['greg7'] = [d('Then Totilas himself in person'), d('The Bishop also of Camisina'), '…', d('The man of God, Bennet, being diligent in watching'), '…', d('GREGORY: Assure yourself, Peter'), d('GREGORY. Desirous I am, Peter')]

for k, vv in R.items():
    for p in vv:
        assert not re.search(r'\[(?:[A-Z]|\d+)\]', p), (k, p[:60])
    print(k, [len(x.split()) for x in vv], sum(len(x.split()) for x in vv))
json.dump(R, open(os.path.join(HERE, 'raw.json'), 'w'), ensure_ascii=False, indent=1)
