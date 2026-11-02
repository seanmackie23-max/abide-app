"""Extract the set texts for Socrates (Stage B, November 2026).

Sources, all in .cache/texts (headers checked, see notes.json):
  1656 Plato, Apology, tr. Benjamin Jowett          1657 Crito (Jowett)      1658 Phaedo (Jowett)
  1643 Meno (Jowett)                                1177 Xenophon, Memorabilia, tr. H. G. Dakyns (1897)
  2562 Aristophanes, The Clouds, tr. W. J. Hickie (Bohn, 1853)
  57342 Diogenes Laertius, Lives, tr. C. D. Yonge (1853)
  34901 J. S. Mill, On Liberty (1859)
  url/socrates-justin-2apol.txt  Justin Martyr, Second Apology, tr. M. Dods (ANF I, 1885), New Advent
Paragraphs are split on blank lines, never on line ends. Editorial notes inside the translations
(Jowett's '(Or, ...)', '(Compare ...)'; Dakyns's footnote numbers '(1)'; Yonge's '[19]') are removed
and listed in notes.json. No word of the translations is changed.
Run: python3 tools/journeys/src/socrates/extract.py
"""
import re, json, os
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..'))
T = os.path.join(ROOT, '.cache', 'texts')
def read(n): return open(os.path.join(T, n), encoding='utf-8', errors='ignore').read()
def blocks(t): return [re.sub(r'\s+', ' ', b.strip()) for b in re.split(r'\n\s*\n', t) if b.strip()]
def find(t, s, start=0):
    m = re.compile(r'\s+'.join(re.escape(w) for w in s.split())).search(t, start)
    if not m: raise ValueError(s)
    return m
def between(t, a, b): i = find(t, a).start(); j = find(t, b, i).end(); return t[i:j]
REMOVED = []
def clean(p, pats):
    for pat in pats:
        for m in re.findall(pat, p): REMOVED.append(m.strip())
        p = re.sub(pat, '', p)
    return re.sub(r'\s+([,.;:?])', r'\1', re.sub(r'\s{2,}', ' ', p)).strip()
JOW = [r'\s*\(Aristoph\., Clouds\.\)', r'\s*\(Or,? [^)]*\)', r'\s*\((?:E\.g\. )?[Cc]ompare [^)]*\)']
R = {}

# Apology (Jowett): 17a-24b, 28b-32a
A = read('1656.txt')
R['apol1'] = [clean(p, JOW) for p in blocks(between(A, 'How you, O Athenians, have been affected', 'as you will find out either in this or in any future enquiry.'))]
R['apol2'] = [clean(p, JOW) for p in blocks(between(A, 'Some one will say: And are you not ashamed', 'must have a private station and not a public one.'))]
# memory piece: Apology 21d
m = re.sub(r'\s+', ' ', A); i = m.index('although I do not suppose that either of us knows'); e = 'I seem to have slightly the advantage of him.'; R['apol21d'] = [m[i:m.index(e, i) + len(e)]]

# Meno (Jowett): 80a-86c
M = read('1643.txt')
R['meno'] = [clean(p, JOW + [r'\s*\(Compare Aristot\. Post\. Anal\.\)']) for p in blocks(between(M, 'MENO: O Socrates, I used to be told', 'ready to fight, in word and deed, to the utmost of my power.'))]

# Crito (Jowett): 47a-54e
C = read('1657.txt')
R['crito'] = [clean(p, JOW) for p in blocks(between(C, 'SOCRATES:  The good are to be regarded', 'to fulfil the will of God, and to follow\nwhither he leads.'))]

# Phaedo (Jowett): 57a-69e, with cuts
P = read('1658.txt')
pb = [clean(p, JOW) for p in blocks(between(P, 'ECHECRATES: Were you yourself, Phaedo', 'better than I did the Athenian\njudges, it will be well.'))]
R['phaedo'] = pb[0:14] + ['…'] + pb[16:18] + ['…'] + pb[25:26] + ['…'] + pb[31:57] + pb[57:126]

# Xenophon, Memorabilia (Dakyns): I.1 whole; I.2 the accuser's charges
X = read('1177.txt')
xb = blocks(between(X, 'I have often wondered by what arguments', 'BOOK II'))
FN = [r'\s*\(\d+\)(?=[\s,;:.?!])']
xb = [p for p in xb if not re.match(r'^\(\d+\)', p) and p not in ('I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'BOOK II')]
def xp(start):
    h = [p for p in xb if p.startswith(start)]; assert len(h) == 1, start; return clean(h[0], FN)
R['mem1'] = [xp('I have often wondered by what arguments'), xp('In the first place, what evidence did they produce'),
             xp('But his mode of dealing with his intimates'), xp('Again, Socrates ever lived in the public eye'),
             xp('But the questioning of Socrates on the merits'), xp('Now, in so far as the opinions of Socrates were unknown'),
             xp('At one time Socrates was a member of the Council'), xp('I can, therefore, but repeat my former words')]
R['mem2'] = [xp('But, says the accuser, (2) by all'), xp('But, the accuser answers, the two men (4)'),
             xp('Never were two more ambitious citizens'), '…', xp('The hatred of Critias to Socrates')]

# Aristophanes, Clouds (Hickie): 218-256 (Socrates in the basket) and 1462-1510 (the end)
K = read('2562.txt')
def kb(a, b): return [re.sub(r'\s+', ' ', x.strip()) for x in re.split(r'\n\s*\n', between(K, a, b)) if x.strip()]
R['clouds1'] = kb('Come, who is this man who is in the basket?', 'Strep. Yes, by Jupiter, if it be possible!')
R['clouds2'] = kb('Strep. Ah me! it is severe, O Clouds!', 'the gods!')

# Diogenes Laertius II.40 (Yonge): the sworn indictment
D = read('57342.txt')
R['dl'] = [re.sub(r'\s+', ' ', between(D, 'But the sworn informations, on which the trial proceeded', 'the punishment he has incurred\nis death.”'))]

# Mill, On Liberty ch. II (1859)
L = read('34901.txt')
lb = blocks(between(L, 'Mankind can hardly be too often reminded', 'one of those persecutors was Saint Paul.'))
R['mill'] = [re.sub(r'_', '', p) for p in lb]   # Gutenberg's _italic_ marks only
REMOVED.append('Mill: Gutenberg underscores marking italics removed')

# Justin, Second Apology 10 (Dods, ANF I, 1885), from New Advent
J = read(os.path.join('url', 'socrates-justin-2apol.txt'))
R['justin'] = blocks(between(J, 'Our doctrines, then, appear to be greater than all human teaching', 'not the mere instrument of human reason.'))

for k, v in R.items(): print(k, len(v), sum(len(x.split()) for x in v), 'words')
print('removed:', REMOVED)
json.dump(R, open(os.path.join(HERE, 'raw.json'), 'w'), ensure_ascii=False, indent=1)
json.dump(REMOVED, open(os.path.join(HERE, 'removed.json'), 'w'), ensure_ascii=False, indent=1)
