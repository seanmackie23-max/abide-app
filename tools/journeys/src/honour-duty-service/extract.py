"""Extract the set texts for Honour, duty and service from the cached Gutenberg and New Advent files (.cache/texts).

Editorial changes, all recorded in notes.json: in Miller's Cicero (a Loeb with Latin and English) only the English is taken;
the margin section numbers (*5*), sidenotes (#...#), footnote markers ([A]) and italic underscores are removed.
In New Advent's Ambrose the hyperlinked Scripture references that the website inserts after quotations are removed.
No word of any author or translator is changed. Paragraphs are split on blank lines, never on line ends.
"""
import re, json, os
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.join(HERE, '..', '..', '..', '..', '.cache', 'texts')
def read(p): return open(os.path.join(T, p), encoding='utf-8', errors='ignore').read().replace('\r', '')
def blocks(t): return [re.sub(r'\s+', ' ', b).strip() for b in re.split(r'\n\s*\n', t) if b.strip()]
def para(bl, start, after=0):
    hits = [i for i, b in enumerate(bl) if b.startswith(start)]
    return bl[[i for i in hits if i >= after][0]]
def idx(bl, start, after=0): return [i for i, b in enumerate(bl) if b.startswith(start) and i >= after][0]
R = {}

# Cicero, On Duties, tr. Walter Miller (Loeb, 1913), Gutenberg #47001
C = blocks(read('47001.txt'))
def clean_cic(s):
    s = re.sub(r'#[^#]*#', ' ', s)            # sidenotes
    s = re.sub(r'\*\(?\d+\)?\*', ' ', s)       # margin section numbers
    s = re.sub(r'\[[A-Z]{1,2}\]', '', s)       # footnote markers
    s = s.replace('_', '')                     # italics
    return re.sub(r'\s+', ' ', s).strip()
def cic(start, after=0): return clean_cic(para(C, start, after))
b1 = idx(C, 'II. But since I have decided to write you')
R['cic1'] = [cic('II. But since I have decided to write you'), cic('*5* Moreover, the subject of this inquiry', b1), '…',
             cic('III. Every treatise on duty has two parts', b1), cic('*9* The consideration necessary to determine conduct', b1), '…',
             cic('*11* IV. First of all, Nature has endowed', b1), cic('*12* Nature likewise by the power of reason', b1),
             cic('*13* Above all, the search after truth', b1), cic('*14* And it is no mean manifestation', b1),
             cic('It is from these elements that is forged', b1), cic('*15* V. You see here, Marcus, my son', b1),
             cic('*(15)* Although these four are connected', b1), cic('*17* Before the three remaining virtues', b1)]
b93 = idx(C, '*93* XXVII. We have next to discuss')
R['cic_decorum'] = [cic('*93* XXVII. We have next to discuss'), cic('The relation of propriety to fortitude', b93),
                    cic('*95* This propriety, therefore', b93), cic('*96* The classification of propriety', b93), '…',
                    cic('*98* The poets will observe', b93), cic('*99* We should, therefore, in our dealings', b93)]
b99 = idx(C, '*99* Nay, for him it had been better')
R['cic_regulus'] = [cic('But let us leave illustrations both from story', b99), cic('*101* "But," you will say', b99),
                    cic('How was it foolish?', b99), cic('*102* "What significance, then,"', b99),
                    cic('"Or was he afraid that his act would be morally wrong?', b99), cic('_Thyestes._ \'Hast thou broke', b99), cic('Although this sentiment is put into the mouth', b99), cic('*103* Their third argument is this', b99),
                    cic('As their concluding argument', b99), cic('These are in substance the arguments', b99), '…',
                    cic('This argument, at all events, has no more weight', b99), cic('"Gracious Good Faith, on wings upborne', b99),
                    cic('Whoever, therefore, violates his oath', b99), '…',
                    cic('*110* "But," they argued against Regulus', b99), cic('"Why, then, did he make the journey', b99),
                    cic('Therein you are criticizing', b99), cic('When they argued also that what is highly expedient', b99),
                    cic('From the many splendid examples in history', b99), cic('*111* XXXI. But of all that is thus praiseworthy', b99), '…',
                    cic('Let this be the conclusion of this topic', b99)]

# Ambrose, On the Duties of the Clergy, tr. H. de Romestin (NPNF II.10, 1896), New Advent
BOOKS = r'(?:Genesis|Exodus|Psalm|Luke|Matthew|Jeremiah|Acts|2 Corinthians)'
def clean_amb(s): return re.sub(r'\s+', ' ', re.sub(r' ' + BOOKS + r' \d+:\d+(?:-\d+)?', '', s)).strip()
A1 = blocks(read('url/hds-ambrose-duties1.txt'))
c24 = idx(A1, 'Chapter 24.')
R['ambrose1'] = [clean_amb(para(A1, '115. What duty connected with the chief virtues', c24)), '…',
                 clean_amb(para(A1, '126. The first source of duty', c24)), clean_amb(para(A1, '127. But the piety of justice', c24)), '…',
                 clean_amb(para(A1, '130. Justice, then, has to do with the society', c24)), clean_amb(para(A1, '131. But that very thing is excluded', c24)),
                 clean_amb(para(A1, '132. Next they considered it consonant', c24)), '…',
                 clean_amb(para(A1, '135. Thus, in accordance with the will of God', c24)), clean_amb(para(A1, '136. Great, then, is the glory of justice', c24)),
                 clean_amb(para(A1, '137. Who would not gladly climb', c24)), clean_amb(para(A1, '138. The desire to gain power', c24))]
A2 = blocks(read('url/hds-ambrose-duties2.txt'))
c28 = idx(A2, 'Chapter 28.')
R['ambrose2'] = [clean_amb(para(A2, x, c28)) for x in ('136. It is a very great incentive to mercy', '137. Although we did not act thus', '138. To this no answer could be given', '139. These, then, I preferred', '140. Such gold the holy martyr Lawrence')]

# Washington, Rules of Civility, ed. Moncure D. Conway (1890), Gutenberg #12029: Washington's text only, not the French or Conway's notes
W = blocks(read('12029.txt'))
R['washington'] = [para(W, n) for n in ('1st. Every Action', '6th. Sleep not', '17th. Be no Flatterer', '22d. Shew not yourself glad', '25th. Superfluous Complements', '28th. If any one come to Speak')] + ['…'] + \
                  [para(W, n) for n in ('44th. When a man does all he can', '49th. Use no Reproachfull', '58th. let your conversation', '82d. Undertake not what you cannot', '89th. Speak not Evil', '110th. Labour to keep alive')]

# Aristotle, Nicomachean Ethics, tr. D. P. Chase (1847; Everyman 1911), Gutenberg #8438: Book IV, on the Great-minded man
N = blocks(read('8438.txt'))
g = idx(N, 'The very name of Great-mindedness')
R['aristotle'] = [para(N, s, g) for s in ('Well then, he is thought to be Great-minded', 'The Great-minded man is then, as far as greatness', 'This virtue, then, of Great-mindedness')] + ['…'] + \
                 [para(N, s, g) for s in ('Moreover, he is not a man to incur little risks', 'Further, it is characteristic of the Great-minded', 'Also slow motion, deep-toned voice')]

# Shakespeare, Henry IV Part 1, V.1 (Gutenberg #1780)
S = blocks(read('1780.txt'))
f = para(S, 'Fal. Hal, if thou see me down') if any(b.startswith('Fal. Hal, if thou see me down') for b in S) else next(b for b in S if 'Fal. Hal, if thou see me down' in b)
f = f[f.index('Fal. Hal, if thou see me down'):]; f = f[:f.index('catechism.') + len('catechism.')]
R['falstaff'] = [f]

# Hobbes, Leviathan ch. X (1651), Gutenberg #3207
H = blocks(read('3207.txt'))
h = idx(H, 'CHAPTER X. OF POWER, WORTH')
R['hobbes'] = [para(H, s, h) for s in ('The Value, or WORTH of a man', 'The manifestation of the Value', 'Honourable is whatsoever', 'And therefore To be Honoured', 'Nor does it alter the case of Honour', 'Also amongst men, till there were constituted')]

# Burke, Reflections on the Revolution in France (1790), Works vol. 3 (Gutenberg #15679)
B = blocks(read('15679.txt'))
R['burke'] = [para(B, 'It is now sixteen or seventeen years since I saw the queen'), para(B, 'This mixed system of opinion and sentiment'), para(B, 'But now all is to be changed. All the pleasing illusions')]

# Newman, The Idea of a University (1873 edition), Gutenberg #24526
NW = blocks(read('24526.txt'))
R['newman'] = [para(NW, 'Hence it is that it is almost a definition of a gentleman'), para(NW, 'Not that he may not hold a religion too'),
               para(NW, 'Pride, under such training'), para(NW, 'Such are some of the lineaments of the ethical character'),
               para(NW, 'Useful Knowledge then, I grant, has done its work')]

for k, v in R.items(): print(k, [len(x.split()) for x in v])
json.dump(R, open(os.path.join(HERE, 'raw.json'), 'w'), ensure_ascii=False, indent=1)
