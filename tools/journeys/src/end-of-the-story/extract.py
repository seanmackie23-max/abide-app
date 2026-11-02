"""Set texts for The end of the story, copied by script from the fetched Gutenberg files in .cache/texts.

  Strauss, The Life of Jesus Critically Examined, section 115, tr. George Eliot (1846)       #64037
  1 Enoch 1, tr. R. H. Charles (SPCK, 1917)                                                  #77935
  Augustine, The City of God XX.7 and XX.9, tr. Marcus Dods (1871)                            #45305
  Plato, Phaedo 79c-81a, tr. Benjamin Jowett                                                  #1658
  Hopkins, 'The Wreck of the Deutschland', stanzas 34-35 (ed. Bridges, 1918)                  #22403

Prose is split on blank lines and its line ends joined. Poetry keeps its printed lines. Editorial marks are removed
(listed in notes.json): Gutenberg footnote numbers like [1680] and [699], underscores for italics, Charles's text-critical
brackets (the corner and white square brackets; the words inside them are kept), and Jowett's cross-reference
'(compare Apol.)'. No word is changed.
"""
import re, json, os
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.join(HERE, '..', '..', '..', '..', '.cache', 'texts')
def read(n): return open(os.path.join(T, f'{n}.txt'), encoding='utf-8').read().replace('\r', '')
def blocks(t): return [b for b in re.split(r'\n\s*\n', t) if b.strip()]
def prose(b): return re.sub(r'\s+', ' ', re.sub(r'([a-z]‐)\n\s*', r'\1', b)).strip()  # a word hyphenated at a line end ('lake‐\nside') stays one word
def para(bl, start): return prose(next(b for b in bl if prose(b).startswith(start)))
R = {}

# Strauss, The Life of Jesus Critically Examined, section 115, tr. George Eliot (1846). Schweitzer (d. 1965) is not
# quoted: by DECISIONS.md his book is still in copyright even in Montgomery's translation, so he is taught in our own words.
G = blocks(read(64037)); fnS = lambda s: re.sub(r' ?\[\d+\]', '', s)
s1 = para(G, 'Not only did Jesus, according to the evangelical accounts, predict')
s2 = prose(next(b for b in G if 'But the very possibility of interpreting' in prose(b)))
s2 = s2[s2.index('But the very possibility of interpreting'):s2.index('catastrophe should occur.') + len('catastrophe should occur.')]
s3 = para(G, 'Thus it is impossible to evade the acknowledgment')
s4 = para(G, 'Thus the last attempt to discover in the discourse before us')
R['strauss'] = [fnS(x) for x in [s1, '…', s2, '…', s3, s4]]

# 1 Enoch 1:1-9 (Charles). Poetry: keep lines, join a wrapped line to the one before it.
E = read(77935); i = E.index('I. 1. The words of the blessing of Enoch'); j = E.index('II. 1. Observe ye every thing')
marks = lambda s: re.sub('[⌜⌝〚〛]', '', s)
def poem(b):
    out = []
    for ln in b.split('\n'):
        if not ln.strip(): continue
        ind = len(ln) - len(ln.lstrip())
        if out and (ind >= 10 or out[-1].endswith('Mount')) and not re.match(r'\s*\d', ln): out[-1] += ' ' + ln.strip()
        else: out.append(ln.strip())
    return '\n'.join(out)
en = blocks(E[i:j])
R['enoch'] = [marks(prose(en[0]))] + [marks(poem(x)) for x in en[1:]]

# Augustine, City of God XX.7 (first two paragraphs) and XX.9 (first two paragraphs)
C = blocks(read(45305)); clean = lambda s: re.sub(r'\[\d+\]', '', s).replace('_', '')
A7a = clean(para(C, 'The evangelist John has spoken of these two resurrections'))
A7b = clean(para(C, 'The Lord Jesus Christ Himself says, "No man can enter into a strong'))
A7b = A7b[:A7b.index('to mark the fulness of time.') + len('to mark the fulness of time.')]
A9a = clean(para(C, 'But while the devil is bound, the saints reign with Christ'))
A9a = A9a[:A9a.index('and the kingdom of heaven. Accordingly') + len('and the kingdom of heaven.')]
A9b = clean(para(C, 'It is then of this kingdom militant'))
x = A9b.index('the Apocalypse speaks in the words just quoted.') + len('the Apocalypse speaks in the words just quoted.')
y = A9b.index('"And the souls," says John'); z = A9b.index('though not as yet in conjunction with their bodies.') + len('though not as yet in conjunction with their bodies.')
R['augustine'] = [A7a, A7b, '…', A9a, '…', A9b[:x], '…', A9b[y:z]]

# Plato, Phaedo 79c-81a (Jowett): from 'But when returning into herself' to Cebes' 'beyond a doubt'
P = blocks(read(1658)); k = next(n for n, x in enumerate(P) if prose(x).startswith('But when returning into herself she reflects'))
m = next(n for n, x in enumerate(P) if prose(x).startswith('Yes, said Cebes, beyond a doubt.'))
R['phaedo'] = [prose(x).replace(' (compare Apol.)', '') for x in P[k:m + 1]]

# Hopkins, The Wreck of the Deutschland, stanzas 34 and 35 (printed lines kept)
H = read(22403); h = H.index('\n34\n'); g = H.index('\n_5\nPenmaen Pool_')
st = [[l.strip() for l in b.split('\n') if l.strip()] for b in blocks(H[h:g])]
assert [s[0] for s in st] == ['34', '35']
R['hopkins'] = ['\n'.join(s[1:]) for s in st]

for k_, v in R.items(): print(k_, [len(x.split()) for x in v], sum(len(x.split()) for x in v))
json.dump(R, open(os.path.join(HERE, 'raw.json'), 'w'), ensure_ascii=False, indent=1)
