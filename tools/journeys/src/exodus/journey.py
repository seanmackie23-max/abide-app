from sA import S1, S2, S3
from sB import S4, S5
from sC import S6, S7

HALL = "bible"; AFTER = "abraham"; LATER_TITLE = "Exodus and the law"
SESSIONS = [S1, S2, S3, S4, S5, S6, S7]

META = {
"id": "exodus",
"title": "Exodus and the law",
"question": "What are freedom and law for?",
"line": "Seven sessions from slavery in Egypt to the mountain of Sinai: the God who hears the cry of slaves, the name from the burning bush, the night of Passover, the sea and the desert, the Ten Commandments beside the laws of Babylon, the question whether it happened, and the promise of a new covenant written on the heart.",
"why": "No story has shaped the West's idea of freedom more than the Exodus, and no law has shaped its idea of justice more than the law given at Sinai. Jews retell it every Passover; Christians read Jesus's death through it; slaves in America sang it; revolutionaries and civil rights leaders preached it. This journey reads Exodus with the Talmud, Hammurabi, Frederick Douglass and Tacitus, faces the archaeology honestly, and asks what freedom and law are for. It is written at the depth of a first-year university course, for anyone.",
"level": "foundation",
"follows": "A first-year theology paper on the Pentateuch (Exodus, the law and covenant) in its ancient Near Eastern setting, with elements of papers on biblical archaeology and on law and ethics.",
"art": "bourdon-finding-moses",
"status": "draft",
"before": ["abraham"],
"outcomes": [
 "Explain how Exodus 1–2 presents slavery, resistance and the God who hears, and how enslaved people read it.",
 "Explain the burning bush and the main interpretations of the divine name, and Jewish and Christian practice with the name.",
 "Explain the plagues and the Passover, face the moral questions honestly, and trace the Passover into the Last Supper and the Eucharist.",
 "Discuss the meaning of freedom in the story of the sea and the wilderness, and the Exodus in Western history.",
 "Explain the Sinai covenant and the Ten Commandments, compare the law of Moses with Hammurabi's, and assess its treatment of slavery.",
 "State the case against the historicity of the Exodus at full strength, and the evidence and scholarly positions on the other side.",
 "Explain the love command, Jeremiah's new covenant, the meaning of 'Old' and 'New Testament', and how Jews and the churches relate to the law."
],
"people": [
 {"name": "Moses", "years": "traditionally 13th century BC", "line": "Hebrew raised in Pharaoh's court; called at the burning bush; led Israel out of Egypt and received the law at Sinai."},
 {"name": "Aaron", "years": "traditionally 13th century BC", "line": "Moses' brother and spokesman; Israel's first high priest; made the golden calf."},
 {"name": "Miriam", "years": "traditionally 13th century BC", "line": "Moses' sister; watched over his basket; led the women's song at the sea; the first woman called a prophet."},
 {"name": "Shiphrah and Puah", "years": "traditionally 13th century BC", "line": "The Hebrew midwives who refused Pharaoh's order to kill the baby boys."},
 {"name": "Ramesses II", "years": "reigned 1279–1213 BC", "line": "Pharaoh who built Pi-Ramesses; the Pharaoh of the Exodus in many scholars' view."},
 {"name": "Merneptah", "years": "reigned 1213–1203 BC", "line": "His victory stele contains the first mention of 'Israel' outside the Bible."},
 {"name": "Hammurabi", "years": "king of Babylon about 1792–1750 BC", "line": "Issued the most famous law code of the ancient world."},
 {"name": "Jeremiah", "years": "active about 627–580 BC", "line": "Prophet of Jerusalem's fall, who promised a new covenant written on the heart."},
 {"name": "Hillel", "years": "died about AD 10", "line": "Great rabbi who summed up the Torah: 'What is hateful to you, do not do to your neighbour.'"},
 {"name": "Rabbi Akiva", "years": "about 50–135", "line": "The greatest teacher of his age, executed by Rome, who died saying the Shema."},
 {"name": "Tacitus", "years": "about 56–120", "line": "Roman historian whose Histories preserve a hostile pagan version of the Exodus."},
 {"name": "Thomas Aquinas", "years": "1225–1274", "line": "Divided the law of Moses into moral, ceremonial and judicial precepts."},
 {"name": "Frederick Douglass", "years": "1818–1895", "line": "Escaped slave and abolitionist who described how the enslaved read Exodus."},
 {"name": "Isaiah Berlin", "years": "1909–1997", "line": "Philosopher who distinguished negative liberty (freedom from) and positive liberty (freedom for)."},
 {"name": "Michael Walzer", "years": "living", "line": "Political philosopher whose Exodus and Revolution traced the story through Western politics."},
 {"name": "Israel Finkelstein", "years": "living", "line": "Israeli archaeologist, co-author of The Bible Unearthed, the leading sceptic of the Exodus as history."},
 {"name": "Richard Elliott Friedman", "years": "living", "line": "Bible scholar who argues for a real but smaller exodus, of the Levites."},
 {"name": "Jonathan Sacks", "years": "1948–2020", "line": "Chief Rabbi of the UK and Commonwealth, whose essays on Exodus are among the best modern readings."}
],
"timeline": [
 {"year": "c. 1792–1750 BC", "text": "Hammurabi's law code."},
 {"year": "c. 1650–1550 BC", "text": "The Hyksos, rulers of Canaanite origin, in northern Egypt."},
 {"year": "c. 1446 BC", "text": "The Exodus, if the Bible's own numbers are added up."},
 {"year": "1279–1213 BC", "text": "Ramesses II builds Pi-Ramesses; the date many scholars prefer."},
 {"year": "c. 1208 BC", "text": "The Merneptah Stele names 'Israel' in Canaan."},
 {"year": "c. 1200 BC", "text": "New villages appear in the central hills of Canaan, the first Israelites."},
 {"year": "587 BC", "text": "Babylon destroys Jerusalem; Jeremiah promises a new covenant."},
 {"year": "c. AD 30", "text": "Jesus's last Passover: 'the new covenant in my blood'."},
 {"year": "c. AD 100", "text": "Tacitus writes his hostile account of the Exodus."},
 {"year": "1776", "text": "Franklin and Jefferson propose a Great Seal showing Pharaoh in the Red Sea."},
 {"year": "1855", "text": "Frederick Douglass, My Bondage and My Freedom."},
 {"year": "1901", "text": "The Code of Hammurabi discovered at Susa."},
 {"year": "1968", "text": "Martin Luther King: 'I've been to the mountaintop'."},
 {"year": "2001", "text": "Finkelstein and Silberman, The Bible Unearthed."}
],
"places": [
 {"name": "St Catherine's Monastery and Jebel Musa", "where": "South Sinai, Egypt", "why": "The traditional Mount Sinai, with a monastery founded in the sixth century around the traditional burning bush."},
 {"name": "Pi-Ramesses (Qantir)", "where": "Eastern Nile Delta, Egypt", "why": "Ramesses II's capital, the 'Raamses' of Exodus 1:11."},
 {"name": "The Louvre", "where": "Paris", "why": "Holds the black stone pillar of the Code of Hammurabi."},
 {"name": "The Egyptian Museum", "where": "Cairo", "why": "Holds the Merneptah Stele, with the first mention of Israel outside the Bible."},
 {"name": "The Liberty Bell", "where": "Philadelphia", "why": "Inscribed with Leviticus 25:10: 'Proclaim liberty throughout the land'."},
 {"name": "The National Civil Rights Museum", "where": "Memphis, Tennessee", "why": "At the Lorraine Motel, where Martin Luther King was killed the day after his 'mountaintop' speech."}
],
"glossary": [
 {"term": "Archaeology", "def": "The study of the human past through material remains: buildings, pottery, inscriptions, bones."},
 {"term": "Civil disobedience", "def": "Refusing, openly or quietly, to obey an unjust law or order, out of conscience."},
 {"term": "Covenant", "def": "A binding agreement with promises and obligations; at Sinai, between God and Israel, modelled on ancient treaties."},
 {"term": "Decalogue", "def": "Greek for 'ten words': the Ten Commandments."},
 {"term": "Elef", "def": "Hebrew for 'thousand', which may originally have meant a clan or military unit; important for the Exodus numbers."},
 {"term": "Eucharist", "def": "From the Greek for 'thanksgiving': the Christian meal of bread and wine instituted at the Last Supper; also called Mass, Holy Communion or the Lord's Supper."},
 {"term": "Exodus", "def": "Greek for 'the way out': the second book of the Bible, and Israel's departure from Egypt."},
 {"term": "Founding myth", "def": "A story a people tells about its origins, which shapes its identity whether or not it is historical."},
 {"term": "Golden calf", "def": "The idol Aaron made while Moses was on Sinai (Exodus 32): the first breaking of the covenant."},
 {"term": "Hebrew", "def": "An old name for the Israelites, used especially by foreigners; also their language."},
 {"term": "Holiness", "def": "Being set apart for God and sharing his character; in Leviticus 19, shown in justice and love."},
 {"term": "Holy", "def": "Set apart for God, because of God's presence."},
 {"term": "Kadesh-barnea", "def": "An oasis in the northern Sinai where Israel is said to have camped for many years; excavated without finding remains from the time."},
 {"term": "Lex talionis", "def": "'An eye for an eye': a law limiting punishment to the harm done, found in Hammurabi and in Exodus."},
 {"term": "Manna", "def": "The 'bread from heaven' that fed Israel in the wilderness; its name means 'What is it?'"},
 {"term": "Massah and Meribah", "def": "'Testing' and 'quarrel': the place where Israel quarrelled with God over water (Exodus 17)."},
 {"term": "Matzah", "def": "Unleavened bread, eaten at Passover in memory of the hasty departure from Egypt."},
 {"term": "Merneptah Stele", "def": "An Egyptian victory inscription of about 1208 BC containing the first mention of 'Israel' outside the Bible."},
 {"term": "Midwife", "def": "A woman who helps at childbirth; Shiphrah and Puah were the Hebrew midwives who defied Pharaoh."},
 {"term": "Negative liberty", "def": "Freedom from interference: no one stopping you doing what you choose (Isaiah Berlin)."},
 {"term": "New covenant", "def": "The covenant promised in Jeremiah 31, with the law written on the heart; Christians believe Jesus made it."},
 {"term": "Noahide laws", "def": "In Jewish teaching, seven basic laws given to all humanity through Noah, which righteous non-Jews keep."},
 {"term": "Pascha", "def": "Greek form of Pesach, 'Passover'; the name for Easter in most of the world's languages."},
 {"term": "Passover", "def": "Pesach: the Jewish festival remembering the night God 'passed over' Israel's houses and brought them out of Egypt."},
 {"term": "Pharaoh", "def": "The title of the kings of ancient Egypt, worshipped as gods."},
 {"term": "Positive liberty", "def": "Freedom for: the power to govern yourself and live well (Isaiah Berlin)."},
 {"term": "Prophet", "def": "Someone who speaks God's word to the people; Miriam is the first woman called a prophet."},
 {"term": "Redeem", "def": "To buy back a relative from slavery or debt; used of God freeing Israel."},
 {"term": "Sabbath", "def": "The seventh day, of rest for everyone, including servants, foreigners and animals."},
 {"term": "Sea of Reeds", "def": "The Hebrew yam suph, usually translated 'Red Sea'; probably a marshy lake near today's Suez Canal."},
 {"term": "Seder", "def": "'Order': the Passover meal and service at which Jews retell the Exodus."},
 {"term": "Septuagint", "def": "The Greek translation of the Hebrew Bible, made in Egypt from the third century BC."},
 {"term": "Shekinah", "def": "The rabbis' word for God's presence dwelling in the world."},
 {"term": "Shema", "def": "'Hear, O Israel': Deuteronomy 6:4–9, the central prayer of Judaism, said morning and evening."},
 {"term": "Spiritual", "def": "A religious song created by enslaved African Americans, often with a double meaning of heaven and escape."},
 {"term": "Stranger", "def": "Hebrew ger: a resident foreigner, the most vulnerable person in ancient Israel, whom the law commands Israel to love."},
 {"term": "Testament", "def": "From the Latin for 'covenant': the Old and New Testaments are the books of the old and new covenants."},
 {"term": "Tetragrammaton", "def": "Greek for 'four letters': YHWH, the personal name of God, not spoken by Jews."},
 {"term": "Torah", "def": "Hebrew for 'teaching' or 'law': the five books of Moses, and God's law as a whole."},
 {"term": "Yahweh", "def": "Scholars' reconstruction of the divine name YHWH, printed 'the LORD' in most English Bibles."}
],
"reading": [
 {"author": "Jonathan Sacks", "title": "Covenant and Conversation: Exodus", "year": 2010, "level": "start", "why": "Wise, readable essays on every section of Exodus."},
 {"author": "Michael Walzer", "title": "Exodus and Revolution", "year": 1985, "level": "start", "why": "How the Exodus shaped Western politics."},
 {"author": "Richard Elliott Friedman", "title": "The Exodus", "year": 2017, "level": "deeper", "why": "The case for a real but smaller exodus."},
 {"author": "Joshua Berman", "title": "Created Equal", "year": 2008, "level": "deeper", "why": "How the Torah broke with the politics of Egypt and Babylon."},
 {"author": "Israel Finkelstein and Neil Asher Silberman", "title": "The Bible Unearthed", "year": 2001, "level": "deeper", "why": "The sceptical case from archaeology."},
 {"author": "Brevard Childs", "title": "The Book of Exodus", "year": 1974, "level": "scholars", "why": "The classic theological commentary."},
 {"author": "James K. Hoffmeier", "title": "Israel in Egypt", "year": 1997, "level": "scholars", "why": "The Egyptian background, from an Egyptologist who defends the story's historicity."}
]
}

CLOSING = {
"title": "Your answer",
"prompt": "What are freedom and law for? In about 300 words, answer from the story of Exodus, using at least three of its episodes, and answer the strongest objection to your view.",
"practice": "Read the whole of Exodus 1–20 over the next week, three chapters a day. Then, if you can, ask a Jewish friend or synagogue whether you might join a Passover Seder, or read a Haggadah at home.",
"music": "messiah",
"synthesis": [
 "This journey asked what freedom and law are for, following Israel from slavery in Egypt to the mountain of Sinai. Here are the short answers to its questions.",
 "How did Abraham's family become slaves? A new king who 'didn't know Joseph' feared them as foreigners and turned them into forced labour, building cities like Raamses. The first to resist were two midwives who 'feared God' more than Pharaoh. Moses' own attempt at justice, a secret killing, failed. Then 'God heard their groaning', remembered, saw and knew. Israel's founding story is unique: we were slaves. The enslaved in America read it as their own.",
 "Who is the God of Exodus? He speaks from a bush that burns and is not consumed, as the God of Abraham, Isaac and Jacob, and gives his name: 'I AM WHO I AM', meaning both 'I will be with you' and 'I am the one who simply is'. Jews do not speak the name; English Bibles print 'the LORD'; Christians hear Jesus claim it ('before Abraham was, I AM').",
 "Why the plagues and the Passover? The plagues answer Pharaoh's 'Who is Yahweh?' and judge Egypt's gods; Pharaoh hardened his own heart before God hardened it. The death of the firstborn is a real moral difficulty, which Jewish tradition refused to celebrate. The Passover meal makes every generation part of the story; Jesus died at Passover, his last supper became the Eucharist, and 'the new covenant in my blood' gave the New Testament its name.",
 "What is freedom like? At the sea the people were helpless; freedom was a gift before it was an achievement. Then they longed for Egypt again and again: it took one night to take Israel out of Egypt and forty years to take Egypt out of Israel. Freedom from Pharaoh was freedom for serving God; the same Hebrew word means 'serve' and 'slave'. The story became the West's pattern of liberation, used by the enslaved and by revolutionaries, and sometimes by conquerors; Amos insisted God frees other peoples too.",
 "What is the law for? At Sinai a freed people received a covenant that begins with grace: 'I brought you out'. The Ten Commandments bind kings, give a day of rest to slaves and animals, and forbid even coveting. Beside Hammurabi's law, Israel's has one law for rich and poor and protects the runaway slave, though it regulated slavery rather than abolishing it, and Hammurabi was kinder to debt-slaves. The people broke the covenant at once with the golden calf; it survived by mercy.",
 "Did it happen? No Egyptian record or Sinai excavation confirms it, the numbers cannot be literal, and the conquest does not fit the archaeology. But the story has real Egyptian roots, slave ancestors are not invented, and most historians think a smaller exodus lies behind it, while some think it a founding myth. Its claims about God and justice do not hang on the numbers.",
 "So what are freedom and law for? Freedom is God's gift to slaves, for love; law is freedom's shape. Its heart is love of God and of neighbour, including the stranger, 'for you were strangers in Egypt'. Because law on stone could not make people faithful, Jeremiah promised a new covenant written on the heart, which Christians believe Jesus made; that is why their Bible has an Old and a New Testament. Jews keep the Torah as their covenant way of life; the churches keep its moral law in different ways; all agree that its heart is love.",
 "One more thing. Count how much of the West comes from these chapters: the weekly day of rest; the idea that even rulers are under law; one law for rich and poor; the right to refuse an unjust order; care for the stranger; a calendar that remembers liberation; and the story every movement for freedom has told, from the American founders to Martin Luther King. When people in the West say that no one should be a slave, they are, knowingly or not, retelling Exodus."
],
"exam": [
 "'Israel's founding story is that its ancestors were slaves.' What difference does this make to its law and ethics?",
 "What does 'I AM WHO I AM' mean? Assess the main interpretations.",
 "Was the tenth plague just? Discuss with reference to Jewish and Christian readings.",
 "'Freedom from Pharaoh was freedom for God.' Discuss, with reference to Isaiah Berlin.",
 "Compare the law of Moses with the Code of Hammurabi. What, if anything, was new at Sinai?",
 "Did the law of Moses approve of slavery?",
 "Did the Exodus happen? Assess the archaeological evidence and the main scholarly positions.",
 "What did Jeremiah mean by a 'new covenant', and how have Jews and Christians understood it?",
 "Is law the opposite of freedom?"
],
"next": {"place": "Visit the Louvre in Paris to see the Code of Hammurabi, or, if you can, St Catherine's Monastery at the foot of Jebel Musa in Sinai, where pilgrims have climbed the traditional mountain of the law since the fourth century.", "book": "Jonathan Sacks, Covenant and Conversation: Exodus (2010), with a Passover Haggadah.", "journey": "who-was-jesus"}
}
