"""Extract the set texts for How to read the Bible from the fetched files in .cache/texts and .cache/books.

Every paragraph is copied by script. The only changes are editorial, and each kind is listed in notes.json:
- New Advent's inline Bible references (e.g. "John 6:53") are removed: they are the web editor's, not the translator's;
- soft hyphens and line-break hyphens ("Transla- tion") are joined; page markers ({156}) and italics underscores are removed;
- the marginal references in square brackets in The Translators to the Reader are removed;
- in Oesterley's Pirke Aboth (an OCR text) footnote markers are removed and OCR misreadings corrected (listed below).
Cuts are marked with a paragraph that is just "…".
"""
import re, json, os
HERE = os.path.dirname(os.path.abspath(__file__))
C = os.path.join(HERE, '..', '..', '..', '..', '.cache')
def read(p): return open(os.path.join(C, p), encoding='utf-8', errors='ignore').read().replace('\r', '').replace('­', '')
def blocks(t): return [re.sub(r'\s+', ' ', b).strip() for b in re.split(r'\n\s*\n', t) if b.strip()]
def para(bl, start): return next(b for b in bl if b.startswith(start))
def cut(p, a=None, b=None):
    """The part of paragraph p from the words a (inclusive) to the words b (inclusive)."""
    i = p.index(a) if a else 0
    j = p.index(b, i) + len(b) if b else len(p)
    return p[i:j]
def unref(p, refs):
    for r in refs:
        if r not in p: raise SystemExit(f'reference not found: {r}')
        p = p.replace(' ' + r, '', 1) if ' ' + r in p else p.replace(r, '', 1)
    return re.sub(r'\s+([,.;:])', r'\1', p)
R = {}; LOG = []

# 1. The Translators to the Reader (1611), "Translation necessary" (KJV preface, part 4)
T4 = blocks(read('texts/url/kjv-translators-reader-4.txt'))
p = para(T4, 'But how shall men meditate in that')
for a, b in [('Transla- tion', 'Translation'), ('inter- preter', 'interpreter')]:
    p = p.replace(a, b); LOG.append(f'Translators to the Reader: line-break hyphen joined: "{a}" -> "{b}"')
marg = re.findall(r' ?\[[^\]]*\]', p); LOG.append('Translators to the Reader: marginal references removed: ' + ' '.join(m.strip() for m in marg))
p = re.sub(r' ?\[[^\]]*\]', '', p)
R['translators'] = [p]

# 2. Augustine, On Christian Doctrine III.10-16 (tr. J. F. Shaw, NPNF I.2)
A3 = blocks(read('texts/url/how-to-read-the-bible-augustine-ocd-3.txt'))
R['aug3'] = [para(A3, '14. But in addition to the foregoing rule'),
             para(A3, '15. But as men are prone to estimate sins'),
             '…',
             para(A3, '22. But when men unacquainted with other modes of life'),
             para(A3, '23. The tyranny of lust being thus overthrown'),
             unref(cut(para(A3, '24. If the sentence is one of command'), None, 'that His flesh was wounded and crucified for us.'), ['John 6:53'])]

# 3. Aquinas, Summa Theologiae I, q. 1, a. 10 (Fathers of the English Dominican Province, 2nd ed. 1920)
Q = blocks(read('texts/url/reason-st-q1a1.txt'))
R['aquinas3'] = [para(Q, 'Reply to Objection 3. The parabolical sense')]
R['aquinas10'] = [para(Q, 'Objection 1. It seems that in Holy Writ a word cannot have several senses'),
                  para(Q, 'On the contrary, Gregory says (Moral. xx, 1)'),
                  para(Q, 'I answer that, The author of Holy Writ is God'),
                  para(Q, 'Reply to Objection 1. The multiplicity of these senses')]

# 4. Origen, On First Principles IV (from the Greek; tr. F. Crombie, ANF IV, 1885)
O = read('texts/url/how-to-read-the-bible-origen-principles-4.txt')
O = O[O.index('Translated from the Greek'):]
OB = blocks(O)
R['origen'] = [cut(para(OB, '11. The way, then, as it appears to us'), None, 'which has been arranged to be given by God for the salvation of men.'),
               '…',
               cut(para(OB, '12. But as there are certain passages of Scripture'), 'That the first sense, then, is profitable', None),
               '…',
               para(OB, '15. But since, if the usefulness of the legislation'),
               cut(para(OB, '16. It was not only, however, with the'), None, 'but which did not literally take place?'),
               '…',
               para(OB, 'All these statements have been made by us'),
               cut(para(OB, '19. But that no one may suppose'), None, 'than those which are interspersed with a purely spiritual signification.')]

# 5. Augustine, On Christian Doctrine I.35-40 (tr. J. F. Shaw)
A1 = blocks(read('texts/url/how-to-read-the-bible-augustine-ocd-1.txt'))
R['aug1'] = [para(A1, '39. Of all, then, that has been said'),
             cut(para(A1, '40. Whoever, then, thinks that he understands'), None, 'he is wholly clear from the charge of deception.'),
             '…',
             para(A1, '41. Whoever takes another meaning out of Scripture'),
             unref(para(A1, 'For if he takes up rashly a meaning'), ['2 Corinthians 5:7']),
             '…',
             unref(para(A1, '44. And, therefore, if a man fully understands'), ['1 Timothy 1:5'])]

# 6. Pirke Aboth, tr. W. O. E. Oesterley (SPCK, 1919); OCR text from archive.org
P = read('texts/url/how-to-read-the-bible-pirkei-avot-taylor.txt'); PN = re.sub(r'\s+', ' ', P)
def ocr(a, b, fixes):
    s = PN[PN.index(a):PN.index(b, PN.index(a)) + len(b)]
    for x, y in fixes:
        if x not in s: raise SystemExit(f'OCR fix not found: {x}')
        s = s.replace(x, y); LOG.append(f'Pirke Aboth (OCR): "{x}" -> "{y}"')
    return s
a11 = ocr('I. (i) Moses received tlie Torah', 'Prophets delivered it to the men of the Great Synagogue.^', [
    ('I. (i) ', ''), ('tlie', 'the'), ('Sinai,i and', 'Sinai, and'), ('delivered - it', 'delivered it'), ('Joshua ; ^ and', 'Joshua; and'),
    ('Elders ; * and', 'Elders; and'), ('Prophets ;8 and', 'Prophets; and'), ('Great Synagogue.^', 'Great Synagogue.')])
a11b = ocr('These (men) said^ three things', 'a fence* to the Torah."', [
    ('said^', 'said'), ('judge- ment " ; ^ and', 'judgement"; and'), ('" Raise', '"Raise'), ('disciples " ; ^ and', 'disciples"; and'),
    ('" Make a fence*', '"Make a fence')])
a525 = ocr('25. (32) Ben Bag-Bag * said', 'no better guide \'\' for thee than this."', [
    ('25. (32) ', ''), ('Bag-Bag * said :', 'Bag-Bag said:'), ('"Turn it,\' and', '"Turn it, and'), ('again ; and', 'again; and'),
    ('therein ; * for', 'therein; for'), ('in it. And look into it;^ become', 'in it. And look into it; become'), ('in it; and move not away ® from it ;', 'in it; and move not away from it;'),
    ("guide '' for", 'guide for')])
R['avot'] = [a11 + ' ' + a11b, a525]

# 7. Frederick Douglass, My Bondage and My Freedom (1855), Gutenberg #202
D = read('books/bondage/202.txt')
def dclean(s):
    s = re.sub(r'\{\d+\}', '', s)
    return re.sub(r'\s+', ' ', s.replace('_', '')).strip()
DB = [dclean(b) for b in re.split(r'\n\s*\n', D) if b.strip()]
lw = next(b for b in DB if 'colored man, named Lawson' in b)
R['douglass'] = [cut(lw, 'While thus religiously seeking knowledge', 'but he could teach me "the spirit;" and high, refreshing times we had together, in singing, praying and glorifying God.'),
                 '…',
                 para(DB, 'Our first Sabbath passed delightfully'),
                 cut(para(DB, 'It was not merely the agency of Master Thomas'), None, 'shall be beaten with many stripes."'),
                 '…',
                 cut(next(b for b in DB if 'in the name of the constitution and the bible' in b), 'Standing with God and the crushed and bleeding', None),
                 '…',
                 para(DB, 'What, then, remains to be argued?')]

# 8. Thomas à Kempis, The Imitation of Christ I.5 (tr. William Benham), Gutenberg #1653
K = read('texts/1653.txt'); K = K[K.index('CHAPTER V\n\nOf the reading of Holy Scriptures'):]
KB = blocks(K)
R['kempis'] = KB[2:4]

# 9. Benedict, Rule ch. 48 (tr. E. F. Henderson, Select Historical Documents of the Middle Ages, 1910; Fordham Sourcebook)
B = blocks(read('texts/url/wm-benedict-fordham.txt'))
R['benedict'] = [para(B, 'Idleness is the enemy of the soul.')]

# 10. Athanasius, Life of Antony 2-3 (tr. H. Ellershaw, NPNF II.4, 1892)
L = blocks(read('texts/url/how-to-read-the-bible-athanasius-antony.txt'))
R['antony'] = [unref(para(L, '2. After the death of his father and mother'), ['Matthew 4:20', 'Acts 4:35', 'Matthew 19:21']),
               unref(para(L, '3. And again as he went into the church'), ['Matthew 6:34', '2 Thessalonians 3:10'])]

for k, v in R.items(): print(k, [len(x.split()) for x in v])
print('\n'.join(LOG))
json.dump(R, open(os.path.join(HERE, 'raw.json'), 'w'), ensure_ascii=False, indent=1)
json.dump(LOG, open(os.path.join(HERE, 'extract_log.json'), 'w'), ensure_ascii=False, indent=1)
