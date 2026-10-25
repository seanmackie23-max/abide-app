"""Extract the set texts for The last week and the cross from the fetched files in .cache/texts.

Sources (headers checked):
- Philo, On the Embassy to Gaius 299-305, tr. C. D. Yonge (1855): .cache/texts/url/the-last-week-philo-embassy.txt (earlychristianwritings.com)
- Cicero, Against Verres II.5.162-170, tr. C. D. Yonge (Bohn/Bell, 1903 printing): .cache/texts/url/the-last-week-cicero-verres-perseids.txt (Perseus, perseus-eng2)
- D. F. Strauss, The Life of Jesus Critically Examined, section 140, tr. George Eliot: .cache/texts/64037.txt (Gutenberg #64037)
- Josephus, The Jewish War V.11.1, tr. William Whiston (1737): .cache/texts/2850.txt (Gutenberg #2850)
- The Koran, Sura IV, tr. J. M. Rodwell (1861): .cache/texts/2800.txt (Gutenberg #2800)
Paragraphs are split on blank lines, never on line ends. Footnote markers are removed (listed in notes.json); no word is changed.
"""
import re, json, os
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.join(HERE, '..', '..', '..', '..', '.cache', 'texts')
def read(p): return open(os.path.join(T, p), encoding='utf-8', errors='ignore').read().replace('\r', '')
def blocks(t): return [re.sub(r'\s+', ' ', b).strip() for b in re.split(r'\n\s*\n', t) if b.strip()]
def para(bl, start): return next(b for b in bl if b.startswith(start))
def after(bl, start, n):
    i = next(k for k, b in enumerate(bl) if b.startswith(start)); return bl[i:i + n]
R = {}

# Philo: one paragraph, sections (299)-(305). The chapter numeral 'XXXVIII. ' is an editor's heading and is dropped.
P = blocks(read('url/the-last-week-philo-embassy.txt'))
p = para(P, 'XXXVIII. (299)')
R['philo'] = [p[len('XXXVIII. '):]]

# Cicero: the nine paragraphs of II.5.162-170, from 'Then he orders the man' to 'within sight of all passers-by'.
C = blocks(read('url/the-last-week-cicero-verres-perseids.txt'))
G = after(C, 'Then he orders the man to be most violently scourged', 9)
assert G[-1].startswith('It is a crime to bind a Roman citizen'), G[-1][:60]
# 162, 163, (cut 164), 165, (cut 166-168), 169, 170
R['cicero'] = [G[0], G[1], '…', G[3], '…', G[7], G[8]]

# Strauss, section 140: the dilemma, the swoon, the theft and the change in the disciples, the visions, the return to Galilee.
S = blocks(read('64037.txt'))
fn = lambda s: re.sub(r'\s*\[\d{4}\]', '', s)
R['strauss'] = [fn(para(S, x)) if x != '…' else x for x in (
    'Hence the cultivated intellect of the present day',
    'Rationalism has principally given its adhesion',
    '…',
    'Notwithstanding all these improbabilities',
    'If we compare with this account of the resurrection',
    'Far more fruitful is the appeal to the passage of Paul',
    '…',
    'Meanwhile, if the body of Jesus was interred')]

# Josephus, The Jewish War V.11.1 (5.446-451), tr. William Whiston (1737): .cache/texts/2850.txt (Gutenberg #2850).
# The section number '1. ' at the start and the footnote number ' 19' at the end are removed.
J = blocks(read('2850.txt'))
j = para(J, "1. So now Titus's banks were advanced a great way")
assert j.endswith('crosses wanting for the bodies. 19')
R['josephus'] = [j[len('1. '):-len(' 19')]]

# Rodwell, Sura IV (Women) 156-159 (standard numbering): footnote number '30' glued to 'likeness.' removed.
Q = blocks(read('2800.txt'))
q1 = para(Q, 'And for their unbelief,-and for their having spoken against Mary')
q2 = para(Q, 'And for their saying, "Verily we have slain the Messiah')
q3 = para(Q, 'There shall not be one of the people of the Book but shall believe in Him')
R['quran'] = [q1, q2.replace('likeness.30', 'likeness.'), q3]

for k, v in R.items(): print(k, [len(x.split()) for x in v])
json.dump(R, open(os.path.join(HERE, 'raw.json'), 'w'), ensure_ascii=False, indent=1)
