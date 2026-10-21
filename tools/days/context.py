"""Background for each story in content/bank.json: `setting` (who, where, when, what came before:
what a newcomer needs before reading) and `why` (why this story here on the path, in a sentence).
Run: python3 tools/days/context.py   (merges into content/bank.json)"""
import json, os
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

C = {
"the-life-of-st-francis-la-verna-1224-free-hands": (
 "Francis of Assisi (about 1181–1226) is one of the best-loved Christians who ever lived. Our story comes from the lives written by his companions and early followers, notably Bonaventure in the 1260s. La Verna is a wooded mountain in Tuscany, given to Francis by a nobleman as a place to pray.",
 "The path begins with setting out, and Francis set out by putting everything down: the first step of any journey is to travel light."),
"luke-15-coming-home": (
 "Jesus told this story, the parable of the prodigal son, to people who were grumbling that he ate with tax collectors and 'sinners' (Luke 15:1–2). It is the third of three stories about something lost and found: a sheep, a coin, and here a son. A younger son asking for his inheritance early was, in effect, wishing his father dead.",
 "Setting out often means coming home. Before anything else, the path shows you the father who runs to meet you."),
"matthew-4-leaving-the-nets": (
 "Jesus has just begun to teach in Galilee, in the north of Israel, around AD 28. Simon (later called Peter) and his brother Andrew were fishermen on the Sea of Galilee, a freshwater lake, working the family trade. Matthew's Gospel was written later in the first century, from the memories of Jesus's first followers.",
 "Setting out means leaving something behind. Here two fishermen leave their nets in a single moment."),
"tobit-5-6-company-on-the-road": (
 "Tobit is a Jewish story written around 200 BC, set among the exiles of the northern tribes in Assyria. Tobit is a good man who buried the dead at his own risk and went blind. It is read in Catholic and Orthodox Bibles but not in Jewish or most Protestant ones. Its angel, Raphael, appears in disguise.",
 "No one walks the road alone. The last story of setting out is about the companion God sends."),
"john-2-good-anger": (
 "It is Passover in Jerusalem, the great spring festival, and the Temple courts are full of pilgrims. To make offerings they needed animals and Temple coins, so a market had grown up in the outer court, the only part where non-Jews could pray. John places this scene at the start of Jesus's ministry; the other Gospels put it in his last week.",
 "Once you set out, you begin to see others. The first thing you notice may be what makes you rightly angry."),
"luke-16-the-man-at-the-gate": (
 "Another parable of Jesus, told to Pharisees who, Luke says, loved money (16:14). A rich man and a beggar live a gate apart. It is the only parable in which a character has a name: Lazarus, from the Hebrew Eleazar, 'God helps'. The 'bosom of Abraham' means the place of honour at the heavenly feast.",
 "Seeing others means seeing the person at your own gate, the one you pass every day."),
"the-life-of-st-jerome-from-the-golden-legend-mer": (
 "Jerome (about 347–420) translated the Bible into Latin; his translation, the Vulgate, was the Bible of the West for a thousand years. The lion story was first told of another monk, Gerasimus, and later attached to Jerome. It comes to us through The Golden Legend, a collection of saints' lives compiled by Jacobus de Voragine around 1260, the most-read book of the Middle Ages after the Bible.",
 "Seeing others includes seeing the wounded, even the frightening ones that everyone else runs from."),
"mark-1-loved-first": (
 "Mark is the shortest and probably the earliest Gospel, written around AD 65–70. It skips Jesus's birth and childhood and begins with John the Baptist calling people to be washed in the river Jordan as a sign of a new start. Jesus, about thirty, comes from Nazareth and joins the queue.",
 "A new stage: love that comes first. Jesus hears that he is loved before he has done a single public thing."),
"luke-1-saying-yes": (
 "Mary was a young Jewish woman, probably in her teens, engaged to Joseph, a builder, in Nazareth, a small village in Galilee. In that culture an engagement was a binding contract. Luke, a doctor and companion of Paul, wrote his Gospel around AD 80 after, he says, carefully investigating everything from eyewitnesses (1:1–4).",
 "Love comes first, and invites an answer. Mary's yes is the most famous answer ever given."),
"luke-1-glad-for-someone-else": (
 "Just after the angel's visit, Mary travels south to the hill country of Judea to see her older relative Elizabeth, the wife of a priest, Zechariah. Elizabeth had been childless all her life and is now six months pregnant with the child who will be John the Baptist.",
 "Love that comes first spills over. Elizabeth is glad for someone else before herself."),
"luke-2-asking-questions": (
 "Every year Jewish families went up to Jerusalem for Passover. Jesus is twelve, on the edge of adulthood in Jewish custom. Pilgrims travelled in large groups of relatives and neighbours, which is how his parents could walk a day home before noticing he was missing. This is the only story the Gospels tell of Jesus between his infancy and age thirty.",
 "Love that comes first leaves you free to ask questions. Here the boy Jesus sits among the teachers, listening and asking."),
"1-samuel-25-the-peacemaker": (
 "Around 1015 BC. David has been anointed future king but is on the run from King Saul, living in the wilderness with six hundred men. They have protected the flocks of a rich landowner, Nabal, whose name means 'fool', and David asks for a share of food at shearing time. Nabal insults him, and David sets out to kill every man of his household.",
 "Holding steady starts with provocation. Abigail shows how to stop a quarrel before it becomes a crime."),
"daniel-6-as-he-did-before": (
 "The book of Daniel is set among the Jewish exiles in Babylon and then Persia, in the 500s BC; many scholars think it was written down around 165 BC, to encourage Jews under persecution. Daniel is a young man from Jerusalem who has risen to high office at the foreign court. Jealous officials trick the king into a law they know Daniel will break.",
 "Holding steady under pressure: Daniel simply goes on praying as he always had."),
"ovid-metamorphoses-book-8-strangers-at-the-door": (
 "Ovid (43 BC–about AD 17) was the most famous poet of Augustus's Rome. His Metamorphoses, finished around AD 8, is a long poem of stories of transformation, and it shaped European painting and poetry for centuries. This is not a Bible story; Christians have always loved it because it says what the Bible says: welcome the stranger.",
 "Holding steady means keeping the door open. A Roman poet and the letter to the Hebrews say the same thing."),
"luke-24-known-in-the-breaking-of-bread": (
 "It is the Sunday after Jesus's crucifixion. That morning women have found his tomb empty, but the disciples did not believe them. Two followers, one named Cleopas, are walking home from Jerusalem to Emmaus, a village about seven miles away, sad and confused. Luke wrote this Gospel, and today is his feast day.",
 "Looking back on the road: the friends at Emmaus see who was walking with them only when they look back."),
"elijah-fed-by-ravens": (
 "Around 860 BC, in the northern kingdom of Israel. King Ahab and his queen Jezebel are promoting the worship of Baal, the Canaanite storm god said to send the rain. The prophet Elijah announces that there will be no rain at all, except at the word of Israel's God, and then he has to hide.",
 "A new stage: learning to pray. It begins with daily bread, and with a man who had to trust God for every meal."),
"moses-cries-out": (
 "Israel has escaped from slavery in Egypt and is crossing the desert of Sinai, perhaps in the 1200s BC. The people have already complained about food and been fed with manna. Now there is no water at Rephidim, and they turn on Moses. The place was afterwards named Massah and Meribah, 'testing' and 'quarrel'.",
 "Learning to pray includes crying out. Moses does not make a polished prayer; he tells God the plain, frightened truth."),
"the-servants-prayer": (
 "Abraham, the father of the Jewish people, is now very old and living in Canaan. His son Isaac, born to him and Sarah in their old age, is unmarried. Abraham will not have him marry a Canaanite, so he sends his most trusted servant, probably Eliezer of Damascus (Genesis 15:2), five hundred miles back to his relatives in northern Mesopotamia, around Haran in today's Turkey.",
 "Learning to pray: the first prayer for guidance in the Bible, made by a servant in a few plain words."),
"joan-hears-a-voice": (
 "Joan of Arc (about 1412–1431) lived during the Hundred Years' War, when England held much of France and the French heir had not been crowned. Our story comes from the official record of her trial in Rouen in 1431, where she described her voices to judges trying to condemn her. She was later declared innocent, and made a saint in 1920.",
 "Learning to pray includes learning to listen. Joan's story begins with a voice heard in a garden."),
"gethsemane-not-my-will": (
 "It is the night before Jesus's death, around AD 30. After the Passover meal, his last supper, he goes with his disciples to a garden on the Mount of Olives, across the valley from Jerusalem, called Gethsemane, 'oil press'. He knows that one of his friends has gone to betray him.",
 "Learning to pray ends at its hardest point: 'not my will, but yours'."),
"mary-of-egypt": (
 "Mary of Egypt probably lived in the 400s or 500s. Her story was written down in Greek, traditionally by Sophronius, patriarch of Jerusalem in the 630s, as told by the monk Zosimas. The Orthodox Church reads it aloud every year in Lent. It may be part history, part legend; its point is how far grace can reach.",
 "Learning to pray: a whole life turned into prayer, by a woman whose past would have shut most doors."),
"cana-they-have-no-wine": (
 "Early in Jesus's ministry, he, his mother and his first disciples are guests at a village wedding in Cana in Galilee. Weddings lasted up to a week, and running out of wine would shame the family for years. John calls what follows the first of Jesus's 'signs'.",
 "The last prayer of this stage is the simplest: Mary just tells Jesus what is wrong."),
"peter-by-the-lake": (
 "After Jesus's resurrection, some of the disciples have gone home to Galilee and back to fishing. Peter had denied knowing Jesus three times on the night of his arrest (John 18). Now, after a night of catching nothing, they see a stranger on the shore at dawn.",
 "A new stage: witnesses. It begins with Peter, who failed as a witness and is given a second chance."),
"paul-in-prison": (
 "Paul, the great missionary of the early church, is in prison in Rome, probably in the mid-60s AD under the emperor Nero, and expects to be executed. Tradition says he was beheaded there. This letter is written to Timothy, the young man he had trained and loved like a son.",
 "Witnesses: Paul at the end, looking back on a race he has finished."),
"esther-for-such-a-time": (
 "The book of Esther is set in the Persian court at Susa in the 400s BC. Esther, a Jewish orphan raised by her cousin Mordecai, has become queen without revealing she is Jewish. The king's chief minister, Haman, has obtained a decree to destroy every Jew in the empire. Jews read the story at the festival of Purim.",
 "Witnesses: Esther must decide whether to risk her life by speaking up."),
"joan-on-trial": (
 "In 1429 Joan, aged about seventeen, persuaded the French heir to let her ride with his army; she helped lift the siege of Orléans and saw him crowned. In 1430 she was captured and sold to the English. Our words come from the official record of her trial for heresy in Rouen; she was burned on 30 May 1431.",
 "Witnesses: Joan answers her judges with a wisdom they could not trap."),
"centurion-at-the-cross": (
 "It is the afternoon of Jesus's crucifixion outside Jerusalem. A centurion, a Roman officer in charge of about eighty men, commands the execution squad. He is a pagan, serving the empire that is killing Jesus, and has probably seen many crucifixions.",
 "Witnesses: the first person in Mark's Gospel to call Jesus the Son of God is the man who oversaw his death."),
"anthony-finds-paul": (
 "Anthony of Egypt (about 251–356) was the most famous of the desert fathers, the first Christian monks. Jerome wrote The Life of Paul the First Hermit around 375; it is part history and part legend, and Jerome himself may have embellished it. Its point is that the greatest saint may be someone nobody has heard of.",
 "Witnesses: on the eve of All Saints, a famous saint discovers a hidden one."),
"all-saints-great-multitude": (
 "Revelation was written by a Christian called John on the island of Patmos, around AD 95, to churches suffering under Rome. It is full of visions in symbolic language. Today is All Saints' Day, when Christians remember all the holy dead, known and unknown.",
 "The stage of witnesses ends with all of them together: the great multitude no one could count."),
"all-souls-the-burial": (
 "Jesus has died on the cross on Friday afternoon, and the Sabbath begins at sunset. Joseph of Arimathea, a rich member of the ruling council, and Nicodemus, who had once come to Jesus by night (John 3), ask for the body and bury it in a new tomb. Today, All Souls' Day, Christians pray for their own dead.",
 "A new stage, death and hope, begins with a burial done with love."),
"widow-of-zarephath": (
 "During the drought Elijah had announced, God sends him out of Israel to Zarephath, a town on the coast of Phoenicia, in today's Lebanon: the homeland of Queen Jezebel and of Baal worship. There he meets a foreign widow at the end of her food. Jesus later cited this story (Luke 4:25–26).",
 "Death and hope: a mother preparing a last meal finds there is more."),
"lazarus-unbound": (
 "Lazarus and his sisters Martha and Mary were close friends of Jesus, living in Bethany, two miles from Jerusalem. Jesus arrives four days after Lazarus's death; Jewish belief held that the soul lingered near the body for three days. John places this story just before Jesus's own death.",
 "Death and hope: the door of a tomb opens, and grief is not the last word."),
"clare-blessed-be-you": (
 "Clare of Assisi (1194–1253) was a noblewoman who, at eighteen, ran away to follow Francis and founded the order of 'Poor Clares'. Our story comes from the Legend of Saint Clare, written soon after her death, probably by Thomas of Celano, and from the testimony of her sisters gathered for her canonisation.",
 "Death and hope: a woman dies thanking God for having made her."),
"behold-your-mother": (
 "Jesus is dying on the cross. Standing near are his mother, some other women, and 'the disciple whom he loved', traditionally John. Joseph seems to have died by now, and as eldest son Jesus was responsible for his mother's care.",
 "Death and hope: even while dying, Jesus makes a family."),
"job-and-his-daughters": (
 "The book of Job is a poem, framed by a prose story, about why the innocent suffer. Its date is unknown; many scholars place it in the 500s BC. Job's friends insisted that suffering must be punishment; God rebukes them. This passage is the very end of the book.",
 "Death and hope: after loss, a life is rebuilt, not erased."),
"the-guards-at-the-tomb": (
 "The Sunday morning after Jesus's death. Matthew alone tells that the authorities had set soldiers to guard the tomb so that his disciples could not steal the body. Two women named Mary come at dawn. Today is Remembrance Sunday, when Britain and the Commonwealth remember the dead of war.",
 "Death and hope ends where it was going: the empty tomb."),
"adam-and-eve-blame": (
 "Genesis 2–3 tells of the first man and woman in a garden. They have just eaten the one fruit God told them not to. This is the oldest story in the Bible about guilt, and it is told less as history than as a mirror: the rabbis and the church fathers saw every human being in it.",
 "A new stage, justice and mercy, begins with the first excuse."),
"joseph-accused": (
 "Joseph, the favourite son of Jacob, was sold into slavery by his jealous brothers and taken to Egypt. There he became the trusted head of the household of Potiphar, an official of Pharaoh. The story is set perhaps in the 1700s or 1600s BC; it may have been written much later.",
 "Justice and mercy: an innocent man is falsely accused, and keeps his integrity anyway."),
"st-martin-cloak": (
 "Martin of Tours (about 316–397) was a Roman soldier who became a monk and a bishop in France. His life was written by his friend Sulpicius Severus while Martin was still alive. Today, 11 November, is St Martin's Day; in Germany and the Netherlands children walk with lanterns in his honour.",
 "Justice and mercy: half a cloak given to a man at the gate."),
"through-the-roof-forgiven": (
 "Early in Jesus's ministry, in Capernaum, the lakeside town that became his base. Houses were small, with flat roofs of beams, branches and packed earth, reached by an outside stair. The house is so crowded that four friends cannot get a paralysed man through the door.",
 "Justice and mercy: before healing the man's body, Jesus forgives him."),
"cosmas-and-damian-quick-to-judge": (
 "Cosmas and Damian were Christian doctors, probably martyred in Syria around 287. Very little is known for certain; their legends were collected in The Golden Legend in the 1200s. They became patron saints of doctors and pharmacists, and are still remembered in the Catholic Mass.",
 "Justice and mercy: one twin judges the other too quickly."),
"manna-enough-for-all": (
 "Israel has left Egypt and is a month into the desert. The people complain that they had better food as slaves. God promises 'bread from heaven' each morning, enough for each day, with a double portion before the Sabbath. Its name, manna, means 'What is it?'",
 "Justice and mercy: in the desert, everyone has enough and no one has too much."),
"woman-at-the-well": (
 "Jesus is travelling from Judea to Galilee through Samaria. Jews and Samaritans had been enemies for centuries over religion and history; Jews usually avoided the region. At noon, in the heat, he sits by Jacob's well and asks a Samaritan woman for water. A Jewish teacher did not normally speak to a woman alone, still less a Samaritan.",
 "The last story of justice and mercy: a man who knows everything about her, and does not condemn her."),
"the-kingdoms-refused": (
 "Straight after his baptism, Jesus goes into the Judean desert for forty days, as Israel spent forty years in the desert. There he is tempted by Satan, 'the accuser'. Each time he answers with words from Deuteronomy.",
 "A new stage, the kingdom, begins with the kingdoms Jesus refused."),
"david-without-the-armour": (
 "Around 1020 BC. The Philistines, Israel's powerful neighbours on the coast, have challenged Israel to settle a war by single combat with their champion, Goliath. King Saul and his army are terrified. David, a shepherd boy bringing food to his brothers, volunteers.",
 "The kingdom: a different kind of strength, without the king's armour."),
"melchizedek-bread-and-wine": (
 "Abraham has just rescued his nephew Lot by defeating four raiding kings. On his way back he is met by two kings: the king of Sodom, and Melchizedek, king of Salem (probably Jerusalem) and priest of God Most High. Melchizedek appears only here; Psalm 110 and the letter to the Hebrews later see him as a picture of Christ.",
 "The kingdom: a mysterious king who comes out with bread and wine."),
"the-king-with-a-towel": (
 "It is the evening of Jesus's last supper, before Passover. In that world, guests' feet, dusty from the roads, were washed by the lowest servant of the house. None of the disciples has offered to do it.",
 "The kingdom: the king takes a towel and kneels."),
"not-of-this-world": (
 "Jesus has been arrested and handed over to Pontius Pilate, the Roman governor of Judea from AD 26 to 36, the only one who could order an execution. The charge is that Jesus claims to be 'king of the Jews', which to Rome meant rebellion.",
 "The kingdom: a prisoner tells the Roman governor what kind of king he is."),
"clovis-bows-his-head": (
 "Clovis (about 466–511) united the Franks, a Germanic people, and conquered most of Roman Gaul. His baptism at Reims, around 496–508, made France a Christian kingdom; French kings were crowned at Reims ever after. Our account comes from Gregory of Tours, a bishop who wrote his History of the Franks about seventy years later.",
 "The kingdom: a conquering king bows his head."),
"remember-me-christ-the-king": (
 "Jesus is crucified between two criminals, under a sign mocking him as 'king of the Jews'. The crowds, the rulers and the soldiers jeer. Today is the feast of Christ the King, the last Sunday of the church's year, created by Pope Pius XI in 1925 as dictators were rising in Europe.",
 "The church's year ends by asking who really rules. The answer is a dying king who promises a thief paradise."),
"noah-shut-in": (
 "The flood story in Genesis 6–9 has close parallels in older Babylonian stories, such as the Epic of Gilgamesh. In Genesis, God grieves that the earth is full of violence and saves Noah, his family and the animals in a great wooden ark. Today Noah has built it, and the waiting begins.",
 "A new stage: waiting. It begins with Noah, shut in by God, waiting for the rain."),
"luke-5-all-night-and-nothing": (
 "Jesus is teaching by the Lake of Gennesaret, another name for the Sea of Galilee. Simon Peter and his partners have fished all night, when fishing was best, and caught nothing. They are washing their nets, finished for the day, when Jesus borrows Simon's boat to use as a pulpit.",
 "Waiting: after a night of nothing, one more try at someone else's word."),
"flight-until-i-tell-you": (
 "Wise men from the east have visited the infant Jesus in Bethlehem. King Herod the Great, a ruthless ruler who killed several of his own sons, has learned of a newborn 'king of the Jews'. Egypt, a few days' journey away, had large Jewish communities and was outside Herod's power.",
 "Waiting: Joseph is told to flee and stay 'until I tell you', without knowing how long."),
"golden-calf-moses-delayed": (
 "Israel has arrived at Mount Sinai and agreed to the covenant. Moses has gone up the mountain to receive the law and has been gone for forty days. The people, at the foot of the mountain, lose patience. The calf or young bull was a common symbol of divine power in the ancient Near East.",
 "Waiting: what happens when people cannot bear to wait."),
"ascension-wait-for-the-promise": (
 "Forty days after his resurrection, Jesus leads his followers out to the Mount of Olives and is taken from their sight. Acts, written by Luke as the sequel to his Gospel, begins here. The 'promise' is the Holy Spirit, who will come at Pentecost ten days later.",
 "Waiting: the disciples are told not to rush off, but to wait and pray together."),
"simeon-and-anna": (
 "Forty days after Jesus's birth, Mary and Joseph bring him to the Temple in Jerusalem, as the law required for a firstborn son, with the offering of the poor: two birds. There they meet two very old people who have spent their lives waiting for God to keep his promise.",
 "Waiting ends with Simeon and Anna, who waited a lifetime and were not disappointed."),
"john-in-the-desert": (
 "John the Baptist was the son of the priest Zechariah and Elizabeth, Mary's relative, born a few months before Jesus. Luke dates his public appearance precisely, to the fifteenth year of the emperor Tiberius, about AD 28. The Jewish historian Josephus also describes John and his execution. Today is Advent Sunday, the first day of the church's new year.",
 "Advent begins, and waiting becomes getting ready. The first figure of Advent is John in the wilderness."),
"andrew-brings-his-brother": (
 "Andrew, a fisherman from Bethsaida, was first a follower of John the Baptist. When John pointed to Jesus, Andrew followed him. Today is St Andrew's Day. Tradition says Andrew was crucified at Patras in Greece on an X-shaped cross, which is why the Scottish flag, his saltire, has that shape.",
 "Prepare the way: Andrew's first act is to fetch his brother."),
"what-should-we-do": (
 "Crowds are coming out to the Jordan to hear John the Baptist and be baptised. He greets them harshly, calling them a 'brood of vipers', and warns that being Abraham's descendants will not save them. The tax collectors worked for Rome and were notorious for overcharging; the soldiers were probably Herod's.",
 "Prepare the way: the crowds ask the most practical question in the Bible."),
"elijahs-mantle": (
 "Elijah, the great prophet of the northern kingdom, is near the end of his life. Elisha has been his assistant and disciple for years. They walk together from Gilgal to Bethel to Jericho and across the Jordan, and Elisha refuses to leave him. A mantle was a prophet's cloak, the sign of his calling.",
 "Prepare the way: Elijah hands on his cloak. Jews still expect Elijah to return before the Messiah."),
"anthony-makes-room": (
 "Anthony of Egypt (about 251–356) became the father of Christian monks. His life was written by Athanasius, bishop of Alexandria, around 360, soon after his death, and it was read across the Roman world; Augustine was moved by it on the eve of his own conversion.",
 "Prepare the way: Anthony makes room in his life by giving away what filled it."),
"john-tells-the-truth": (
 "Herod Antipas, son of Herod the Great, ruled Galilee under Rome. He had divorced his wife to marry Herodias, the wife of his brother. John the Baptist publicly said this was against God's law, and Herod had him imprisoned. Josephus confirms that Herod executed John.",
 "Prepare the way: John tells a king the truth, and pays for it."),
"walking-on-the-water": (
 "Jesus has just fed five thousand people. He sends his disciples ahead by boat across the Sea of Galilee while he prays alone on a mountain. In the night a storm rises; the 'fourth watch' is between three and six in the morning. The lake is known for sudden violent winds.",
 "A new stage, light in darkness, begins at the darkest hour of the night, on the water."),
"drawn-from-the-water": (
 "Pharaoh, fearing the growing number of Hebrew slaves, has ordered every newborn Hebrew boy to be thrown into the Nile. A Levite woman, later named as Jochebed, hides her baby for three months, then puts him in a basket among the reeds. His older sister Miriam watches.",
 "Light in darkness: a baby in a basket, in the darkest decree of all."),
"joachim-and-anna-giving-in-the-dark": (
 "The Bible says nothing about Mary's parents. The Protevangelium of James, written in the 100s, is not Scripture, but it shaped Christian art and the church's calendar. Today, 8 December, Catholics keep the feast of the Conception of Mary, and the Orthodox keep it the following day.",
 "Light in darkness: years of childlessness, met with generosity."),
"light-on-the-road": (
 "Saul of Tarsus was a brilliant young Jewish scholar and a Pharisee who saw the followers of Jesus as dangerous heretics. He had watched the stoning of Stephen, the first Christian martyr, and now travels to Damascus with authority to arrest Christians there. He will become Paul, the apostle.",
 "Light in darkness: a light so bright that the persecutor is blinded, and begins to see."),
"last-supper-on-the-night": (
 "It is the night of Jesus's arrest, at a Passover meal in an upper room in Jerusalem. Passover remembered Israel's escape from Egypt: the lamb, the unleavened bread, the cups of wine. Jesus gives the bread and wine a new meaning. Christians have repeated this meal ever since.",
 "Light in darkness: 'on the night he was betrayed', Jesus gives thanks."),
"a-great-light": (
 "Isaiah 9 was spoken around 730 BC, when Assyria had overrun the north of Israel, the region of Galilee. 1 Peter was written to persecuted Christians in the later first century. The Apostles' Creed says Christ 'descended into hell': the old picture of his visit to the dead, called the Harrowing of Hell.",
 "Light in darkness: the light reaching even the place of the dead."),
"lucy-would-not-be-moved": (
 "Lucy was martyred in Syracuse in Sicily around 304, in the last and worst Roman persecution under Diocletian. Her legend was written later and gathered in The Golden Legend. Her feast is 13 December, once the shortest day of the year; in Sweden girls in white with candles in their hair celebrate it.",
 "Light in darkness: on the eve of St Lucy's Day, a girl who would not be moved."),
"immanuel-god-with-us": (
 "Around 735 BC. Ahaz, king of Judah, is terrified: the kings of Israel and Damascus are marching on Jerusalem to force him into an alliance against Assyria. The prophet Isaiah tells him to trust God and offers him a sign. Ahaz refuses. Matthew later read the sign as fulfilled in Jesus.",
 "A new stage: God comes close. It begins with a name, Immanuel, 'God with us'."),
"joseph-quietly": (
 "Joseph, a builder from Nazareth, is engaged to Mary. Engagement was legally binding, and could only be ended by divorce. He discovers she is pregnant, and the child is not his. The law allowed him to accuse her publicly.",
 "God comes close: to a righteous man about to do the decent thing quietly."),
"joseph-takes-mary-home": (
 "Joseph has decided to divorce Mary quietly. That night an angel tells him in a dream that the child is from the Holy Spirit, and that he is to name him Jesus, 'God saves'.",
 "God comes close: Joseph wakes, and does what he was told."),
"zechariah-his-name-is-john": (
 "Nine months earlier, the old priest Zechariah was told in the Temple that his wife Elizabeth would bear a son. He did not believe it, and was struck dumb. Now the baby is born, and the relatives gather on the eighth day for his circumcision and naming, expecting him to be named after his father.",
 "God comes close: a silent father's first words are a song."),
"the-road-to-bethlehem": (
 "Luke says the emperor Augustus ordered a census, and everyone went to their ancestral town to register. Joseph, a descendant of King David, goes from Nazareth to Bethlehem, David's town, about ninety miles, with Mary heavily pregnant. Historians debate the date of the census Luke mentions.",
 "God comes close: on a long road, to the town of David."),
"the-peaceable-kingdom": (
 "Isaiah, around 730 BC, promises a new king from the 'stump of Jesse', David's father: as if David's royal family tree had been cut down and a shoot would grow from the stump. It is one of the great Advent readings.",
 "God comes close: the promise of the peace he will bring."),
"no-room": (
 "Mary and Joseph have reached Bethlehem. The 'inn' may have been the guest room of a relative's house; many village houses kept animals at night in a lower room, with a feeding trough. Either way, there was no room, and the baby is laid in the manger.",
 "Christmas begins: no room, and a feeding trough for a cradle."),
"keeping-watch": (
 "Shepherds were among the poorest workers in the land, out with the flocks through the night, and often looked down on. The fields near Bethlehem were where David had kept sheep a thousand years before.",
 "Christmas: the news comes first to shepherds on the night shift."),
"glory-in-the-highest": (
 "The angel has just told the shepherds of the birth. Then a great company of angels appears. Their song, in Latin 'Gloria in excelsis Deo', became the opening of the Gloria, sung in churches for more than fifteen hundred years.",
 "Christmas: heaven sings."),
"the-shepherds-go": (
 "The angels are gone and the night is dark again. The shepherds have to decide whether to leave their flocks and go into Bethlehem to see.",
 "Christmas: the shepherds go and see for themselves."),
"mary-ponders": (
 "The shepherds have found Mary, Joseph and the baby, and told everyone what the angels said. Luke says Mary kept all these things in her heart; some scholars think she was one of his sources. Today is Christmas Eve.",
 "Christmas Eve: Mary keeps it all in her heart."),
"the-word-became-flesh": (
 "John's Gospel, probably the last written, around AD 90–100, does not tell the nativity. It begins instead before creation, echoing the first words of Genesis, 'In the beginning'. The Greek word for 'Word', logos, also meant reason, the order of the universe, to the Greek philosophers. Today is Christmas Day.",
 "Everything on the path has led here: God with us."),
}

if __name__ == '__main__':
    p = os.path.join(ROOT, 'content', 'bank.json'); b = json.load(open(p))
    miss = [k for k in b if k not in C]; extra = [k for k in C if k not in b]
    print('missing', miss, 'extra', extra)
    for k, (s, w) in C.items():
        if k in b: b[k]['setting'] = s; b[k]['why'] = w
    # a better verse for the servant's prayer: the prayer itself, not the genealogy
    sp = b['the-servants-prayer']['story']
    if sp['verseRef'] == 'Genesis 24:15':
        sp['verse'] = '“Yahweh, the God of my master Abraham, please give me success today, and show kindness to my master Abraham.'
        sp['verse'] = 'He said, “Yahweh, the God of my master Abraham, please give me success today, and show kindness to my master Abraham.'
        sp['verseRef'] = 'Genesis 24:12'
    json.dump(b, open(p, 'w'), ensure_ascii=False, indent=1); open(p, 'a').write('\n')
