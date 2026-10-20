from sA import S1, S2, S3
from sB import S4, S5
from sC import S6, S7

HALL = "bible"; AFTER = "can-i-trust-the-bible"; LATER_TITLE = "In the beginning"
SESSIONS = [S1, S2, S3, S4, S5, S6, S7]

META = {
"id": "in-the-beginning",
"title": "In the beginning",
"question": "What does Genesis say about the world and about us?",
"line": "Seven sessions on the Bible's first eleven chapters, through the oldest questions people ask: where did everything come from, who am I, why is the world broken, why do people hurt each other, will God give up on us, why so many peoples? And the question an adult asks: doesn't science say otherwise?",
"why": "No pages have shaped the West's picture of the world and of human beings more than the first chapters of Genesis: a good creation, every person in God's image, freedom, the fall, the flood and the promise. This journey reads them as their first hearers did, beside the Babylonian creation and flood stories they answered, then gives the scientific case against them its full weight, and ends with a verdict and the call of Abraham. It is written at the depth of a first-year university course, for anyone.",
"level": "foundation",
"follows": "A first-year theology paper introducing the Hebrew Bible, on Genesis 1–11 in its ancient Near Eastern setting, with elements of a paper on science and religion.",
"art": "goltzius-fall",
"status": "draft",
"before": ["can-i-trust-the-bible"],
"outcomes": [
 "Explain the structure and main claims of Genesis 1, and how it answers the Babylonian Enuma Elish.",
 "Explain what 'made in the image of God' means, with the three main readings and the evidence of ancient royal images.",
 "Read Genesis 3 closely, and set out the Catholic, Orthodox, Protestant and Jewish views of original sin and the main views on Adam and Eve.",
 "Trace the spread of violence in Genesis 4–6, and compare it with Hesiod's ages of man.",
 "Compare the Genesis flood with Gilgamesh Tablet XI, and say what geology shows about a worldwide flood.",
 "State the scientific case against reading Genesis as history at full strength, and weigh the best replies.",
 "Explain how Jews and the main Christian traditions read Genesis 1–11 today, and the four main readings of the days."
],
"people": [
 {"name": "Moses", "years": "traditionally 13th century BC", "line": "By tradition the author of Genesis and the rest of the Torah."},
 {"name": "Hesiod", "years": "about 700 BC", "line": "Greek poet whose Works and Days tells of five declining ages of humanity."},
 {"name": "Ashurbanipal", "years": "king of Assyria 668–about 631 BC", "line": "Built the library at Nineveh where the Enuma Elish and Gilgamesh tablets were found."},
 {"name": "Origen", "years": "about 185–254", "line": "Alexandrian scholar who asked how there could be days before the sun."},
 {"name": "Basil of Caesarea", "years": "about 330–379", "line": "Bishop whose sermons on the six days, the Hexaemeron, are a classic of Orthodox reading."},
 {"name": "Augustine of Hippo", "years": "354–430", "line": "Wrote several commentaries on Genesis; gave the West the term 'original sin'."},
 {"name": "Rashi", "years": "1040–1105", "line": "French rabbi whose commentary on the Torah is still the most read in Judaism."},
 {"name": "Maimonides", "years": "1138–1204", "line": "Jewish philosopher who held that the creation story should not all be read literally."},
 {"name": "John Calvin", "years": "1509–1564", "line": "Reformer who taught that Moses spoke of nature in everyday language."},
 {"name": "John Milton", "years": "1608–1674", "line": "Poet of Paradise Lost, the great English retelling of the fall."},
 {"name": "James Ussher", "years": "1581–1656", "line": "Archbishop who dated creation to 4004 BC."},
 {"name": "Charles Darwin", "years": "1809–1882", "line": "Naturalist whose Origin of Species (1859) set out evolution by natural selection."},
 {"name": "Charles Kingsley", "years": "1819–1875", "line": "Clergyman and novelist who welcomed Darwin's theory as a noble view of God."},
 {"name": "Thomas Henry Huxley", "years": "1825–1895", "line": "Biologist, 'Darwin's bulldog', inventor of the word 'agnostic'."},
 {"name": "William Ewart Gladstone", "years": "1809–1898", "line": "Prime Minister who argued that science confirmed Genesis, and was answered by Huxley."},
 {"name": "George Smith", "years": "1840–1876", "line": "British Museum Assyriologist who found the Gilgamesh flood tablet in 1872."},
 {"name": "E. A. Wallis Budge", "years": "1857–1934", "line": "British Museum keeper whose translations of the Babylonian texts are read in this journey."},
 {"name": "Georges Lemaître", "years": "1894–1966", "line": "Belgian priest and physicist who proposed the expanding universe and its beginning."},
 {"name": "Francis Collins", "years": "living", "line": "Geneticist, leader of the Human Genome Project, founder of BioLogos."},
 {"name": "Richard Dawkins", "years": "living", "line": "Biologist and the best-known advocate of the view that evolution leaves no room for God."}
],
"timeline": [
 {"year": "c. 1700 BC", "text": "The Babylonian flood poem Atrahasis is written."},
 {"year": "c. 1200–1100 BC", "text": "Enuma Elish probably takes its present form."},
 {"year": "c. 700 BC", "text": "Hesiod writes Works and Days."},
 {"year": "7th century BC", "text": "Ashurbanipal's library at Nineveh copies Enuma Elish and Gilgamesh."},
 {"year": "6th–5th c. BC", "text": "Genesis reaches its final form, by most scholars' dating."},
 {"year": "c. 230", "text": "Origen questions days before the sun."},
 {"year": "c. 378", "text": "Basil of Caesarea preaches the Hexaemeron."},
 {"year": "c. 401–415", "text": "Augustine writes The Literal Meaning of Genesis."},
 {"year": "1554", "text": "Calvin's Commentary on Genesis."},
 {"year": "1650", "text": "Ussher dates creation to 4004 BC."},
 {"year": "1667", "text": "Milton's Paradise Lost."},
 {"year": "1859", "text": "Darwin's On the Origin of Species."},
 {"year": "1872", "text": "George Smith reads the Gilgamesh flood tablet in London."},
 {"year": "1885", "text": "Huxley answers Gladstone on Genesis."},
 {"year": "1929", "text": "Woolley finds flood deposits at Ur."},
 {"year": "1927–31", "text": "Lemaître proposes the expanding universe."},
 {"year": "1950", "text": "Pius XII, Humani Generis."},
 {"year": "1961", "text": "The Genesis Flood launches modern young-earth creationism."},
 {"year": "1979", "text": "The Tell Fekheriye statue, an 'image and likeness' of a king, is found."}
],
"places": [
 {"name": "The British Museum", "where": "London", "why": "Holds the Gilgamesh flood tablet that George Smith read in 1872, and the Enuma Elish tablets."},
 {"name": "Nineveh", "where": "Mosul, northern Iraq", "why": "The Assyrian capital whose library preserved the Babylonian creation and flood stories."},
 {"name": "Babylon", "where": "Hillah, Iraq", "why": "City of Marduk and of the great ziggurat Etemenanki, the setting of Babel."},
 {"name": "Ur", "where": "Southern Iraq", "why": "Abraham's city, by tradition; site of Woolley's flood deposits and a restored ziggurat."},
 {"name": "The Sistine Chapel", "where": "Vatican City", "why": "Michelangelo's ceiling (1508–12) paints the creation, the fall and the flood."},
 {"name": "The Natural History Museum", "where": "London", "why": "Built in the age of Darwin and Huxley; a 'cathedral of nature' with Darwin's statue on its stairs."}
],
"glossary": [
 {"term": "Agnostic", "def": "Someone who holds that we cannot know whether God exists; a word coined by Huxley in 1869."},
 {"term": "Ancestral sin", "def": "The Orthodox view that we inherit mortality and a tendency to sin from Adam, but not his guilt."},
 {"term": "Atrahasis", "def": "A Babylonian poem of about 1700 BC that tells of creation and a great flood."},
 {"term": "Cosmogony", "def": "An account of how the world began."},
 {"term": "Cosmology", "def": "A picture of the shape and structure of the universe."},
 {"term": "Covenant", "def": "A binding promise or agreement; in the Bible, between God and people."},
 {"term": "Deep time", "def": "The immense age of the earth and universe revealed by geology and astronomy."},
 {"term": "Eden", "def": "The garden where God put the first humans; the name probably means 'delight'."},
 {"term": "Enuma Elish", "def": "The Babylonian creation epic, named from its first words, 'When above'."},
 {"term": "Epic of Gilgamesh", "def": "A Mesopotamian poem about a king seeking immortality; its eleventh tablet tells of a great flood."},
 {"term": "Evolution", "def": "The descent of all living things from common ancestors, with change over generations."},
 {"term": "Expanse", "def": "The 'firmament' of Genesis 1: the dome of the sky, in the ancient picture holding back waters above."},
 {"term": "Fall", "def": "The first human disobedience, in Genesis 3, and its consequences."},
 {"term": "Flood geology", "def": "The view that a recent worldwide flood laid down most of the earth's rock layers."},
 {"term": "Genesis", "def": "The first book of the Bible; Greek for 'origin'. In Hebrew, Bereshit, 'In the beginning'."},
 {"term": "Image of God", "def": "What Genesis 1:27 says every human being is: God's representative and likeness in the world."},
 {"term": "Lex talionis", "def": "'An eye for an eye': a law limiting punishment to the harm done."},
 {"term": "Midrash", "def": "Jewish interpretation of Scripture, often through stories and questions."},
 {"term": "Myth", "def": "A traditional story about gods and origins; in ordinary speech, a false story. Scholars use it in the first sense."},
 {"term": "Natural selection", "def": "Darwin's mechanism: living things better suited to their surroundings leave more offspring."},
 {"term": "Nephilim", "def": "Mysterious 'mighty men of old' in Genesis 6:4."},
 {"term": "Original sin", "def": "Augustine's term for the state of sin all humans inherit from Adam; understood differently by different churches."},
 {"term": "Polemic", "def": "A text that argues against another view; Genesis 1 is often read as a polemic against Babylonian myth."},
 {"term": "Primeval history", "def": "Genesis 1–11: the story of the whole human race before Abraham."},
 {"term": "Privation", "def": "A lack or twisting of something good; Christians describe evil as a privation rather than a thing in its own right."},
 {"term": "Protoevangelium", "def": "'First gospel': Genesis 3:15, read by Christians as the first promise of a saviour."},
 {"term": "Sabbath", "def": "The seventh day, of rest; from the Hebrew word for 'to stop' or 'rest'."},
 {"term": "Yahweh", "def": "The personal name of God in the Hebrew Bible, often printed 'the LORD' in English Bibles."},
 {"term": "Ziggurat", "def": "A stepped temple tower of Mesopotamia, like the tower of Babel."}
],
"reading": [
 {"author": "Leon Kass", "title": "The Beginning of Wisdom: Reading Genesis", "year": 2003, "level": "start", "why": "A philosopher's slow, wise reading of Genesis."},
 {"author": "John Walton", "title": "The Lost World of Genesis One", "year": 2009, "level": "start", "why": "Genesis 1 in its ancient setting."},
 {"author": "David Damrosch", "title": "The Buried Book", "year": 2007, "level": "start", "why": "The rediscovery of Gilgamesh."},
 {"author": "Francis Collins", "title": "The Language of God", "year": 2006, "level": "start", "why": "A geneticist on faith and evolution."},
 {"author": "Robert Alter", "title": "Genesis: Translation and Commentary", "year": 1996, "level": "deeper", "why": "A literary translation with notes."},
 {"author": "Alan Jacobs", "title": "Original Sin: A Cultural History", "year": 2008, "level": "deeper", "why": "The idea of original sin through history."},
 {"author": "Denis Alexander", "title": "Creation or Evolution: Do We Have to Choose?", "year": 2008, "level": "deeper", "why": "A biologist on science and Genesis."},
 {"author": "Gordon Wenham", "title": "Genesis 1–15", "year": 1987, "level": "scholars", "why": "The standard evangelical scholarly commentary."},
 {"author": "Claus Westermann", "title": "Genesis 1–11", "year": 1984, "level": "scholars", "why": "The great critical commentary."},
 {"author": "W. G. Lambert", "title": "Babylonian Creation Myths", "year": 2013, "level": "scholars", "why": "The Babylonian texts, edited and translated."},
 {"author": "Peter Harrison", "title": "The Territories of Science and Religion", "year": 2015, "level": "scholars", "why": "How the 'conflict' between science and religion was invented."}
]
}

CLOSING = {
"title": "Your answer",
"prompt": "What does Genesis say about the world and about us, and can a thinking person today still believe it? In about 300 words, make the case for what you think Genesis 1–11 truly teaches, and answer the strongest objection to it.",
"practice": "Read the whole of Genesis 1–11 in one sitting, aloud if you can. Then, over the next week, read it again a chapter a day, asking each time: what does this say about God, and what does it say about me?",
"music": "haydn-creation",
"synthesis": [
 "This journey asked what the Bible's first eleven chapters say about the world and about us, through the oldest questions people ask. Here are the short answers.",
 "Where did everything come from? From one God, who made everything freely by his word, and called it good. Genesis 1 is a carefully patterned account, forming and then filling the world, crowned by a day of rest. Read beside Babylon's Enuma Elish, it is a deliberate answer: no battle of the gods, no monster's body, sun and moon not gods but lamps, and human beings not slaves made from a rebel's blood but God's own images.",
 "Who am I? Dust and breath: part of the natural world, and alive with God's own breath. Every human being, man and woman, bears God's image, as an ancient king's statues showed his rule. That idea became the root of the West's belief in the dignity of every person. We are made for work, for each other and for God; the first thing called 'not good' is to be alone.",
 "Why is the world broken? Not because it was made bad, but because human beings mistrusted God and grasped at deciding good and evil for themselves. Shame, hiding, blame, toil and death followed. Christians differ on what we inherit: Catholics speak of inherited loss, the Orthodox of inherited mortality without guilt, Protestants of inherited guilt and corruption; Jews reject original sin altogether. They differ too on whether Adam and Eve were two historical people. All agree the story is true of every one of us, and that God came looking: 'Where are you?'",
 "Why do people hurt each other? Because broken trust spreads: from one murder between brothers, to Lamech's boast of seventy-sevenfold revenge, to a world 'filled with violence'. Yet no one is fated to do wrong: God warns Cain that he can master sin, holds him responsible, and still protects him. Hesiod told a similar story of decline, but as fate; Genesis tells it as choice, and keeps hope open.",
 "Will God give up on us? No. The flood story, which shares much with the Babylonian flood in Gilgamesh, transforms it: one God who grieves over violence, saves those who trust him, sends his wind over the waters as at creation, and binds himself to every living creature never to destroy the world again. Geology finds no worldwide flood, though great local floods in Mesopotamia are well attested; Christians read the story as global, local or theological, and agree on what it teaches about God.",
 "Doesn't science say otherwise? Science shows that the universe is billions of years old, that life evolved, and that humans share ancestors with apes. That rules out reading Genesis as a scientific timetable, as Huxley showed in 1885. But Huxley himself called the war between science and religion 'purely factitious', and Darwin wrote of laws 'impressed on matter by the Creator'. The hardest questions are real: Adam and Eve and genetics, and animal death before the fall. What science cannot do is test what Genesis claims about God, goodness and human dignity.",
 "Why so many peoples? Because, at Babel, humanity tried to make a name for itself and build its way to heaven, and God scattered it, as both judgement and mercy. Then, in one sentence, he called Abraham, promising that through his family 'all the families of the earth will be blessed'. Christians read Pentecost, many languages and one message, as Babel reversed.",
 "So what is Genesis 1–11? Neither science nor mere myth, but true stories about God and humanity, told in the forms of their time. Its picture of us is realistic and hopeful: creatures of dust, bearing God's image; free and fallen; violent and responsible; never abandoned. The rest of the Bible, beginning with Abraham, tells how God answers the questions these chapters raise.",
 "One more thing. It is worth counting how much of the West grew from these few pages. The goodness of the material world, which made it worth studying, and the confidence that it is orderly because one rational God made it, both helped science to be born. The dignity of every person as God's image lies behind our belief in human rights. The weekly day of rest, for servants and animals as well as masters, begins on the seventh day. The idea that each person is responsible for their choices, and that we are our brothers' keepers, runs from Cain to our courts and charities. The unity of the human family stands against every racism. Even the dove with an olive branch, still the world's sign of peace, flies out of Noah's ark. Whatever you conclude about Genesis, you cannot understand the West without it."
],
"exam": [
 "'Genesis 1 is best read as a polemic against Babylonian myth.' Discuss.",
 "What does it mean to say that human beings are made in the image of God? Assess the main interpretations.",
 "Compare the Catholic, Orthodox and Protestant doctrines of original sin. Which best fits Genesis 3 and Romans 5?",
 "'Am I my brother's keeper?' What does Genesis 4 teach about human responsibility?",
 "Compare the flood narratives of Genesis and Gilgamesh. What do the differences reveal?",
 "Does evolution disprove Genesis? Discuss with reference to Huxley and Darwin.",
 "Must Adam and Eve be historical for the Christian doctrine of the fall to be true?",
 "'True stories told in the forms of their time.' Is this an adequate account of Genesis 1–11?"
],
"next": {"place": "Visit the British Museum's Mesopotamian galleries in London, to see the Assyrian tablets and the Lachish reliefs, or the Sistine Chapel in Rome, where Michelangelo painted the creation, the fall and the flood.", "book": "Leon Kass, The Beginning of Wisdom (2003), and Robert Alter's translation of Genesis (1996), read side by side.", "journey": "story-in-seven-acts"}
}
