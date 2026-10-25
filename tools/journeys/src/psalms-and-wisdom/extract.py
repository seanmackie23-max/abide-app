"""Extract the set texts for Psalms and wisdom from the fetched files in .cache/texts/url.

Tolstoy, A Confession, tr. Aylmer Maude (1921), from the Standard Ebooks single-page text
(built on the Wikisource transcription and HathiTrust scans). The Wisdom of Solomon 7 is the
World English Bible (public domain) from ebible.org.

Editorial changes, all noted in notes.json: the invisible word-joiner characters (U+2060) that
Standard Ebooks puts before dashes and ellipses are removed; footnote markers (Tolstoy's
'words.7', the WEB's daggers and their notes) are removed. No word is changed.
Paragraphs are split on blank lines, never on line ends.
"""
import re, json, os
HERE = os.path.dirname(os.path.abspath(__file__))
U = os.path.join(HERE, '..', '..', '..', '..', '.cache', 'texts', 'url')
def read(p): return open(os.path.join(U, p), encoding='utf-8').read().replace('\r', '')
def blocks(t): return [re.sub(r'\s+', ' ', b.replace('⁠', '')).strip() for b in re.split(r'\n\s*\n', t) if b.strip()]

R = {}
# Tolstoy: split into chapters by the Roman-numeral headings that follow the imprint
bl = blocks(read('psalms-and-wisdom-tolstoy-confession.txt'))
NUM = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'XIII', 'XIV', 'XV', 'XVI']
start = [k for k, b in enumerate(bl) if b == 'I'][1]
ch, cur = {}, None
for b in bl[start:]:
    if b in NUM: cur = b; ch[cur] = []; continue
    if b == 'Afterword': break
    ch[cur].append(b)
def tol(c, i): return ch[c][i]
fix = lambda s: re.sub(r'(words\.)7$', r'\1', s)  # footnote marker 7 after 'words.'

# Session 4 (compare): the crisis (IV) and the sages, with Solomon (VI)
R['tolstoy-crisis'] = [tol('IV', 0), tol('IV', 1), tol('IV', 2), '…', tol('IV', 6), tol('IV', 7), '…',
                      tol('VI', 13), fix(tol('VI', 15)), '…', tol('VI', 22), tol('VI', 24), tol('VI', 26)]
# Session 5 (read): the four ways out (VII), and where his reason had brought him (VIII)
R['tolstoy-four-ways'] = [tol('VII', 0), tol('VII', 1), tol('VII', 2), tol('VII', 3), tol('VII', 4), tol('VII', 5), tol('VII', 6), '…',
                         tol('VII', 8), tol('VII', 9), tol('VII', 10), tol('VII', 11), tol('VII', 12), tol('VII', 13), '…',
                         tol('VIII', 5)]

# Wisdom of Solomon 7:22b-30, WEB
w = blocks(read('web-wisdom-7.txt'))
i = next(k for k, b in enumerate(w) if b.startswith('For there is in her a spirit'))
j = next(k for k, b in enumerate(w) if b.startswith('30 For daylight'))
lines = w[i:j + 2]
lines = [re.sub(r'^\d+ ', '', x) for x in lines]  # verse numbers are given in the ref
lines = [re.sub(r'†.*?\. |‡\S+ ', '', x) for x in lines]
R['wisdom-7'] = [' '.join(lines[0:4]), ' '.join(lines[4:10]), ' '.join(lines[10:15]), ' '.join(lines[15:])]

for k, v in R.items(): print(k, [len(x.split()) for x in v], sum(len(x.split()) for x in v))
json.dump(R, open(os.path.join(HERE, 'raw.json'), 'w'), ensure_ascii=False, indent=1)
