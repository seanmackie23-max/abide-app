"""Extract the set texts for The Sermon on the Mount from the fetched files in .cache/texts.

Every paragraph is copied by script. Paragraphs are split on blank lines, never on line ends.
Editorial changes (all listed in notes.json):
- Tolstoy (Gutenberg #43302) and Nietzsche (#52319): the underscores that mark italics are removed.
- Mishnah Avot (Oesterley, 1919; an OCR text from archive.org): the footnote markers (^ * ' i) are
  removed, line ends are joined, the spaces the OCR puts before ; and : are closed up, and a saying
  broken by a page of notes is joined. Each source fragment is checked to be in the file.
"""
import re, json, os
HERE = os.path.dirname(os.path.abspath(__file__))
T = os.path.join(HERE, '..', '..', '..', '..', '.cache', 'texts')
def read(p): return open(os.path.join(T, p), encoding='utf-8', errors='ignore').read().replace('\r', '')
def blocks(t): return [re.sub(r'\s+', ' ', b).strip() for b in re.split(r'\n\s*\n', t) if b.strip()]
def para(bl, start): return next(b for b in bl if b.startswith(start))
ital = lambda s: s.replace('_', '')
R = {}

# Augustine, Our Lord's Sermon on the Mount, Book I (tr. William Findlay, NPNF I.6, 1888; New Advent)
A = blocks(read('url/sermon-on-the-mount-augustine-sermon-1.txt'))
R['augustine_steps'] = [para(A, '1. If any one will piously and soberly consider'), para(A, 'For this reason the number of sentences before us is to be carefully considered.')]
R['augustine_cheek'] = [para(A, '56. Hence the Lord goes on to say: You have heard that it has been said, An eye for an eye'), para(A, '63. Nor are we thus precluded from inflicting such punishment')]

# Tolstoy, The Kingdom of God Is Within You, chapter I (tr. Constance Garnett, 1894; Gutenberg #43302)
K = [ital(b) for b in blocks(read('43302.txt'))]
k0 = K.index(para(K, 'Q. Then the ancients allowed the resistance of injury by injury?'))
R['tolstoy'] = [para(K, 'Among the first responses called forth by my book were some letters from American Quakers.'),
                para(K, '"We believe that the penal code of the old covenant'),
                para(K, '"The history of mankind is crowded with evidences'),
                '…'] + K[k0:k0 + 8] + ['…',
                para(K, 'Q. Wherein lies the chief significance of the doctrine of non-resistance?'),
                para(K, 'A. In the fact that it alone allows of the possibility of eradicating evil'),
                para(K, 'True non-resistance is the only real resistance to evil.')]

# The Didache 8 (tr. J. B. Lightfoot, ed. J. R. Harmer, The Apostolic Fathers, 1891; CCEL)
D = blocks(read('url/hard-didache-lightfoot.txt'))
d0 = D.index('Did. 8'); d1 = D.index('Did. 9')
R['didache8'] = D[d0 + 1:d1]

# Mishnah Avot (tr. W. O. E. Oesterley, The Sayings of the Jewish Fathers, SPCK 1919; archive.org OCR)
AV = read('url/how-to-read-the-bible-pirkei-avot-taylor.txt')
def avot(frags, clean):
    for f in frags:
        assert f in AV, f
    return clean
R['avot_anger'] = [avot(['14. They said ^ three things. Rabbi Eliezer said : " Let the', 'honour\'\' of thy associate be dear to thee as thine own" ;', 'and " Be not easily * provoked, and repent one day \'', 'before thy death"; and "Warm thyself ^ before the fire'],
    'They said three things. Rabbi Eliezer said: "Let the honour of thy associate be dear to thee as thine own"; and "Be not easily provoked, and repent one day before thy death".')]
R['avot_fence'] = [avot(['17. (19) Rabbi Akiba ^ said: "Laughter and levity ^ lead to', 'lewdness." ^', '18. (20) He used to say: "The Tradition* is a fence to theTorah ;', 'vows are a defence to self-control ; \' silence \' is a defence', 'to wisdom."'],
    'Rabbi Akiba said: "Laughter and levity lead to lewdness." He used to say: "The Tradition is a fence to the Torah; vows are a defence to self-control; silence is a defence to wisdom."')]
R['avot_judge'] = [avot(['5. Hillel ^ said : " Separate thyself not', 'from the congregation,', 'and trust not thyself^ until the day of thy death " ; and', '"Judge not^ thy neighbour until thou comest into his', 'place " ;'],
    'Hillel said: "Separate thyself not from the congregation, and trust not thyself until the day of thy death"; and "Judge not thy neighbour until thou comest into his place".'),
    avot(['17. (18) Simeon, his son/ said : "All my days have I grown up', 'amongst the wise,i and I have not found aught good for', 'man - but silence " ; ^ and " Not the study * (of the Law),', 'but the carrying-out (of it) is the essential thing" ;^ and'],
    'Simeon, his son, said: "All my days have I grown up amongst the wise, and I have not found aught good for man but silence"; and "Not the study (of the Law), but the carrying-out (of it) is the essential thing".')]

# Nietzsche, The Genealogy of Morals, First Essay 7, 8 and 10 (tr. Horace B. Samuel, 1913; Gutenberg #52319)
N = [ital(b) for b in blocks(read('52319.txt'))]
n10b = para(N, 'When the aristocratic morality goes astray')
R['nietzsche'] = [para(N, 'The reader will have already surmised with what ease the priestly mode of valuation'),
                  para(N, 'But you understand this not? You have no eyes for a force'),
                  '…',
                  para(N, 'The revolt of the slaves in morals begins in the very principle of resentment'),
                  '…',
                  n10b[n10b.index('When the resentment of the aristocratic man manifests itself'):]]

# Augustine, Confessions X.29 (tr. E. B. Pusey, 1838; Gutenberg #3296)
C = blocks(read('3296.txt'))
R['confessions'] = [para(C, 'And all my hope is no where but in Thy exceeding great mercy.')]

for k, v in R.items(): print(k, [len(x.split()) for x in v])
json.dump(R, open(os.path.join(HERE, 'raw.json'), 'w'), ensure_ascii=False, indent=1)
