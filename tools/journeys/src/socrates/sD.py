ARIS = {"author": "Aristophanes", "work": "The Clouds", "translator": "W. J. Hickie (1853)", "source": "https://www.gutenberg.org/ebooks/2562", "kind": "poetry",
        "who": "Aristophanes (about 446–386 BC), the great comic poet of Athens; then Xenophon (about 430–354 BC), reporting the prosecution's case", "when": "Athens, 423 BC (revised about 418–416 BC); Xenophon writing in the 380s–370s BC"}
XEN = {"author": "Xenophon", "work": "Memorabilia (Recollections of Socrates)", "translator": "H. G. Dakyns (1897)", "source": "https://www.gutenberg.org/ebooks/1177"}
MILL = {"author": "John Stuart Mill", "work": "On Liberty, chapter II", "translator": "", "source": "https://www.gutenberg.org/ebooks/34901"}
PHAEDO = {"author": "Plato", "work": "Phaedo", "translator": "Benjamin Jowett (1871)", "source": "https://www.gutenberg.org/ebooks/1658", "kind": "philosophy",
          "who": "Plato (about 428–348 BC), Socrates' pupil, who was ill and absent that day, and wrote from the accounts of those who were there", "when": "Athens, probably the 380s or 370s BC; the conversation is set in the prison on the day of Socrates' death, 399 BC"}
JUSTIN = {"author": "Justin Martyr", "work": "Second Apology", "translator": "Marcus Dods (1885), Ante-Nicene Fathers I", "source": "https://www.newadvent.org/fathers/0127.htm"}

S6 = {
"title": "The case against: was Socrates a danger?",
"line": "Athens had its reasons. This session gives the prosecution the floor: the comic poet, the accuser, the historians and a philosopher who thought Socrates was a disease.",
"objection": True,
"plain": "So far we have heard Socrates' side, told by his friends. But five hundred ordinary Athenians found him guilty, and they were not all fools or villains. His companions had included a traitor and a tyrant. He mocked the democracy and its choice of officials by lot. His questions dissolved the beliefs that held the city together and, critics say, put nothing in their place. This session states the case against Socrates as strongly as its best advocates have made it, from Aristophanes and the ancient prosecutor to the journalist I. F. Stone and the philosopher Friedrich Nietzsche. Only then do we ask what can be said in reply.",
"why": "Sessions 2 to 5 followed the trial through Socrates' own words: his mission, his method, his defence and his refusal to escape. Every one of those texts was written by an admirer. A fair verdict needs the other side, and now we have the tools to weigh it.",
"answers": [
 "Why was Socrates really put to death?",
 "What did Socrates have to do with Alcibiades and Critias?",
 "Was Socrates against democracy?",
 "What did Nietzsche have against Socrates?"
],
"finding": "Athens had real reasons: his companions included the traitor Alcibiades and the tyrant Critias, he scorned democratic equality, and his questioning dissolved the city's beliefs without replacing them; the charge deserves a hearing, though it does not justify his death.",
"background": [
 {"h": "The story so far", "paras": [
  "We have followed Socrates through his trial and into prison. His friends' accounts show a man of integrity: obedient to a divine mission, poor, brave, unwilling to do wrong even to save his life. That picture has shaped the West. But it comes almost entirely from Plato and Xenophon, both devoted followers writing to clear his name.",
  "The prosecution's speeches are lost. What we know of their case comes from hints in the defence, from a pamphlet called The Accusation of Socrates written a few years after the trial by a teacher of rhetoric named Polycrates (also lost, but answered by Xenophon), and from what later Athenians said. Historians have reconstructed it carefully. Here it is."
 ], "key": "Our sources are Socrates' admirers; the prosecution's case must be pieced together from hints, from Polycrates' lost pamphlet and from Xenophon's reply to it."},
 {"h": "Alcibiades and Critias", "paras": [
  "Alcibiades (about 450–404 BC) was the most brilliant young man of his generation: rich, beautiful, a ward of Pericles, and Socrates' close companion, who served beside him at Potidaea. In 415 BC he persuaded Athens to send a vast expedition to conquer Sicily. Accused of mocking the sacred Mysteries, he fled to Sparta and advised it how to beat Athens. He switched sides twice more. The Sicilian disaster cost Athens perhaps forty thousand men.",
  "Critias (about 460–403 BC), a poet, thinker and relative of Plato, was another of Socrates' companions. In 404 BC he became the leader of the Thirty Tyrants, who executed about 1,500 Athenians, seized property and disarmed the citizens. He was killed fighting the democrats in 403 BC. Charmides, Plato's uncle and another companion of Socrates, died with him. To many Athenians at the trial, these were the young men Socrates had 'corrupted'."
 ], "timeline": [
  {"year": "415 BC", "text": "Alcibiades leads the Sicilian expedition; accused of impiety, he defects to Sparta"},
  {"year": "413 BC", "text": "The Sicilian expedition destroyed"},
  {"year": "411 BC", "text": "A first oligarchic coup, the Four Hundred, briefly overthrows the democracy"},
  {"year": "404–403 BC", "text": "Critias leads the Thirty Tyrants"},
  {"year": "401 BC", "text": "The last oligarchs, at Eleusis, are crushed"},
  {"year": "399 BC", "text": "Trial of Socrates"},
  {"year": "c. 393 BC", "text": "Polycrates' pamphlet, The Accusation of Socrates"}
 ], "key": "Alcibiades betrayed Athens to Sparta; Critias led the Thirty Tyrants. Both had been Socrates' companions, and many jurors had suffered from them."},
 {"h": "Why we read these passages", "paras": [
  "The main reading has two parts. First, the end of Aristophanes' The Clouds: the old farmer, ruined by what Socrates' school taught his son, burns the 'thinking-shop' down. It shows what many Athenians feared from Socrates a generation before the trial. Second, two charges from 'the accuser', almost certainly Polycrates, as Xenophon reports them: that Socrates taught the young to despise the laws, and that he was the teacher of Critias and Alcibiades.",
  "The comparison is from John Stuart Mill's On Liberty (1859), the most famous modern defence of free speech. Mill grants something important to the prosecution: the jurors were very likely honest men doing what they thought right. That is exactly why the case is so troubling."
 ], "key": "The burning of the thinking-shop in The Clouds, the accuser's charges in Xenophon, and Mill on the honesty of Socrates' judges."}
],
"before": [
 "In The Clouds, what has the son learned at Socrates' school, and what does it lead him to do?",
 "What two charges does 'the accuser' bring in Xenophon? How strong are they?",
 "Mill says the jurors 'honestly found him guilty'. If so, what went wrong?"
],
"readWhy": "The prosecution's case in the oldest words we have: the comic poet's warning and the accuser's charges.",
"read": [
 dict(ARIS, raw="clouds2", idx=list(range(0, 25)), ref="Aristophanes, The Clouds, about lines 1462–1510", title="The thinking-shop burns",
  context="The end of the play. The farmer Strepsiades sent his son Phidippides to Socrates' school to learn the argument that wins bad cases, to cheat his creditors. The son learned it too well: he has just beaten his father, and proved by argument that a son may beat his father, and his mother too. The Chorus of Clouds, whom Socrates worshipped as new gods, now reveal that they lead the wicked on to ruin so that they learn to fear the gods. 'Vortex' is the swirling force some natural philosophers said ruled the universe; Strepsiades has a cup, a 'vortex' in Greek, in front of his house. Hermes was the god whose statues stood at Athenian doors. Hickie, 1853, writes 'Jove' and 'Jupiter' for Zeus.",
  plain="The father admits he was wrong to cheat his creditors and calls his son to take revenge on Socrates. The son refuses: there is no Zeus any more, only Vortex. The father, ashamed that he threw away the gods for Socrates, asks the god Hermes for advice and decides not to sue but to burn the school. He climbs on the roof with a torch. Socrates, inside, cries out that he is choking. The father mocks him with his own words, 'I am walking on air', and shouts that they insulted the gods.",
  commentary=[
   {"on": "Phid. I will not injure my teachers.", "text": "The son has learned loyalty to his teachers and contempt for his father. For the audience this was the nightmare: a clever education that turns the young against the family and the gods."},
   {"on": "There is not, no; for Vortex reigns having expelled Jupiter.", "text": "The joke is on natural philosophy, which explained thunder and rain by physical forces instead of Zeus. Socrates was lumped with these thinkers, wrongly, as he insisted in court. But the fear was real: if the gods are explained away, what holds people to their oaths?"},
   {"on": "How mad, then, I was when I ejected the gods on account of Socrates!", "text": "The play's verdict, in the mouth of a foolish old man who has learned his lesson. Some twenty-four years later, a jury of men like him would decide Socrates' fate."},
   {"on": "You advise me rightly, not permitting me to get up a lawsuit, but as soon as possible to set fire to the house", "text": "A comic ending of mob justice. Modern readers find it chilling. Aristophanes cannot have meant it as a call to violence; but in Plato's Apology Socrates blames the comedy for the prejudice that killed him."},
   {"on": "I am walking on air, and speculating about the sun.", "text": "The farmer repeats Socrates' own first words in the play, now from the burning roof. The circle closes: the man who looked down on the gods is brought down."},
   {"on": "For what has come into your heads that you acted insolently toward the gods, and pried into the seat of the moon?", "text": "The last charge of the play is impiety: insolence to the gods. It is, almost exactly, the charge of 399 BC."}
  ]),
 dict(XEN, raw="mem2", idx=[0, 1], ref="Xenophon, Memorabilia I.2.9 and I.2.12", title="The accuser's charges",
  context="In the second chapter of his Memorabilia, Xenophon quotes and answers the charges of 'the accuser'. Most scholars think this is Polycrates, whose Accusation of Socrates appeared about 393 BC, six years after the trial, and probably drew on what was said in court. Choosing officials 'by ballot' means by lot: most Athenian officials were picked at random from volunteers, a central democratic practice. Read the charges first; Xenophon's replies follow each one, and the lecture weighs them.",
  plain="The accuser says: Socrates taught his followers to despise the laws, by mocking the choice of officials by lot; nobody would choose a ship's pilot or a flute-player that way. That made the young violent and contemptuous of the constitution. And the two men who did Athens the greatest harm, Critias the oligarch and Alcibiades the democrat, were both his companions. Xenophon replies that wise men use persuasion, not violence, and that he will explain what the two men's friendship with Socrates really was.",
  commentary=[
   {"on": "did not Socrates cause his associates to despise the established laws when he dwelt on the folly of appointing state officers by ballot?", "text": "This charge is about democracy itself. Choosing by lot expressed the democratic belief that any citizen was fit to serve. Socrates thought ruling was a skill, like steering a ship, which needs knowledge. To democrats this was not a neutral opinion; it was the argument the oligarchs had used to justify their coups."},
   {"on": "Words like these, according to the accuser, tended to incite the young to contemn the established constitution, rendering them violent and headstrong.", "text": "The heart of 'corrupting the young'. The accuser does not say Socrates taught violence. He says Socrates taught contempt for democratic equality, and that contempt in clever, rich young men turned violent."},
   {"on": "But for myself I think that those who cultivate wisdom and believe themselves able to instruct their fellow-citizens as to their interests are least likely to become partisans of violence.", "text": "Here Xenophon's reply begins. Hold it for now: the point of this session is to hear the charge first."},
   {"on": "the two men who wrought the greatest evils to the state at any time--to wit, Critias and Alcibiades--were both companions of Socrates", "text": "The strongest single point for the prosecution. Critias, 'the oligarch', led a reign of terror; Alcibiades, 'the democrat', betrayed the city in war. One from each side: Socrates' influence seemed dangerous whatever party a young man belonged to."},
   {"on": "Where would you find a more arrant thief, savage, and murderer than the one?", "text": "Xenophon does not defend them at all. He concedes the facts and contests only their connection with Socrates."}
  ])
],
"compare": {"title": "Honest judges", "why": "John Stuart Mill was the great English liberal philosopher of the nineteenth century. In On Liberty (1859) he begins his case for free speech with the trial of Socrates, and then the trial of Jesus. Read how much he concedes to the prosecution.",
 "parts": [
  dict(MILL, raw="mill", idx=[0, 1], ref="Mill, On Liberty (1859), chapter II", title="A memorable collision",
   context="Mill is arguing that no society should silence an opinion because it is sure the opinion is false and harmful, since history shows how wrong such certainty can be. He chooses the most famous examples he can. 'I maestri di color che sanno', 'the masters of those who know', is Dante's description of Aristotle; Mill applies it to Plato and Aristotle together. 'Cotemporaries' is an old spelling. Gutenberg's marks for italics have been removed.",
   plain="Mill says: remember that Athens put to death, after a fair trial, the man who was the best of them all and the teacher of all later philosophy, for impiety and immorality. The jurors very probably believed honestly that he was guilty. The same is true of those who condemned Jesus as a blasphemer: they were not bad men, but ordinary, respectable, religious, patriotic people of their time, the kind we would think blameless today. That is the point. Good people, sure they are right, can do the greatest wrong.",
   commentary=[
   {"on": "there took place a memorable collision", "text": "Mill's word is well chosen: a collision is not a crime by one side. Two forces met: the city's settled beliefs, and a man who questioned them."},
   {"on": "Of these charges the tribunal, there is every ground for believing, honestly found him guilty", "text": "This is Mill's great concession, and it strengthens the case against Socrates as a case: the jury was not corrupt. By the standards of Athens, he really was impious and a danger to the young."},
   {"on": "These were, to all appearance, not bad men--not worse than men commonly are, but rather the contrary", "text": "Mill turns from Socrates to Jesus. His point is uncomfortable for every age: the people who condemned the best men were respectable and sincere, and we would very likely have done the same."},
   {"on": "one of those persecutors was Saint Paul", "text": "Paul, whose words you have read beside Socrates in this journey, began as a persecutor of Christians, 'in all good conscience' as he said later (Acts 23:1). Mill's moral: sincerity is no guarantee of being right, so we should never silence dissent merely because we are sure."}
   ])
 ]},
"lecture": {"sections": [
 {"h": "The prosecution's case", "paras": [
  "Put the case against Socrates as the prosecution might have, in its strongest form. First, his companions. Alcibiades betrayed Athens; Critias and Charmides led the Thirty, who killed about 1,500 citizens. A teacher who spent years with such men cannot simply wash his hands of them. Fifty years later Athenians still remembered the trial this way: the orator Aeschines told a jury, 'you put to death Socrates the sophist, because he was shown to have educated Critias' (Against Timarchus 173).",
  "Second, his politics. Socrates mocked the lot and the Assembly; he held that ruling, like medicine, belongs to experts; he admired Sparta and Crete, the very cities the oligarchs held up as models. Third, his religion. He spoke of a private divine voice that overruled the city's customs, and claimed God's authority for his questioning. Fourth, his effect. He took the city's shared beliefs about justice, piety and courage, showed they did not hold together, and offered no replacement but more questions. In a city that had just survived defeat, terror and civil war, that was not a harmless hobby."
 ], "key": "The prosecution's case: his companions (Alcibiades, Critias), his contempt for democracy, his private religion, and questioning that dissolved shared beliefs."},
 {"h": "I. F. Stone: the political trial", "paras": [
  "In 1988 the American radical journalist I. F. Stone, a lifelong champion of free speech, published The Trial of Socrates, after teaching himself ancient Greek in his seventies to write it. His aim was not to defend the verdict but to understand it. His case, in summary, is this.",
  "Socrates was, in Stone's view, a consistent enemy of democracy: he taught that the many are ignorant and that the city should be ruled by 'the one who knows'. Athens had suffered three oligarchic seizures of power in twelve years, in 411, 404 and, in a last attempt from Eleusis, 401 BC. The jurors had every reason to fear a man whose teaching had formed the leaders of the second. Yet Stone also argues that Socrates could have won. Athens prided itself on free speech, parrhēsia; had Socrates appealed to it, he might have been acquitted. Instead, in Stone's reading, he provoked the jury, as if he wanted to die and to shame the democracy. Stone concludes that Athens betrayed its own principles, but that Socrates helped it to."
 ], "key": "I. F. Stone (1988) argued that Socrates was an enemy of democracy feared after three oligarchic coups, who could have appealed to free speech but provoked the jury instead."},
 {"h": "Hegel: two rights in collision", "paras": [
  "The German philosopher G. W. F. Hegel (1770–1831), in his Lectures on the History of Philosophy, gave the most profound version of the objection. He called Socrates' fate truly tragic, in the sense of Greek tragedy: not good against evil, but right against right.",
  "On one side stood the ethical life of the Greek city: its customs, gods and laws, which people lived by without needing to justify them. On the other stood a new principle, which Socrates introduced: that the individual must test everything by his own reason and conscience, and accept only what survives the test. Socrates' inner voice, Hegel says, was the first form of this principle. Athens was right that the principle would destroy the old city; it did. Socrates was right that the principle was true and must come. The Athenians condemned him justly by their own law, and then repented, because they recognised that the principle was already in them. Hegel thought the modern world was born from this collision."
 ], "key": "Hegel saw a tragedy of two rights: the city's inherited ethical life against the individual's right to test everything by reason; both were justified."},
 {"h": "Nietzsche: Socrates as a symptom", "paras": [
  "Friedrich Nietzsche (1844–1900) brought a different, deeper charge. In The Birth of Tragedy (1872) he blamed Socrates for killing the spirit of Greek tragedy, with its acceptance of life's dark and irrational depths, and replacing it with 'theoretical man', who believes reason can understand and even correct everything.",
  "In 'The Problem of Socrates', in Twilight of the Idols (1889), he went further. Socrates, he says, was a sign of decline. His famous ugliness and low birth, his irony and his endless arguments were the weapons of a man who had no other way to win: dialectic as revenge on the noble and the strong. He made reason a tyrant over the instincts, as if a healthy person needed reasons for everything. And his last words, asking for a cock to be offered to Asclepius, the god of healing, show what he really thought: that life is a long illness, and death the cure. Socrates wanted to die, Nietzsche says; Athens only gave him what he asked. On this view Socrates did not corrupt the young; he corrupted life itself, and Christianity, 'Platonism for the people', spread the disease."
 ], "key": "Nietzsche charged Socrates with making reason a tyrant over instinct and treating life as an illness, a decline Christianity later spread."},
 {"h": "What can be said in reply", "paras": [
  "The replies begin with the facts. Critias turned against Socrates: Xenophon says the Thirty forbade him to teach the young, and Plato that Socrates refused their order to arrest Leon of Salamis. Alcibiades' own speech in Plato's Symposium shows a man who admired Socrates and failed to follow him. A teacher is not responsible for every pupil, as Xenophon argues; and Socrates had democratic friends too, such as Chaerephon. He obeyed the laws of the democracy all his life and died rather than break them.",
  "On politics, scholars such as Gregory Vlastos and Richard Kraut point out that Socrates criticised every regime, defied the democracy at Arginusae and the oligarchy over Leon, and chose to live in democratic Athens. On religion, his piety was real. Against Nietzsche, many answer that Socrates' last words are more naturally read as gratitude, or as care for a small debt, and that his reason was never a tyrant: it served his love of the good. And the deepest reply is Mill's: even if the jurors were sincere, a city that kills its questioners loses the only means it has of correcting its own mistakes."
 ], "key": "Critias turned on Socrates; he criticised all regimes and obeyed democratic law; his piety was real; Mill: killing questioners destroys a city's means of correcting itself."},
 {"h": "What stands", "paras": [
  "Even after the replies, something in the objection stands. Socratic questioning really can dissolve. It can leave clever young people without the beliefs they were raised in and without anything to replace them, proud of their doubts and contemptuous of those who still believe. Plato knew this: in the Republic (VII.537e–539d) he warns that young people who taste argument too early become like puppies, tearing at everything, and end by believing nothing. Many parents and teachers have watched it happen.",
  "So the objection leaves a real question for the verdict: is the examined life enough by itself? Socrates claimed only to know that he did not know. Is that a foundation, or only a clearing of the ground? Hegel thought Athens' faith could not survive it. Nietzsche thought nothing should replace it but a stronger will. The early Christians, as we will see in the last session, gave a third answer."
 ], "key": "Socratic questioning can dissolve beliefs without replacing them, as Plato himself warned; whether the examined life is enough by itself remains the open question."}
], "refs": [
 "Aristophanes, Clouds 1452–1510, tr. W. J. Hickie (1853).",
 "Xenophon, Memorabilia I.2.9–48, tr. H. G. Dakyns (1897); Hellenica II.3–4.",
 "Plato, Apology 32c–d (Leon of Salamis); Symposium 215a–222b (Alcibiades); Republic VII.537e–539d.",
 "Aeschines, Against Timarchus 173 (345 BC).",
 "Thucydides VI–VII (Alcibiades, Sicily); Aristotle, Athenian Constitution 29–40.",
 "J. S. Mill, On Liberty (1859), ch. II.",
 "I. F. Stone, The Trial of Socrates (1988).",
 "G. W. F. Hegel, Lectures on the History of Philosophy (1833), vol. I, part I, ch. II, 'Socrates' (tr. E. S. Haldane, 1892).",
 "F. Nietzsche, The Birth of Tragedy (1872), §§12–15; Twilight of the Idols (1889), 'The Problem of Socrates'; The Gay Science (1882), §340.",
 "Gregory Vlastos, 'The Historical Socrates and Athenian Democracy', Political Theory 11 (1983); Richard Kraut, Socrates and the State (1984)."
]},
"debate": {"question": "Was Athens right to fear Socrates?", "positions": [
 {"name": "The prosecution: yes", "who": "Anytus and Polycrates (as reported by Xenophon); I. F. Stone (1988), in part", "view": "Socrates taught contempt for democratic equality to rich young men, two of whom did Athens enormous harm, and dissolved the city's religious and moral beliefs. After war, terror and three coups, the city was entitled to defend itself, even if the verdict was harsh.", "evidence": "Critias and Alcibiades; his mockery of the lot; Aeschines' remark; the fear of oligarchic coups in 411, 404 and 401 BC."},
 {"name": "Plato and Xenophon: no", "who": "Plato; Xenophon; Gregory Vlastos and most modern scholars", "view": "Socrates was the best citizen Athens had: brave, law-abiding, just, and critical of every regime. Critias and Alcibiades became bad when they left him. The city killed the conscience it needed.", "evidence": "Arginusae and Leon of Salamis; the Thirty's ban on his teaching; his obedience to the laws even to death."},
 {"name": "Nietzsche: yes, but for the wrong reason", "who": "Friedrich Nietzsche", "view": "The danger was not to democracy but to life. Socrates replaced the instincts and tragic wisdom of the Greeks with the tyranny of reason, and taught people to treat life as a sickness to be cured. The jury did not understand the real charge.", "evidence": "The 'problem of Socrates' in Twilight of the Idols; his last words about Asclepius; the decline of tragedy."}
], "agree": "All agree that Socrates was not an ordinary citizen, that his questioning changed Athens, and that the trial was about more than the words of the charge."},
"look": {"art": None, "why": "The National Gallery of Art's open collection has no painting of Alcibiades, Critias or a Greek symposium. Paintings of Socrates' companions, such as Jean-Baptiste Regnault's Socrates Dragging Alcibiades from the Embrace of Sensual Pleasure (1791), are in other museums.", "points": []},
"music": {"id": "tallis-fantasia", "why": "Ralph Vaughan Williams, who called himself an agnostic, spent years editing The English Hymnal (1906), and here takes a hymn tune that Thomas Tallis wrote for the Archbishop of Canterbury's psalter in 1567 and builds from it something vast and new. It is a picture of the other way to treat an inherited tradition: not to dissolve it, but to question it, love it and make it sing again."},
"think": {"library": "does-morality-need-god", "depth": 4, "why": "If questioning dissolves inherited morality, what can ground it? The modern form of the objection to Socrates."},
"check": [
 {"q": "Which was the prosecution's strongest piece of evidence for 'corrupting the young'?", "options": ["Socrates was poor", "Two of his companions, Critias and Alcibiades, had done Athens great harm", "Socrates studied the stars", "Socrates charged high fees"], "answer": 1, "why": "Xenophon himself concedes their crimes; even he can only argue about their link to Socrates."},
 {"q": "Why would Socrates' criticism of choosing officials by lot sound dangerous to a democratic jury in 399 BC?", "options": ["Because the lot was a religious ritual", "Because it echoed the oligarchs' argument that ruling needs experts, used to justify coups in 411 and 404 BC", "Because the lot was a recent invention", "Because Socrates had lost a lottery"], "answer": 1, "why": "The argument that the many are unfit to rule was the oligarchs' case, and the city had just survived their terror."},
 {"q": "What does Mill concede to the prosecution?", "options": ["That Socrates was guilty of treason", "That the jurors very probably honestly believed him guilty", "That Socrates' philosophy was false", "That free speech is dangerous"], "answer": 1, "why": "Mill thinks the tribunal 'honestly found him guilty': which is why sincerity cannot justify silencing anyone."},
 {"q": "Hegel called Socrates' death tragic because:", "options": ["Socrates was innocent and the jury wicked", "It was a collision of two rights: the city's inherited ethical life and the individual's right to test everything by reason", "Socrates died young", "Tragedy was popular in Athens"], "answer": 1, "why": "For Hegel, both Athens and Socrates were justified: right against right."},
 {"q": "How did Nietzsche read Socrates' last words about a cock for Asclepius?", "options": ["As a joke", "As proof he believed in the gods", "As a sign that he thought life was an illness and death its cure", "As a debt Crito forgot to pay"], "answer": 2, "why": "Asclepius was the god of healing: Nietzsche took the offering as thanks for being cured of life."},
 {"q": "Which reply best answers the charge that Socrates made Critias a tyrant?", "options": ["Critias was never in Athens", "Critias, once in power, banned Socrates from teaching and Socrates defied the Thirty's order to arrest Leon", "Socrates never met Critias", "Critias was a democrat"], "answer": 1, "why": "Their later conflict suggests Critias abandoned Socrates' influence rather than followed it."}
],
"tutorial": {"question": "'Why was Socrates executed?' State the case for the prosecution at full strength, then decide how far it succeeds.", "approach": "Begin with the prosecution in its strongest form: Alcibiades and Critias, Socrates' contempt for the lot, his private religion, the dissolving effect of his questioning, and the fear of coups. Use Stone, Hegel and Nietzsche. Then give the replies and judge which parts of the case stand and which fall.",
 "strong": [
  "States the prosecution's case without caricature.",
  "Uses the evidence of Alcibiades, Critias and Aeschines accurately.",
  "Explains Stone's political reading, including the amnesty and the coups.",
  "Explains Hegel's 'two rights' and Nietzsche's deeper charge in its own terms.",
  "Gives the replies (the Thirty's ban, Leon, Arginusae, Mill).",
  "Concludes with a clear judgement on what remains of the objection."
 ]},
"reading": [
 {"author": "I. F. Stone", "title": "The Trial of Socrates", "year": 1988, "level": "start", "why": "The prosecution's case, passionately argued by a lover of free speech."},
 {"author": "Friedrich Nietzsche", "title": "Twilight of the Idols", "year": 1889, "level": "deeper", "why": "Read 'The Problem of Socrates': ten short sections that changed how many moderns see him."},
 {"author": "Gregory Vlastos", "title": "'The Historical Socrates and Athenian Democracy', Political Theory 11", "year": 1983, "level": "scholars", "why": "The scholarly reply: Socrates as a critic of every regime, not an oligarch."}
],
"practice": "Live it this week: choose one person whose views you think are dangerous. Write down their case as they would put it, so well that they would agree with your summary. Only then write your reply.",
"reflect": "Have your questions ever dissolved something in someone else, or in you, without putting anything better in its place? What would it take to build as well as to question?",
"takeaways": [
 "The prosecution had real grounds: Alcibiades and Critias, Socrates' contempt for choosing by lot, his private religion, and questioning that dissolved shared beliefs.",
 "Stone read the trial as political; Hegel as a tragic collision of two rights; Nietzsche as a verdict on a man who treated life as a disease.",
 "Replies show Socrates defied the Thirty and obeyed democratic law; but the question whether questioning alone can build a life remains."
],
"terms": ["Thirty Tyrants", "Amnesty", "Sophist", "Assembly", "Impiety", "Dialectic"]
}

S7 = {
"title": "Practising death: the verdict",
"line": "On his last day Socrates tells his friends that philosophy is practice for dying, and drinks the poison. What should we make of him?",
"plain": "The verdict: Socrates was not guilty of impiety, and Athens was wrong to kill him, though it was not wrong to find him unsettling. His examined life, honest about ignorance, ruled by conscience and caring for the soul above everything, was worth living and worth dying for. But it was not complete in itself, and the early Christians who loved him said so. This session reads his last conversation in Plato's Phaedo, where he calls philosophy 'the practice of dying', and Justin Martyr's comparison of Socrates with Christ, and then draws the journey together.",
"why": "Session 6 gave the prosecution its full say and left a question standing: is the examined life enough by itself? Now we go to the prison on the last day to see how Socrates answered it with his own death, and to hear how the first Christian philosophers judged him.",
"answers": [
 "How did Socrates face death, and what did he believe about the soul?",
 "What did he mean by calling philosophy 'practice for dying'?",
 "Is Socrates like Jesus?",
 "So: what is the examined life, and is it worth living?"
],
"finding": "Socrates said philosophy is practice for dying and the care of the soul the only thing that matters; the Church Fathers called him a Christian before Christ, while noting what he did not have: the whole Word, and a death others would die for.",
"background": [
 {"h": "The story so far", "paras": [
  "Here are the findings so far. Socrates questioned Athens for a lifetime; his only wisdom was knowing he did not know (sessions 1 and 2). His method stunned the proud and helped the humble (session 3). Condemned, he would obey God rather than the city (session 4), and he would not escape, because he would not return wrong for wrong (session 5). The prosecution had real reasons, and its deepest question remains: does questioning only dissolve, or can it build a life (session 6)?",
  "If you have taken Death and hope, you have read the end of the Phaedo: the poison, the last words and Phaedo's tribute. Here we read the beginning, which that journey left out: how the day began, and why Socrates was not afraid."
 ], "key": "The case so far: Socrates' wisdom, method, defence and refusal to flee, and the prosecution's question, whether questioning can build a life."},
 {"h": "The last day", "paras": [
  "The sacred ship returned from Delos, and the day of execution came. Socrates' friends gathered at dawn outside the prison. Athenian executions were by a cup of poison, prepared from hemlock (Plato only calls it 'the poison'), drunk at sunset. The friends spent the whole day with him, talking about whether the soul survives death. Plato, Phaedo tells us, was ill and not there.",
  "The Phaedo is told some time later by Phaedo of Elis, a young man who had been a slave before Socrates' friends freed him, to a philosopher called Echecrates in the town of Phlius in the Peloponnese. Two young men from Thebes, Simmias and Cebes, do most of the questioning; they had studied with followers of Pythagoras, who believed in the soul's rebirth."
 ], "timeline": [
  {"year": "Dawn", "text": "Friends gather; Socrates' chains are removed; Xanthippe is sent home"},
  {"year": "Morning", "text": "Why a philosopher should not fear death (our reading)"},
  {"year": "Midday and afternoon", "text": "The arguments for the immortality of the soul; the objections of Simmias and Cebes"},
  {"year": "Sunset", "text": "Socrates bathes, says farewell to his family, drinks the poison and dies (read in Death and hope)"}
 ], "key": "Socrates spent his last day talking with friends about the soul; Phaedo, who was there, tells the story to Echecrates."},
 {"h": "Why we read these passages", "paras": [
  "The main reading is the first part of the Phaedo (57a–69e): the last morning and Socrates' 'defence' of why a philosopher welcomes death. It answers the question left by the last session: what positive vision lay behind his questioning? The answer is the care of the soul, pursued to the end.",
  "The comparison is from Justin Martyr, a philosopher who became a Christian and was beheaded in Rome about AD 165. In his Second Apology, a defence of Christians addressed to the Roman Senate, he compares Christ with Socrates: the first serious Christian verdict on the man this journey has followed."
 ], "key": "The Phaedo's opening (57a–69e), and Justin Martyr's verdict comparing Socrates with Christ."}
],
"before": [
 "What does Phaedo say he felt, being with Socrates on his last day? Why?",
 "What does Socrates mean by saying that true philosophers are 'always occupied in the practice of dying'?",
 "Justin says Socrates knew Christ 'partially'. What, according to Justin, did he lack?"
],
"readWhy": "Socrates' last morning, and his reason for meeting death without fear: philosophy as the practice of dying and the care of the soul.",
"read": [
 dict(PHAEDO, raw="phaedo", idx=list(range(0, 19)), ref="Plato, Phaedo 57a–60b", title="The ship from Delos",
  context="The town of Phlius, some weeks or months after the death. Echecrates, a philosopher there, asks Phaedo, who was in the prison, to tell him everything. Cuts in the text are marked '…'. Jowett, 1871.",
  plain="Echecrates asks how Socrates died. Phaedo explains the delay: the sacred ship to Delos. He says that being there was strange: he could not pity Socrates, who seemed happy and fearless, but he felt pleasure and pain mixed. That morning the friends found Socrates just released from his chains. Xanthippe, his wife, was there with their child, crying; Socrates had her taken home. Then he sat up, rubbed his leg, and remarked how strangely pleasure and pain follow each other.",
  commentary=[
   {"on": "the ship which the Athenians send to Delos", "text": "The delay that gave us the Crito and the Phaedo. Athens' piety towards Apollo, whose oracle had sent Socrates on his mission, kept him alive for a month."},
   {"on": "he died so fearlessly, and his words and bearing were so noble and gracious, that to me he appeared blessed", "text": "This is the impression Plato wants to leave: not tragedy, but blessedness. Phaedo cannot even pity him."},
   {"on": "we were laughing and weeping by turns", "text": "A very human detail. The friends are not philosophers in marble; they are people losing a friend."},
   {"on": "Plato, if I am not mistaken, was ill.", "text": "The only time Plato mentions himself in a dialogue by name in this way. He tells us honestly that he was not there; the account comes from others."},
   {"on": "Socrates turned to Crito and said: 'Crito, let some one take her home.'", "text": "Modern readers wince. Xanthippe has been treated harshly by later writers, as a scold. Here she simply grieves. Socrates will see her and the children again at the end of the day, in private, before he dies. Plato's dialogue is about the friends' conversation; it is not the whole of Socrates' last day."},
   {"on": "How singular is the thing called pleasure, and how curiously related to pain", "text": "Even rubbing a sore leg, Socrates starts to philosophise. The examined life does not stop for the last day."}
  ]),
 dict(PHAEDO, raw="phaedo", idx=list(range(19, 46)), ref="Plato, Phaedo 61c–64a", title="A defence before his friends",
  context="Socrates has said that any philosopher will be willing to die. This passage also discusses why we must not take our own lives. If you are struggling with thoughts of ending your life, please talk to someone today: in the UK and Ireland, Samaritans on 116 123; elsewhere, a local helpline or a doctor. Philolaus was a Pythagorean philosopher. 'The Eleven' were the officials in charge of the prison.",
  plain="Socrates says a philosopher will be willing to die, but must not kill himself: we are like possessions of the gods, or soldiers on guard, and must wait until God summons us, as he is summoning Socrates now. Cebes objects: then why would a wise man be glad to leave such good masters? Socrates agrees to make his 'defence' to them, as he did to the jury: he hopes to go to other wise and good gods, and perhaps to good men who have died. The jailer has sent a message not to talk too much, or the poison may need two doses. Socrates says: let him prepare two, or three.",
  commentary=[
   {"on": "but he will not take his own life, for that is held to be unlawful", "text": "Socrates distinguishes accepting death from seeking it. This passage became one of the main ancient arguments against suicide, taken up by Christian writers such as Augustine (City of God I.17–22)."},
   {"on": "the gods are our guardians, and that we are a possession of theirs", "text": "Our lives are not wholly our own. Christians would say something similar: 'you are not your own, for you were bought with a price' (1 Corinthians 6:19–20)."},
   {"on": "Here, said he, turning to us, is a man who is always inquiring", "text": "Socrates loves Cebes for objecting. Even on his last day, he wants to be questioned. The examined life welcomes the hardest questions."},
   {"on": "I am going to other gods who are wise and good (of which I am as certain as I can be of any such matters)", "text": "Notice the careful levels of confidence. Of the good gods he is as sure as he can be; of meeting good men 'I am not so sure'. Even facing death, Socrates will not claim more than he knows."},
   {"on": "let him mind his business and be prepared to give the poison twice or even thrice if necessary", "text": "A flash of dry humour. He will not stop talking to make dying easier."}
  ]),
 dict(PHAEDO, raw="phaedo", idx=list(range(46, 97)), ref="Plato, Phaedo 64a–67e", title="The practice of dying",
  context="Now Socrates gives his 'defence': why a philosopher should be of good cheer at death. 'Absolute justice' and 'absolute beauty' are what Plato elsewhere calls the forms: justice itself, beauty itself, as distinct from just acts and beautiful things.",
  plain="Socrates says: people don't realise that true philosophers spend their lives pursuing death. Death is the separation of soul and body. The philosopher cares little for food, sex or fine clothes, and turns from the body to the soul. The body's senses deceive us; we grasp justice, beauty and goodness themselves only by thought, when the mind is most gathered into itself. The body fills us with desires and fears and wars. So pure knowledge comes, if at all, after death. Therefore philosophers practise dying all their lives, and it would be absurd for them to fear it now.",
  commentary=[
   {"on": "they do not perceive that he is always pursuing death and dying", "text": "The famous claim. Socrates does not mean that philosophers want to die soon; he has just forbidden suicide. He means that the philosopher's whole life is a loosening of the soul from the body's demands, so that death completes what life began."},
   {"on": "Is it not the separation of soul and body?", "text": "The Greek definition of death that Christians also used for centuries. The difference will be in what happens next: Plato's soul is glad to be free of the body; Christian hope is for the body to be raised and made new."},
   {"on": "Is there or is there not an absolute justice?", "text": "Here the Socratic question 'What is justice?' meets Plato's answer. Justice itself is never seen with the eyes, only grasped by the mind. If you continue to the Plato journey you will study these forms in depth."},
   {"on": "Whence come wars, and fightings, and factions? whence but from the body and the lusts of the body?", "text": "Compare James 4:1: 'Where do wars and fightings among you come from? Don't they come from your pleasures that war in your members?' Plato and the New Testament agree that disordered desire, not ignorance alone, lies behind violence."},
   {"on": "the true philosophers, Simmias, are always occupied in the practice of dying, wherefore also to them least of all men is death terrible", "text": "The line this session is named after. Practising death means living now for what does not die: the soul, wisdom, justice. Christian monks and spiritual writers took up the idea; the Rule of Benedict tells monks to keep death daily before their eyes (ch. 4)."}
  ]),
 dict(PHAEDO, raw="phaedo", idx=list(range(97, 115)), ref="Plato, Phaedo 67e–69e", title="The one true coin",
  context="Socrates now argues that only the philosopher has true courage and self-control. 'The thyrsus-bearers' carried decorated staffs in the processions of the god Dionysus; 'the mystics' were those truly initiated into the sacred rites.",
  plain="Socrates says: a man who grieves at death loves his body, money or power, not wisdom. Ordinary people are brave out of fear of something worse, and self-controlled because they want other pleasures more: they trade one fear or pleasure for another like coins. But wisdom is the one true coin; without it, virtue is only a shadow. Many carry the staff, few are truly initiated. I have tried all my life to be one of the few. Whether I succeeded I shall know soon, if God wills.",
  commentary=[
   {"on": "is not his reluctance a sufficient proof that he is not a lover of wisdom, but a lover of the body", "text": "A hard saying. Socrates thinks fear of death shows what we really love. Most readers, including many Christians, would add that grief at death is also love for those we leave, and need not be a failure."},
   {"on": "Then all but the philosophers are courageous only from fear", "text": "A sharp observation that still bites. Much ordinary 'virtue' is self-interest in disguise: honest because we fear being caught, brave because we fear shame."},
   {"on": "is there not one true coin for which all things ought to be exchanged?--and that is wisdom", "text": "Here is Socrates' positive vision, the answer to the charge that he only dissolved. Beneath all the questioning was a conviction: wisdom, the knowledge of the good, is worth everything. The questions cleared the way for it."},
   {"on": "'many,' as they say in the mysteries, 'are the thyrsus-bearers, but few are the mystics,'", "text": "Compare Jesus: 'many are called, but few chosen' (Matthew 22:14). Both say that outward membership is not the same as the real thing."},
   {"on": "whether I have sought in a right way or not, and whether I have succeeded or not, I shall truly know in a little while, if God will", "text": "Even here, on the edge of death, Socrates' ignorance is honest. He has hope, not certainty. This is perhaps the most moving sentence in the reading."}
  ])
],
"compare": {"title": "Christ and Socrates", "why": "Justin Martyr was a philosopher from Samaria who searched through the schools, Stoic, Aristotelian, Pythagorean and Platonist, before becoming a Christian. He kept wearing the philosopher's cloak, taught in Rome and was beheaded there about AD 165. Here, in a defence addressed to the Roman Senate, he gives the first Christian verdict on Socrates.",
 "parts": [
  dict(JUSTIN, raw="justin", idx=[0], ref="Justin Martyr, Second Apology 10", title="Partially known even by Socrates",
   context="Justin writes about AD 150–160, after Christians in Rome had been executed simply for being Christians. Like Socrates, they were accused of atheism, because they refused the gods of the city. 'The Word' translates the Greek logos: reason, word, account. John's Gospel says that the Word was with God and was God, and 'became flesh' in Jesus (John 1:1, 14). Justin uses the idea to explain how pagans could know some truth. The translation is by Marcus Dods, in the Ante-Nicene Fathers (1885).",
   plain="Justin says: whatever lawgivers and philosophers said well, they found by seeing part of the Word, God's Reason; but they did not know the whole Word, who is Christ, so they contradicted themselves. Socrates, the most zealous of them, was accused of the same crimes as Christians: new gods and denying the city's gods. He told people to reject the poets' wicked stories and seek the unknown God by reason. But no one trusted Socrates so far as to die for his teaching; Christ, whom Socrates partly knew, is trusted to death not only by philosophers but by craftsmen and the uneducated, because he is the power of God, not a human theory.",
   commentary=[
    {"on": "they elaborated by finding and contemplating some part of the Word", "text": "This is Justin's key idea. The Word, God's own Reason, is present in every human mind. So whatever any philosopher saw truly, he saw by the Word's light: truth anywhere belongs to Christ."},
    {"on": "And Socrates, who was more zealous in this direction than all of them, was accused of the very same crimes as ourselves", "text": "Justin sees Socrates as a forerunner of the Christian martyrs: tried for 'atheism', for refusing the gods everyone else worshipped."},
    {"on": "he exhorted them to become acquainted with the God who was to them unknown, by means of the investigation of reason", "text": "An echo of Paul at Athens, who spoke of the altar 'to an unknown god' (Acts 17:23). Justin's Socrates is a seeker of the one true God, by reason."},
    {"on": "That it is neither easy to find the Father and Maker of all, nor, having found Him, is it safe to declare Him to all", "text": "Justin is quoting Plato's Timaeus (28c), a later dialogue in which Plato, through another speaker, says that the maker of the universe is hard to find and impossible to declare to all. Justin attributes it to Socrates' teaching."},
    {"on": "For no one trusted in Socrates so as to die for this doctrine", "text": "Here is the difference, for Justin. Socrates died for his convictions; no one died for Socrates. Christians, including ordinary working people, were dying for Christ."},
    {"on": "who was partially known even by Socrates", "text": "Justin's verdict in four words. Socrates knew Christ 'partially': not by name, but as the Reason and Truth he served. This became the Church's most generous way of honouring the best of the pagans."},
    {"on": "not the mere instrument of human reason", "text": "The last word marks the limit. Socrates' examined life was the best that human reason could do. Christianity claims to be something else: not a better argument, but the power of God."}
   ])
 ]},
"lecture": {"sections": [
 {"h": "The verdict", "paras": [
  "On the evidence of this journey, Socrates was not guilty as charged. He honoured the gods as he understood them; he served what he believed was a divine command; he corrupted no one by teaching injustice, and two of his worst companions turned against what he taught. Athens had real fears, and Hegel was right that Socrates' questioning would change the city for ever. But a city that kills its questioner because his questions are uncomfortable destroys its own means of correcting itself, as Athens soon recognised.",
  "What of the examined life? The journey has shown what it was for Socrates: to know the limits of your knowledge; to test your beliefs and other people's, honestly, in conversation; to care for the soul, what kind of person you are, more than for money, reputation or even life; never to do wrong, even in return; and to follow the argument, and conscience, wherever they lead. He showed that it can be lived, and died for. The objection showed that it is not complete in itself: questioning can clear the ground, but it needs something to build."
 ], "key": "Socrates was not guilty as charged; his examined life, knowing one's limits, testing beliefs, caring for the soul, never doing wrong, is worth living, though questioning alone cannot build everything."},
 {"h": "Immortality and resurrection", "paras": [
  "Socrates met death calmly because he hoped the soul would be freed from the body to be with the gods. Christianity agrees that death is not the end, and Christians borrowed much from the Phaedo. But its hope is different. The New Testament does not promise the soul's escape from the body; it promises the resurrection of the body, raised and transformed, as Christ was raised (1 Corinthians 15).",
  "The Swiss scholar Oscar Cullmann made this contrast famous in a lecture of 1955, 'Immortality of the Soul or Resurrection of the Dead?'. He set Socrates' serene death beside Jesus in Gethsemane, 'greatly troubled and distressed' (Mark 14:33), praying for the cup to pass. For Socrates death was a friend; for the New Testament it is 'the last enemy' (1 Corinthians 15:26), defeated not by philosophy but by God. Many theologians think Cullmann drew the line too sharply, since Christians have also taught that the soul lives on with God until the resurrection. But the difference he saw is real."
 ], "key": "Socrates hoped for the soul's release from the body; Christianity hopes for the body's resurrection, and treats death as an enemy defeated by God, not a friend."},
 {"h": "The cock for Asclepius", "paras": [
  "Socrates' last words, at sunset, after the poison had begun to work, were: 'Crito, I owe a cock to Asclepius; will you remember to pay the debt?' (Phaedo 118a). You can learn the whole passage as this session's memory piece. Asclepius was the god of healing; the sick offered him a cockerel when they recovered. What did Socrates mean?",
  "Readers have given at least four answers. Nietzsche, as the last session showed, took it as thanks for being cured of life, the sickness. Others read it as thanks for the healing of his soul by philosophy, or of Plato's illness, mentioned at the start of the dialogue. Some read it as plain piety: a man who kept the city's customs to the end and would not die owing a god anything. The classicist Glenn Most suggested it referred to Plato's recovery; Emily Wilson's book surveys the rest. The words are left open. What they are not is bitter. The last thing Socrates did was to remember a small duty and ask a friend to do it: the examined life, to the end, attending to the next right thing."
 ], "key": "Socrates' last words asked Crito to pay a cock to Asclepius, god of healing: read as thanks for release from life, for a healed soul, or simple piety; they are not bitter."},
 {"h": "Socrates and Jesus", "paras": [
  "People have compared the two since the second century. Both taught by conversation and questions, wrote nothing and are known through followers who disagree in details. Both were tried on religious charges with political undertones, before their own people's authorities. Both could have escaped and did not. Both died with forgiveness rather than revenge.",
  "The differences matter as much. Socrates claimed to know that he did not know; Jesus taught 'with authority' and spoke of God as his Father. Socrates died at seventy, among friends, calmly, by a painless poison; Jesus died in his thirties, abandoned, by torture, crying out to God. Socrates died for his convictions; Christians claim that Jesus died for others, and rose. In the eighteenth century Jean-Jacques Rousseau, no orthodox believer, put the comparison in a famous sentence: if Socrates lived and died like a sage, Jesus lived and died like a God."
 ], "table": {"cols": ["", "Socrates", "Jesus"], "rows": [
  ["Wrote", "Nothing; known through Plato, Xenophon, Aristophanes", "Nothing; known through four Gospels and Paul"],
  ["Taught", "By questions; claimed not to know", "By parables, questions and direct authority"],
  ["Charged with", "Impiety and corrupting the young", "Blasphemy, and claiming to be king"],
  ["Escape", "Refused Crito's plan", "Did not flee Gethsemane; told Peter to put away his sword"],
  ["Death", "Aged 70, by poison, calm, among friends", "In his thirties, by crucifixion, in anguish, mostly abandoned"],
  ["Last words", "'Crito, I owe a cock to Asclepius'", "'Father, into your hands I commit my spirit' (Luke 23:46)"],
  ["Afterwards", "His followers founded schools", "His followers proclaimed his resurrection"]
 ], "note": "Rousseau's comparison is in Emile (1762), Book IV, the 'Profession of Faith of the Savoyard Vicar'."}, "key": "Both taught orally, were tried on religious charges and refused escape; Socrates died calm for his convictions, Jesus in anguish, his followers say, for others, and rose."},
 {"h": "A Christian before Christ?", "paras": [
  "Justin was not alone. In his First Apology (46) he says that those who lived 'with the Word', such as Socrates and Heraclitus, were Christians, even if they were thought atheists. Clement of Alexandria (about 150–215) called philosophy a schoolmaster that prepared the Greeks for Christ, as the law prepared the Jews. Augustine (City of God VIII.3) praised Socrates for turning philosophy to the purifying of the heart, and noted with approval that he would not claim more than he knew.",
  "In 1522 the Dutch scholar Erasmus, in his dialogue The Godly Feast, has a character say that when he reads such pagans he can hardly stop himself saying, 'Saint Socrates, pray for us' (Sancte Socrates, ora pro nobis). Others in the Church were more cautious. Tertullian asked 'What has Athens to do with Jerusalem?', and Augustine himself warned that philosophers saw the homeland from afar but not the road to it (Confessions VII.20–21). The Church's mainstream answer, from Justin to Thomas Aquinas, was that grace does not destroy nature but perfects it: Socrates' honest search was real, and pointed beyond itself."
 ], "key": "Justin, Clement and Augustine honoured Socrates as one who served the Word in part; Erasmus nearly prayed to him; others warned that philosophy sees the goal but not the road."},
 {"h": "The examined life now", "paras": [
  "What would the examined life look like today? Not necessarily a life of argument. Socrates' habits translate into practices anyone can keep: asking what our words mean before we fight over them; admitting what we do not know; listening to the strongest form of the other side; doing a daily review of our actions and motives; refusing to repay a wrong; caring more about what kind of person we are becoming than about what we own or how we look.",
  "Christians have practised several of these for centuries in their own way: the daily examination of conscience, confession, the love of enemies, the 'remembrance of death' as a way of seeing life clearly. The two traditions meet here. Socrates showed how far an honest human being can go by questioning. The Christian claim is that the One he was looking for came looking for us. That claim, too, the examined life must test."
 ], "key": "The examined life today: question your words, admit ignorance, hear the other side, review your day, refuse revenge, care for the soul; Christians practise much of this, and claim its goal came to meet us."}
], "refs": [
 "Plato, Phaedo 57a–69e, 116a–118a, tr. B. Jowett (1871); Timaeus 28c.",
 "Justin Martyr, Second Apology 10; First Apology 46, tr. M. Dods (ANF I, 1885).",
 "Clement of Alexandria, Stromata I.5; Augustine, City of God VIII.3; I.17–22; Confessions VII.20–21; Tertullian, Prescription against Heretics 7.",
 "Erasmus, Convivium religiosum (The Godly Feast, 1522).",
 "J.-J. Rousseau, Emile (1762), Book IV.",
 "Oscar Cullmann, Immortality of the Soul or Resurrection of the Dead? (Ingersoll Lecture, 1955; English 1958).",
 "Mark 14:32–36; Luke 23:46; 1 Corinthians 6:19–20; 15:26, 42–44; James 4:1; Matthew 22:14; Acts 17:23; John 1:1–14.",
 "The Rule of Benedict, ch. 4; Emily Wilson, The Death of Socrates (2007)."
]},
"debate": {"question": "Was Socrates a Christian before Christ?", "positions": [
 {"name": "Yes, in part", "who": "Justin Martyr; Clement of Alexandria; Erasmus; many Christian humanists", "view": "Socrates served the Word, God's Reason present in every mind, as fully as anyone could without knowing Christ. His honesty, piety, justice and death show the light of Christ at work outside the Church.", "evidence": "Justin, Second Apology 10 and First Apology 46; Socrates' 'God only is wise', his refusal to return wrong for wrong, his care for the soul."},
 {"name": "No: a noble pagan, nothing more", "who": "Tertullian; many Reformation and later Protestant writers; Kierkegaard in his way", "view": "Socrates was admirable, but his hope rested on human reason and the soul's own immortality. Christianity is not the completion of philosophy but a revelation that judges it. To call him a Christian blurs the difference.", "evidence": "1 Corinthians 1:21 ('the world through its wisdom didn't know God'); the contrast between immortality and resurrection; Kierkegaard's insistence that Christ is not a teacher like Socrates but the Saviour."},
 {"name": "Neither: Socrates on his own terms", "who": "Most secular philosophers; Nietzsche, from the other side", "view": "Socrates belongs to Greek philosophy, not to a Christian story. Claiming him as a forerunner of Christ takes him over. His questioning stands or falls on its own.", "evidence": "His gods were Apollo and the city's; his hope was Pythagorean and Platonic; his last offering was to Asclepius."}
], "agree": "All agree that the early Church honoured Socrates more than almost any other pagan, and that the comparison with Jesus shows both a deep likeness and a real difference."},
"look": {"art": "latour-repentant-magdalen", "why": "There is no painting of the death of Socrates at the National Gallery of Art; Jacques-Louis David's famous one is in New York. Georges de La Tour painted this picture of Mary Magdalene around 1635–1640. It is not Socrates. It is here because it is a painting of exactly what the Phaedo describes: a life spent in the practice of dying. In the Christian tradition such a picture is a meditation on death, a memento mori, 'remember you will die', meant to help the viewer live well.", "points": [
 "A young woman with long chestnut-brown hair sits at a table in a darkened room.",
 "She rests her chin in her right hand, in thought.",
 "Her left hand reaches for a skull placed on a thick book on the table.",
 "The scene is lit by a single candle, mostly hidden behind the skull.",
 "Shown in profile, she looks into a small mirror beside the skull, which reflects the skull and the book: 'know thyself' and 'remember death' in one image."
]},
"music": {"id": "faure-requiem", "why": "Gabriel Fauré's Requiem (1888) is a requiem without terror: he left out most of the Day of Judgement and ended with 'In Paradisum', the angels leading the soul into paradise. He called death 'a happy deliverance, an aspiration towards happiness above'. It is as close as music comes to the mood of the Phaedo, and it is Christian: listen for the 'Pie Jesu', a prayer for rest addressed to Christ."},
"think": {"library": "what-happens-when-we-die", "depth": 3, "why": "Immortality of the soul or resurrection of the body? The great teachers on what happens when we die."},
"learn": {"memory": "death-of-socrates", "why": "Socrates' last words and Phaedo's tribute: the end of the story this journey has followed."},
"check": [
 {"q": "What does Socrates mean by saying philosophers practise dying?", "options": ["That philosophers should seek an early death", "That philosophy is a lifelong loosening of the soul from the body's demands, so death completes what life began", "That philosophers are often executed", "That the body is evil and should be harmed"], "answer": 1, "why": "He forbids suicide; 'practising death' means living for the soul and wisdom now."},
 {"q": "Why, according to Socrates, are most people's courage and self-control not true virtue?", "options": ["Because they are too rare", "Because they trade one fear or pleasure for another, like coins, instead of acting for the sake of wisdom", "Because only soldiers can be brave", "Because pleasure is always wrong"], "answer": 1, "why": "Wisdom is 'the one true coin'; without it, virtue is only a shadow."},
 {"q": "What did Justin think Socrates lacked?", "options": ["Courage", "Any knowledge of God at all", "The whole Word, Christ; and the power that led even the uneducated to die for Christ", "A good reputation"], "answer": 2, "why": "Socrates knew the Word 'partially'; no one died for Socrates' doctrine, but many died for Christ."},
 {"q": "Which is the clearest difference between the hope of the Phaedo and the hope of the New Testament?", "options": ["The Phaedo has no hope at all", "The Phaedo hopes for the soul's release from the body; the New Testament hopes for the body's resurrection", "The New Testament denies the soul exists", "There is no difference"], "answer": 1, "why": "Cullmann's contrast: immortality of the soul versus resurrection of the dead."},
 {"q": "Which statement about Socrates and Jesus is accurate?", "options": ["Both wrote books of teachings", "Both were tried on religious charges and refused to escape, but Socrates died calmly among friends while Jesus died in anguish, largely abandoned", "Both were executed by the Romans", "Both claimed to know nothing"], "answer": 1, "why": "The likeness is real, and so is the contrast in how they died."},
 {"q": "What is the journey's verdict on the prosecution's objection?", "options": ["It was entirely groundless", "It was entirely correct", "Socrates was not guilty as charged, but the objection rightly shows that questioning alone cannot build everything", "It cannot be judged"], "answer": 2, "why": "The verdict acquits Socrates while granting what stands in the objection."}
],
"tutorial": {"question": "'Socrates and Jesus.' Compare their deaths, and say what the comparison shows.", "approach": "Describe Socrates' last day from the Phaedo, and Jesus' arrest, trial and death from one Gospel. Set out likenesses and differences: teaching, charges, refusal to escape, manner of death, hope. Use Justin's verdict and Cullmann's contrast. End with what the comparison reveals about each.",
 "strong": [
  "Uses the Phaedo accurately, including 'the practice of dying'.",
  "Uses a Gospel account accurately.",
  "Identifies real likenesses without forcing them.",
  "Identifies real differences, especially in the hope of immortality versus resurrection.",
  "Uses Justin's 'partially known' fairly.",
  "Reaches a thoughtful conclusion."
 ]},
"reading": [
 {"author": "Plato", "title": "Phaedo", "year": "c. 380 BC", "level": "start", "why": "Read it to the end: the arguments for the soul and the death scene."},
 {"author": "Emily Wilson", "title": "The Death of Socrates", "year": 2007, "level": "deeper", "why": "How Socrates' death has been told, painted and argued over for 2,400 years."},
 {"author": "Oscar Cullmann", "title": "Immortality of the Soul or Resurrection of the Dead?", "year": 1958, "level": "scholars", "why": "The classic short contrast between Socrates' death and Christ's."}
],
"practice": "Live it this week: each night before sleep, spend five minutes on a Socratic and Christian examen. Ask: what did I do today that I would be glad to have done if it were my last day? What would I change? Then let it go and rest.",
"reflect": "If you knew you had one day left, how would you spend it? What does your answer say about what you care for most?",
"takeaways": [
 "On his last day Socrates called philosophy 'the practice of dying' and wisdom 'the one true coin', and met death with hope but without claiming certainty.",
 "Justin Martyr said Socrates knew Christ 'partially', as the Word present to every mind, but no one died for Socrates' teaching as people died for Christ.",
 "The verdict: Socrates was not guilty as charged, and his examined life is worth living; it clears the ground for wisdom, and Christianity claims that the wisdom he sought came to meet us."
],
"terms": ["Practising death", "Immortality of the soul", "Resurrection", "Logos", "Martyr", "Soul", "Hemlock"]
}

CLOSING = {
"title": "Your answer",
"prompt": "What is the examined life, and is it worth dying for? In about 300 words, give your own answer from Socrates' life and death, using at least three of the readings, and answer the strongest objection to your view.",
"practice": "Read the Apology, the Crito and the death scene at the end of the Phaedo over the next week, one each on three evenings. Each time, stop at one sentence that applies to your own life and copy it out. At the end of the week, read the three sentences together.",
"music": "gerontius",
"synthesis": [
 "This journey followed the trial and death of Socrates in 399 BC, step by step, to ask what the examined life is. Here are the short answers to its questions.",
 "Who was Socrates? An Athenian, born about 470 BC, the son of a stonemason and a midwife; a brave infantryman, poor, ugly and barefoot, who spent his life in the market place asking his fellow citizens what they meant by justice, courage and piety. He turned philosophy from the stars to the question of how to live. He married Xanthippe and had three sons. He held no office except, once, a turn on the Council, where he refused to put an illegal vote.",
 "Why didn't he write anything down, and how do we know him? He thought philosophy was a living conversation, and a book cannot answer questions. So we know him through three witnesses who disagree: Aristophanes, who mocked him as a sky-gazing sophist while he lived; Xenophon, who remembered a pious, practical friend; and Plato, his greatest pupil, whose early dialogues most scholars take as closest to the real man. They agree on the public facts.",
 "What did he mean by 'I know that I know nothing'? Not quite that. When the oracle at Delphi said no one was wiser, Socrates tested it by questioning politicians, poets and craftsmen, and found they thought they knew what they did not. His only advantage, he said, was this: 'I neither know nor think that I know.' He did know some things, above all that doing wrong is evil. His wisdom was to know the limits of his knowledge, and that 'God only is wise'.",
 "What is the Socratic method? Questioning that tests a person's beliefs against each other until they see that they do not hang together: the elenchus. It numbs the proud, like a torpedo fish, but it is the first step to learning. In the Meno a slave boy, admitting 'I do not know', goes on to find for himself that the square on the diagonal is double. Plato concluded that learning is remembering; Augustine, that the mind sees truth by the light of God within. Either way, the teacher draws out; he does not pour in.",
 "Why was Socrates put to death? The charge was not recognising the city's gods, bringing in new ones and corrupting the young. Behind it lay real fears: his companions had included Alcibiades, who betrayed Athens, and Critias, who led the Thirty Tyrants; he scorned choosing officials by lot; he spoke of a private divine sign; his questions dissolved the beliefs that held the city together. The amnesty of 403 BC meant the politics could not be named. He refused to plead, told the jury he would 'obey God rather than you', called himself the gadfly God had sent to wake the city, and proposed free meals as his penalty. He was condemned by about 280 votes to 220, and sentenced to death by more.",
 "Why didn't he escape? Because he would not return wrong for wrong. In the Crito he let the Laws of Athens argue that a citizen who had accepted their care for seventy years, and was free to leave, must persuade them or obey them. His defiance in court and his obedience in prison fit together: he would refuse to do wrong at the city's command, but he would suffer wrong rather than escape. Later disobedients, from Thoreau to King, took the lesson: disobey openly, and accept the penalty.",
 "Did Socrates believe in God? Yes, though not in Homer's gods. He sacrificed, obeyed an oracle, spoke of a divine voice and argued that the world shows a caring maker. But he held that the divine must be wholly good and cannot lie, and that only God is wise. That was new, and some Athenians heard it as atheism.",
 "Was he a danger? The case against him is real. Questioning can dissolve beliefs without replacing them; I. F. Stone saw an enemy of democracy, Hegel a tragic collision of two rights, Nietzsche a man who treated life as a disease. But Critias turned against him, he obeyed the democracy's laws to his death, and, as Mill argued, a city that kills its questioners destroys its own means of correcting itself.",
 "Is Socrates like Jesus? In much: both taught orally and wrote nothing, both were tried on religious charges, both refused to escape, both died without revenge. But Socrates claimed not to know, and Jesus taught with authority; Socrates died calmly at seventy among friends, Jesus young, in anguish and abandoned; Socrates hoped for the soul's release from the body, Christians for the body's resurrection. Justin Martyr's verdict has lasted: Socrates knew Christ 'partially', as the Word present to every mind, but no one died for Socrates' teaching as ordinary people died for Christ. Erasmus could hardly keep from praying, 'Saint Socrates, pray for us.'",
 "So, what is the examined life? To know the limits of your knowledge; to test your beliefs, honestly, with others; to care for your soul, what kind of person you are, above money, reputation and even life; never to do wrong, not even in return; and to follow the argument and your conscience wherever they lead. Socrates showed that such a life can be lived, and that it is worth dying for. On his last day he called it 'the practice of dying', and wisdom 'the one true coin'. What it cannot do alone is supply the wisdom it seeks. Socrates knew that; he ended with hope, not certainty: 'I shall truly know in a little while, if God will.' The Christian claim, which this journey leaves you to examine, is that the One he was looking for came looking for us."
],
"exam": [
 "Why was Socrates executed?",
 "Should Socrates have escaped?",
 "Socrates and Jesus: compare their trials and deaths.",
 "'I neither know nor think that I know.' What was Socratic wisdom, and was it really wisdom?",
 "Can the Apology and the Crito be reconciled?",
 "Does the slave-boy scene in the Meno show that learning is recollection?",
 "Was Athens right to fear Socrates? Discuss with reference to Aristophanes, Xenophon and at least one modern critic.",
 "'The unexamined life is not worth living.' Is it true?"
],
"next": {"place": "Visit the Ancient Agora in Athens, where Socrates questioned his fellow citizens and stood trial; the Agora Museum in the Stoa of Attalos shows a jury allotment machine and small clay cups found near a building some archaeologists identify as the prison. Or see Jacques-Louis David's The Death of Socrates at the Metropolitan Museum of Art, New York.", "book": "Plato, The Last Days of Socrates (Euthyphro, Apology, Crito, Phaedo), read in one week, with Bettany Hughes, The Hemlock Cup (2010).", "journey": "plato"}
}
