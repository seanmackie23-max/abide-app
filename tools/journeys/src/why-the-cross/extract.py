"""Extract the set texts for Why the cross? from the fetched files in .cache/texts.

New Advent pages (Athanasius, Irenaeus, Gregory Nazianzen) insert Scripture references into the
text ("a legal Genesis 2:15 hold"); CCEL pages (Anselm, Calvin) carry printed page numbers glued
to words ("202Boso"); the CCEL Herbert page carries footnote numbers ("fruit,4"). Each is removed
by an exact replacement listed below and recorded in notes.json. No word is changed.
"""
import re, json, os
HERE = os.path.dirname(os.path.abspath(__file__))
T = os.path.join(HERE, '..', '..', '..', '..', '.cache', 'texts')
def read(p): return open(os.path.join(T, p), encoding='utf-8', errors='ignore').read().replace('\r', '')
def blocks(t): return [re.sub(r'\s+', ' ', b).strip() for b in re.split(r'\n\s*\n', t) if b.strip()]
def para(bl, start): return next(b for b in bl if b.startswith(start))
def fix(p, subs):
    for a, b in subs:
        assert a in p, (a, p[:60])
        p = p.replace(a, b)
    return p
R = {}

# Athanasius, On the Incarnation 6-10 (Robertson, NPNF II.4, 1892). The italic chapter summaries are left out.
A = blocks(read('url/why-the-cross-athanasius-incarnation.txt'))
R['athanasius'] = [
 fix(para(A, 'For this cause, then, death having gained upon men'), [('a legal Genesis 2:15 hold', 'a legal hold')]),
 para(A, '7. So, as the rational creatures were wasting'),
 para(A, 'But just as this consequence must needs hold'),
 fix(para(A, 'For this purpose, then, the incorporeal and incorruptible'), [('not far from us Acts 17:27 before', 'not far from us before')]),
 para(A, 'For the Word, perceiving that no otherwise'),
 fix(para(A, 'Now in truth this great work was peculiarly suited'), [('For the love of Christ 2 Corinthians 5:14 constrains us', 'For the love of Christ constrains us'), ('which 1 Timothy 6:15 in its own times', 'which in its own times')]),
]

# Irenaeus, Against Heresies (Roberts and Rambaut, ANF I, 1885)
I5 = blocks(read('url/why-the-cross-irenaeus-5-1.txt'))
R['irenaeus51'] = [fix(para(I5, '1. For in no other way could we have learned'), [('counsellor? Romans 11:34 Again', 'counsellor? Again')])]
I3 = blocks(read('url/why-the-cross-irenaeus-3-18.txt'))
p7 = fix(para(I3, '7. Therefore, as I have already said'), [("transgression. Romans 5:14 But", "transgression. But"), ('made sinners, Romans 5:19 and', 'made sinners, and'), ('true are His works. Deuteronomy 32:4 But', 'true are His works. But')])
R['irenaeus318'] = [para(I3, '1. As it has been clearly demonstrated'), p7]

# Gregory Nazianzen, Oration 45.22 and 45.28 (Browne and Swallow, NPNF II.7, 1894)
N = blocks(read('url/why-the-cross-nazianzen-oration-45.txt'))
n22 = para(N, 'XXII. Now we are to examine another fact')
R['nazianzen'] = [n22[:n22.index('the greater part of what we might say shall be reverenced with silence.') + len('the greater part of what we might say shall be reverenced with silence.')]]

# Anselm, Why God Became Man (Cur Deus Homo), tr. James Gardiner Vose (Bibliotheca Sacra 1854-55), in the Open Court volume (1903; reprint 1926)
C = blocks(read('url/why-the-cross-anselm-ccel.txt'))
def run(start, end):
    i = C.index(next(b for b in C if b.startswith(start)))
    j = C.index(next(b for b in C[i:] if b.startswith(end)))
    return C[i:j + 1]
pages = [('202Boso', 'Boso'), ('203demanded', 'demanded'), ('204Anselm', 'Anselm'), ('apply 205to him', 'apply to him'), ('unpunished 206 who', 'unpunished who'), ('207Boso', 'Boso'), ('not 208only', 'not only'), ('can 245give', 'can give'), ('ask with 229regard', 'ask with regard')]
def unpage(p):
    for a, b in pages:
        if a in p: p = p.replace(a, b)
    assert not re.search(r'\d{3}', p), p[:80]
    return p
s1 = run('I HAVE been often and most earnestly requested', 'I HAVE been often and most earnestly requested')[0]
s1 = s1[:s1.index('or merely by his will.') + len('or merely by his will.')]
R['anselm'] = [s1] + ['…'] + [unpage(p) for p in run('Anselm. We must needs inquire, therefore, in what manner God puts away', 'Boso. Since we have determined to follow reason')] \
 + ['…'] + [unpage(p) for p in run('Anselm. Let us return and consider whether it were proper', 'Boso. If I wish to oppose this, I fear to sin.')] \
 + [unpage(p) for p in run('Anselm. There is also another thing which follows', 'Anselm. There is no inconsistency in God’s commanding us')] \
 + ['…'] + [unpage(p) for p in run('Anselm. Therefore the honor taken away must be repaid', 'Boso. I think that nothing more reasonable can be said.')] \
 + ['…'] + [unpage(p) for p in run('Anselm. Suppose that you did not owe any of those things', 'Boso. Show it me then.')] \
 + ['…'] + [unpage(p) for p in run('Anselm. Not to detain you too long; what if it were necessary', 'Boso. I must confess that I ought not to oppose the will of God')] \
 + ['…'] + [unpage(p) for p in run('Anselm. But this cannot be effected, except the price paid to God', 'Boso. Now blessed be God!')]
# Anselm I.8: Boso's objection and Anselm's first answer (for session 6)
R['anselm8'] = [unpage(fix(para(C, 'Boso. Be it so; let nothing be referred to the Divine nature'), [])), unpage(para(C, 'Anselm. God the Father did not treat that man as you seem to suppose'))]

# Calvin, Institutes II.16.2, 3 and 5 (Beveridge, 1845). Section 6 is left out: the CCEL page garbles its Greek and Hebrew.
K = blocks(read('url/why-the-cross-calvin-institutes-2-16.txt'))
k2 = fix(para(K, '2. But before we proceed farther'), [('how can 435it be said', 'how can it be said')])
k2 = k2[k2.index('The mode in which the Spirit usually speaks'):]
k3 = fix(para(K, '3. Though this is said in accommodation'), [('All of us, therefore, 436have', 'All of us, therefore, have')])
k5 = para(K, '5. When it is asked then how Christ')
k5 = fix(k5[k5.index('Moreover, as the curse consequent upon guilt'):], [('public testimony 439to his innocence', 'public testimony to his innocence')])
R['calvin'] = [k2, k3, '…', k5]

# Paine, The Age of Reason, Part I (1794), chapters VIII and XIII (Conway's edition, Gutenberg #3743)
P = blocks(read('3743.txt'))
i = P.index(para(P, 'The invention of a purgatory, and of the releasing of souls'))
R['paine'] = P[i:i + 4] + ['…', para(P, 'From the time I was capable of conceiving an idea'), para(P, 'It seems as if parents of the christian profession were ashamed')]
assert R['paine'][3].endswith('consolation to think so.')

# George Herbert, 'The Sacrifice' (The Temple, 1633), selected stanzas, from the CCEL Herbert page
H = blocks(read('url/why-the-cross-herbert-sacrifice.txt').translate({0x91: '‘', 0x92: '’', 0x93: '“', 0x94: '”'}))  # the page's cp1252 apostrophes
st = lambda s: para(H, s)
R['herbert'] = [st('OH all ye, who passe by'), '…', st('I answer nothing, but with patience prove'), '…',
 fix(st('So sits the earths great curse'), []), '…', fix(st('O all ye who passe by, behold and see'), [('Man stole the fruit,4 but', 'Man stole the fruit, but')]),
 st('Lo, here I hang, charg’d with a world of sinne'), '…', st('But, O my God, my God!'), '…', st('Now heal thy self, Physician'), st('In healing not my self'), '…',
 fix(st('But now I die; now all is finished.'), [('My wo, mans weal:5 and', 'My wo, mans weal: and')])]

for k, v in R.items(): print(k, len(v), sum(len(x.split()) for x in v), [len(x.split()) for x in v])
json.dump(R, open(os.path.join(HERE, 'raw.json'), 'w'), ensure_ascii=False, indent=1)
