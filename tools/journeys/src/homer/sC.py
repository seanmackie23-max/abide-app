from sA import IL, OD

PLATO = {"author": "Plato", "work": "The Republic, Books II–III", "translator": "Benjamin Jowett (1871; 3rd ed. 1888)", "source": "https://www.gutenberg.org/ebooks/1497", "kind": "philosophy",
         "who": "Plato (c. 428–348 BC), Athenian philosopher, pupil of Socrates", "when": "Athens, about 375 BC"}
AUG = {"author": "Augustine of Hippo", "work": "Confessions, Book I", "translator": "E. B. Pusey (1838)", "source": "https://www.gutenberg.org/ebooks/3296", "kind": "church",
       "who": "Augustine (354–430), teacher of rhetoric, then bishop of Hippo in North Africa", "when": "Hippo (Annaba, Algeria), about 397–400"}

S5 = {
"title": "The long way home",
"line": "On an enchanted island a goddess offers Odysseus eternal life if he will stay with her. He sits on the shore and weeps for home, for an ageing wife on a rocky island. Twenty years on, she tests him with a secret only the two of them share.",
"plain": "The Odyssey tells how Odysseus, the cleverest of the Greeks, took ten years to get home from Troy. When we meet him he has lost all his men and is held on an island by the goddess Calypso, who loves him and offers to make him immortal. He refuses: he wants to go home to his wife Penelope, though he admits she is not as beautiful as a goddess. When at last he gets home, Penelope, who has waited twenty years, tests him before she believes it is really him. This session asks what kind of hero chooses home over immortality, and what the Odyssey thinks a good life is.",
"why": "The Iliad ended in session 4 with mercy in Achilles' hut, but its hero had chosen a short life and undying glory. Homer's second poem tells of a hero who makes the opposite choice. Having seen what glory costs, we now see what it means to choose a mortal life, a home and a faithful love.",
"answers": [
 "What is the Odyssey about?",
 "Why does Odysseus refuse to become immortal?",
 "What did the Greeks admire in Odysseus: cunning, endurance, or something else?",
 "Who is Penelope, and why is she his equal?"
],
"finding": "Odysseus refuses an immortal goddess to go home to an ageing wife: the Odyssey's hero chooses a mortal, faithful life, and finds his match in a woman as clever and as faithful as he is.",
"background": [
 {"h": "The story of the Odyssey", "paras": [
  "When Troy fell, by the trick of the wooden horse that Odysseus devised, the Greek kings sailed home. Many never arrived. Odysseus, king of the small rocky island of Ithaca off the west coast of Greece, spent ten years at sea. On the way he blinded the one-eyed giant Polyphemus, a son of the sea god Poseidon, who cursed him; he escaped the witch Circe, went down to the land of the dead, sailed past the Sirens, and lost his last men when they ate the sacred cattle of the Sun. Alone, he was washed up on the island of Ogygia, where the goddess Calypso kept him for seven years (Odyssey VII.259).",
  "At home, his wife Penelope has waited for twenty years. More than a hundred young nobles, the suitors, have moved into the palace, eating and drinking her husband's wealth and demanding that she marry one of them. She has held them off by cunning: she said she would choose when she had finished weaving a shroud for Odysseus's father, and for three years she unpicked by night what she wove by day (II.93–110). Their son Telemachus, a baby when Odysseus left, is now a young man."
 ], "key": "Odysseus spends ten years getting home, the last seven held by Calypso. At home Penelope holds off the suitors by cunning, and Telemachus has grown up."},
 {"h": "How the poem is built", "paras": [
  "The Odyssey does not tell the story in order. It opens in the tenth year of the wanderings, with Telemachus at home (Books I–IV). Then it turns to Odysseus on Calypso's island (Book V), our main reading. He reaches the land of the Phaeacians, a people of perfect hosts, and tells them his adventures in a long flashback (Books IX–XII). They sail him home to Ithaca (Book XIII). There, disguised by Athena as an old beggar, he tests who is loyal, kills the suitors and is reunited with Penelope (Books XIV–XXIII)."
 ], "table": {"cols": ["Books", "What happens"], "rows": [
  ["I–IV", "Ithaca and the suitors; Telemachus goes to look for news of his father"],
  ["V", "The gods order Calypso to release Odysseus; he builds a raft"],
  ["VI–VIII", "The Phaeacians: the princess Nausicaa, the court of King Alcinous"],
  ["IX–XII", "Odysseus tells his adventures: the Cyclops, Circe, the dead, the Sirens, the cattle of the Sun"],
  ["XIII–XVI", "Home on Ithaca, disguised; Telemachus returns; father and son meet"],
  ["XVII–XXI", "The beggar in his own palace; the dog Argus; the contest of the bow"],
  ["XXII–XXIV", "The killing of the suitors; Penelope and the bed; peace on Ithaca"]
 ]}, "key": "The Odyssey begins near the end, tells the adventures as a flashback, and gives half its length to the return to Ithaca."},
 {"h": "Why we read these passages", "paras": [
  "The main reading is Book V, where the gods order Calypso to let Odysseus go and she offers him immortality one last time. It answers the question of what this hero values, because he is offered the one thing no mortal can have and turns it down.",
  "The comparison is from near the end, Book XXIII: Penelope's test. It answers the question of what he goes home to, and shows that she is as clever as he is."
 ], "key": "Calypso's offer of immortality, refused; then Penelope's test of the bed, which shows what he has come home for."}
],
"before": [
 "What is Odysseus doing when Hermes arrives on the island?",
 "What does Calypso offer him, and what does she say about Penelope?",
 "In the comparison, how does Penelope test whether the stranger really is her husband?"
],
"readWhy": "Calypso is ordered to release Odysseus; he is offered immortality and chooses to go home.",
"read": [
 dict(OD, raw="od5", idx=[0, 1, 2, 3, 4], ref="Homer, Odyssey V.1–58", title="The gods decide",
  context="Mount Olympus, the home of the gods. Athena ('Minerva'), who loves Odysseus, complains to Zeus ('Jove'). Hermes ('Mercury') is the gods' messenger; 'slayer of Argus' is one of his titles (not the dog of that name). Scheria is the land of the Phaeacians.",
  plain="Athena tells the gods that Odysseus, a just and fatherly king, has been forgotten: he is stuck on Calypso's island and the suitors are plotting to kill his son. Zeus agrees that he must go home and sends Hermes to tell Calypso. Hermes flies over the sea like a seabird to her island.",
  commentary=[
   {"on": "there is not one of his subjects but has forgotten Ulysses, who ruled them as though he were their father", "text": "Athena's case for Odysseus is not only that he is clever. It is that he was a good king, who ruled like a father. The Odyssey cares about justice in a way the Iliad rarely does: the good are rescued, the wicked punished."},
   {"on": "He is to be convoyed neither by gods nor men, but after a perilous voyage of twenty days upon a raft", "text": "Even rescued, Odysseus must save himself: on a raft, with his own strength and wits. The gods help those who keep going."},
   {"on": "whose waves he skimmed like a cormorant that flies fishing every hole and corner of the ocean", "text": "Homer's similes, here a seabird diving for fish, bring the ordinary world into the world of the gods. The audience knew cormorants. They had never seen a god fly."}
  ]),
 dict(OD, raw="od5", idx=[5, 6, 7, 8, 9, 10], ref="Homer, Odyssey V.59–147", title="Calypso's island",
  context="Ogygia, Calypso's island, far out in the sea. Calypso is a nymph, a minor goddess, who lives in a cave. Her name means something like 'she who hides'. Ambrosia and nectar are the food and drink of the gods. Dawn, Orion, Ceres (Demeter) and Iasion are figures from older stories of goddesses who loved mortal men.",
  plain="Calypso's cave is beautiful: a fire of cedar, vines, springs and meadows of violets. Hermes admires it. Odysseus is not there: he is on the shore, weeping and looking out to sea. Hermes gives Calypso Zeus's order. She is furious: the male gods always punish goddesses who love mortals. She saved Odysseus from the sea and wanted to make him immortal. But she cannot defy Zeus.",
  commentary=[
   {"on": "Even a god could not help being charmed with such a lovely spot", "text": "Calypso's island is paradise: warmth, fragrance, birds, water, flowers. Homer makes it as attractive as he can, so that we feel what Odysseus is giving up."},
   {"on": "he was on the sea-shore as usual, looking out upon the barren ocean with tears in his eyes", "text": "The first time the poem shows us its hero, he is weeping on a beach. In paradise, he is homesick. Butler's 'barren' translates a word for the sea that cannot be harvested: the place of no home."},
   {"on": "You are always jealous and hate seeing a goddess take a fancy to a mortal man", "text": "Calypso has a point. Zeus has loved many mortal women; the goddesses who loved mortal men were punished. Homer lets a goddess accuse the gods of a double standard."},
   {"on": "had set my heart on making him immortal, so that he should never grow old all his days", "text": "Here is the offer: to be young and alive for ever. It is the thing every hero in the Iliad longed for and could not have. Sarpedon said he would not fight if he could escape death. Achilles fought because he could not."}
  ]),
 dict(OD, raw="od5", idx=[11, 12, 13, 14, 15, 16, 17, 18], ref="Homer, Odyssey V.148–227", title="I want to get home",
  context="Calypso goes to tell Odysseus he may leave. The river Styx, in the underworld, was the most solemn oath of the gods. The scene ends with the two going to bed for the last time: the poem is frank that he has been her lover, unwillingly.",
  plain="Calypso finds Odysseus weeping and tells him to build a raft; she will help him. He suspects a trick and makes her swear she means no harm. She laughs, swears, and gives him supper. Then she tries once more: if he knew what suffering lies ahead, he would stay and become immortal; and surely she is more beautiful than his wife. He answers that he knows Penelope cannot compare with her, but he wants to go home, whatever it costs.",
  commentary=[
   {"on": "for he had got tired of Calypso, and though he was forced to sleep with her in the cave by night, it was she, not he, that would have it so", "text": "The poem is honest: Odysseus is a prisoner, and a goddess's love is not freely returned. Paradise without freedom is a prison."},
   {"on": "nothing that you can say or do shall make me go on board a raft unless you first solemnly swear that you mean me no mischief", "text": "Even when he is offered what he longs for, Odysseus suspects a trap. His caution has kept him alive. It is mētis, the practical cunning that is his great quality."},
   {"on": "but you are quite wrong here", "text": "Calypso smiles at him. She knows him well: always clever, always suspicious. The two have a real, if unequal, intimacy."},
   {"on": "keep house along with me, and let me make you immortal, no matter how anxious you may be to see this wife of yours", "text": "The final offer: immortality, and a goddess. And a sting: you are thinking about her all the time. Calypso knows she has already lost."},
   {"on": "I am quite aware that my wife Penelope is nothing like so tall or so beautiful as yourself. She is only a woman, whereas you are an immortal. Nevertheless, I want to get home, and can think of nothing else.", "text": "This is the centre of the Odyssey. Odysseus does not pretend that Penelope is a goddess. He admits that what he is choosing is less, by every outward measure: a mortal, ageing woman on a rocky island. He chooses it anyway, because it is his. The word 'nevertheless' carries a whole idea of love: not for the best, but for the one."},
   {"on": "If some god wrecks me when I am on the sea, I will bear it and make the best of it.", "text": "Odysseus' other great quality: endurance. One of his titles in Greek is polytlas, 'much-enduring'. He chooses suffering and home over ease and exile. Two days later, the sea god will wreck his raft."}
  ])
],
"compare": {"title": "The bed", "why": "Odysseus refused a goddess for a mortal wife. Twenty years on, home at last, he finds that she will not simply take him back. Read how Penelope tests him.",
 "parts": [
  dict(OD, raw="od23", idx=[0, 1, 2], ref="Homer, Odyssey XXIII.153–204", title="Penelope's test",
   context="The palace on Ithaca. Odysseus has killed the suitors, and the old nurse has told Penelope that the beggar was her husband. She does not believe it. Eurynome and Euryclea are servants. Athena ('Minerva') makes Odysseus look young again.",
   plain="Odysseus, bathed and handsome, sits opposite Penelope and complains that she is hard-hearted. He asks for a bed to sleep alone. Penelope tells the nurse to move the bed he built out of their bedroom. Odysseus explodes: no one could move that bed, because he built it round a living olive tree, with the trunk as one of its posts. He describes exactly how he made it.",
   commentary=[
    {"on": "this woman has a heart as hard as iron", "text": "The phrase Hector used of Achilles, and Achilles of Priam. Here it is a husband's frustration with a wife who will not believe him. But Penelope's 'iron' is not cruelty. It is the caution that kept her faithful for twenty years."},
    {"on": "take his bed outside the bed chamber that he himself built", "text": "Her test is a trick worthy of Odysseus himself. She speaks as if the bed could be moved. Only the real Odysseus would know that it cannot."},
    {"on": "I built my room round this with strong walls of stone and a roof to cover them", "text": "The bed is the heart of the house, and the house was built round it. It is rooted in the earth, a living tree. It is the poem's image of their marriage: made by his own hands, unmovable, known only to the two of them."},
    {"on": "or whether any one has been removing it by cutting down the olive tree at its roots", "text": "Odysseus' anger gives him away. The man who can lie about everything cannot hide his fear that the marriage, the rooted thing, has been cut. Penelope has outwitted the cleverest man in Greece."}
   ]),
  dict(OD, raw="od23", idx=[3, 4], ref="Homer, Odyssey XXIII.205–240", title="Like land to a swimmer",
   context="Penelope's response. Helen, whose story began the war, is mentioned as the wife who was not faithful.",
   plain="Penelope breaks down and throws her arms round him. She explains that she was afraid of being deceived by a stranger. Now she believes. Odysseus weeps and holds her. She is as glad of him as shipwrecked sailors are of the shore. Athena holds back the dawn to give them a longer night.",
   commentary=[
    {"on": "We have suffered, both of us. Heaven has denied us the happiness of spending our youth, and of growing old, together", "text": "The Odyssey's great theme in one sentence. The war took twenty years from both of them. What they have now is not youth but the rest of a mortal life together."},
    {"on": "I have been shuddering all the time through fear that someone might come here and deceive me with a lying story", "text": "Penelope's caution mirrors his. Odysseus tested everyone in disguise; she tested him. The poem calls such a marriage homophrosynē elsewhere (VI.183): being of one mind."},
    {"on": "As the sight of land is welcome to men who are swimming towards the shore, when Neptune has wrecked their ship", "text": "The simile describes Odysseus's own experience, the shipwreck after leaving Calypso. But it is applied to Penelope. She too has been at sea for twenty years. The two survivors reach land in each other."},
    {"on": "had not Minerva determined otherwise, and held night back in the far west", "text": "The goddess stops the sun for a married couple. In the Iliad the gods fought over heroes on a battlefield. Here a goddess's greatest gift is a longer night for husband and wife."}
   ])
 ]},
"lecture": {"sections": [
 {"h": "Nostos: homecoming", "paras": [
  "The Greeks had a word, nostos, for the return home from war, and a whole group of poems, now lost, about the homecomings of the heroes from Troy. Most were stories of disaster. Agamemnon got home and was murdered in his bath by his wife and her lover. Ajax the Lesser drowned. Menelaus wandered for years. The Odyssey alludes to them all, as a dark background to its own story of a homecoming that succeeds. Our English word 'nostalgia' was made from it in 1688, by a Swiss medical student, for the sickness of homesickness: nostos plus algos, pain.",
  "So the Odyssey's question is the opposite of the Iliad's. The Iliad asks what is worth dying for. The Odyssey asks what is worth living for, and answers: home. Not a place only, but a household, a wife, a son, an old father, a dog, a bed, servants who stayed loyal, a land you can kiss."
 ], "key": "Nostos, homecoming, was the subject of many Greek poems, most of them tragic. The Odyssey asks what is worth living for, and answers: home."},
 {"h": "Refusing immortality", "paras": [
  "Odysseus is the only hero in Greek poetry who is offered immortality and turns it down. Why? The French classicist Jean-Pierre Vernant, in an essay called 'The Refusal of Odysseus', suggested an answer in our own words: to stay with Calypso would be to vanish. Her name means 'she who hides'. On her island, out of all stories, Odysseus would live for ever but be nobody: no past, no future, no name in anyone's song. To be human, for the Odyssey, is to be mortal, with a particular past, particular loves and a place in the world.",
  "Set this beside Achilles. Achilles could have had a long life and chose a short one, for undying glory. Odysseus could have had an undying life and chose a mortal one, for love and home. Both refuse the long, empty life. Both choose a human life with meaning. But they place the meaning differently: Achilles in what is sung of him after death, Odysseus in the people he lives among."
 ], "key": "Odysseus refuses immortality because it would make him nobody; he chooses a mortal life with a name, a past and people he loves."},
 {"h": "Mētis: the clever hero", "paras": [
  "If Achilles' excellence is strength, Odysseus's is mētis: practical intelligence, cunning, the ability to find a way out. He devised the wooden horse. He escaped the Cyclops by telling him his name was 'Nobody', so that when the blinded giant called for help, he shouted 'Nobody is killing me!' (IX.366–414). He has himself tied to the mast to hear the Sirens without dying. Again and again he survives by lying, disguising himself, waiting.",
  "His other quality is endurance. Homer calls him 'much-enduring' and 'much-suffering'. He loses everything: his ships, his men, twenty years of his life. He goes on. Mētis and endurance together make a new kind of heroism, one that suits not the battlefield but ordinary life, where most of our problems cannot be solved by force. That is part of why later ages loved him: from Tennyson's old Ulysses, still setting out, to James Joyce's Ulysses (1922), which turned a day in the life of an ordinary Dublin man into an Odyssey."
 ], "key": "Odysseus' excellence is mētis, cunning, and endurance: a heroism for ordinary life, where force rarely solves anything."},
 {"h": "Penelope's equal mind", "paras": [
  "Penelope is not a prize waiting to be won. She is as clever as her husband. She invented the trick of the weaving and kept a hundred suitors waiting for three years. When the beggar comes, she half-recognises him and sets up the contest of the bow (XIX–XXI), which only Odysseus can win. And she tests him with the bed, and wins. The poem calls her 'circumspect' or 'wise' again and again.",
  "In Book VI Odysseus wishes the young princess Nausicaa a husband and a home and, best of all, homophrosynē: a man and woman 'of one mind' in their home, a grief to their enemies and a joy to their friends (VI.180–185). That is what he and Penelope have. Samuel Butler, our translator, was so struck by the women of the poem that he argued in The Authoress of the Odyssey (1897) that it was written by a young woman in Sicily. Few scholars agree, but his question was a good one: why does this poem take its women so seriously?"
 ], "key": "Penelope matches Odysseus in cunning and faithfulness; their marriage is homophrosynē, being of one mind. Butler even thought a woman wrote the poem."},
 {"h": "Guests, hosts and justice", "paras": [
  "The Odyssey is a poem about hospitality. Every place Odysseus comes to is a test of xenia, the bond between host and guest that you met in session 4. The Phaeacians are perfect hosts: they feed him, honour him and sail him home with gifts. The Cyclops is the worst host imaginable: he eats his guests. The suitors are the worst guests: they eat their absent host's wealth and abuse the beggar at his door, not knowing he is the master of the house.",
  "This gives the Odyssey a moral world clearer than the Iliad's. At its beginning Zeus complains that mortals blame the gods for troubles they bring on themselves by their own wickedness (I.32–43). The suitors are warned, and ignore the warnings. When Odysseus kills them, the poem presents it as justice, the punishment of those who broke the laws of Zeus of strangers. In the Odyssey, unlike the Iliad, the gods seem to care how people behave."
 ], "key": "The Odyssey tests everyone by xenia: perfect hosts, a cannibal host, guests who devour their host. Its gods punish the wicked, as the Iliad's rarely do."},
 {"h": "The dark side of the homecoming", "paras": [
  "The homecoming is not gentle. Odysseus and his son kill all the suitors in the hall, more than a hundred young men, though some beg for mercy (Book XXII). Then Telemachus hangs twelve slave women who had slept with the suitors, and the disloyal goatherd is mutilated (XXII.465–477). Homer presents this as just punishment. Many modern readers find it horrifying, and Margaret Atwood retold the story from the side of the hanged maids in The Penelopiad (2005).",
  "It is right to see this clearly. The Odyssey's justice is real but harsh, and its mercy is narrow. The household is restored by a massacre. Only in the last book does Athena stop the killing, when the suitors' families come for revenge, and impose a peace (XXIV.528–548). The Odyssey reaches a world of home and order. It does not reach a world of forgiveness. Keep this in mind for the case against Homer, which comes next."
 ], "key": "The homecoming ends in a massacre of the suitors and the hanging of twelve slave women: the Odyssey's justice is real but harsh, and its mercy narrow."}
], "refs": [
 "Homer, Odyssey I.32–43; II.93–110; V.1–227; VI.180–185; VII.259; IX.366–414; XXII; XXIII.153–240; XXIV.528–548. Tr. Samuel Butler (1900).",
 "Jean-Pierre Vernant, 'The Refusal of Odysseus', in Seth Schein (ed.), Reading the Odyssey (1996).",
 "Samuel Butler, The Authoress of the Odyssey (1897).",
 "Johannes Hofer, Dissertatio medica de nostalgia (Basel, 1688), for the word 'nostalgia'.",
 "Alfred Tennyson, 'Ulysses' (1842); James Joyce, Ulysses (1922); Margaret Atwood, The Penelopiad (2005)."
]},
"terms": ["Nostos", "Mētis", "Xenia", "Homophrosynē", "Nymph", "Suitors"],
"debate": {"question": "Is Odysseus a hero or a con man?", "positions": [
 {"name": "A hero of intelligence", "who": "The Odyssey itself and Athena; Tennyson; many modern readers", "view": "Odysseus shows that wit, patience and endurance are as heroic as strength. He keeps his men alive as long as he can, refuses a goddess for his wife, and restores justice to his home. He is the model of a mind that will not give up.", "evidence": "His refusal of Calypso; the Cyclops escape; Athena's love for him; Zeus calling him the wisest of mortals (I.65–67)."},
 {"name": "A liar and manipulator", "who": "Sophocles (Philoctetes, 409 BC); Euripides; Virgil (Aeneid II, 'cruel Ulysses'); Dante (Inferno XXVI)", "view": "Later Greeks and Romans saw the darker side of mētis: Odysseus lies, tricks and betrays, and loses all his men. Dante put him in hell among the fraudulent counsellors for the trick of the wooden horse and for leading his men to their deaths.", "evidence": "His lying tales; the death of all his crew; the massacre of the suitors and the maids; his tricking of Philoctetes in Sophocles' play."},
 {"name": "Neither: a human being", "who": "Many recent scholars", "view": "The Odyssey shows a man whose gifts can be used well or badly. His cunning saves his life and also costs his men theirs. The poem lets us admire and doubt him, and that complexity is why he has lasted.", "evidence": "The opening's admission that 'he could not save his men'; the poem's mixture of tenderness and cruelty."}
], "agree": "All agree that Odysseus is a new kind of hero, whose greatness is in his mind and his endurance rather than in strength, and that his cunning has a dark side."},
"look": {"art": "ingres-ulysses", "why": "Jean-Auguste-Dominique Ingres painted this study of Ulysses, the Roman name for Odysseus, in 1827. It is not a scene from the poem but a portrait of the hero himself.", "points": [
 "The man's upper body and face are seen from below, in profile, facing the right side of the painting.",
 "He has a long, straight nose, a thick dark beard and curly dark hair.",
 "A yellow helmet sits tipped upward on top of his head.",
 "He wears a warm reddish-orange garment, and his left hand, in shadow, is clenched against his chest.",
 "The background is a muted blend of yellows and greens; the signature 'Ingres' is in the lower right corner."
]},
"music": {"id": "song-for-athene", "why": "John Tavener's Song for Athene was written in memory of a young woman named Athene, and sets words of rest and homecoming from the Orthodox funeral service over a single held note. Hear it as music of arrival, after a long voyage."},
"think": {"library": "the-individual", "depth": 1, "why": "Odysseus chooses not the most beautiful but his own: this particular wife, this home. See in brief how the West came to believe that each single person counts."},
"learn": {"memory": "argus-the-dog", "why": "When Odysseus comes home disguised, the first to know him is his old dog, who has waited twenty years. Note that this piece is in Alexander Pope's verse translation (1726), not Butler's prose."},
"check": [
 {"q": "Why does Homer make Calypso's island so beautiful?", "options": ["Because it is where Odysseus was born", "So that we feel what Odysseus is giving up when he chooses home", "Because the gods wanted to reward him", "To show that Calypso is wicked"], "answer": 1, "why": "Paradise makes the choice real: he is turning down ease, beauty and immortality. Calypso is not shown as wicked; she is honest and even kind."},
 {"q": "Odysseus admits that Penelope is less beautiful than Calypso. What does this admission add to his choice?", "options": ["It shows he is lying to Calypso to escape", "It shows he does not love Penelope", "It shows that he chooses Penelope not because she is the best by any outward measure, but because she is his: love for the one, not the best", "It shows that he is afraid of Calypso"], "answer": 2, "why": "'Nevertheless, I want to get home': he admits the comparison and chooses anyway. That is what makes the choice an act of love."},
 {"q": "How does Odysseus' choice compare with Achilles' choice in session 2?", "options": ["Both choose glory over life", "Achilles chooses a short life for undying glory; Odysseus chooses a mortal life over an undying one, for love and home: both refuse an empty life, but place meaning differently", "Both choose to go home", "Achilles chooses immortality and Odysseus refuses it"], "answer": 1, "why": "The two heroes face mirror-image choices. Achilles was never offered immortality, so the last option is wrong."},
 {"q": "Why is Penelope's test of the bed so clever?", "options": ["Because she knows the bed is broken", "Because only the real Odysseus would know that the bed cannot be moved, being built round a living olive tree, and his anger proves it", "Because she has asked the nurse to watch his face", "Because Athena told her what to say"], "answer": 1, "why": "The bed's secret is known only to the two of them and one servant. Odysseus' outburst gives him away."},
 {"q": "What makes the Odyssey's moral world different from the Iliad's?", "options": ["The Odyssey has no gods in it", "In the Odyssey the gods seem to care how people behave, and the breakers of hospitality are punished", "In the Odyssey everyone is forgiven", "The Iliad's gods punish the wicked and the Odyssey's do not"], "answer": 1, "why": "Zeus's complaint in Book I, the suitors' warnings and their punishment show a world of justice. But it is not a world of forgiveness: the suitors and maids are killed."},
 {"q": "Which is the best objection to reading the Odyssey as a simple story of love and home?", "options": ["That Odysseus never really reaches Ithaca", "That the homecoming is achieved by a massacre of the suitors and the hanging of twelve slave women, presented as justice", "That Penelope marries one of the suitors", "That Calypso is the real heroine"], "answer": 1, "why": "Book XXII is brutal. The home is restored, but by a justice that is harsh and a mercy that is narrow."}
],
"tutorial": {"question": "'Glory or home?' Compare the choices of Achilles and Odysseus.", "approach": "Set out Achilles' two fates (Iliad IX) and Calypso's offer (Odyssey V). Explain kleos and nostos. Ask what each hero gains and loses by his choice, and what each thinks gives a life meaning. Use Penelope to show what Odysseus' choice is for. Do not forget the dark side of both poems. End with your own view: which is the better life, and is there a third answer neither poem gives?",
 "strong": [
  "Explains the two fates and kleos aphthiton accurately.",
  "Explains Calypso's offer and why refusing immortality is unique.",
  "Uses 'nevertheless, I want to get home' to show the nature of Odysseus' love.",
  "Explains nostos, mētis and Penelope's equal cleverness.",
  "Notes that both heroes reject a long, empty life, but place meaning differently.",
  "Acknowledges the massacre in Book XXII and the limits of the Odyssey's justice."
 ]},
"reading": [
 {"author": "Homer, tr. Emily Wilson", "title": "The Odyssey", "year": 2017, "level": "start", "why": "A clear, fast modern verse translation, the first into English by a woman; read it beside Butler."},
 {"author": "Edith Hall", "title": "The Return of Ulysses: A Cultural History of Homer's Odyssey", "year": 2008, "level": "deeper", "why": "How the Odyssey has been retold, from antiquity to film."},
 {"author": "Seth Schein (ed.)", "title": "Reading the Odyssey: Selected Interpretive Essays", "year": 1996, "level": "scholars", "why": "Includes Vernant on the refusal of immortality and other classic essays."},
 {"author": "Sheila Murnaghan", "title": "Disguise and Recognition in the Odyssey", "year": 1987, "level": "scholars", "why": "On the poem's tests and recognitions, Penelope's above all."}
],
"practice": "Live it this week: do one ordinary, faithful thing for the people you live with that no one will notice or praise: mend something, cook a meal they love, write a note. Do it as Odysseus chose Penelope: not because it is glorious, but because they are yours.",
"reflect": "What, for you, is home? What would you refuse, even immortality, to keep it?",
"takeaways": [
 "Odysseus refuses Calypso's offer of immortality to go home to a mortal, ageing wife: 'nevertheless, I want to get home'.",
 "His greatness is mētis and endurance, and Penelope is his equal in both; their marriage is homophrosynē, being of one mind.",
 "The Odyssey's world has more justice than the Iliad's, but its homecoming ends in a massacre: home and order, not yet forgiveness."
]
}

S6 = {
"title": "The case against: were the gods any good, and is glory worth it?",
"line": "Among the dead, Achilles says he would rather be a poor man's servant than king of all the ghosts. Three centuries later Plato says Homer's gods are liars and his heroes poor models, and wants the poems censored. The case against Homer's world, at full strength.",
"plain": "This journey has admired Homer: the honesty of the Iliad, the mercy in Achilles' hut, Odysseus' faithful choice. Now hear the case against. It comes first from Homer himself: in the Odyssey, the ghost of Achilles says that glory is worthless beside life. Then from the Greek philosophers, above all Plato, who said that Homer's gods lie, cheat and quarrel, that his heroes weep and despair, and that the poems should not be taught to the young. Put at its strongest, the charge is this: Homer's world has courage and pity, but its gods are not good and its glory is hollow.",
"why": "Sessions 1 to 5 followed both poems to their endings and found greatness in them: honour, glory, mercy, home. Before we can say what Homer gave the West, we have to face the strongest reasons to think his picture of greatness is wrong. The objection comes here, after you have read enough Homer to weigh it.",
"answers": [
 "Was glory worth it, by the heroes' own account?",
 "Were the Greek gods good?",
 "Why did Plato want to censor Homer?",
 "What is the strongest case against Homer's idea of a great life?"
],
"finding": "Homer's own Achilles repudiates glory among the dead, and Plato charged that Homer's gods are neither good nor truthful; the strongest charge is that Homer's world has courage and pity but no goodness at the top and no mercy beyond the tent.",
"objection": True,
"background": [
 {"h": "The case so far", "paras": [
  "The Iliad opened with Achilles' anger over his honour (session 1). Achilles weighed glory against a long life and doubted the code (session 2). At the height of his glory he was at his most inhuman, dragging Hector's body (session 3). The poem ended with mercy between enemies, a truce and not yet forgiveness (session 4). In the Odyssey, Odysseus refused immortality to go home, and found home restored by a harsh justice (session 5).",
  "Through all of it, the gods have been there: Athena pulling Achilles' hair, Zeus weighing deaths, Athena tricking Hector, Calypso protesting, Athena stopping the dawn. And through all of it, the heroes have lived by one belief: that death is the end of anything worth having, and glory is all that survives it. This session asks whether either the gods or the glory deserve the place Homer gives them."
 ], "key": "The journey has found honour, glory, mercy and home in Homer. Behind them stand the gods and the belief that only glory survives death: now both are tested."},
 {"h": "The land of the dead", "paras": [
  "In Book XI of the Odyssey, Odysseus, on Circe's instructions, sails to the edge of the world and calls up the dead. He digs a pit and pours in the blood of sacrificed sheep; the ghosts come up and must drink before they can speak. He meets the prophet Tiresias, and the ghost of his own mother, who died of grief while he was away: three times he tries to hold her, and three times she slips through his arms like a shadow (XI.204–208). He meets Agamemnon, murdered by his wife on his return. Then come Achilles and his friends.",
  "Homer's Hades is not heaven or hell. It is a dim, joyless place where all the dead go, good and bad alike, as shadows without strength or understanding. This is the background to the whole heroic code: if this is what waits for everyone, glory in the memory of the living is the only kind of survival worth having."
 ], "key": "In Odyssey XI Odysseus calls up the dead with blood. Homer's Hades is a dim place where all go as shadows, which is why glory mattered so much."},
 {"h": "Who were the critics?", "paras": [
  "The first known critic of Homer's gods was Xenophanes of Colophon (about 570–475 BC), a wandering poet-philosopher. Next came Heraclitus of Ephesus (about 500 BC). The greatest was Plato (about 428–348 BC), an Athenian aristocrat, pupil of Socrates, who founded the Academy, the first school of philosophy. His Republic, written around 375 BC, is a long conversation in which Socrates and two young men, Glaucon and Adeimantus (Plato's own brothers), design an ideal city in order to discover what justice is.",
  "In Books II and III they ask how the city's guardians should be educated. In Greece, education meant Homer. So Socrates goes through the poems and asks which stories are fit to be taught. His answer is the most famous attack on Homer ever written. You will read it in Benjamin Jowett's translation (1871), the classic Victorian English Plato."
 ], "timeline": [
  {"year": "c. 750–650 BC", "text": "The Iliad and the Odyssey"},
  {"year": "c. 570–475 BC", "text": "Xenophanes attacks the gods of Homer and Hesiod"},
  {"year": "c. 525 BC", "text": "Theagenes of Rhegium, the first known allegorical reader of Homer"},
  {"year": "c. 500 BC", "text": "Heraclitus says Homer should be thrown out of the contests"},
  {"year": "c. 375 BC", "text": "Plato's Republic"},
  {"year": "c. 335 BC", "text": "Aristotle's Poetics defends the poets"},
  {"year": "1872, 1887", "text": "Nietzsche praises the Homeric Greeks against Christianity"}
 ], "key": "Xenophanes, Heraclitus and above all Plato's Republic (c. 375 BC) attacked Homer's gods and heroes as unfit to educate the young."},
 {"h": "Why we read these passages", "paras": [
  "The main reading is Achilles' ghost in Odyssey XI, and the silent ghost of Ajax. It answers the question 'was glory worth it?' in the words of the greatest hero himself. The comparison is Plato's charge from Republic II and III: that Homer's gods are made the authors of evil, and his heroes taught to fear death and weep. It answers the question 'were the gods any good?'. The objection is given here without reply. The replies come in the debate."
 ], "key": "Achilles' ghost judges glory; Plato judges the gods. The case is stated before any reply."}
],
"before": [
 "What does Odysseus say to comfort Achilles, and how does Achilles answer?",
 "What does Achilles ask about, and what makes him happy at the end?",
 "List Plato's charges against Homer. Which do you find strongest?"
],
"readWhy": "Achilles' ghost says what glory is worth among the dead, and Ajax's ghost will not speak.",
"read": [
 dict(OD, raw="od11", idx=[0, 1, 2, 3, 4], ref="Homer, Odyssey XI.465–540", title="Better a servant above ground",
  context="Odysseus is telling his story to the Phaeacians. At the edge of the world, among the dead, he has just spoken with Agamemnon's ghost. 'The son of Peleus' and 'descendant of Aeacus' are Achilles; Patroclus, Antilochus and Ajax were his friends. Neoptolemus is Achilles' son, who fought at Troy after his father's death. Mars is Ares, god of war.",
  plain="Achilles' ghost asks Odysseus why he has dared to come among the dead. Odysseus says he came for advice, and tells Achilles he should not grieve: he was honoured like a god in life and is a great prince among the dead. Achilles answers that he would rather be a poor man's paid servant on earth than king of all the dead. He asks about his son and his father. Odysseus tells him his son was a brave fighter at Troy, and Achilles strides away across the meadow, happy.",
  commentary=[
   {"on": "among us silly dead, who are but the ghosts of them that can labour no more", "text": "'Silly' here means senseless, without mind. The greatest hero of all now speaks of himself as one of the witless dead. This is Homer's Hades: not punishment, just emptiness."},
   {"on": "no one was ever yet so fortunate as you have been, nor ever will be, for you were adored by all us Argives as long as you were alive, and now that you are here you are a great prince among the dead", "text": "Odysseus offers the heroic code's consolation: you had honour in life and you have rank in death. It is exactly the bargain Achilles chose in the Iliad, and exactly what he made his choice for."},
   {"on": "I would rather be a paid servant in a poor man's house and be above ground than king of kings among the dead", "text": "Achilles rejects it utterly. A 'paid servant' in a poor man's house was close to the lowest thing a free man could be, a landless labourer. Achilles, who chose glory over a long life, now says he would take the lowest life on earth over all the glory in Hades. This is the strongest objection to the heroic code ever written, and Homer wrote it."},
   {"on": "could I but be as I then was and go even for a short time to my father's house, any one who tried to do him violence or supersede him would soon rue it", "text": "Look at what he still wants: to protect his father. In death, what Achilles longs for is not glory but the chance to care for the old man he left. The Iliad's last book, where he saw Peleus in Priam, is not far away."},
   {"on": "exulting over what I had said concerning the prowess of his son", "text": "And yet. When he hears his son is a great warrior, Achilles strides off happy. The code is not quite dead in him. Glory is worthless for himself, but he still rejoices in it for his son. Homer gives us both, and lets us decide which is the last word."}
  ]),
 dict(OD, raw="od11", idx=[5, 6, 7], ref="Homer, Odyssey XI.541–567", title="The silence of Ajax",
  context="Ajax, son of Telamon, was the greatest Greek warrior after Achilles. After Achilles' death, Odysseus and Ajax competed for his armour, and the judges gave it to Odysseus. Ajax, shamed, killed himself. Erebus is the darkness of the underworld.",
  plain="All the other ghosts tell their stories, but Ajax keeps away, still angry about the contest for Achilles' armour. Odysseus wishes he had never won it, and begs Ajax to forgive him, even in death. Ajax turns away without a word into the darkness.",
  commentary=[
   {"on": "still angry with me for having won the cause in our dispute about the armour of Achilles", "text": "Ajax died for honour. He lost a prize, the armour, and could not bear the shame. It is the Iliad's quarrel over a prize again, and this time it ended in suicide."},
   {"on": "Would that I had never gained the day in such a contest, for it cost the life of Ajax", "text": "Odysseus, now, sees what honour cost: a friend's life for a suit of armour. He has learned something the code cannot teach."},
   {"on": "will you not forget and forgive even in death", "text": "The word 'forgive' appears here, at the edge of the world. Odysseus asks for it. It is the nearest the poems come to the idea."},
   {"on": "He would not answer, but turned away to Erebus and to the other ghosts", "text": "Ajax refuses. His silence is one of the most famous moments in ancient literature: honour wounded beyond healing, even after death. In Homer's world, forgiveness can be asked for, but there is nothing to make it happen."}
  ])
],
"compare": {"title": "Plato's charge", "why": "Achilles' ghost doubted glory. Plato, writing about three centuries later, went further and put Homer's gods and heroes on trial. Read the charges in his own words.",
 "parts": [
  dict(PLATO, raw="rep2", idx=list(range(0, 11)), ref="Plato, Republic II.377d–378e", title="A bad lie about the gods",
   context="Socrates (the 'I' speaking) and Adeimantus are discussing which stories should be told to the children who will become the guardians of their ideal city. Uranus and Cronus are gods in Hesiod's account of the beginning, who mutilated and overthrew their fathers. Hephaestus and Here (Hera) are the smith god and the queen of the gods.",
   plain="Socrates says the greatest fault of Homer, Hesiod and the other poets is to tell lies, and bad lies, about the gods and heroes: like a painter whose portrait looks nothing like its subject. Stories of gods attacking their fathers, fighting and plotting against one another should not be told to the young, even as allegories, because the young cannot tell allegory from fact, and what they hear first stays with them for life.",
   commentary=[
    {"on": "Whenever an erroneous representation is made of the nature of gods and heroes", "text": "Plato's charge is not that the stories are untrue history. It is that they are untrue to what the divine is. If the gods are truly gods, they cannot be what Homer shows."},
    {"on": "he will only be following the example of the first and greatest among the gods", "text": "The danger is imitation. Children learn by copying. If the greatest god punished his father, a young man may think he can too. Myths are not harmless entertainment; they shape character."},
    {"on": "and all the battles of the gods in Homer—these tales must not be admitted into our State, whether they are supposed to have an allegorical meaning or not", "text": "Plato knows the defence that the stories are allegories, symbols of deeper truths, and rejects it for the young. 'Our State' is the ideal city of the dialogue. This is a call for censorship, made openly."},
    {"on": "anything that he receives into his mind at that age is likely to become indelible and unalterable", "text": "The heart of Plato's concern: early stories become part of who we are. Modern psychologists and every parent would agree with the premise, whatever they think of the conclusion."}
   ]),
  dict(PLATO, raw="rep2", idx=list(range(11, 26)), ref="Plato, Republic II.379c–380c", title="God is not the author of evil",
   context="After a cut ('…'), Socrates states the first principle of a true theology. The 'two casks' are the two urns of Zeus that Achilles described to Priam in Iliad XXIV; Plato quotes the passage. Pandarus broke a truce in Iliad IV at Athena's prompting; Niobe and the house of Pelops were subjects of tragedies.",
   plain="Since God is good, he is the cause only of good things, not of evil. So we must not believe Homer when he says that Zeus hands out good and evil from two jars, or that the gods caused men to break oaths. If a poet tells of suffering, he must either not say God caused it, or say it was just punishment that did the sufferers good. To say a good God causes evil is impious.",
   commentary=[
    {"on": "Then God, if he be good, is not the author of all things", "text": "This is the first rule of Plato's theology, and one of the most important sentences in the history of religion: God is good, and so cannot be the cause of evil. Notice the singular, 'God'. Plato is moving beyond Homer's many quarrelling gods towards one perfectly good divine being."},
    {"on": "Lie at the threshold of Zeus, full of lots, one of good, the other of evil lots", "text": "Plato quotes Achilles' consolation to Priam, the parable of the two urns that you read in session 4, and condemns it. The very words that brought two enemies together are, for Plato, a lie about God."},
    {"on": "the violation of oaths and treaties, which was really the work of Pandarus, was brought about by Athene and Zeus", "text": "In Iliad IV the gods arrange for a Trojan to break a sworn truce, so that the war will continue. Plato says this cannot be true: a god who causes oath-breaking is no god."},
    {"on": "but that God being good is the author of evil to any one is to be strenuously denied", "text": "Plato's alternative: if God punishes, it is for the good of the punished. This is an early form of what later Christians would call theodicy, the defence of God's goodness in the face of evil."}
   ]),
  dict(PLATO, raw="rep3", idx=list(range(0, 23)), ref="Plato, Republic III.386a–387b", title="Do not fear the world below",
   context="Book III continues. The guardians must be brave, so they must not fear death. Socrates quotes, in verse, several of Homer's lines about Hades. The first is Achilles' words to Odysseus in the passage you have just read, in a different translation.",
   plain="Brave men must not fear death. But Homer describes the world of the dead as horrible, so we must cut out such passages: Achilles saying he would rather be a serf than rule the dead; Hades as a mindless place; souls flying off like smoke, or squeaking like bats. Not because they are bad poetry, but because the better the poetry, the more harm it does to men who should fear slavery more than death.",
   commentary=[
    {"on": "Can any man be courageous who has the fear of death in him?", "text": "Plato's argument is practical: a society needs brave defenders, and fear of death makes cowards. Homer's bleak Hades undermines the very courage his heroes display."},
    {"on": "I would rather be a serf on the land of a poor and portionless man than rule over all the dead who have come to nought.", "text": "The first line Plato wants to strike out is the one you have just read in Butler. He understood its power exactly. It says that nothing, not even glory, outweighs life, and so it makes men afraid to die."},
    {"on": "not because they are unpoetical, or unattractive to the popular ear, but because the greater the poetical charm of them, the less are they meet for the ears of boys and men who are meant to be free", "text": "A remarkable admission. Plato loved Homer, and says so elsewhere. He is not attacking bad poetry but great poetry, because great poetry shapes the soul most powerfully. The better Homer is, the more dangerous."}
   ]),
  dict(PLATO, raw="rep3", idx=list(range(23, 36)), ref="Plato, Republic III.388a–388e", title="Heroes must not weep",
   context="After another cut, Socrates turns to the heroes' grief. He describes Achilles' mourning for Patroclus in Iliad XVIII and XXIV, and quotes Priam rolling in the dirt (Iliad XXII, which you read in session 3), Thetis lamenting, and Zeus grieving for Hector and for his son Sarpedon.",
   plain="Homer should not show Achilles, a goddess's son, rolling about and pouring ashes on his head, or Priam begging in the dirt, or the gods weeping. Above all he should not show Zeus himself lamenting. If the young hear such things without laughing at them, they will think it fine for them to whine and lament at every small trouble.",
   commentary=[
    {"on": "Rolling in the dirt, calling each man loudly by his name.", "text": "Plato quotes the line about Priam on the walls of Troy, from the comparison in session 3. What Homer offered as the truth of grief, Plato sees as an unworthy example."},
    {"on": "O heavens! with my eyes verily I behold a dear friend of mine chased round and round the city, and my heart is sorrowful.", "text": "Zeus's words as he watches Achilles chase Hector round Troy. Plato's objection is double: a god should not grieve, and if he grieves, he should act. A Zeus who pities Hector and lets him die anyway is neither happy nor good."},
    {"on": "he will be always whining and lamenting on slight occasions", "text": "Here Plato's case is at its weakest for many modern readers, and its most revealing. He wants heroes who do not weep. Homer's greatness, and much of what moved you in sessions 3 and 4, lies in the weeping."}
   ])
 ]},
"lecture": {"sections": [
 {"h": "The charge from Homer's own mouth", "paras": [
  "The strongest witness against the heroic code is Achilles. In the Iliad he chose a short life and undying glory. In the Odyssey, dead, he says he would rather be a poor man's labourer than king of all the dead. The scholar Jasper Griffin and many others have read this as the Odyssey's deliberate answer to the Iliad: the poet of homecoming judging the poet of glory, and finding glory wanting.",
  "Think through what follows. If glory is worthless to the one who has it, then the whole bargain of the code collapses: risk your life, and you will be remembered. Remembered by whom, and for what, if you are a mindless shadow? Ajax's silence completes the picture. He died for honour, and in death he is still trapped in his wounded pride, unable to forgive. Homer's world offers the dead neither peace nor reconciliation. The best it can offer is a name, and Achilles has just told us what a name is worth."
 ], "key": "Achilles' ghost repudiates the glory he chose; Ajax remains trapped in wounded honour. The code's promise, a name that survives, is empty to those who have it."},
 {"h": "Xenophanes: gods made in our image", "paras": [
  "The philosophical attack on Homer began two centuries before Plato. Xenophanes of Colophon complained, in our own words, that Homer and Hesiod had attributed to the gods everything that is shameful among humans: theft, adultery and deceiving one another (fragment B11). He went further. Ethiopians, he said, make their gods dark-skinned and snub-nosed, and Thracians make theirs blue-eyed and red-haired; and if oxen and horses had hands, they would draw gods that looked like oxen and horses (B15–16). The gods of the poets, in other words, are human beings projected onto the sky.",
  "Against them, Xenophanes proposed one god, greatest among gods and men, unlike mortals in body or thought, who moves all things by the power of his mind without moving (B23–26). His contemporary Heraclitus said that Homer deserved to be thrown out of the poetry contests and beaten (B42). The Greeks' own thinkers, in other words, saw early that Homer's gods could not be the true divine."
 ], "key": "Xenophanes (c. 570–475 BC) said Homer's gods were human vices projected onto the sky, and proposed one god unlike us. Heraclitus wanted Homer flogged."},
 {"h": "Plato's case", "paras": [
  "Plato built these complaints into a system. In the Republic, Books II and III, he lays down rules for any true account of the divine. God is good, so he causes only good (379b–c). God is unchanging, so he does not disguise himself as strangers, as Homer's gods constantly do (381d). God is truthful, so he does not deceive, as Zeus does when he sends Agamemnon a lying dream (383a). And the poets must not make men fear death or admire heroes who weep and rage.",
  "In Book X Plato goes further still. He argues that poetry as such is an imitation of an imitation, far from truth, and that it feeds the emotions that reason should govern. Homer, 'the first of the tragedians', must be banished from the ideal city, though Plato admits his own love for him since childhood (595b, 607a). He calls this 'the ancient quarrel between philosophy and poetry' (607b), and invites anyone to defend poetry if they can. It is the first great argument in the West about whether art can be dangerous, and whether truth or beauty should rule."
 ], "key": "Plato's rules: God is good, unchanging and truthful; Homer's gods are none of these. In Republic X he banishes Homer, while admitting he loves him."},
 {"h": "Courage without mercy", "paras": [
  "Put the case together and it is formidable. Homer's world has courage, honour, loyalty, endurance and moments of piercing pity. But at the top of it are gods who are not good: they cheat, take sides, punish the innocent and watch human suffering like a game. Their favour goes to the strong and the clever, not the just. Zeus gives evil from his urn, and Achilles can only tell Priam to bear it.",
  "And the mercy is narrow. It happens once, in a tent, for one night, between two men who have both lost everything. It is a truce. The war resumes; Troy is burned; its women are enslaved; Hector's son is thrown from the walls. In the Odyssey, the hero's homecoming ends with a massacre and twelve women hanged. Glory, the highest good Homer knows, needs victims: there is no kleos without someone to kill. At its strongest, the charge is this: Homer saw the human condition with terrible clarity, and offered no remedy for it. His world has pity but no goodness at its source, and no hope beyond the grave."
 ], "key": "The full charge: Homer's gods are powerful but not good, his mercy is a one-night truce, his glory needs victims, and he offers no hope beyond the grave."},
 {"h": "The objection from the other side: Nietzsche", "paras": [
  "There is a second objection, aimed not at Homer but at those who criticise him. The German philosopher Friedrich Nietzsche (1844–1900), who began his career as a professor of Greek, admired the Homeric world precisely for what Plato and Christianity disliked. In an early essay, 'Homer's Contest' (1872), and later in On the Genealogy of Morality (1887), he argued, in our own words, that the Homeric nobles lived by a healthy morality of strength, pride, competition and self-affirmation, in which 'good' meant noble and powerful.",
  "Then, Nietzsche said, came a revolt of the weak, which reached its height in Christianity. It turned the values upside down: humility, meekness and pity became 'good', and pride and strength 'evil'. On this view the Christian reading of Homer is not an improvement but a loss: the replacement of a brave, tragic acceptance of life with a morality of resentment. If you have taken 'The Sermon on the Mount', you met a version of this charge there. Here it means that the case against Homer can be turned round into a case for him, and against the saint."
 ], "key": "Nietzsche praised the Homeric world's morality of strength and pride, and called Christianity's elevation of humility and pity a revolt of the weak: the case turned round."},
 {"h": "What the case does not prove", "paras": [
  "An objection at full strength should also be weighed honestly. The critics' best points stand: Homer's gods are not good, and his heroes' hope ends at the grave. But some of Plato's charges cut against what readers have valued most. He wanted heroes who never weep and a Zeus who never grieves. Most readers since have thought Homer's tears truer than Plato's calm, and Aristotle, Plato's own pupil, answered him in the Poetics: poetry may show things as they are said to be, or as they ought to be, and its pity and fear can purify rather than corrupt (Poetics 6, 25).",
  "So the objection leaves us with a real question rather than a verdict. If Homer's gods are not good, and his glory is hollow, what did his poems actually give the West that was worth keeping? That question is for the next and last session, which is still to come."
 ], "key": "The critics are right that Homer's gods are not good and his hope ends at the grave; but Aristotle defended poetry's truth, and Homer's tears have convinced more readers than Plato's calm."}
], "refs": [
 "Homer, Odyssey XI.204–208, 465–567 (Butler 1900); Iliad II.1–34 (Agamemnon's dream), IV.68–104 (Pandarus), XXIV.527–533 (the two urns).",
 "Plato, Republic II.377d–383c; III.386a–388e; X.595b, 606e–608a. Tr. Benjamin Jowett (1871; 3rd ed. 1888).",
 "Xenophanes, fragments B11, B15, B16, B23–26 (Diels–Kranz); Heraclitus, fragment B42. In J. H. Lesher, Xenophanes of Colophon (1992); G. S. Kirk, J. E. Raven and M. Schofield, The Presocratic Philosophers (2nd ed., 1983).",
 "Aristotle, Poetics 6 (catharsis) and 25 (answers to critics of Homer).",
 "Friedrich Nietzsche, 'Homer's Contest' (1872); On the Genealogy of Morality, First Essay (1887).",
 "Jasper Griffin, Homer on Life and Death (1980); Christopher Janaway, Images of Excellence: Plato's Critique of the Arts (1995)."
]},
"terms": ["Hades", "Shade", "Theology", "Censorship", "Allegory", "Theodicy", "Olympians"],
"debate": {"question": "Should Homer be taught?", "positions": [
 {"name": "No, or only in part: censor it", "who": "Plato, Republic II, III and X", "view": "Stories shape character, especially in the young. Homer's gods are liars and evildoers and his heroes are bad examples, and the greater his art the more harm he does. A just city would keep only the passages that show the gods as good and the heroes as brave and self-controlled.", "evidence": "The two urns; Pandarus' broken oath; Achilles' lament among the dead; Priam in the dirt; Zeus weeping for Hector."},
 {"name": "Yes: read it for its hidden meaning", "who": "Theagenes of Rhegium (c. 525 BC); the Stoics; the Neoplatonist Porphyry (3rd century AD)", "view": "Homer's stories are allegories. The battles of the gods are the conflicts of the elements or of virtues and vices; Athena is wisdom; the cave of the nymphs on Ithaca is the cosmos. Read rightly, Homer teaches truth.", "evidence": "Porphyry's essay On the Cave of the Nymphs, on Odyssey XIII; the Stoic readings of the gods as forces of nature."},
 {"name": "Yes: take the honey, leave the poison", "who": "Aristotle (Poetics); later, Christian teachers such as Basil of Caesarea (4th century), whom you will meet in Hall IV", "view": "Poetry shows human life as it is, and its pity and fear can purify the soul. A wise reader admires what is noble, such as courage, endurance and mercy, and passes over what is base, as a bee takes honey from flowers and leaves the rest.", "evidence": "Aristotle's answers to Homer's critics (Poetics 25); the long tradition of teaching Homer in Christian schools from late antiquity on."}
], "agree": "All three agree that Homer is the most powerful educator the Greeks had, that stories shape the soul, and that some of what he says about the gods cannot be true of the divine as such."},
"look": {"art": "bellini-titian-feast-of-the-gods", "why": "Giovanni Bellini painted The Feast of the Gods in 1514, and Titian later repainted its landscape. Its story comes from the Roman poet Ovid, not from Homer. It is here because it shows the gods of Greek and Roman myth as the poets imagined them, and as Plato objected to them: feasting, drinking and taking their ease.", "points": [
 "Six women, eight men, two satyrs and one child gather in pairs and trios in a loose row across the width of the painting.",
 "The two satyrs have men's torsos and furry goat's legs.",
 "The men wear loose robes in white, blue, green, coral and pink; the women wear long dresses, most of them slipping from one shoulder.",
 "On the rocky ground in front lie a wooden bucket, a glass goblet, a pitchfork, a blue and white dish of grapes and fruit, and an overturned cup.",
 "Craggy cliffs rise on the left and a grove of dark green trees on the right, under a vivid blue sky.",
 "A slip of paper on the bucket bears Bellini's signature and the date 1514."
]},
"music": {"id": "allegri-miserere", "why": "Allegri's Miserere sets Psalm 51, 'Have mercy on me, O God', a prayer to a God who is good and who forgives. It sounds the note that this session finds missing at the top of Homer's world."},
"think": {"library": "does-morality-need-god", "depth": 4, "why": "Plato said the gods must be good to be gods; Nietzsche said strength, not goodness, is the old and healthy morality. Read the modern debate on whether morality needs God."},
"learn": {"memory": "achilles-rather-be-a-slave", "why": "Achilles' verdict on glory, from among the dead: the objection to the heroic code in Homer's own words."},
"check": [
 {"q": "Odysseus tells Achilles' ghost that he was honoured in life and is a prince among the dead. Why does Achilles' answer matter so much for this journey?", "options": ["Because it shows that Achilles was a coward all along", "Because the greatest hero, who chose glory over a long life, now says glory is worth less than the lowest life on earth, so the code is judged by its own champion", "Because it proves that the Odyssey was written by a different poet", "Because Achilles is lying to Odysseus out of jealousy"], "answer": 1, "why": "Odysseus offers the code's consolation and Achilles rejects it. The objection comes from inside Homer, which makes it stronger."},
 {"q": "Achilles strides away happy when he hears his son is a great warrior. What is the best reading of this?", "options": ["It shows that Achilles has changed his mind again and now values glory for himself", "It shows that the code is not quite dead in him: glory is worthless to the dead man, but he still rejoices in it for his son", "It is a mistake in the text", "It shows that the dead feel nothing"], "answer": 1, "why": "Homer gives both: the repudiation and the lingering pride. The answer does not say he wants glory for himself, and the dead in Homer do feel grief and joy, faintly."},
 {"q": "What is Plato's first principle about God in Republic II?", "options": ["That God is the author of all things, good and evil alike", "That God is good, and therefore the cause only of good things, not of evil", "That there are many gods, all equal", "That the gods do not exist"], "answer": 1, "why": "'God, if he be good, is not the author of all things.' The first option is the view he rejects, and Homer's two urns express it."},
 {"q": "Why does Plato reject the defence that Homer's stories of the gods are allegories?", "options": ["Because he thinks allegory is always false", "Because the young cannot tell what is allegorical from what is literal, and what they hear first becomes part of them", "Because Homer said himself that they were literal", "Because allegories were illegal in Athens"], "answer": 1, "why": "Republic 378d: 'a young person cannot judge what is allegorical and what is literal'. He objects to their effect on the young, not to allegory as such."},
 {"q": "Plato wants to strike out the passages about weeping heroes and grieving gods. Which is the best objection to this part of his case?", "options": ["That Homer's heroes never weep", "That the weeping is where much of Homer's truth and power lie: the mercy in Achilles' hut comes from shared tears, and Aristotle argued that pity can purify the soul", "That Plato did not know Homer well", "That gods cannot feel anything"], "answer": 1, "why": "This is where Plato's case is weakest. Priam and Achilles weep together; Aristotle answered Plato in the Poetics. Plato knew Homer very well."},
 {"q": "Nietzsche's objection runs the opposite way to Plato's. What does it claim?", "options": ["That Homer's gods were too good", "That the Homeric nobles' morality of strength and pride was healthy, and that Christianity's elevation of humility and pity was a revolt of the weak", "That Homer was a Christian before Christ", "That Plato was right to censor Homer"], "answer": 1, "why": "For Nietzsche the Homeric world is the standard, and the saint is the decline. It turns the case against Homer into a case against Christianity."}
],
"tutorial": {"question": "'Homer's world has courage but no mercy beyond the tent.' Is this fair?", "approach": "State the case against at full strength, using Achilles' ghost, Ajax's silence, Xenophanes and Plato. Then test it against what you have read: the mercy of Iliad XXIV, Homer's pity for both sides, the justice of the Odyssey. Consider Nietzsche's opposite objection. Decide which parts of the charge stand, and which do not.",
 "strong": [
  "Uses Achilles' words among the dead and explains why they come from Homer himself.",
  "Explains Ajax's silence as honour beyond healing.",
  "Sets out Xenophanes' and Plato's charges accurately, with Plato's principle that God is good.",
  "Assesses the mercy in Iliad XXIV: real, but a one-night truce.",
  "Weighs Plato's weakest point, the objection to weeping, against Aristotle's reply.",
  "Considers Nietzsche's counter-charge fairly."
 ]},
"reading": [
 {"author": "Plato, tr. Desmond Lee", "title": "The Republic", "year": 1955, "level": "start", "why": "A clear modern translation; read Books II, III and X."},
 {"author": "Iris Murdoch", "title": "The Fire and the Sun: Why Plato Banished the Artists", "year": 1977, "level": "deeper", "why": "A novelist and philosopher on Plato's quarrel with poetry."},
 {"author": "Robert Lamberton", "title": "Homer the Theologian", "year": 1986, "level": "scholars", "why": "How ancient readers defended Homer by allegory."},
 {"author": "J. H. Lesher", "title": "Xenophanes of Colophon: Fragments", "year": 1992, "level": "scholars", "why": "The fragments, with translation and commentary."}
],
"practice": "Live it this week: notice one story you take in, a film, a series, a game or the news, and ask Plato's question of it: what does this teach me to admire? Write down one sentence of answer, and decide whether you want to be shaped by it.",
"reflect": "Plato wanted only good gods and heroes who never weep. Homer gave weeping heroes and gods who are not good. Which is nearer the truth about the world you know?",
"takeaways": [
 "Among the dead, Achilles says he would rather be a poor man's servant than king of the dead: the code is judged by its greatest hero.",
 "Xenophanes and Plato charged that Homer's gods are human vices writ large; Plato's first rule was that God is good, and so not the author of evil.",
 "The full charge is that Homer's world has courage and pity but no goodness at its source and no mercy beyond a one-night truce; Nietzsche turned it into a charge against Christianity."
]
}

S7 = {
"title": "Hero and saint: the verdict",
"line": "Odysseus wakes on his own island and does not know it; the goddess who loves him laughs at his lies. Augustine remembers weeping for a heroine at school. The verdict: what Homer gave the West, and what Christianity kept and turned upside down.",
"plain": "This last session gives the journey's answer. Homer gave the West its first picture of a great life: courage, honour, endurance, loyalty to home, and a glimpse of pity even for an enemy. The case against it is real: its gods are not good, and its glory ends at the grave. When Christianity met Homer, it did not throw him out. It kept the courage and the pity, and turned glory upside down: the greatest became the one who serves. We read Odysseus coming home, Augustine on learning Homer at school, and the prophet Jeremiah and Paul on what is worth glorying in.",
"why": "Session 6 put the case against Homer's world at full strength: gods who are not good, a glory Achilles himself rejected, mercy that lasts one night. That left a question: what did Homer give the West that was worth keeping, and what did the West do with it? This session answers, setting the hero beside the saint.",
"answers": [
 "So what did the Greeks think a great life was?",
 "Why is Homer still read?",
 "How did Christians read Homer?",
 "How is a Homeric hero different from a Christian saint?"
],
"finding": "Homer gave the West its first picture of greatness, courage, honour and home, and its first glimpse of pity; Christianity kept the courage and the pity and turned glory upside down, so that the greatest became the one who serves.",
"background": [
 {"h": "The verdict, first", "paras": [
  "Here is the answer to this journey's question, before the evidence for it. The Greeks of Homer thought a great life was one of aretē, excellence, shown in courage and skill; of timē, the honour others give you; and of kleos, the glory that outlives you in song. The Iliad tests that idea to breaking point and finds, in its last book, something greater: pity between enemies who share a mortal lot. The Odyssey offers a second picture: a great life is a faithful, enduring, clever life, lived among the people you love, at home.",
  "Homer's own poems, and the philosophers after him, exposed its limits: gods who are not good, glory that the dead despise, a mercy that is a truce. Christianity, when it met this world, kept its courage, its honesty, its pity and its love of home, and turned its idea of glory upside down. The rest of this session shows how."
 ], "key": "Homer: greatness is excellence, honour and glory, deepened by pity and the love of home. Christianity kept courage and pity and turned glory upside down."},
 {"h": "The case so far", "paras": [
  "The Iliad began with anger over honour (session 1). Achilles weighed glory against a long life (session 2), and at his triumph became inhuman (session 3). The poem ended in mercy between enemies, a truce and not forgiveness (session 4). Odysseus refused immortality for home (session 5). Homer's own Achilles, and then Plato, judged the code and the gods and found them wanting (session 6)."
 ], "key": "Anger, the choice of glory, its inhuman triumph, mercy in the tent, the choice of home, and the case against: six steps to a verdict."},
 {"h": "Odysseus home, and Augustine at school", "paras": [
  "The main reading returns to the Odyssey. The Phaeacians have sailed Odysseus home while he slept and left him on the shore of Ithaca with their gifts. Athena has wrapped the island in mist, so he does not recognise it. It is the moment the whole poem has been moving towards, and Homer turns it into a game of wits between the hero and his goddess. Some ancient readers made this passage the centre of their allegories: the Neoplatonist Porphyry wrote a whole essay on the cave of the nymphs it mentions.",
  "The comparison is from Augustine of Hippo (354–430). Born in Thagaste in North Africa, he was educated in the Roman schools in Latin literature, became a famous teacher of rhetoric in Carthage, Rome and Milan, and became a Christian in 386. He was bishop of Hippo, on the coast of modern Algeria, for over thirty years. Around 397–400 he wrote the Confessions, the story of his life addressed as a prayer to God. In Book I he remembers his schooldays, where boys learned Virgil, the Roman Homer, and Homer himself in Greek."
 ], "key": "Odysseus wakes on Ithaca in Athena's mist; Augustine, educated on Virgil and Homer, looks back on his schooling as a Christian bishop."},
 {"h": "Why we read these passages", "paras": [
  "The main reading, Odysseus' homecoming and his meeting with Athena, answers the question of what Homer's gods love in a man, and so what his world finally admires. The comparison has three short parts. Augustine answers the question of how a Christian who loved the classics judged them. Then two passages from the Bible, Jeremiah 9:23–24 and 2 Corinthians 12:9–10, answer the question of what Scripture thinks is worth glorying in, the very word at the heart of Homer."
 ], "key": "Odysseus and Athena show what Homer's gods admire; Augustine, Jeremiah and Paul show how the Bible's idea of glory differs."}
],
"before": [
 "Odysseus has just reached home. What does he do when the 'shepherd' tells him where he is?",
 "What does Athena admire in Odysseus? Is it his goodness?",
 "In the comparison, what does Augustine say he wept for, and what should he have wept for instead?"
],
"readWhy": "Odysseus wakes on Ithaca, lies to the goddess in disguise, and is welcomed by her laughter; then kisses his own soil.",
"read": [
 dict(OD, raw="od13", idx=[0, 1, 2, 3, 4, 5], ref="Homer, Odyssey XIII.187–286", title="A lying tale on his own shore",
  context="Ithaca, at dawn. The Phaeacians have left Odysseus asleep on the beach with all their gifts. Athena ('Minerva') has hidden the island in mist. Idomeneus was a king of Crete; the Phoenicians were the great traders of the Mediterranean; Pylos and Elis are on the Greek mainland.",
  plain="Odysseus wakes and does not know where he is. He fears he has been abandoned, counts his treasure, and weeps. Athena comes to him disguised as a young shepherd. He asks where he is, and she tells him: Ithaca. He is overjoyed, but instead of telling the truth he invents a long lie: that he is a Cretan on the run after killing a man.",
  commentary=[
   {"on": "among what manner of people am I fallen? Are they savage and uncivilised or hospitable and humane?", "text": "Odysseus asks the question he has asked on every shore of his voyage: will these people honour strangers? It is the Odyssey's test of a civilisation. Now he asks it of his own home, without knowing."},
   {"on": "Still, I suppose I must count my goods and see if the crew have gone off with any of them.", "text": "The first thing the hero does at home is count his treasure. Homer's heroes care about their goods; gifts are honour made visible, as you saw in session 1. It is also a little comic."},
   {"on": "the name of Ithaca is known even as far as Troy", "text": "Athena teases him. The name he has longed for through twenty years is the last word of her speech in the Greek. She holds it back to the end."},
   {"on": "he did not speak the truth, and made up a lying story in the instinctive wiliness of his heart", "text": "At the moment of homecoming, his reflex is to lie. It has kept him alive among Cyclopes and suitors; now it is part of him. Homer calls it instinctive: mētis has become his nature."},
   {"on": "I killed him because he wanted to rob me of the spoils I had got from Troy", "text": "The lie he invents is a story of honour and spoils: a quarrel over a prize, ending in murder. It is the Iliad's world, told as a lie. He presents himself as a dangerous man, a sensible thing to do on a strange shore."}
  ]),
 dict(OD, raw="od13", idx=[6, 7, 8, 9], ref="Homer, Odyssey XIII.287–360", title="The goddess and the liar",
  context="Athena reveals herself. Neptune (Poseidon) is angry with Odysseus for blinding his son, the Cyclops. Phorcys is an old sea god; the Naiads are water nymphs; Neritum is the island's mountain. Butler prints a square bracket ('[near it') where he thought the Greek text was doubtful; it is kept here as he printed it.",
  plain="Athena smiles and strokes him, and takes the form of a woman. She says it would take a master trickster to outdo him, and that they are a pair: he the best liar among men, she the cleverest among gods. She tells him he must bear insults silently at home. He reproaches her for abandoning him on his voyage; she says she never doubted he would get home. She clears the mist, and he sees Ithaca, kisses the ground and prays to the nymphs.",
  commentary=[
   {"on": "Minerva smiled and caressed him with her hand", "text": "The goddess's response to a lie is affection. She is delighted. Calypso smiled at him in the same way in session 5. Homer's divine women love Odysseus for his cleverness."},
   {"on": "for we can both of us deceive upon occasion—you are the most accomplished counsellor and orator among all mankind, while I for diplomacy and subtlety have no equal among the gods", "text": "This is the heart of the session. What does the goddess of wisdom love in her favourite? Not his goodness, his justice or his humility, but that he is the best deceiver among men, as she is among gods. Homer's heaven rewards excellence, and here excellence is cunning. Plato would say: a god who boasts of deceiving is no god."},
   {"on": "Bear everything, and put up with every man's insolence, without a word.", "text": "And yet the next thing she asks of him is humility: to bear insults in silence, disguised as a beggar in his own house. In the Odyssey, the hero must become the lowest before he can be restored. It is a hint of something the saint would take much further."},
   {"on": "from that day, Minerva, I saw no more of you, and cannot ever remember your coming to my ship to help me in a difficulty", "text": "Odysseus speaks for every believer who has felt abandoned: where were you? Athena's answer is not love but confidence: 'I was certain you would get back safely though you would lose all your men'. She did not want to quarrel with her uncle Poseidon. The gods' friendship is real, but it has its politics."},
   {"on": "Then Ulysses rejoiced at finding himself again in his own land, and kissed the bounteous soil", "text": "The homecoming at last: the hero kisses the ground. Of all the moments in Homer, this is perhaps the simplest and most human. The great life, in the Odyssey, ends here: on your own earth, among your own people, with the gods' blessing."}
  ])
],
"compare": {"title": "What is worth glorying in?", "why": "Homer's word for the highest good was glory. Read how a Christian who had learned Homer at school judged it, and two passages of the Bible that redefine glory itself.",
 "parts": [
  dict(AUG, raw="conf", idx=[0, 1, 2, 3, 4, 5], ref="Augustine, Confessions I.13–16", title="Weeping for Dido",
   context="Augustine, now a bishop, remembers his schooldays in North Africa around 365–370. Aeneas and Dido are the hero and the queen of Carthage in Virgil's Aeneid, the Roman epic modelled on Homer; Dido killed herself when Aeneas left her. Augustine speaks to God throughout. 'Fornication' is his strong word for loving the world in God's place. Pusey's text has no chapter numbers; the cuts are marked '…'. The last sentence's quotation ('These were Homer's fictions…') is from the Roman orator Cicero.",
   plain="Augustine asks why he hated learning Greek as a boy but loved Latin poetry. He learned to weep for Dido, who died for love, while not weeping for himself, dying without God's love. He found Homer bitter only because he was forced to learn him in a foreign language, under the cane; a free curiosity teaches better than fear. And he complains that the schools taught stories of Jupiter the thunderer and adulterer, so that crimes would seem divine.",
   commentary=[
    {"on": "I was forced to learn the wanderings of one Aeneas, forgetful of my own", "text": "Augustine's great insight about the epics. He studied a hero's wanderings and forgot that he was a wanderer too: a soul far from its true home. The Christian reading of the Odyssey, the soul's journey home to God, is in this one phrase."},
    {"on": "weeping the death of Dido for love to Aeneas, but weeping not his own death for want of love to Thee, O God", "text": "Augustine does not say the poems are worthless. He says they moved him deeply, to tears, but for the wrong things. The pity Homer and Virgil awakened was real; it was aimed at a story, while his own life was going wrong."},
    {"on": "For Homer also curiously wove the like fictions, and is most sweetly-vain", "text": "Augustine's verdict on Homer in four words: 'most sweetly-vain'. Sweet, because the poetry is beautiful; vain, because its stories are empty fictions. He loved and distrusted the classics at once, as Plato had."},
    {"on": "No doubt, then, that a free curiosity has more force in our learning these things, than a frightful enforcement.", "text": "An aside that every teacher should know. Augustine hated Homer only because he was beaten into learning him. Love of learning, he says, teaches better than fear."},
    {"on": "Did not I read in thee of Jove the thunderer and the adulterer? both, doubtless, he could not be", "text": "Augustine repeats Plato's charge, in a Christian voice: the supreme god of the poets cannot be both the just judge who thunders and an adulterer. Stories that make the gods immoral make immorality seem divine."}
   ]),
  {"bible": "Jeremiah 9:23-24", "title": "Let him who glories", "ref": "Jeremiah 9:23–24 (the Bible)",
   "context": "Jeremiah was a prophet in Jerusalem about 627–580 BC, a century or so after Homer, in the years before Babylon destroyed the city. Here God speaks through him about what a person may rightly boast of. 'Yahweh' is the personal name of Israel's God.",
   "commentary": [
    {"on": "Don’t let the mighty man glory in his might.", "text": "The Hebrew word for 'glory' here means to boast, to praise oneself. Jeremiah names the three things every ancient hero gloried in: wisdom, strength and riches: Odysseus' cunning, Achilles' might, the treasure of the spoils. All three are set aside."},
    {"on": "But let him who glories glory in this, that he has understanding, and knows me", "text": "The only glory left is knowing God. Glory is moved from what you are and do to whom you know."},
    {"on": "that I am Yahweh who exercises loving kindness, justice, and righteousness in the earth, for I delight in these things", "text": "And this God is defined by goodness: loving kindness, justice and righteousness. It is exactly what Plato said a true god must be, and what Homer's gods are not. Athena delights in deception; the God of Jeremiah delights in kindness."}
   ]},
  {"bible": "2 Corinthians 12:9-10", "title": "When I am weak, then am I strong", "ref": "2 Corinthians 12:9–10 (the Bible)",
   "context": "Paul, the early Christian missionary, writing to the church in Corinth, a Greek city, in the mid-50s AD. Rivals there had boasted of their credentials and visions, and Paul answers with a mock boast. He has prayed to be freed of some suffering he calls 'a thorn in the flesh', and Christ has answered him.",
   "commentary": [
    {"on": "My grace is sufficient for you, for my power is made perfect in weakness.", "text": "Here the Homeric order is turned upside down. In Homer, power is shown in strength and victory. Here God's power is shown in weakness: in Christ crucified, and in a suffering apostle. Paul writes this to Greeks, who knew their Homer."},
    {"on": "Most gladly therefore I will rather glory in my weaknesses", "text": "Paul uses the very word, glory, and attaches it to the opposite of what a hero boasts of. A Homeric hero would never boast of weakness, injury or persecution. Paul does."},
    {"on": "For when I am weak, then am I strong.", "text": "Five words that sum up the change. The saint's greatness is not the hero's. It does not deny courage: Paul's life was full of danger. But it locates strength in dependence on God rather than in oneself, and glory in service rather than in fame."}
   ]}
 ]},
"lecture": {"sections": [
 {"h": "Athena loves a liar", "paras": [
  "The main reading shows, very clearly, what Homer's gods admire. Athena, the goddess of wisdom, loves Odysseus not because he is good, but because he is the best liar and schemer among men, as she is among gods. She delights in his deceit. That is not a flaw in the story; it is the Homeric idea of excellence. Aretē is being outstanding at what you do, and the gods love the outstanding: the strongest, the cleverest, the most beautiful.",
  "Notice what follows. In such a world, there is no reason for the gods to love the weak, the poor or the plain, except as they happen to favour someone. Priam is pitied, but Troy is destroyed. The suitors are punished, but so are the maids. Compare Jeremiah: the God of Israel delights in loving kindness, justice and righteousness. The difference between the two heavens is the difference between two ideas of greatness."
 ], "key": "Athena loves Odysseus for his cunning, not his goodness: Homer's gods love excellence. Jeremiah's God delights in kindness and justice."},
 {"h": "Why Homer is still read", "paras": [
  "For the Greeks Homer was the schoolbook: boys learned him by heart, and Plato called him the educator of Greece. Alexander the Great, by Plutarch's account, slept with the Iliad under his pillow. The scholars of Alexandria in the 200s and 100s BC edited the text we read and divided each poem into twenty-four books. In the Greek East, in Byzantium, Homer was never lost: the 12th-century bishop Eustathius of Thessalonica wrote a vast commentary on both poems.",
  "In the Latin West Homer was almost forgotten for a thousand years. Dante, around 1310, put him first among the poets in Limbo (Inferno IV), but could not read him. Petrarch was given a Greek manuscript of Homer in 1354 and wept that he could not read it. The first printed Greek Homer came out in Florence in 1488. Then the translations came: George Chapman's (1598–1616), which inspired Keats's sonnet 'On First Looking into Chapman's Homer' (1816), Alexander Pope's (1715–26), and many more. Homer has been read for nearly three thousand years because he saw human beings whole: their rage and their tenderness, their courage and their grief, under a sky that does not care."
 ], "key": "Homer was the Greeks' schoolbook, never lost in Byzantium, rediscovered in the West after 1354, and read for nearly three thousand years for his whole view of human life."},
 {"h": "How Christians read Homer", "paras": [
  "The first Christians lived in a world where everyone educated had learned Homer. They had to decide what to do with him. Some, like the Latin writer Tertullian (around 200), asked what Athens had to do with Jerusalem. Jerome (around 347–420) dreamed in 384 that he was accused before Christ's judgement seat of being 'a Ciceronian, not a Christian' for loving the classics too much (Letter 22.30). Augustine, as you have read, wept for Dido and called Homer 'sweetly-vain'.",
  "But most did not throw the classics away. Clement of Alexandria (around 200) read Odysseus tied to the mast as he sailed past the Sirens as a picture of the Christian bound to the cross, sailing safely past the world's temptations (Exhortation to the Greeks 12). Basil of Caesarea, in the 4th century, wrote an address to young men on how to read the Greek poets, which you will meet in Hall IV. The pattern that won was Augustine's and Basil's: read the classics, admire their beauty, take what is true and good, and judge the rest by Christ. That is why Homer was still taught in Christian schools in every century after."
 ], "key": "Some Christians feared the classics (Tertullian, Jerome's dream); most kept them, reading Odysseus at the mast as the Christian at the cross and taking what was true and good."},
 {"h": "Hero and saint", "paras": [
  "Put the Homeric hero beside the Christian saint and the differences are plain. Both are brave. Both endure. Both can be moved by pity. But they differ about almost everything else: where a person's worth comes from, what to do with enemies, what death is, and what glory means. The table sets them side by side. It is a picture of two ideals, not of how every Greek or every Christian actually lived."
 ], "table": {"cols": ["", "The Homeric hero", "The Christian saint"], "rows": [
  ["Greatness is", "Excellence (aretē): strength, skill, cunning, beauty", "Holiness: love of God and neighbour"],
  ["Worth comes from", "Honour (timē) others give you", "God, who made and loves every person"],
  ["Glory is", "Kleos: your name sung after death", "God's glory; 'your names are written in heaven' (Luke 10:20)"],
  ["Weakness is", "Shame, to be hidden", "Where God's power is made perfect (2 Corinthians 12:9)"],
  ["Enemies", "To be killed, or pitied for a night", "To be loved and prayed for (Matthew 5:44)"],
  ["Death", "The end of all that matters; a shadow life in Hades", "Not the end; the hope of resurrection"],
  ["The gods", "Powerful, partial, not always good", "One God, perfectly good, who became a servant"]
 ], "note": "Homer's two poems already point towards some saintly qualities: pity in Iliad XXIV, faithfulness and endurance in the Odyssey."}, "key": "Hero and saint share courage, endurance and pity, but differ on worth, glory, weakness, enemies, death and God."},
 {"h": "What Christianity kept", "paras": [
  "It is easy to stress only the contrast. Christianity kept a great deal of Homer. It kept courage: the martyrs were praised as athletes and soldiers, and Paul told Christians to put on armour (Ephesians 6). It kept endurance: Odysseus, 'much-enduring', became a figure of the Christian life as a voyage home through trials, as Augustine saw when he wrote of 'my own' wanderings. It kept pity: Weil thought the Gospels were the last and greatest expression of the Greek genius for seeing the suffering of others.",
  "It kept the love of a particular home and a particular person, which the Odyssey had shown in Penelope and the bed. And it kept Homer's honesty about suffering. The Psalms and Job weep as frankly as Achilles. What it did not keep was the idea that glory belongs to the strong, and that the divine is merely powerful."
 ], "key": "Christianity kept Homer's courage, endurance, pity, love of home and honesty about suffering."},
 {"h": "Glory turned upside down", "paras": [
  "What Christianity changed was glory itself. In Homer, glory goes to the one who kills. In the Gospels, the one called 'the Lord of glory' is killed. Paul's hymn in Philippians 2 says that Christ, though in the form of God, did not consider equality with God 'a thing to be grasped' but 'emptied himself, taking the form of a servant' and was obedient 'to the point of death, yes, the death of the cross'. Achilles grasps glory with both hands. Christ lets it go.",
  "And the comparison passages put the turn in two sentences. Jeremiah: let no one glory in wisdom, strength or riches, but in knowing a God of kindness and justice. Paul: I will glory in my weaknesses, for when I am weak, then am I strong. Homer's Achilles, among the dead, said glory was worth less than a servant's life on earth. Christianity agreed that the hero's glory was hollow, and then said something Homer never imagined: that the true glory is a servant's. The West has lived with both ideals ever since, the hero and the saint, and much of its history is the argument between them."
 ], "key": "In Homer glory goes to the killer; in the Gospels the Lord of glory is killed. Christ 'emptied himself, taking the form of a servant': glory became a servant's."}
], "refs": [
 "Homer, Odyssey XIII.187–360 (Butler 1900); Porphyry, On the Cave of the Nymphs (3rd century AD).",
 "Augustine, Confessions I.13–16, tr. E. B. Pusey (1838); Cicero, Tusculan Disputations I.26.65; Jerome, Letter 22.30; Tertullian, Prescription against Heretics 7; Clement of Alexandria, Exhortation to the Greeks 12; Basil of Caesarea, Address to Young Men on Greek Literature.",
 "Jeremiah 9:23–24; 2 Corinthians 12:9–10; Philippians 2:6–8; Luke 10:20; Matthew 5:44; Ephesians 6:10–17; 1 Corinthians 2:8 (World English Bible).",
 "Plutarch, Life of Alexander 8; Dante, Inferno IV.86–88; Petrarch, letter to Nicholas Sigeros (1354); the Florence editio princeps of Homer (1488).",
 "George Chapman, Homer (1598–1616); Alexander Pope, Iliad (1715–20) and Odyssey (1725–26); John Keats, 'On First Looking into Chapman's Homer' (1816)."
]},
"terms": ["Aretē", "Kleos", "Mētis", "Saint", "Humility", "Allegory"],
"debate": {"question": "Did Christianity improve on Homer, or betray him?", "positions": [
 {"name": "It fulfilled him", "who": "Augustine; Simone Weil; many Christian humanists", "view": "Homer saw the human condition truly but had no remedy. His pity for both sides and his sense that glory is hollow reach towards something only the Gospel supplies: a God who is good, who suffers with us, and who makes the servant great. Christianity keeps what was best in Homer and completes it.", "evidence": "Achilles among the dead; Priam and Achilles weeping; Weil's view of the Gospels as heir of the Iliad; Philippians 2."},
 {"name": "It betrayed him", "who": "Friedrich Nietzsche; some modern humanists", "view": "Homer's world faced death and suffering bravely without consolation, and honoured strength, pride and excellence. Christianity replaced that tragic courage with a morality of humility and pity, born of weakness, and offered comforts that are not true.", "evidence": "Hector's 'some great thing'; the Homeric love of excellence; Nietzsche's Genealogy of Morality (1887)."},
 {"name": "Two ideals in tension", "who": "Many historians of the West; the poet John Milton (Paradise Lost IX, 1667)", "view": "The West inherited both the hero and the saint and never fully reconciled them. Its literature, from the medieval knight to Milton, who said he preferred to sing the 'better fortitude' of patience and martyrdom to the wars of epic, keeps trying to join courage and humility, glory and service.", "evidence": "Chivalry, which tried to make warriors Christian; Milton's opening to Book IX; the enduring popularity of both Homer and the Gospels."}
], "agree": "All agree that Christianity changed the meaning of glory decisively, and that the West carries both ideals, the Homeric and the Christian, to this day."},
"look": {"art": "claude-judgment-of-paris", "why": "Claude Lorrain painted The Judgment of Paris in 1645–46. It shows where, in the Greek story, the Trojan war began: a young man choosing between three goddesses. It is here because this whole journey has been about choices of what makes a life great.", "points": [
 "The figures are small, in the lower left of a vast landscape.",
 "A young man in red drapery, Paris, sits on a rock with a long staff and points at three women.",
 "The woman in the centre, in red and blue, stands beside a peacock with its tail fanned open: by tradition, the bird of Hera.",
 "A second woman holds a white cloth around her, with a winged child holding an arrow and a quiver beside her: by tradition, Aphrodite and Cupid.",
 "The third sits on a yellow-draped rock with a long lance and a metal helmet with a red feather beside her: by tradition, Athena's arms.",
 "Six sheep graze in the foreground; a waterfall and tall trees fill the left; water winds towards hazy purple mountains under a blue sky."
]},
"music": {"id": "for-all-the-saints", "why": "'For All the Saints' is a hymn to those who 'from their labours rest': a company of the faithful remembered not for their glory but for their faith. Hear it as the saint's answer to the hero's kleos."},
"think": {"library": "athens-and-jerusalem", "depth": 3, "why": "This journey began with Athens and Jerusalem in brief. Now read the great teachers who held the two together, and how they judged what to keep from the Greeks."},
"learn": {"memory": "odyssey-1-1", "why": "The first lines of the Odyssey: the man of many turns, trying to bring himself and his friends home. Augustine read his own life as such a voyage."},
"check": [
 {"q": "What does Athena admire most in Odysseus, according to the main reading?", "options": ["His justice as a king", "His faithfulness to Penelope", "That he is the most accomplished deceiver and counsellor among men, as she is among gods", "His piety towards the nymphs"], "answer": 2, "why": "'We can both of us deceive upon occasion': she loves his cunning. Athena praised his fatherly rule in Book V, but that is not what she admires here."},
 {"q": "Augustine says he wept for Dido but not for himself. What is his point about the classics?", "options": ["That the poems are worthless and should not be read", "That they move us deeply, but can direct our pity at stories while our own lives go wrong", "That Virgil was a better poet than Homer", "That boys should not be taught to read"], "answer": 1, "why": "He does not call the poems worthless: they moved him to tears. His complaint is that the tears were for the wrong thing."},
 {"q": "Jeremiah 9:23–24 sets aside glorying in wisdom, might and riches. Why is this so pointed after reading Homer?", "options": ["Because Jeremiah had read Homer", "Because those are exactly the things Homer's heroes gloried in, Odysseus' cunning, Achilles' might, the spoils, and Jeremiah puts glory instead in knowing a God of kindness and justice", "Because Jeremiah was against all learning", "Because Israel had no warriors"], "answer": 1, "why": "Jeremiah did not know Homer; but his three boasts match the hero's three. And his God delights in kindness, not cunning."},
 {"q": "What does Paul mean by 'when I am weak, then am I strong'?", "options": ["That weakness is good in itself", "That God's power is shown in weakness and dependence on him, so that glory lies in service rather than self", "That Christians should avoid danger", "That strength is an illusion"], "answer": 1, "why": "Paul's life was full of courage and danger; he does not praise weakness for its own sake but says God's power is 'made perfect in weakness'."},
 {"q": "Which of these did Christianity keep from Homer, according to the lecture?", "options": ["The belief that glory belongs to the strongest", "Courage, endurance, pity, love of home and honesty about suffering", "The worship of the Olympian gods", "The belief that death is the end"], "answer": 1, "why": "These were kept and transformed. The other three are what it rejected."},
 {"q": "What is the best summary of the journey's verdict?", "options": ["Homer was simply wrong and should be forgotten", "Homer gave the West its first picture of greatness, courage, honour and home, with a glimpse of pity; Christianity kept the courage and pity and turned glory upside down", "Christianity copied Homer exactly", "The Greeks thought a great life was a long and comfortable one"], "answer": 1, "why": "This is the finding. The last option is precisely what Achilles rejected in the Iliad."}
],
"tutorial": {"question": "How is a Homeric hero different from a Christian saint?", "approach": "Define the hero from the poems: aretē, timē, kleos, mētis, and the choices of Achilles and Odysseus. Define the saint from the comparison texts and Philippians 2. Use the table, but go beyond it: show what they share as well as how they differ. Bring in Augustine's double attitude and Nietzsche's objection. End with your own judgement: can a person be both?",
 "strong": [
  "Defines aretē, timē and kleos accurately, with examples from both poems.",
  "Uses Athena's love of Odysseus' cunning to show what Homer's gods admire.",
  "Uses Jeremiah 9 and 2 Corinthians 12 to show glory redefined.",
  "Notes what the two ideals share: courage, endurance, pity.",
  "Explains Augustine's love and distrust of the classics.",
  "Engages Nietzsche's view that the change was a loss."
 ]},
"reading": [
 {"author": "Bernard Knox", "title": "The Oldest Dead White European Males", "year": 1993, "level": "start", "why": "Short lectures on why the Greeks, Homer above all, still matter."},
 {"author": "Augustine, tr. Henry Chadwick", "title": "Confessions", "year": 1991, "level": "deeper", "why": "A clear modern translation; read Book I with what you have read here."},
 {"author": "Tom Holland", "title": "Dominion: The Making of the Western Mind", "year": 2019, "level": "deeper", "why": "A historian's account of how Christianity overturned ancient ideas of power and glory."},
 {"author": "Robert Lamberton", "title": "Homer the Theologian", "year": 1986, "level": "scholars", "why": "How pagan and Christian readers made Homer a teacher of truth."}
],
"practice": "Live it this week: do one piece of real service for someone that no one will praise: the task at work or at home that everyone avoids. Do it well, as Odysseus did his work, and quietly, as a servant does, and notice how it feels to do something great without kleos.",
"reflect": "Whose life do you most admire: someone strong and brilliant, or someone faithful and kind? What does your answer say about which ideal you live by?",
"takeaways": [
 "For Homer's Greeks a great life was excellence, honour and glory, deepened in the Iliad by pity and in the Odyssey by faithful love of home.",
 "Homer's gods love excellence, even cunning, not goodness; the critics, from Plato to Augustine, saw this clearly.",
 "Christianity kept Homer's courage, endurance and pity, and turned glory upside down: 'when I am weak, then am I strong'; the greatest is the servant."
]
}
