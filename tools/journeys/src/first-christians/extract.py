"""Extract the set texts for The first Christians from the fetched files in .cache/texts (see specs/AGENTS.md, Stage B).

Every paragraph is copied from the file by script. Editorial changes, all recorded in notes.json:
- Didache (earlychristianwritings.com transcription of Lightfoot): the site's verse numbers ('1:3 ') and its curly
  braces marking Scripture quotations are removed, with one stray encoding mark in 4:15. No word is changed.
- Pliny (Gutenberg #2811): the edition's footnote markers [1066]-[1069] are removed.
- Lucian (Gutenberg #47242): underscores marking italics are removed.
- Minucius Felix and Tertullian (New Advent, ANF IV and III): HTML entities are decoded; Tertullian's bracketed
  editorial gloss '[i.e., the court of God.]' is removed. Cuts are marked by a paragraph that is just '…'.
"""
import re, json, os, html
HERE = os.path.dirname(os.path.abspath(__file__))
T = os.path.join(HERE, '..', '..', '..', '..', '.cache', 'texts')
def read(p): return open(os.path.join(T, p), encoding='utf-8', errors='replace').read().replace('\r', '')
def blocks(t): return [re.sub(r'\s+', ' ', b).strip() for b in re.split(r'\n\s*\n', t) if b.strip()]
def between(s, a, b=None):
    i = s.index(a); j = s.index(b, i) + len(b) if b else len(s); return s[i:j]
R = {}

# Didache, tr. J. B. Lightfoot, ed. J. R. Harmer, The Apostolic Fathers (1891)
D = blocks(read('url/didache-lightfoot.txt'))
def did(n):
    b = next(x for x in D if x.startswith(f'{n}:1 '))
    b = re.sub(r'\s*�LA1�\s*', ' ', b)          # a stray encoding mark in 4:15
    b = re.sub(r'(^|\s)\d+:\d+\s', r'\1', b)              # the site's verse numbers
    b = b.replace('{', '').replace('}', '')                 # the site's marks round Scripture quotations
    return re.sub(r'\s+', ' ', b).strip()
R['didache'] = [did(1), did(2), did(3), did(4), '…', did(9), did(10)]

# Pliny, Letters X.96-97, tr. William Melmoth (1746), rev. F. C. T. Bosanquet (Gutenberg #2811)
P = read('2811.txt')
P = P[P.index('XCVII To THE EMPEROR TRAJAN[1066]'):]
strip = lambda s: re.sub(r'\s+', ' ', re.sub(r'\[\d{4}\]', '', s)).strip()
R['pliny'] = [strip(between(P, 'IT is my invariable rule, Sir', 'shall repent of their error.')),
              strip(between(P, 'You have adopted the right course', 'quite foreign to the spirit of our age.'))]

# Lucian, The Death of Peregrine 11-13, tr. H. W. and F. G. Fowler (1905) (Gutenberg #47242)
L = blocks(read('47242.txt'))
R['lucian'] = [next(b for b in L if b.startswith("'It was now that he came across the priests")).replace('_', '')]

# Minucius Felix, Octavius 8-9, tr. R. E. Wallis, ANF IV (1885) (New Advent)
M = blocks(html.unescape(read('url/first-christians-minucius-octavius.txt')))
def ch_after(bl, head): return bl[next(i for i, b in enumerate(bl) if b.startswith(head)) + 1]
m8 = ch_after(M, 'Chapter 8. Argument'); m9 = ch_after(M, 'Chapter 9. Argument')
R['minucius'] = [m8,
                 between(m9, 'And now, as wickeder things advance', 'a worthy and appropriate religion for such manners.'), '…',
                 between(m9, 'I know not whether these things are false;')]

# Tertullian, Apology 39, tr. S. Thelwall, ANF III (1885) (New Advent)
A = blocks(html.unescape(read('url/first-christians-tertullian-apology.txt')))
a39 = A[next(i for i, b in enumerate(A) if b == 'Chapter 39') + 1]
R['tertullian'] = [between(a39, 'I shall at once go on', 'All things are common among us but our wives.'), '…',
                   between(a39, 'Our feast explains itself by its name.', 'but a curia').rstrip('—').strip()]

for k, v in R.items(): print(k, [len(x.split()) for x in v])
json.dump(R, open(os.path.join(HERE, 'raw.json'), 'w'), ensure_ascii=False, indent=1)
