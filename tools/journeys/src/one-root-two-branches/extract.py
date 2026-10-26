"""Extract the set texts for One root, two branches into raw.json.

Sources (all in .cache/texts):
- 2850.txt: Josephus, The Wars of the Jews, tr. William Whiston (1737), Project Gutenberg #2850.
- url/one-root-two-branches-eusebius-2.txt: Eusebius, Church History II, tr. A. C. McGiffert, NPNF II.1 (1890), New Advent 250102.
- url/one-root-two-branches-ignatius-magnesians.txt: Ignatius, To the Magnesians, tr. Roberts and Donaldson, ANF I (1885), New Advent 0105.
- url/one-root-two-branches-irenaeus-1-27.txt and -3-12.txt: Irenaeus, Against Heresies, tr. Roberts and Rambaut, ANF I (1885).
- url/what-happens-at-church-justin-1apol.txt: Justin, First Apology, tr. Dods and Reith, ANF I (1885), New Advent 0126
  (fetched for another journey; the same New Advent page; we read only chapter 31, which no other journey reads).

Editorial changes, all listed in notes.json: HTML entities decoded (C&aelig;sar -> Cæsar); New Advent's inserted
Scripture-reference links (e.g. 'John 19:15') removed; Whiston's footnote numbers removed. Words are never changed.
Paragraphs are split on blank lines only.
"""
import re, json, os, html
HERE = os.path.dirname(os.path.abspath(__file__))
T = os.path.join(HERE, '..', '..', '..', '..', '.cache', 'texts')
def read(p): return html.unescape(open(os.path.join(T, p), encoding='utf-8', errors='ignore').read().replace('\r', ''))
def blocks(t): return [re.sub(r'\s+', ' ', b).strip() for b in re.split(r'\n\s*\n', t) if b.strip()]
def para(bl, start):
    m = [b for b in bl if b.startswith(start)]
    assert len(m) >= 1, start
    return m[0]
def section(bl, head, nxt):
    i = bl.index(next(b for b in bl if b.startswith(head))); j = bl.index(next(b for b in bl[i + 1:] if b.startswith(nxt)))
    return bl[i + 1:j]
REMOVED = []
def strip(s, *bits):
    for b in bits:
        assert b in s, (b, s[:80]); s = s.replace(b, ' '); REMOVED.append(b.strip())
    return re.sub(r'\s+([,.;:?])', r'\1', re.sub(r'\s{2,}', ' ', s)).strip()
R = {}

# Josephus, Jewish War VI.4.5-8 and VI.5.1, 5.3 (Whiston). Book VI starts at 'BOOK VI.'; chapter 4 is the burning.
J = read('2850.txt'); b6 = J.index('\nBOOK VI.\n'); W = blocks(J[b6:J.index('\nBOOK VII.\n', b6)])
w45 = para(W, '5. So Titus retired into the tower of Antonia')
w46 = strip(para(W, '6. And now a certain person came running to Titus'), ' 16 ')
w47 = para(W, '7. And now, since Caesar was no way able to restrain')
w48 = para(W, '8. Now although any one would justly lament')
w51 = strip(para(W, '1. While the holy house was on fire'), ' 17 ', ' 18 ')
w53 = strip(para(W, '3. Thus were the miserable people persuaded'), ' 20 ', ' 21 ', ' 22 ', ' 23 ')
R['josephus'] = [w45, w46, w47, w48, w51, w53]

# Eusebius, Church History II.6 (selected) and II.23 (Hegesippus on James)
E = blocks(read('url/one-root-two-branches-eusebius-2.txt'))
c6 = section(E, 'Chapter 6. The Misfortunes', 'Chapter 7.')
R['eusebius6'] = [para(c6, '3. '), '…', strip(para(c6, '5. '), ' John 19:15'), '…', para(c6, '8. ')]
c23 = section(E, 'Chapter 23. The Martyrdom of James', 'Chapter 24.')
R['hegesippus'] = [para(c23, '3. '), para(c23, '4. '), para(c23, '5. '), para(c23, '6. '), para(c23, '7. '), '…',
                   strip(para(c23, '10. '), ' Matthew 22:16'), para(c23, '11. '), para(c23, '12. '), para(c23, '13. '), para(c23, '14. '),
                   para(c23, '15. '), strip(para(c23, '16. '), ' Luke 23:34'), para(c23, '17. '), para(c23, '18. ')]

# Ignatius, To the Magnesians 8-10
I = blocks(read('url/one-root-two-branches-ignatius-magnesians.txt'))
R['ignatius'] = [section(I, 'Chapter 8.', 'Chapter 9.')[0], strip(section(I, 'Chapter 9.', 'Chapter 10.')[0], ' Matthew 27:52'), section(I, 'Chapter 10.', 'Chapter 11.')[0]]

# Irenaeus, Against Heresies I.27.1-2 and III.12.11, 12, 15
I1 = blocks(read('url/one-root-two-branches-irenaeus-1-27.txt'))
R['iren127'] = [para(I1, '1. Cerdo'), para(I1, '2. Marcion of Pontus')]
I3 = blocks(read('url/one-root-two-branches-irenaeus-3-12.txt'))
R['iren312'] = [strip(para(I3, '11. And that the whole range'), ' 1 Timothy 6:4'), para(I3, '12. For all those who are of a perverse mind'), '…',
                strip(para(I3, '15. Neither [in that case]'), ' Acts 10:28-29', ' Acts 10:47', ' Galatians 2:12-13')]

# Justin, First Apology 31
JA = blocks(read('url/what-happens-at-church-justin-1apol.txt'))
R['justin31'] = section(JA, 'Chapter 31. Of the Hebrew prophets', 'Chapter 32.')

for k, v in R.items(): print(k, [len(x.split()) for x in v])
print('removed:', REMOVED)
json.dump(R, open(os.path.join(HERE, 'raw.json'), 'w'), ensure_ascii=False, indent=1)
