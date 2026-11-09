"""Extract the set texts for The martyrs and the empire.

Sources: New Advent pages (ANF/NPNF, fetched into .cache/texts/url/) and Gibbon (Gutenberg #25717).
Paragraphs are split on blank lines. Removed and noted for the reviewer:
- New Advent's inserted Bible cross-references (e.g. 'Romans 13:1-7; Titus 3:1', 'John 16:24', 'Philippians 3:20');
- a stray fragment of McGiffert's footnote that New Advent leaks into Church History VIII.6.6;
- Gibbon's and Milman's footnote numbers (e.g. ' 1811', ' 182').
HTML entities (C&aelig;sar) are decoded. No word is changed.
"""
import re, json, os, html
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..'))
T = os.path.join(ROOT, '.cache', 'texts')
def read(p): return html.unescape(open(os.path.join(T, p), encoding='utf-8', errors='ignore').read().replace('\r', ''))
def blocks(t): return [re.sub(r'\s+', ' ', b).strip() for b in re.split(r'\n\s*\n', t) if b.strip()]
def para(bl, start): return next(b for b in bl if b.startswith(start))
REFS = r' (?:\d )?(?:[1-3] )?(?:Romans|Titus|John|Philippians|Corinthians|Peter|Matthew|Luke|Acts|Hebrews|Galatians) \d+:\d+(?:-\d+)?(?:; (?:[1-3] )?[A-Z][a-z]+ \d+:\d+(?:-\d+)?)*'
def norefs(s): return re.sub(REFS, '', s)
R = {}

# Martyrdom of Polycarp 9-16, 17-18
P = blocks(read('url/mae-polycarp.txt'))
i = P.index(para(P, 'Chapter 9.')); j = P.index(para(P, 'Chapter 19.'))
pol = [norefs(b) for b in P[i:j] if not b.startswith('Chapter ')]
R['polycarp'] = pol
# Ignatius, Romans 4
I = blocks(read('url/mae-ignatius-romans.txt'))
R['ignatius'] = [para(I, 'I write to the Churches, and impress on them all')]
# Perpetua 2-6 (ANF 1.1-2.2), 15 (ANF 5.2), 18-21 (ANF 6.1-6.4)
PP = blocks(read('url/mae-perpetua.txt'))
g = lambda s: re.sub(r'^\d\. ', '', norefs(para(PP, s)))  # ANF's sub-section numbers dropped; standard numbering is given in each ref
R['perpetua'] = [g('1. The young catechumens'), g('2. While says she'), g('3. Then my brother said to me'), g("1. After a few days there prevailed a report"), g('2. Another day, while we were at dinner'),
                 g('2. But respecting Felicitas'), g('1. The day of their victory shone forth'), g('2. But He who had said'), g('3. Moreover, for the young women'), g('4. The same Saturus at the other entrance')]
# Diognetus 5-6
D = blocks(read('url/mae-diognetus.txt'))
R['diognetus'] = [norefs(para(D, 'For the Christians are distinguished from other men')), norefs(para(D, 'To sum up all in one word'))]
# Tertullian, Apology 10 (opening), 40 (opening), 50
TA = blocks(read('url/mae-tertullian-apology.txt'))
a10 = para(TA, 'You do not worship the gods, you say'); k = a10.index('This, therefore, is what you should do')
a40 = para(TA, 'On the contrary, they deserve the name of faction'); m = a40.index(' Pray, tell me how many calamities')
R['tert-gods'] = [a10[:k].strip(), a40[:m].strip()]
R['tert50'] = [para(TA, 'In that case, you say, why do you complain of our persecutions')]
# Lactantius 12-13, 44, 48
L = blocks(read('url/mae-lactantius.txt'))
R['lact-12-13'] = [para(L, 'A fit and auspicious day was sought out'), para(L, 'That day, the harbinger of death'), para(L, 'of woes which befell not only the Christians'), para(L, 'Next day an edict was published')]
R['lact-44'] = [para(L, 'And now a civil war broke out between Constantine and Maxentius'), para(L, 'Constantine was directed in a dream'), para(L, 'On the same day the enemy of the Romans should perish'), para(L, 'Led by this response to the hopes of victory')]
R['lact-48'] = [para(L, 'Not many days after the victory, Licinius'), para(L, 'When we, Constantine and Licinius, emperors'), para(L, 'All those places are, by your intervention'), para(L, 'And thus, from the overthrow of the Church')]
# Eusebius, Church History VIII.6, 7.2, 7.4, 9.3-5
E = blocks(read('url/mae-eusebius-he8.txt'))
e66 = para(E, '6. At this time Anthimus')
e66 = re.sub(r' vaguest information in regard to the progress.*?\}\}-->', '', e66)
R['he8'] = [para(E, '1. This period produced divine'), para(E, '2. We will describe the manner'), para(E, '3. But as he was unmoved'), para(E, '4. But he held his purpose firmly'), e66,
            para(E, '9. What was to be seen after this'), para(E, '10. And as other decrees followed the first'),
            para(E, '2. We were present ourselves'), para(E, '3. All these things were done'), para(E, '4. We, also being on the spot'), para(E, '5. And we beheld the most wonderful ardor')]
# Eusebius, Life of Constantine I.28-31
V = blocks(read('url/mae-eusebius-vc1.txt'))
R['vc'] = [para(V, 'Accordingly he called on him with earnest prayer'), para(V, 'He said, moreover, that he doubted'), para(V, 'At dawn of day he arose'), para(V, 'Now it was made in the following manner'), para(V, 'The emperor constantly made use of this sign')]
# Gibbon, Decline and Fall XVI and XX (Milman's edition)
G = blocks(read('25717.txt'))
fn = lambda s: re.sub(r' \d{2,4}(?= |[,.;]|$)', '', s)
R['gibbon16'] = [fn(para(G, 'The religious policy of the ancient world seems')), fn(para(G, 'The vague descriptions of exile and imprisonment')), fn(para(G, 'We shall conclude this chapter by a melancholy truth'))]
mil = para(G, '1811 (return) [ Perhaps there never was an instance')
mil = mil[len('1811 (return) [ '):].rstrip(']').strip(); assert mil.endswith('—M.'); R['milman'] = [mil[:-2].rstrip('—').strip()]
g2 = fn(para(G, 'Personal interest is often the standard of our belief')); g2 = g2[:g2.index('fervent devotion.') + len('fervent devotion.')]
R['gibbon20'] = [fn(para(G, 'The Protestant and philosophic readers of the present age')), g2]
for k, v in R.items(): print(k, [len(x.split()) for x in v])
json.dump(R, open(os.path.join(HERE, 'raw.json'), 'w'), ensure_ascii=False, indent=1)
