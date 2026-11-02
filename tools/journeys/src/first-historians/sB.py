from sA import HDT
HDT2 = dict(HDT, source="https://www.gutenberg.org/ebooks/2456", translator="G. C. Macaulay (1890; third edition 1914)")
THU = {"author": "Thucydides", "work": "History of the Peloponnesian War", "translator": "Richard Crawley (1874)", "source": "https://www.gutenberg.org/ebooks/7142", "kind": "philosophy", "who": "Thucydides (c. 460–c. 400 BC), an Athenian general exiled in 424 BC, who wrote the history of the war he lived through.", "when": "Written in exile and in Athens, c. 424–400 BC"}

S3 = {
"title": "Free men and a king",
"line": "The King of Kings weeps over his vast army, asks an exiled Spartan whether the Greeks will dare to fight, and is told: their master is the law. Then three hundred Spartans hold the pass.",
"plain": "In 480 BC Xerxes, king of Persia, led the largest army the world had seen into Greece. Herodotus tells how, before the battle, Xerxes asked a Greek exile at his court whether the Greeks would really fight. The answer was that they would, because they were free men who obeyed the law more than Persians feared their king. A few days later, at the narrow pass of Thermopylae, the Spartan king Leonidas and his men fought to the last. This session asks what Herodotus thought the war was about, and how far we can trust him.",
"why": "The last session showed Herodotus finding a pattern in history: pride before a fall, in the story of Croesus. Now that pattern meets its greatest example, the Persian king who tried to conquer Europe. But Herodotus adds something new: he sees the war as a contest between two ways of living, under a master or under the law. And because his story has become a legend, we must ask how much of it is true.",
"answers": [
 "What happened at Marathon, Thermopylae and Salamis?",
 "Why did the Greeks win against such odds?",
 "What did Herodotus mean by free men under law?",
 "Why is Herodotus called the 'father of lies', and is it fair?",
 "Is the story of 'East against West' true?"
],
"finding": "Herodotus made freedom the meaning of the war: at Thermopylae the Greeks fought as free men whose master was the law, not as slaves driven by a king. Archaeology confirms much of his account, though not his numbers.",
"background": [
 {"h": "The story so far", "paras": [
  "Croesus' fall, about 547 BC, put the Greek cities of the Turkish coast under Persian rule. In 499 BC they rebelled, and Athens sent twenty ships to help them. The revolt was crushed. King Darius sent an army to punish Athens, and in 490 BC, at Marathon, 26 miles from the city, the Athenians and their small neighbour Plataea beat it. Herodotus says 6,400 Persians died and 192 Athenians (VI.117).",
  "Darius died before he could try again. His son Xerxes spent four years preparing. In 480 BC he crossed from Asia into Europe over the Hellespont, the narrow strait by modern Gallipoli, on two bridges of boats, with an army and fleet drawn from every nation of the empire. Many Greek cities submitted. About thirty, led by Sparta and Athens, decided to fight."
 ], "key": "After Athens helped the Ionian revolt, Persia was beaten at Marathon (490 BC); in 480 BC Xerxes invaded with a vast army, and about thirty Greek cities resisted."},
 {"h": "Who are the people in this reading?", "paras": [
  "Xerxes (reigned 486–465 BC) was the King of Kings, ruler of perhaps a quarter of the world's people. Artabanus was his uncle, who had warned him against the invasion. Demaratus had been one of Sparta's two kings until he was deposed in about 491 BC, after a quarrel with his fellow king; he fled to Persia, and now marched with Xerxes as an adviser.",
  "Sparta was the strongest military power in Greece. Its citizens trained for war from the age of seven, and lived under strict laws said to come from an ancient lawgiver, Lycurgus. Their land was farmed by helots, a whole population of Greeks held in serfdom. Leonidas was one of Sparta's kings in 480 BC."
 ], "key": "Xerxes, the Persian king; Artabanus, his cautious uncle; Demaratus, a deposed Spartan king at his court; and Sparta, a city of soldiers whose land was worked by serfs."},
 {"h": "When and where", "paras": [
  "Thermopylae, the 'hot gates', named after its hot springs, was a narrow pass between mountains and the sea in central Greece, the only good road south. There a small Greek force could hold back a huge army. At sea, the Greek fleet waited nearby at Artemisium."
 ], "timeline": [
  {"year": "499–494 BC", "text": "The Ionian revolt; Athens sends ships"},
  {"year": "490 BC", "text": "Marathon: Athens beats Darius' army"},
  {"year": "486 BC", "text": "Xerxes becomes king"},
  {"year": "480 BC (spring)", "text": "Xerxes crosses the Hellespont at Abydos"},
  {"year": "480 BC (August or September)", "text": "Thermopylae and the sea battle of Artemisium; Athens is burned"},
  {"year": "480 BC (September)", "text": "The Greek fleet wins at Salamis"},
  {"year": "479 BC", "text": "The Greeks win at Plataea and Mycale"}
 ], "key": "In 480 BC Xerxes crossed into Europe, broke through at Thermopylae and burned Athens, then lost at Salamis; in 479 BC the invasion ended."},
 {"h": "Why we read these passages", "paras": [
  "The main reading has two scenes from Book VII. At Abydos, on the Asian shore of the Hellespont, Xerxes looks over his army, calls himself happy, and weeps. Then, in Thrace, he asks Demaratus whether the Greeks will really fight. Demaratus' answer is Herodotus' clearest statement of what the war meant.",
  "The comparison is Herodotus' account of the last day at Thermopylae, and the epitaphs on the Spartans' graves. It shows whether Demaratus was right."
 ], "key": "Xerxes weeping at Abydos and his conversation with Demaratus; then the last stand at Thermopylae."}
],
"before": [
 "Why does Xerxes weep, and what does Artabanus reply? Does it remind you of Solon?",
 "What two things does Demaratus say the Greeks have instead of wealth?",
 "Why does Xerxes think free men will not fight, and what is Demaratus' answer?"
],
"readWhy": "Two scenes before the battle: the King of Kings weeps over his army, and an exiled Spartan tells him what free men will do.",
"read": [
 dict(HDT2, raw="hdt-abydos", idx=[0, 1, 2], ref="Herodotus, Histories VII.44–46", title="The king weeps",
  context="Spring 480 BC. Xerxes has marched across Asia and reached Abydos, on the Asian side of the Hellespont, where his engineers have built two bridges of boats into Europe. The people of Abydos have built him a throne of white marble on a hill. Below him are his army and fleet. Footnote numbers in Macaulay's edition have been removed.",
  plain="Xerxes sits on a marble throne and watches his army and fleet fill the shore and the sea. He calls himself happy, and then weeps. His uncle Artabanus asks why. Xerxes says that in a hundred years not one of all these men will be alive. Artabanus answers that there is something worse: life is so full of trouble that every man has wished at some time to be dead, and the divine is jealous of us.",
  commentary=[
   {"on": "then Xerxes pronounced himself a happy man, and after that he fell to weeping", "text": "Herodotus' readers would have heard Croesus behind these words. The greatest king on earth calls himself happy at the height of his power, exactly as Croesus did in the treasury. We know what follows."},
   {"on": "how brief was the whole life of man, seeing that of these multitudes not one will be alive when a hundred years have gone by", "text": "It is a moving moment, and it makes Xerxes human. He is not a monster. He sees, for a moment, what Solon saw: that no power lasts. But he does not change course."},
   {"on": "God, having given him to taste of the sweetness of life, is discovered in this matter to be full of jealousy", "text": "Artabanus repeats Solon's theology of the 'envious' divine. In Herodotus, the wise warners all say the same thing, and the great kings never listen."}
  ]),
 dict(HDT2, raw="hdt-demaratos", idx=[0, 1], ref="Herodotus, Histories VII.101–102", title="Will they fight?",
  context="Xerxes has crossed into Europe and reviewed his forces at Doriscus in Thrace (north-eastern Greece). He sends for Demaratus, the exiled king of Sparta who has lived at the Persian court for about ten years. 'Hellas' is Greece; 'Lacedemonians' are the Spartans.",
  plain="Xerxes asks Demaratus whether the Greeks will dare to fight him, when even all the peoples of the West together could not stand against his army. Demaratus asks whether he wants the truth or flattery. Told to speak the truth, he says: Greece has always been poor, but it has courage, learned through wisdom and law. The Spartans will never accept slavery, and they will fight however few they are.",
  commentary=[
   {"on": "O king, shall I utter the truth in speaking to thee, or that which will give pleasure?", "text": "The same question Solon faced in Croesus' treasury. In Herodotus, the man who tells a king the truth is always worth listening to."},
   {"on": "with Hellas poverty is ever an inbred growth, while valour is one that has been brought in, being acquired by intelligence and the force of law", "text": "Here is Herodotus' explanation of how the Greeks could win. They were poor, but their courage was learned, made by good sense and by law. Courage is not something a people is born with; it is something its laws and customs teach."},
   {"on": "it is not possible that they will ever accept thy terms, which carry with them servitude for Hellas", "text": "For Demaratus, as for Herodotus, the war is about freedom. To accept Xerxes' terms, earth and water as a sign of submission, would be to become the king's slaves."},
   {"on": "whether it chances that a thousand of them have come out into the field, these will fight with thee", "text": "Numbers do not matter. This is the prediction that Thermopylae will test."}
  ]),
 dict(HDT2, raw="hdt-demaratos", idx=[2, 3], ref="Herodotus, Histories VII.103–104", title="Law as a master",
  context="Xerxes laughs at Demaratus and argues back. His argument is the core of the scene: how can men who are free, with no one to command them, stand against an army driven by one man's will?",
  plain="Xerxes laughs. How can a few thousand free men, with no one ruling them, fight so huge an army? Under one master they might fight from fear, or under the whip; free, they will do neither. Demaratus answers: the Spartans are free, but not free in everything, because they have a master, the law, whom they fear more than Persians fear their king. The law commands them never to run, but to stand and win or die.",
  commentary=[
   {"on": "at least if they were all equally free and were not ruled by one man", "text": "Xerxes speaks for a whole view of power. Men fight only if someone makes them. Freedom means no one is in charge, so free men will run. To an absolute ruler, it is obvious."},
   {"on": "they might go compelled by the lash to fight with greater numbers", "text": "This is not Greek propaganda only. Persian commanders did drive men forward with whips; Herodotus describes it at Thermopylae itself (VII.223), in the comparison reading."},
   {"on": "for though free, yet they are not free in all things, for over them is set Law as a master", "text": "This sentence is the heart of the session. Freedom, for Demaratus, is not having no master. It is having the right master: a law that everyone, king included, obeys. The Greek word is nomos, law or custom. The Persians obey a man; the Greeks obey a law."},
   {"on": "whom they fear much more even than thy people fear thee", "text": "Fear has not disappeared. It has changed its object. The Spartans fear disgrace before the law more than death. Xerxes' soldiers fear Xerxes."},
   {"on": "he bids them not flee out of battle from any multitude of men, but stay in their post and win the victory or lose their life", "text": "The law gives one command, and Thermopylae will show them keeping it."}
  ])
],
"compare": {"title": "The last stand", "why": "Was Demaratus right? Read Herodotus' account of the last day at Thermopylae, and the words carved on the graves.",
 "parts": [
  dict(HDT2, raw="hdt-thermopylae", idx=[0, 1, 2], ref="Herodotus, Histories VII.223–225", title="The last day",
   context="For two days the Greeks held the pass. Then a local man, Ephialtes ('Epialtes' in Macaulay), showed the Persians a mountain path round behind them. Leonidas sent most of the Greek army away and stayed with his 300 Spartans, about 700 men of Thespiae and 400 Thebans. Herodotus says the Thebans were kept against their will and later surrendered. The 'Medes' are the Persians.",
   plain="On the last morning the Greeks, knowing they would die, advanced into the open and killed many Persians, whose officers drove them on with whips. Leonidas fell; the Spartans fought over his body and drove the Persians back four times. When the Persians who had come round the mountain arrived, the Greeks withdrew to a small hill and fought with daggers, hands and teeth until they were overwhelmed.",
   commentary=[
    {"on": "the leaders of the divisions with scourges in their hands were striking each man, ever urging them on to the front", "text": "Herodotus makes Xerxes' words come true in the opposite way. The Persians are driven 'by the lash'; the Greeks go forward of their own will."},
    {"on": "of whose names I was informed as of men who had proved themselves worthy, and indeed I was told also the names of all the three hundred", "text": "This is Herodotus the historian at work: he went and found out the names. In his day, a list of the 300 was kept at Sparta, and the Greek traveller Pausanias saw it there in the second century AD (Description of Greece III.14.1)."},
    {"on": "they were overwhelmed by the missiles of the Barbarians", "text": "In 1939 the Greek archaeologist Spyridon Marinatos excavated the little hill, Kolonos, and found many Persian bronze arrowheads, as the account would lead us to expect."}
   ]),
  dict(HDT2, raw="hdt-thermopylae", idx=[3, 5, 6, 7, 8], ref="Herodotus, Histories VII.226, 228", title="Tell the Spartans",
   context="Herodotus records the sayings and the graves. The epitaphs were in verse; the one for the Spartans is often attributed to the poet Simonides, though Herodotus names him only for the seer Megistias. A 'myriad' is ten thousand, so 'three hundred myriads' is three million. Chapter 227, on the bravest men, has been left out.",
   plain="The Spartan Dienekes, told that the Persian arrows would hide the sun, said: good, then we shall fight in the shade. The dead were buried where they fell. One stone honoured all the Peloponnesians who fought. Another, for the Spartans, asked a passer-by to tell Sparta that they lay there, obedient to its laws.",
   commentary=[
    {"on": "the battle against them would be in the shade and not in the sun", "text": "A Spartan joke in the face of death. 'Laconic', meaning short and dry, comes from Laconia, the Spartans' country."},
    {"on": "Here once, facing in fight three hundred myriads of foemen", "text": "Three million is a poet's number, and it matches Herodotus' own impossible figure for Xerxes' forces, over five million men with their attendants (VII.186). Modern historians think the army may have been between about 100,000 and 300,000 men: still overwhelming."},
    {"on": "Stranger, report this word, we pray, to the Spartans, that lying Here in this spot we remain, faithfully keeping their laws.", "text": "The most famous epitaph in the world. Notice what it says: not 'we died for glory', nor 'we died for Sparta', but 'faithfully keeping their laws'. It is Demaratus' answer carved in stone. Their master was the law, and they obeyed it."}
   ])
 ]},
"lecture": {"sections": [
 {"h": "Three battles", "paras": [
  "The war of 480–479 BC turned on three battles. At Thermopylae the Greeks held the pass for three days and lost; the Persians marched south and burned Athens, whose people had fled to the island of Salamis. Then, in September 480 BC, the Athenian leader Themistocles lured the Persian fleet into the narrow strait between Salamis and the mainland, where its numbers were useless. The Greek ships, most of them Athenian, destroyed it while Xerxes watched from a throne on the shore. He went home.",
  "The next summer, at Plataea, a Greek army under the Spartan regent Pausanias destroyed the Persian land army that Xerxes had left behind, and on the same day, Herodotus says, a Greek force beat the Persians at Mycale on the Turkish coast. The invasion was over. Thermopylae was a defeat, but it became the symbol of the whole war."
 ], "table": {"cols": ["Battle", "Year", "What happened"], "rows": [
  ["Marathon", "490 BC", "Athenians and Plataeans beat Darius' army"],
  ["Thermopylae", "480 BC", "Leonidas holds the pass, then is destroyed"],
  ["Salamis", "480 BC", "The Greek fleet destroys the Persian fleet in a narrow strait"],
  ["Plataea", "479 BC", "A Greek army destroys the Persian land army"]
 ], "note": "Herodotus VI–IX."},
 "key": "Thermopylae was lost, Athens burned; Salamis (480 BC) and Plataea (479 BC) won the war."},
 {"h": "Freedom under law", "paras": [
  "Why did the Greeks win? Herodotus gives practical reasons: the narrow places at Thermopylae and Salamis, Themistocles' cunning, the Greek heavy infantry. But his deepest explanation is the one Demaratus gives. Free men fight for themselves; slaves fight because they are driven. Earlier, he says the same of Athens: once freed from its tyrants, it became the first of cities, 'when they were kept down they were wilfully slack, because they were working for a master, whereas when they had been set free each one was eager to achieve something for himself' (V.78).",
  "This is a new idea of freedom. It is not doing whatever you want. It is living under a law that you and your fellow citizens share, and that binds the powerful too. The Greeks called it isonomia, 'equality under the law'. It is close to what Israel's law said of its king, who must not think himself 'above his brothers' (Deuteronomy 17:20), which you may have read in 'Kings and prophets'. Two ancient peoples, in different ways, had come to the same thought: no one should be above the law."
 ], "key": "Herodotus' deepest explanation is freedom: men who obey a shared law, not a master, fight for themselves. The Greeks called it isonomia, equality under law."},
 {"h": "But not everyone was free", "paras": [
  "We must be honest about the limits of this freedom. Sparta's citizens were a few thousand men. Its land was worked by helots, Greeks held as serfs, whom the Spartans each year formally declared war on, so that killing them would not be a crime (Plutarch, Life of Lycurgus 28). Athens, the city of democracy, had tens of thousands of slaves. Women had no vote anywhere. 'Free Greeks against slave Persians' was a proud simplification.",
  "The historian Paul Cartledge, in Thermopylae (2006), argues that the battle really was a turning point in the history of freedom, and also that Sparta was, in its own way, one of the least free societies in Greece. Both are true. The Greeks had found an idea larger than their own practice. It would take more than two thousand years, and much help from the Christian conviction that every person bears God's image, before the West began to apply it to everyone."
 ], "key": "Greek freedom was for citizen men only: Sparta rested on serfs and Athens on slaves. The idea was larger than the practice."},
 {"h": "The father of lies?", "paras": [
  "Herodotus was attacked even in antiquity. Thucydides, as we will see in the next session, quietly criticised writers who prefer a good story to the truth. Ctesias, a Greek doctor at the Persian court around 400 BC, said Herodotus lied about Persia. Plutarch wrote a whole essay, On the Malice of Herodotus, accusing him of bias. Later readers turned Cicero's compliment around and called him 'the father of lies'.",
  "In 1971 the German scholar Detlev Fehling went further: he argued that Herodotus invented most of his sources, and that his 'the Egyptians say' is a literary device. Others, such as W. Kendrick Pritchett in The Liar School of Herodotus (1993), replied that where Herodotus can be checked, he is usually describing real places and real reports. Most scholars now take a middle view: Herodotus reports honestly what he was told, and often says so; what he was told was sometimes wrong."
 ], "key": "Critics from Ctesias to Fehling have called Herodotus a liar; most scholars now think he honestly reports what he was told, which was sometimes wrong."},
 {"h": "What the evidence says", "paras": [
  "Where we can test Herodotus, he often does well. The burial mound of the Athenians at Marathon still stands. At Thermopylae, Marinatos found the arrowheads on the hill. The bronze Serpent Column, which the Greeks dedicated at Delphi after Plataea (Herodotus IX.81), now stands in the Hippodrome in Istanbul, and lists the cities that fought, much as Herodotus does. Darius' own inscription at Behistun in Iran names the six nobles who helped him seize the throne; five of the names match Herodotus' list (III.70). Herodotus' description of Scythian royal burials (IV.71–72) matches tombs excavated on the steppe.",
  "Where he fails, it is usually with numbers, distant lands and the inner thoughts of kings. Five million people could not have crossed the Hellespont or been fed. The speeches of Xerxes and Demaratus are not recordings: Herodotus was a child in 480 BC and was not in Thrace. They are what he believed such men would have said, shaped to show what the war meant."
 ], "key": "Archaeology confirms much of Herodotus (Marathon, Thermopylae, the Serpent Column, Behistun); his numbers and his speeches are not to be taken literally."},
 {"h": "East against West?", "paras": [
  "Herodotus' story has been used ever since as the founding myth of 'the West' against 'the East'. The philosopher John Stuart Mill wrote in 1846 that the battle of Marathon was more important to English history than the battle of Hastings. In the 20th century, the critic Edward Said (Orientalism, 1978) argued that this picture of a free, rational West and a despotic, luxurious East had long served to justify Western empires.",
  "Historians of Persia, such as Pierre Briant, have shown how much the Greeks missed: an empire that tolerated local religions, let the Jews rebuild their Temple, and governed vast lands with roads and law. Yet Herodotus himself is not the problem. He admires Persian courage, honesty and customs, tells us Persian boys are taught 'in three things only, in riding, in shooting, and in speaking the truth' (I.136), and lets Persians state the case against the Greeks on his first page. The simplification belongs to his later readers more than to him."
 ], "key": "Herodotus became the founding story of 'West against East'; critics like Said and historians like Briant show what it missed, but Herodotus himself was fairer to Persia than his later readers."},
 {"h": "A free people delivered", "paras": [
  "One more comparison. If you have taken 'Exodus and the law', you have read how Israel, a people of slaves, crossed the sea while Pharaoh's army was drowned (Exodus 14). The two stories have been told side by side for centuries: a small people, a great empire, the sea, and freedom.",
  "The differences are as important as the likeness. In Herodotus, the Greeks free themselves, by courage, law and clever tactics; the gods help, but men win. In Exodus, the people do nothing but walk: 'Yahweh will fight for you, and you shall be still' (Exodus 14:14). And the freedom Israel receives is not mainly freedom from a foreign king but freedom to serve God under his law. Both stories put freedom under law. They disagree about whose law, and who sets people free."
 ], "key": "Exodus and Thermopylae both tell of a small people's freedom against an empire; in Herodotus men free themselves, in Exodus God does."}
], "refs": [
 "Herodotus, Histories V.78, 97; VI.105–117; VII.35, 44–52, 101–105, 186, 201–228; VIII.40–96; IX.81, tr. G. C. Macaulay (1890, third edition 1914); I.136; III.70; IV.71–72.",
 "Plutarch, On the Malice of Herodotus; Life of Lycurgus 28; Pausanias, Description of Greece III.14.1. Ctesias, Persica (fragments).",
 "S. Marinatos, excavations at Thermopylae, 1939 (reported in Praktika of the Athens Archaeological Society); the Serpent Column, Hippodrome, Istanbul; Darius I, Behistun inscription §68.",
 "Paul Cartledge, Thermopylae: The Battle That Changed the World (2006); Tom Holland, Persian Fire (2005); Detlev Fehling, Herodotus and His 'Sources' (1971, tr. 1989); W. Kendrick Pritchett, The Liar School of Herodotus (1993).",
 "J. S. Mill, review of Grote's History of Greece, Edinburgh Review (1846); Edward Said, Orientalism (1978); Pierre Briant, From Cyrus to Alexander (2002); Exodus 14; Deuteronomy 17:20."
]},
"terms": ["Hoplite", "Helot", "Isonomia", "Nomos", "Myriad", "Hellespont"],
"debate": {"question": "Did the Persian Wars save the West?", "positions": [
 {"name": "Yes: freedom survived", "who": "J. S. Mill (1846); Tom Holland (Persian Fire, 2005); Paul Cartledge, with qualifications", "view": "Had Persia won, Athens would have become a province, and the democracy, drama, philosophy and history that grew there in the next century might never have happened. The idea of citizens living under a law they share survived because a few cities fought.", "evidence": "Athens' great age came after 479 BC; Herodotus V.78 on what freedom did for Athens; the Persians' practice of installing tyrants in Greek cities."},
 {"name": "No: a myth of East and West", "who": "Edward Said (Orientalism, 1978); historians of Persia such as Pierre Briant", "view": "Persia was a tolerant, well-governed empire, and Greek cities under it kept much of their life. The story of free West and slavish East was a Greek self-image, later used to justify Western domination. 'The West' did not exist in 480 BC.", "evidence": "Persian tolerance of local religions (the Cyrus Cylinder; Ezra 1); Greek cities that chose Persia; the later uses of Herodotus by European empires."},
 {"name": "Both: a real turning point, badly remembered", "who": "Many historians, including Cartledge", "view": "The Greek victory did matter: it let a rare kind of self-governing city survive. But the freedom it protected was for a few, and the 'clash of civilisations' was largely invented by later readers, not by Herodotus.", "evidence": "Herodotus' own fairness to Persia; the helots and slaves of the Greek cities; the long afterlife of the story."}
], "agree": "All agree that the Greeks won against heavy odds, that their victory let Athens flourish, and that Herodotus told it as a story of freedom under law."},
"look": {"art": None, "why": "No painting for this session: the gallery's open collection has no work showing Thermopylae, Xerxes or any battle of the Persian Wars, and we use no stand-in that pretends to be the subject.", "points": []},
"music": {"id": "faure-requiem", "why": "A requiem without terror, ending with angels leading the dead into paradise. Listen to it as music for the dead at Thermopylae, who 'remain' where they fell."},
"think": {"library": "the-individual", "depth": 2, "why": "Herodotus' free men under law are one root of the Western idea of the free person. See how the Bible added the rest."},
"learn": {"memory": "tell-the-spartans", "why": "Two lines on a grave that say what freedom under law costs: the most famous epitaph ever written."},
"check": [
 {"q": "Why does Xerxes think free men will not fight?", "options": ["Because the Greeks are too poor to buy weapons", "Because, in his view, men fight only when one master compels them by fear or the whip, and free men have no master", "Because the Spartans had already surrendered", "Because the gods favour Persia"], "answer": 1, "why": "'If they were all equally free and were not ruled by one man' ... 'compelled by the lash'. For an absolute ruler, freedom means no one is in charge."},
 {"q": "What is the best summary of Demaratus' reply?", "options": ["The Spartans have no master at all", "The Spartans fear Xerxes more than their own king", "The Spartans are free but have a master, the law, which they fear more than Persians fear their king", "The Spartans are better armed"], "answer": 2, "why": "'Though free, yet they are not free in all things, for over them is set Law as a master.' Freedom is obeying a shared law, not having no master."},
 {"q": "Why does the Spartan epitaph matter for Herodotus' argument?", "options": ["It proves the army was three million strong", "It says the Spartans died 'faithfully keeping their laws', which is Demaratus' claim carved in stone", "It was written by Xerxes", "It shows the Spartans died for glory alone"], "answer": 1, "why": "The epitaph names obedience to law as the reason they stayed, exactly as Demaratus said."},
 {"q": "Which is the fairest judgement on Herodotus' reliability?", "options": ["He invented all his sources", "Everything he says is confirmed by archaeology", "Much of his account is confirmed by archaeology, but his numbers are impossible and his speeches are not records of what was said", "He was reliable about Persia but not about Greece"], "answer": 2, "why": "Marathon, Thermopylae, the Serpent Column and Behistun confirm him; five million men and verbatim speeches do not survive scrutiny."},
 {"q": "What is the strongest objection to calling the war 'free men against slaves'?", "options": ["The Persians had no army", "Sparta rested on helot serfs and Athens on slaves, and only citizen men had political freedom", "The Greeks lost the war", "Herodotus disliked the Greeks"], "answer": 1, "why": "Greek freedom was real but narrow; the idea was larger than the practice."},
 {"q": "How does Exodus 14 differ most from Herodotus' account of the Greek victory?", "options": ["In Exodus there is no empire", "In Exodus the people are freed by God while they 'stand still'; in Herodotus men free themselves by courage and law", "In Exodus the people fight a great battle", "There is no difference"], "answer": 1, "why": "'Yahweh will fight for you, and you shall be still.' In Herodotus, men win."}
],
"tutorial": {"question": "'Over them is set Law as a master.' What did Herodotus think the Persian Wars were about, and was he right?", "approach": "Explain Xerxes' view of power and Demaratus' answer. Use Thermopylae and its epitaph. Then weigh the evidence for his account and the objections: the numbers, the speeches, the helots and slaves, the myth of East and West. End with your own view of what the war decided.",
 "strong": [
  "Explains freedom under law (nomos, isonomia) as Demaratus states it.",
  "Uses the Thermopylae account and epitaph as evidence for Herodotus' view.",
  "Weighs Herodotus' reliability with specific evidence for and against.",
  "Faces the limits of Greek freedom honestly.",
  "Discusses the 'East and West' critique fairly.",
  "Compares or contrasts Exodus 14 or Deuteronomy 17."
 ]},
"reading": [
 {"author": "Paul Cartledge", "title": "Thermopylae: The Battle That Changed the World", "year": 2006, "level": "start", "why": "Sparta, the battle and its long afterlife, by a leading historian of Greece."},
 {"author": "Tom Holland", "title": "Persian Fire", "year": 2005, "level": "start", "why": "The whole story of the Persian Wars, told from both sides."},
 {"author": "Pierre Briant", "title": "From Cyrus to Alexander: A History of the Persian Empire", "year": 2002, "level": "scholars", "why": "The Persian Empire on its own terms, from its own records."},
 {"author": "W. Kendrick Pritchett", "title": "The Liar School of Herodotus", "year": 1993, "level": "scholars", "why": "A reply to those who think Herodotus invented his sources."}
],
"practice": "Live it this week: choose one rule you have made for yourself (about money, food, speech or time) and keep it every day this week, especially when no one would know if you broke it. Notice what it does to you to obey a law you chose.",
"reflect": "Who, or what, is your master? Is it a law you would choose, or something that drives you?",
"takeaways": [
 "Xerxes believed men fight only when a master drives them; Demaratus answered that the Spartans' master was the law.",
 "Thermopylae and its epitaph made freedom under law the meaning of the war; archaeology confirms much of Herodotus' account, though not his numbers or his speeches.",
 "Greek freedom was for citizen men only, and the 'East against West' story is a later simplification; Herodotus himself was fair to Persia."
]
}

S4 = {
"title": "A possession for ever",
"line": "A disgraced Athenian general sets out to write the history of the war he is living through, and to tell the exact truth, so that it will be useful for ever.",
"plain": "Thucydides was an Athenian who fought in the great war between Athens and Sparta that began in 431 BC, and was exiled for losing a town. He used his exile to write its history. He wanted to do better than Herodotus and the poets: to test every report, to trust only what he or careful witnesses had seen, and to write something that would still be useful when the war was long forgotten. This session reads his own account of his method and asks what it means to tell the truth about the past.",
"why": "The first three sessions followed Herodotus, who listened to everyone and gave the meaning of events in stories, some of them too good to be true. Now the second founder of history answers him. Thucydides lived through the war he describes, and he set out to find the exact truth. To judge what he later says about power, we first need to know how he worked and how far to trust him.",
"answers": [
 "Who was Thucydides?",
 "What was the Peloponnesian War?",
 "How was Thucydides' method different from Herodotus'?",
 "Did he make up the speeches?",
 "What is the 'Thucydides Trap'?"
],
"finding": "Thucydides wanted the exact truth, tested against witnesses who disagreed, so that his work would be 'a possession for all time'; he also wrote speeches of what was 'demanded', and said so.",
"background": [
 {"h": "The story so far", "paras": [
  "After the Persians were driven out in 479 BC, the Greek cities split into two camps. Athens, with the strongest fleet, led a league of island and coastal cities, which it slowly turned into an empire: its 'allies' paid it tribute, and those who tried to leave were crushed. Sparta, with the strongest army, led the cities of the Peloponnese, the southern peninsula of Greece. Athens grew rich and confident: this was the age of the Parthenon, of the plays of Sophocles and of the statesman Pericles.",
  "In 431 BC the two camps went to war. The war lasted, with a break, for twenty-seven years, until Athens surrendered in 404 BC. It is called the Peloponnesian War, and its history was written by a man who fought in it."
 ], "key": "After 479 BC Athens built a naval empire and Sparta led the Peloponnese; in 431 BC they went to war for twenty-seven years."},
 {"h": "Who was Thucydides?", "paras": [
  "Thucydides, son of Olorus, was born an Athenian citizen around 460 BC, from a wealthy family with links to the gold mines of Thrace in northern Greece. He caught the great plague of 430 BC and survived (II.48). In 424 BC he was one of Athens' ten generals; he failed to save the city of Amphipolis from the Spartan general Brasidas, and the Athenians exiled him. He spent twenty years away, which, he says, let him talk to both sides (V.26).",
  "He began writing, he tells us, as soon as the war broke out, because he expected it to be the greatest war ever (I.1). He died around 400 BC, and his book stops in mid-sentence in 411 BC, seven years before the end. If you have taken 'How we got here' or 'Democracy and its dangers', you have already read his account of Pericles' funeral speech and of the Athenian assembly."
 ], "key": "Thucydides (c. 460–c. 400 BC), an Athenian general exiled in 424 BC, wrote the history of the war as it happened; it breaks off in 411 BC."},
 {"h": "When and where", "paras": [
  "Thucydides wrote only a generation after Herodotus. He almost certainly knew Herodotus' work, though he never names him. His history is in eight books, divided by later editors, and covers the war year by year, summer and winter."
 ], "timeline": [
  {"year": "478 BC", "text": "Athens founds its league against Persia"},
  {"year": "c. 460 BC", "text": "Thucydides is born"},
  {"year": "c. 430 BC", "text": "Herodotus' Histories are complete"},
  {"year": "431 BC", "text": "The Peloponnesian War begins"},
  {"year": "430 BC", "text": "Plague in Athens"},
  {"year": "424 BC", "text": "Thucydides loses Amphipolis and is exiled"},
  {"year": "416–413 BC", "text": "Melos; the expedition to Sicily"},
  {"year": "411 BC", "text": "Thucydides' history breaks off"},
  {"year": "404 BC", "text": "Athens surrenders"}
 ], "key": "Thucydides wrote a generation after Herodotus, about a war of 431–404 BC; his book stops in 411 BC."},
 {"h": "Why we read these passages", "paras": [
  "The main reading is the four chapters (I.20–23) in which Thucydides explains how he worked: why most people get the past wrong, how he wrote the speeches and the narrative, why his book will be useful, and what he thinks really caused the war.",
  "The comparison is two short statements by Herodotus about his own method. Read together, they show how the two founders of history disagreed, and what each of them got right."
 ], "key": "Thucydides' account of his method (I.20–23), then two sentences in which Herodotus describes his."}
],
"before": [
 "What does Thucydides say most people do with stories about the past?",
 "How does he say he wrote the speeches? How does he say he wrote the narrative?",
 "Who does he think his history will be useful to, and why?"
],
"readWhy": "Thucydides' own account of how to find the truth about the past, and why it matters.",
"read": [
 dict(THU, raw="thuc-method", idx=[0, 1], ref="Thucydides, History I.20–21", title="Most people do not check",
  context="Thucydides has just written a short history of early Greece, reasoning from what evidence there was. Now he explains why the common stories cannot be trusted. Hipparchus and Hippias were sons of Pisistratus, a tyrant of Athens; in 514 BC two young men, Harmodius and Aristogiton, killed Hipparchus, and Athenians honoured them with statues as the killers of the tyrant. Thucydides says they got the story wrong. 'Lacedaemonian' means Spartan. This is Richard Crawley's translation of 1874.",
  plain="Thucydides says: most people accept the stories they are told, even about their own city, without testing them. The Athenians think Harmodius and Aristogiton killed the tyrant, but the tyrant was actually his brother Hippias. Other Greeks believe false things even about the present. Poets exaggerate and storytellers prefer to please their audience. I have gone by the clearest evidence, and this war, when you look at the facts, was the greatest ever.",
  commentary=[
   {"on": "The way that most men deal with traditions, even traditions of their own country, is to receive them all alike as they are delivered, without applying any critical test whatever.", "text": "This sentence is the beginning of critical history. Do not believe a story because it is old, or because it is your own people's. Test it."},
   {"on": "The general Athenian public fancy that Hipparchus was tyrant when he fell by the hands of Harmodius and Aristogiton", "text": "He chooses a hard example: Athens' favourite story about its own freedom. The statues of the 'tyrant-slayers' stood in the market place. Thucydides says, in effect, your heroes killed the wrong man, for a private quarrel. It takes courage to correct a nation's myth."},
   {"on": "So little pains do the vulgar take in the investigation of truth, accepting readily the first story that comes to hand.", "text": "'The vulgar' means ordinary people, not rude people. The fault he names is laziness: taking the first story you hear. In an age of instant news, it has not gone away."},
   {"on": "the compositions of the chroniclers that are attractive at truth’s expense", "text": "Many scholars think he has Herodotus partly in mind: writers who tell a good story for an audience, at the cost of the truth. He never names him."}
  ]),
 dict(THU, raw="thuc-method", idx=[2, 3], ref="Thucydides, History I.22–23", title="A possession for all time",
  context="These are the most famous paragraphs Thucydides wrote, and among the most discussed in all ancient literature. He explains how he wrote the speeches, which fill about a quarter of his book, and the narrative of events. Then he says why the war was so terrible, and what really caused it. The 'Median War' is the Persian War of Herodotus; the 'thirty years' truce' was a peace made between Athens and Sparta in 446/5 BC.",
  plain="For the speeches, Thucydides says, I could not remember the exact words, so I have made the speakers say what the occasion required, keeping as close as possible to what they actually said. For the events, I did not trust the first report, or even my own impressions; I checked every account as strictly as I could, and found that eyewitnesses disagreed. My history has no romance, but it will be useful to anyone who wants to understand the past and so the future, because human nature does not change. It is not written to please for a moment but as a possession for all time. The war was greater and more terrible than any before. Its real cause was Athens' growing power and the fear it caused in Sparta.",
  commentary=[
   {"on": "so my habit has been to make the speakers say what was in my opinion demanded of them by the various occasions, of course adhering as closely as possible to the general sense of what they really said", "text": "An honest confession. The speeches are not recordings. Thucydides wrote them, keeping to 'the general sense' of what was said. Scholars have argued ever since about how much of each speech is the speaker and how much is Thucydides."},
   {"on": "I did not even trust my own impressions", "text": "This is stricter than Herodotus, who was happy to write 'I saw'. Thucydides distrusts even himself. Memory and first impressions, as modern psychology has confirmed, are often wrong."},
   {"on": "My conclusions have cost me some labour from the want of coincidence between accounts of the same occurrences by different eye-witnesses, arising sometimes from imperfect memory, sometimes from undue partiality for one side or the other.", "text": "He names the two great dangers in any witness: a bad memory and bias. Every judge, journalist and historian still works with these two."},
   {"on": "The absence of romance in my history will, I fear, detract somewhat from its interest", "text": "The Greek word is to muthodes, 'the story-like', from mythos. Thucydides gives up the pleasure of Herodotus' tales for the sake of the truth, and knows it will cost him readers."},
   {"on": "the interpretation of the future, which in the course of human things must resemble if it does not reflect it", "text": "Why study the past? Because human nature stays the same, so similar things will happen again. Thucydides' history is meant to be a tool for understanding.",
   },
   {"on": "not as an essay which is to win the applause of the moment, but as a possession for all time", "text": "The famous phrase. Herodotus probably read his work aloud to audiences who applauded. Thucydides writes for readers far in the future, and he was right: politicians and generals still read him."},
   {"on": "The growth of the power of Athens, and the alarm which this inspired in Lacedaemon, made war inevitable.", "text": "The first distinction in history between the stated reasons for a war and its 'real cause'. In 2017 the political scientist Graham Allison called the danger of a rising power frightening an established one 'the Thucydides Trap'."}
  ])
],
"compare": {"title": "Herodotus on his own method", "why": "Herodotus also explained how he worked, in passing. Read his two sentences, and compare them with Thucydides'.",
 "parts": [
  dict(HDT, raw="hdt-2-123", idx=[0], ref="Herodotus, Histories II.123", title="I write what is told",
   context="Book II is about Egypt, which Herodotus visited. He has just told an Egyptian story about a king who went down alive to the underworld and played dice with the goddess Demeter. The footnote number in Macaulay's edition has been removed.",
   plain="Anyone may believe these Egyptian stories who finds them believable. Throughout my history, I write what the people in each place told me.",
   commentary=[
    {"on": "any man may accept them to whom such things appear credible", "text": "Herodotus passes the judgement to his reader. He does not say the story is true; he says this is what the Egyptians say."},
    {"on": "I write by hearsay that which is reported by the people in each place", "text": "This is his method in one sentence: report faithfully what each people says about itself. It is a method of recording, more than of testing."}
   ]),
  dict(HDT2, raw="hdt-7-152", idx=[0], ref="Herodotus, Histories VII.152", title="Bound to report, not bound to believe",
   context="Herodotus is discussing an accusation that the city of Argos had betrayed Greece to Persia. He gives several versions and then states a rule for his whole book. The sentence continues with another version of the story, left out here.",
   plain="I must report what is said, but I do not have to believe all of it, and this rule applies to everything in my history.",
   commentary=[
    {"on": "I however am bound to report that which is reported, though I am not bound altogether to believe it", "text": "This is fairer to Herodotus than his critics allow. He does not claim everything he reports is true. He keeps the reports, as evidence of what people said, and keeps his own judgement separate."},
    {"on": "let this saying be considered to hold good as regards every narrative in the history", "text": "A reader who remembers this rule will read Herodotus very differently from one who takes every story as his own claim. The two historians disagree less about honesty than about what a history should contain."}
   ])
 ]},
"lecture": {"sections": [
 {"h": "The war in outline", "paras": [
  "Thucydides' war had three stages. In the first (431–421 BC), Sparta invaded Attica, the country round Athens, every summer, and Pericles' strategy was to bring the people inside the city walls and fight by sea. Plague struck the crowded city in 430 BC. The fighting ended in a peace named after the Athenian general Nicias (421 BC).",
  "In the second, Athens tried to extend its power: it destroyed the neutral island of Melos (416 BC) and sent a vast fleet to conquer Sicily (415–413 BC), which ended in disaster. In the third, Sparta, now with Persian money, fought on until it destroyed the last Athenian fleet at Aegospotami in 405 BC. Athens surrendered in 404 BC; its walls were pulled down to the music of flute girls, Xenophon says, and a group of pro-Spartan oligarchs, the 'Thirty Tyrants', took over for a year."
 ], "table": {"cols": ["Years", "Stage", "Key events"], "rows": [
  ["431–421 BC", "The Archidamian War", "Spartan invasions; plague; Pericles dies; Peace of Nicias"],
  ["421–413 BC", "The uneasy peace", "Melos destroyed; the Sicilian expedition fails"],
  ["413–404 BC", "The Ionian War", "Sparta builds a fleet with Persian money; Athens surrenders"]
 ], "note": "Thucydides covers 431–411 BC; Xenophon's Hellenica continues to 404 BC and beyond."},
 "key": "The war ran from 431 to 404 BC in three stages: Spartan invasions and plague, Athenian overreach at Melos and Sicily, and final defeat."},
 {"h": "Truth tested", "paras": [
  "Thucydides' method is close to what a modern historian, a journalist or a judge tries to do. He relies on eyewitnesses, including himself; he cross-examines them; he knows they disagree because memory fails and people take sides. He prefers the 'clearest data'. He uses documents where he has them, and copies some treaties word for word (for example, the treaty of 421 BC in V.18–19). He dates events precisely, by summers and winters, rather than by the years of local officials, which differed from city to city.",
  "He also leaves the gods out. In Herodotus, oracles and dreams explain events. Thucydides mentions oracles only to show how people twisted them to fit what had happened, as we will see in the next session. His causes are human: fear, honour and interest (I.76). This is why he is often called the first scientific historian. It is also why some readers find him cold."
 ], "key": "Thucydides relied on cross-examined eyewitnesses and documents, dated precisely, and left the gods out of his explanations: the first 'scientific' historian."},
 {"h": "The problem of the speeches", "paras": [
  "About a quarter of Thucydides' history is speeches: debates in the Athenian assembly, generals before battle, envoys arguing. They are among the greatest things in Greek, and they all sound like Thucydides: dense, abstract, full of argument. He tells us he wrote them himself, keeping to 'the general sense' of what was said.",
  "How much of each is real? Scholars disagree. Some, like the Cambridge scholar F. M. Cornford in Thucydides Mythistoricus (1907), argued that Thucydides shaped his whole history like a tragedy, and that the speeches carry his own ideas. Others think he kept close to real arguments, where he heard them or had good reports. The honest answer is that the speeches are Thucydides' reconstruction: the best evidence we have of the arguments people made, and also his analysis of what was at stake. We should read them as both."
 ], "key": "The speeches are Thucydides' reconstruction of what was said: evidence of the arguments, and also his own analysis."},
 {"h": "Was he fair?", "paras": [
  "Thucydides was a participant, an exile and a man with opinions. He admired Pericles and despised Cleon, the popular leader who followed him; Cleon may have been behind his exile. He hardly mentions economics, women or religion. He leaves out events we know from inscriptions, such as the sharp rise in the tribute Athens demanded from its allies in 425 BC.",
  "Virginia Hunter, in Thucydides the Artful Reporter (1973), argued that he arranges facts so skilfully that we accept his judgements without noticing. Simon Hornblower, whose commentary on Thucydides (1991–2008) is the standard one in English, finds him generally accurate but always shaping. That is the lesson of this session for every reader of history: the most careful historian is still choosing, and the more persuasive he is, the more we must ask what he left out."
 ], "key": "Thucydides is generally accurate but partisan and selective; the most careful historian still chooses, and we must ask what he left out."},
 {"h": "The real cause", "paras": [
  "Thucydides distinguishes the 'grounds alleged by either side' (a quarrel over Corcyra, a siege at Potidaea, a trade ban on Megara) from the 'real cause', which was 'the growth of the power of Athens, and the alarm which this inspired in Lacedaemon'. This is the first known distinction between the occasion of an event and its underlying cause, and every modern historian uses it.",
  "It also gives the second theme of this journey: what power does. In Thucydides, power grows by its own logic, and fear grows with it, until war seems inevitable. The American political scientist Graham Allison, in Destined for War (2017), studied sixteen cases in the last five hundred years when a rising power challenged a ruling one, and found that twelve ended in war. Critics say Thucydides himself thought choices mattered: the war was 'inevitable' only once both sides chose to see it that way. That argument is still being had about our own century."
 ], "key": "Thucydides separated the stated reasons for the war from its real cause, Athens' growth and Sparta's fear; Allison's 'Thucydides Trap' applies this to today."},
 {"h": "Why read him now?", "paras": [
  "Thucydides wrote 'a possession for all time' because he believed human nature does not change. Read the later chapters of his book and you meet propaganda, party hatred, the excuses of the powerful and the fear of the weak, and you will recognise them. The English philosopher Thomas Hobbes made the first English translation from the Greek in 1629, because he believed Thucydides taught what happens when people trust their passions in politics.",
  "There is a Christian reason to value him too. Christianity rests on claims about real events: a man crucified under Pontius Pilate, an empty tomb. It needs a way of testing what witnesses say. When Luke promised 'certainty', he was using the kind of language Thucydides had made respectable. The habit of asking 'how do we know?' is not the enemy of faith; it is what lets faith be more than a story."
 ], "key": "Thucydides believed human nature does not change, so the past can help us understand the future; his way of testing witnesses also matters for a faith that rests on events."}
], "refs": [
 "Thucydides, History I.1, 20–23, 76, 138; II.48; IV.104–107; V.18–19, 26, tr. Richard Crawley (1874), Gutenberg #7142.",
 "Herodotus, Histories II.123; VII.152, tr. G. C. Macaulay (1890, 1914).",
 "Xenophon, Hellenica II.2.23 (the walls pulled down); the Athenian tribute reassessment of 425 BC (Inscriptiones Graecae I³ 71).",
 "F. M. Cornford, Thucydides Mythistoricus (1907); Virginia Hunter, Thucydides the Artful Reporter (1973); Simon Hornblower, A Commentary on Thucydides (3 vols, 1991–2008) and Thucydides (1987).",
 "Thomas Hobbes, Eight Bookes of the Peloponnesian Warre (1629); Graham Allison, Destined for War: Can America and China Escape Thucydides's Trap? (2017); Donald Kagan, The Peloponnesian War (2003)."
]},
"terms": ["Peloponnesian War", "Eyewitness", "Speeches", "Tribute", "Thucydides Trap", "Romance"],
"debate": {"question": "Can we trust Thucydides?", "positions": [
 {"name": "Yes: the most careful historian of antiquity", "who": "Most historians of Greece; Donald Kagan, who built his four-volume history of the war on him", "view": "Thucydides was a participant who cross-examined witnesses, dated events precisely, copied documents and left the gods out. Where he can be checked against inscriptions, he usually holds up. We would know almost nothing of the war without him.", "evidence": "His own method (I.22); treaties copied verbatim; agreement with surviving inscriptions on many points."},
 {"name": "Only with care: an artful persuader", "who": "F. M. Cornford (1907); Virginia Hunter (1973)", "view": "Thucydides shaped his history like a tragedy and arranged his facts to lead the reader to his own judgements. The speeches are his. His silence about some things (the tribute rise of 425 BC, his own failure at Amphipolis) shows a partisan at work.", "evidence": "The tragic shape of the Melos and Sicily books; the uniform style of the speeches; omissions revealed by inscriptions."},
 {"name": "Both: accurate and shaping", "who": "Simon Hornblower; most modern commentators", "view": "Thucydides is usually right about what happened and always shaping how we see it. Read him as a great historian and a great writer at once, and check him where we can.", "evidence": "Hornblower's commentary, which tests him chapter by chapter."}
], "agree": "All agree that Thucydides is our main source for the war, that the speeches are his reconstructions, and that he set a new standard for testing evidence."},
"look": {"art": "moroni-titians-schoolmaster", "why": "No painting in the gallery shows Thucydides. This portrait by Giovanni Battista Moroni, about 1575, long known as 'Titian's Schoolmaster', shows a learned man in the act of reading: a scholar who has stopped to look up and think, as Thucydides asks his readers to do.", "points": [
 "A man in a loose, ink-black garment with a white collar leans back in a wooden chair, shown from the knees up.",
 "His body faces left, but he turns his head to look at us from the corners of his light hazel-brown eyes, one eyebrow slightly cocked.",
 "He has a close-trimmed silvery-grey beard, lined cheeks and a black, three-pointed cap.",
 "With one hand he marks his place in a closed book with a sand-brown cover, about the size of a thick paperback.",
 "His other arm stretches along the arm of the chair, its hand curled round a carved terminal; he wears a gold ring with a dark blue stone on his little finger.",
 "Behind him is a crimson-red chair lining with fringes, against a brown background that lightens to tan around his head."
]},
"music": {"id": "mass-in-b-minor", "why": "Bach assembled it at the end of his life from music he had written over decades, and it was not performed complete while he lived: a work written, like Thucydides', not for the applause of the moment."},
"think": {"library": "who-was-jesus", "depth": 4, "why": "Historians test the Gospels with the questions Thucydides asked: who saw it, who wrote it down, who disagreed. See how the modern debate about Jesus works."},
"learn": {"memory": "possession-for-all-time", "why": "Thucydides' own reason for writing, and a good test for anything we make: is it for the applause of the moment, or for good?"},
"check": [
 {"q": "Why does Thucydides choose the story of Harmodius and Aristogiton as his example?", "options": ["Because it was a Spartan story", "Because it shows that even a nation's favourite story about its own past can be wrong, if no one tests it", "Because he was related to them", "Because it was the cause of the war"], "answer": 1, "why": "Athenians honoured them as the tyrant-slayers; Thucydides shows they killed the tyrant's brother. Testing applies to your own people's stories too."},
 {"q": "What does Thucydides admit about the speeches in his history?", "options": ["That they are word-for-word records", "That he invented them freely with no basis", "That he made the speakers say what the occasion demanded, keeping as close as possible to the general sense of what was said", "That they were written by the speakers themselves"], "answer": 2, "why": "He could not remember the exact words, so he reconstructed them, keeping to 'the general sense'."},
 {"q": "Why does Thucydides think his history will be useful?", "options": ["Because it entertains", "Because it flatters Athens", "Because human nature does not change, so the past will help people understand what is likely to happen again", "Because it proves the gods favour Sparta"], "answer": 2, "why": "'An aid to the interpretation of the future, which in the course of human things must resemble if it does not reflect it.'"},
 {"q": "What is the best reply to the charge that Herodotus simply believed whatever he was told?", "options": ["He never travelled, so he could not have been told anything", "He says he is bound to report what is said but not bound to believe it, and often gives several versions", "He used written documents only", "He wrote only about events he saw himself"], "answer": 1, "why": "VII.152 is his rule for the whole book; he records reports as reports."},
 {"q": "Thucydides says the 'real cause' of the war was Athens' growing power and Sparta's fear. Why was this distinction important?", "options": ["Because it blamed the gods", "Because it separated the stated reasons for a war from its underlying cause, a distinction historians still use", "Because it proved Sparta was innocent", "Because it showed the war was an accident"], "answer": 1, "why": "Corcyra, Potidaea and Megara were the occasions; the shift in power was the cause."},
 {"q": "Which is the strongest reason to read Thucydides critically, even though he is careful?", "options": ["He believed in oracles", "He was a participant with strong views, who chose what to include and wrote the speeches himself, and inscriptions show things he left out", "He wrote centuries after the war", "He had no eyewitnesses"], "answer": 1, "why": "Care and bias can live together; the tribute rise of 425 BC is one omission."}
],
"tutorial": {"question": "Herodotus or Thucydides: which was the better historian?", "approach": "Set out each man's method in his own words (I.22; II.123; VII.152). Give the strengths of each: Herodotus' breadth and fairness to many voices, Thucydides' testing and precision. Give the weaknesses of each: Herodotus' credulity and numbers, Thucydides' speeches and selectivity. Decide what 'better' means, and answer.",
 "strong": [
  "Quotes or explains Thucydides' account of the speeches and of the narrative accurately.",
  "Gives Herodotus' rule ('bound to report ... not bound to believe') fairly.",
  "Weighs strengths and weaknesses of each with examples.",
  "Explains the 'real cause' and why it mattered.",
  "Notes that even Thucydides shapes and selects.",
  "Defines what makes a historian good before deciding."
 ]},
"reading": [
 {"author": "Robert B. Strassler (ed.)", "title": "The Landmark Thucydides", "year": 1996, "level": "start", "why": "Crawley's translation, revised, with maps on almost every page."},
 {"author": "Donald Kagan", "title": "The Peloponnesian War", "year": 2003, "level": "start", "why": "The whole war in one readable volume, by its leading modern historian."},
 {"author": "Simon Hornblower", "title": "Thucydides", "year": 1987, "level": "deeper", "why": "A short study of how Thucydides worked, and how far to trust him."},
 {"author": "Graham Allison", "title": "Destined for War", "year": 2017, "level": "deeper", "why": "The 'Thucydides Trap' applied to the modern world, to read with its critics."}
],
"practice": "Live it this week: the next time you hear a story that makes you angry (in the news, at work, in the family), before you repeat it, find one other account of the same event. Notice whether the two agree.",
"reflect": "Which story about your own family, town or country have you never tested, because you wanted it to be true?",
"takeaways": [
 "Thucydides set out to find the exact truth, testing eyewitnesses who disagreed through bad memory or bias, and to write 'a possession for all time'.",
 "He admits he reconstructed the speeches, and he separated the stated reasons for the war from its real cause: Athens' growth and Sparta's fear.",
 "Herodotus recorded what he was told without claiming to believe it all; Thucydides tested; both chose and shaped, and we must read both critically."
]
}
