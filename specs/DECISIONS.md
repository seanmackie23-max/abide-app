# Decisions for the parallel drafting (25 October 2026)

Stage A raised questions across journeys. These are the lead agent's rulings; every Stage B and C agent follows them. The owner can overturn any of them in review.

## Copyright

1. **Translations:** translator died before 1955 and published before 1929.
2. **Original English:** the author must also have died before 1955. A text published before 1929 is still in copyright in the UK and the EU (life plus 70 years) when its author died later. So these are in our own words, with one short quotation at most:
   - T. S. Eliot ('Journey of the Magi', the 1921 essay; d. 1965)
   - Bertrand Russell ('A Free Man's Worship', 'Why I Am Not a Christian'; d. 1970)
   - anyone else who died in 1955 or later
3. **These fail the rule. Use our own words:**
   - Gummere's Seneca (d. 1969)
   - Ludovici's Nietzsche (d. 1971)
   - Mencken (d. 1956)
   - Krey's *Gesta Francorum* (d. 1961)
   - McCabe's Voltaire (d. 1955)
   - Freud's 1928 translator
   - Spengler (Atkinson)
   - Barmen and *Mit brennender Sorge* (after 1929)
   - Thornton's Luther
   - Doyle's Benedict (1948)
4. **Check the file header before using these. If the dates can't be shown to qualify, use our own words:**
   - Horace B. Samuel (*Genealogy*, #52319)
   - Thomas Common (#52881, d. 1928, qualifies)
   - Edgar McNeal
   - Bate
   - Mullan (d. 1934?)
   - Trotter
   - Cunningham
   - J. F. Shaw
   - Sellar
   - Strong
5. **Pascal:** use Trotter (#18269) only if his death year before 1955 is found in a reliable source. Otherwise use C. Kegan Paul (#46921, d. 1902), citing fragments by their opening words. Every journey that quotes Pascal uses the same translator. Record which one in notes.
6. **The Rule of Benedict:** Verheyen (d. 1923, published 1906) qualifies. Check the header of Gutenberg #50040:
   - if it is Doyle (1948), don't use it;
   - use Verheyen from another copy, or Gasquet (1909) or Henderson if fetched;
   - failing those, use our own words.
7. **The 1662 Book of Common Prayer:** quote it. It is under Crown letters patent in the UK, but short liturgical texts are fine. Say so in notes.

## Readings and memory pieces in more than one journey

**The general rule:** a passage or memory piece set in two journeys belongs to the one that comes **earlier on the path**:
- Hall order I → IX, and spec `order` within a hall.
- The orientation journey comes first of all.
- Finished journeys come before new ones.

The later journey points back to it in one line ("You read this in …") and reads something else, or quotes only a phrase. A memory piece is created by the earlier journey (in its `memory_new.json`). The later journey recalls it by id and must not create it again.

Specific rulings:
- **Didache 1–4 and 9–10:** first-christians reads them. what-happens-at-church reads Didache 7 and 14 only, and points back for 9–10. hard-cases points back.
- **Pirkei Avot 1:1:** how-to-read-the-bible. sermon-on-the-mount points back.
- **Chesterton, *Orthodoxy* ch. II:** after-the-death-of-god reads it. line-through-the-heart reads ch. IV or points back.
- **Romans 7:** line-through-the-heart reads it in full. Later journeys point back.
- **Lamentations 3:22–23:** suffering (rewrite). finding-gods-will points back.
- **Newman, *Apologia*, "ten thousand difficulties":** faith-hope-love. come-and-see reads the end of ch. IV and the closing dedication.
- **Maxwell's prayer:** scotlands-enlightenment. darwin-and-design points back.
- **Philippians 4:8:** right-and-wrong. four-virtues points back.
- **Galatians 5:22–23:** seven-deadly-sins reads Galatians 5. four-virtues points back.
- **1 John 4:** faith-hope-love reads it. love-and-marriage and mystics quote only.
- **Bede's sparrow (II.13):** fall-of-rome. monks reads Rule 72 instead.
- **Rule ch. 48 (lectio):** how-to-read-the-bible. monks points back.
- **'turning-of-the-soul':** plato creates it. democracy reads a different Republic passage.
- **'within-our-power':** epicureans-and-stoics creates it. aristotle uses a different memory piece.
- **nicene-creed** (planned for the-creed sessions 3 and 7): session 3 only. Session 7 uses a new Chalcedon-based piece, or the existing apostles-creed.
- **who-was-jesus (rewrite):** gives Mark 15, 1 Corinthians 15 and John 20 to the-last-week.
- **Qur'an 19 (Mary):** other-faiths reads it. who-was-jesus points forward only in its reading list, not in a session.
- **Music used twice within one hall** (hildegard, ubi-caritas, tallis-fantasia and the like): fine across journeys. Within one journey, use a piece once.

## Paintings

- **Claimed works:** use the claims in `.cache/nga/claims.jsonl`.
- **Reusing an art id:** a journey may reuse an art id already in `content/art.json` (including ones used only by a day story) when it is exactly the subject. Say so in notes.
- **No painting:** a session with no painting has none. Never use a stand-in that pretends to be the subject. A near subject is fine only when the `look` text says plainly what the painting really shows, and why it is there.
- **Paintings of rape:** rome sessions 4 and 6 do **not** use paintings of rape (Lucretia, the Sabine women). Leave those sessions without a painting, or use a Roman landscape or ruin, described as such. The story itself can be told in a sentence, without detail.
- **Missing gallery descriptions:** a painting with no gallery description gets no `look` points beyond its title, artist, date and medium.

## The Wisdom of Solomon and the deuterocanon

`.cache/web` has no deuterocanon. The WEB chapters are fetched from ebible.org into `.cache/texts/url/web-wisdom-7.txt`, `web-wisdom-8.txt`, `web-wisdom-11.txt` and `web-sirach-1.txt`. Quote them verbatim from there, and strip the footnote markers. If they are missing, use the Psalm alternative.

## Voice

Ideas from in-copyright modern writers (Lewis, Frankl, Jung, Weil, Arendt and others) are in our own words, with work and date, and at most one short quotation under 25 words.

People of other faiths are described as they describe themselves. Each such journey (one-root-two-branches, other-faiths) flags a reader of that faith for review.
