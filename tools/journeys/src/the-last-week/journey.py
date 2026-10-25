import os, importlib
from sA import S1, S2
try:
    from sB import S3, S4
    from sC import S5, S6, S7
    SESSIONS = [S1, S2, S3, S4, S5, S6, S7]
except ImportError:
    SESSIONS = [S1, S2]

HALL = "new-testament"; AFTER = "sermon-on-the-mount"; LATER_TITLE = "The last week and the cross"

META = {
"id": "the-last-week",
"title": "The last week and the cross",
"question": "What happened in Jerusalem, and did he rise?",
"line": "Seven sessions walking through Jesus's last week as a historian walks through a city: the entry and the Temple, the supper, the trials, the cross, the tomb, the case against the resurrection, and the verdict on Easter.",
"why": "Christianity stands or falls on one week in Jerusalem around AD 30. Everything else in the faith, its worship, its ethics, its hope in the face of death, depends on what happened between Palm Sunday and Easter Day. This journey reads the Gospels' accounts of that week beside the prophets they echo, Roman and Jewish writers who knew Pilate and the cross, and the archaeology, then gives the natural explanations of Easter their full weight before asking what best explains the evidence. It is written at the depth of a first-year university course, for anyone.",
"level": "foundation",
"follows": "A first-year theology paper on the Passion narratives of the Gospels and the historical question of the resurrection, with elements of a paper on Jesus in his Jewish and Roman setting.",
"art": "starck-raising-cross",
"status": "draft",
"before": ["sermon-on-the-mount", "who-was-jesus"],
"outcomes": [
 "Explain the setting of Passover in Roman Jerusalem and read Jesus's entry and Temple action as prophetic signs drawing on Zechariah and Jeremiah.",
 "Set out the dating problem of the Last Supper and the main solutions, and explain what Jesus's words over the bread and cup meant, with the main church traditions side by side.",
 "Explain why Jesus was handed to Pilate and crucified, what Philo and Josephus say about Pilate, and how the charge that 'the Jews' killed Jesus was used and later repudiated.",
 "Describe Roman crucifixion from Cicero, Josephus and archaeology, and explain why a crucified Messiah counts as evidence that the first Christians did not invent their message.",
 "Weigh the evidence for the empty tomb, including the women witnesses, Mark's ending and the differences between the Gospels.",
 "State the natural explanations of the resurrection at full strength, from Strauss to Lüdemann and Ehrman, assess them against the replies of Wright and Allison, and explain Jewish and Muslim views of the cross."
],
"people": [
 {"name": "Jesus of Nazareth", "years": "c. 4 BC – AD 30 or 33", "line": "A Jewish teacher from Galilee, crucified in Jerusalem under Pontius Pilate at Passover; his followers proclaimed that God had raised him from the dead."},
 {"name": "Simon Peter", "years": "died c. AD 64", "line": "Leader of the twelve, who denied Jesus three times on the night of his arrest and became the first witness of the resurrection named by Paul."},
 {"name": "Judas Iscariot", "years": "died c. AD 30", "line": "One of the twelve, who led the high priest's men to Jesus at night."},
 {"name": "Mary Magdalene", "years": "1st century", "line": "A follower from Galilee, at the cross and the burial, and in every Gospel the first to find the tomb empty."},
 {"name": "Thomas", "years": "1st century", "line": "One of the twelve, who refused to believe without touching the wounds, and then said 'My Lord and my God'."},
 {"name": "Joseph of Arimathea", "years": "1st century", "line": "A member of the council who asked Pilate for Jesus's body and laid it in a rock tomb."},
 {"name": "Caiaphas", "years": "high priest AD 18–36", "line": "The high priest who handed Jesus to Pilate; a family ossuary probably his was found in Jerusalem in 1990."},
 {"name": "Pontius Pilate", "years": "prefect of Judea AD 26–36", "line": "Roman governor who condemned Jesus to be crucified as 'King of the Jews'; named on a stone found at Caesarea in 1961."},
 {"name": "Paul of Tarsus", "years": "died c. AD 64–67", "line": "A Pharisee who persecuted the first Christians, then saw the risen Jesus, as he believed; his letters are the earliest Christian writings."},
 {"name": "Cicero", "years": "106–43 BC", "line": "Roman orator whose speeches against Verres describe the crucifixion of a Roman citizen."},
 {"name": "Philo of Alexandria", "years": "c. 20 BC – c. AD 50", "line": "Jewish philosopher who described Pilate's character in his Embassy to Gaius."},
 {"name": "Flavius Josephus", "years": "AD 37 – c. 100", "line": "Jewish priest and historian of the war with Rome, who describes Pilate, Passover crowds and mass crucifixions."},
 {"name": "Celsus", "years": "2nd century", "line": "Greek philosopher, the first known writer against Christianity, who said the appearances were the visions of an excitable woman."},
 {"name": "Hermann Samuel Reimarus", "years": "1694–1768", "line": "German scholar, the 'Wolfenbüttel Fragmentist', who argued that the disciples stole the body."},
 {"name": "David Friedrich Strauss", "years": "1808–1874", "line": "German theologian whose Life of Jesus (1835) explained the resurrection as visions and legend."},
 {"name": "George Eliot", "years": "1819–1880", "line": "The novelist Mary Ann Evans, who translated Strauss into English in 1846."},
 {"name": "Raymond E. Brown", "years": "1928–1998", "line": "American Catholic scholar, author of The Death of the Messiah (1994)."},
 {"name": "Martin Hengel", "years": "1926–2009", "line": "German scholar whose Crucifixion (1977) gathered the ancient evidence on the cross."},
 {"name": "Gerd Lüdemann", "years": "1946–2021", "line": "German scholar who argued that the appearances were visions, starting with Peter's grief and guilt."},
 {"name": "Bart D. Ehrman", "years": "living", "line": "American New Testament scholar and agnostic, who accepts that some disciples had visions but doubts the empty tomb."},
 {"name": "N. T. Wright", "years": "living", "line": "British New Testament scholar and former bishop of Durham, whose The Resurrection of the Son of God (2003) argues that only a real resurrection explains the evidence."},
 {"name": "Dale C. Allison Jr.", "years": "living", "line": "American scholar who weighs the case on both sides and concludes that history alone cannot settle it."}
],
"timeline": [
 {"year": "c. 609 BC", "text": "Jeremiah's sermon against the Temple."},
 {"year": "from 520 BC", "text": "Zechariah prophesies in Jerusalem."},
 {"year": "70 BC", "text": "Cicero prosecutes Verres, governor of Sicily, for crucifying a Roman citizen."},
 {"year": "20/19 BC", "text": "Herod the Great begins rebuilding the Temple."},
 {"year": "AD 6", "text": "Judea becomes a Roman province."},
 {"year": "AD 26–36", "text": "Pontius Pilate is prefect of Judea."},
 {"year": "AD 30 or 33", "text": "Jesus is crucified at Passover."},
 {"year": "c. AD 41", "text": "Philo writes the Embassy to Gaius."},
 {"year": "c. AD 53–55", "text": "Paul writes 1 Corinthians."},
 {"year": "c. AD 65–70", "text": "Mark's Gospel."},
 {"year": "AD 70", "text": "Rome destroys Jerusalem and the Temple; Josephus watches the crucifixions."},
 {"year": "c. AD 90–100", "text": "John's Gospel."},
 {"year": "c. AD 116", "text": "Tacitus records that Christ was executed under Pilate."},
 {"year": "AD 325", "text": "The Council of Nicaea agrees that all churches keep Easter on the same Sunday."},
 {"year": "1778", "text": "Lessing publishes Reimarus's fragment on the aim of Jesus and his disciples."},
 {"year": "1835", "text": "Strauss's Life of Jesus; George Eliot's translation follows in 1846."},
 {"year": "1961", "text": "The Pilate stone is found at Caesarea."},
 {"year": "1965", "text": "The Second Vatican Council's Nostra Aetate rejects blaming all Jews for Jesus's death."},
 {"year": "1968", "text": "The heel bone of a crucified man, Yehohanan, is found in Jerusalem."},
 {"year": "2003", "text": "N. T. Wright's The Resurrection of the Son of God."}
],
"places": [
 {"name": "The Mount of Olives", "where": "East of the old city, Jerusalem", "why": "Where the Palm Sunday procession began, and the garden of Gethsemane at its foot."},
 {"name": "The Temple Mount and the Western Wall", "where": "Jerusalem", "why": "Herod's vast Temple platform, where Jesus overturned the tables; the Western Wall is part of its retaining wall."},
 {"name": "The Church of the Holy Sepulchre", "where": "Jerusalem", "why": "Built by the emperor Constantine from 326 over the rock of Golgotha and the tomb remembered as Jesus's; shared today by several churches."},
 {"name": "The Israel Museum", "where": "Jerusalem", "why": "Holds the heel bone of the crucified Yehohanan, the Caiaphas ossuary and the Pilate stone."},
 {"name": "Caesarea Maritima", "where": "Israel's Mediterranean coast", "why": "The Roman governors' capital, where the stone naming Pontius Pilate as prefect was found in the theatre in 1961."},
 {"name": "The Cenacle", "where": "Mount Zion, Jerusalem", "why": "The traditional upper room of the Last Supper, in a Crusader-period building."},
 {"name": "Messina", "where": "Sicily", "why": "Ancient Messana, where Verres crucified the Roman citizen Gavius within sight of Italy."}
],
"glossary": [
 {"term": "Apocalyptic", "def": "Jewish hope, from about 200 BC, that God would soon act to end the present age, judge the world and raise the dead."},
 {"term": "Appearances", "def": "The meetings with the risen Jesus that his followers reported, in Jerusalem and in Galilee."},
 {"term": "Chief priests", "def": "The high priest and the leading priestly families who ran the Temple and dealt with Rome."},
 {"term": "Christophany", "def": "An appearance of Christ, such as Paul's on the road to Damascus."},
 {"term": "Covenant", "def": "A binding agreement between God and his people; at Sinai sealed with blood, and at the Last Supper renewed in Jesus's blood."},
 {"term": "Criterion of embarrassment", "def": "Historians' rule that a story awkward for the people who told it is unlikely to have been invented by them."},
 {"term": "Crucifixion", "def": "Roman execution by nailing or tying a person to a cross to die slowly in public; used for slaves, rebels and the worst criminals."},
 {"term": "Easter", "def": "The feast of the resurrection, the oldest and greatest Christian feast; in most languages called Pascha, from the Hebrew for Passover."},
 {"term": "Empty tomb", "def": "The report that the women, and then Peter, found Jesus's tomb open and his body gone on the Sunday morning."},
 {"term": "Eucharist", "def": "From the Greek for 'thanksgiving': the meal of bread and wine Jesus commanded at the Last Supper, also called the Mass, Holy Communion or the Lord's Supper."},
 {"term": "Flogging", "def": "Roman beating with a whip weighted with bone or metal, often before crucifixion."},
 {"term": "Golgotha", "def": "Aramaic for 'the place of a skull', the site outside Jerusalem's wall where Jesus was crucified; Calvary in Latin."},
 {"term": "Good Friday", "def": "The Friday of Holy Week, when Christians remember the crucifixion."},
 {"term": "Hallel", "def": "Psalms 113 to 118, sung at the feasts and at the end of the Passover meal."},
 {"term": "Hallucination hypothesis", "def": "The view that the disciples' experiences of the risen Jesus were visions produced by their own minds, as in grief."},
 {"term": "Holy Week", "def": "The week from Palm Sunday to Easter, in which Christians follow Jesus's last days."},
 {"term": "Hosanna", "def": "Hebrew for 'save us, please', from Psalm 118; shouted as a welcome when Jesus entered Jerusalem."},
 {"term": "Isa", "def": "The Qur'an's name for Jesus, honoured in Islam as a prophet and the Messiah."},
 {"term": "Maundy Thursday", "def": "The Thursday of Holy Week, remembering the Last Supper; from the Latin mandatum, Jesus's 'new commandment' to love."},
 {"term": "Messiah", "def": "Hebrew for 'anointed one' (Greek christos, Christ): the king from David's line whom Israel hoped for."},
 {"term": "Nostra Aetate", "def": "The Second Vatican Council's declaration of 1965 on other religions, which rejected blaming the Jewish people for Jesus's death."},
 {"term": "Ossuary", "def": "A stone box into which a family gathered a person's bones a year or so after burial; common in Jerusalem in Jesus's time."},
 {"term": "Palm Sunday", "def": "The Sunday before Easter, remembering Jesus's entry into Jerusalem."},
 {"term": "Passover", "def": "Pesach, the Jewish feast remembering the escape from Egypt, with a lamb, unleavened bread and wine."},
 {"term": "Prefect", "def": "The title of the Roman governors of Judea from AD 6 to 41, including Pontius Pilate; later governors were called procurators."},
 {"term": "Praetorium", "def": "A Roman governor's headquarters; in Jerusalem probably Herod's palace, where Pilate stayed at the feasts."},
 {"term": "Real presence", "def": "The belief that Christ's body and blood are truly present in the Eucharist, held in different ways by Catholics, Orthodox, Lutherans and many Anglicans."},
 {"term": "Resurrection", "def": "In Jewish hope, God raising the dead to bodily life at the end of the age; Christians say it happened to Jesus first."},
 {"term": "Sabbath", "def": "The seventh day, from Friday sunset to Saturday sunset, a day of rest on which no work, including burial, could be done."},
 {"term": "Sanhedrin", "def": "The Jewish council in Jerusalem, led by the high priest."},
 {"term": "Sign-act", "def": "A prophet's message acted out in public, such as Jeremiah smashing a jar."},
 {"term": "Swoon theory", "def": "The view that Jesus did not die on the cross but revived in the tomb."},
 {"term": "Synoptic Gospels", "def": "Matthew, Mark and Luke, which share much material and can be 'seen together'."},
 {"term": "Temple", "def": "The house of God in Jerusalem, rebuilt by Herod and destroyed by Rome in AD 70; the only place of sacrifice."},
 {"term": "Titulus", "def": "The notice of the charge carried before a condemned man or fixed to his cross; for Jesus, 'The King of the Jews'."},
 {"term": "Transubstantiation", "def": "The Catholic teaching that in the Mass the substance of the bread and wine becomes Christ's body and blood."},
 {"term": "Unleavened bread", "def": "Bread made without yeast, eaten at Passover in memory of the hasty escape from Egypt."}
],
"reading": [
 {"author": "Marcus J. Borg and John Dominic Crossan", "title": "The Last Week", "year": 2006, "level": "start", "why": "A day-by-day reading of Mark's account of Holy Week."},
 {"author": "N. T. Wright", "title": "Surprised by Hope", "year": 2007, "level": "start", "why": "A popular account of the resurrection and what it means for Christian hope."},
 {"author": "Bart D. Ehrman", "title": "How Jesus Became God", "year": 2014, "level": "start", "why": "An agnostic historian on the burial, the visions and the rise of belief in the resurrection."},
 {"author": "Martin Hengel", "title": "Crucifixion in the Ancient World and the Folly of the Message of the Cross", "year": 1977, "level": "deeper", "why": "The ancient evidence on crucifixion, short and unforgettable."},
 {"author": "Dale C. Allison Jr.", "title": "The Resurrection of Jesus: Apologetics, Polemics, History", "year": 2021, "level": "deeper", "why": "The fairest weighing of the evidence on both sides."},
 {"author": "Raymond E. Brown", "title": "The Death of the Messiah", "year": 1994, "level": "scholars", "why": "The standard commentary on the Passion narratives, in two volumes."},
 {"author": "N. T. Wright", "title": "The Resurrection of the Son of God", "year": 2003, "level": "scholars", "why": "The fullest historical case for the resurrection."},
 {"author": "Gerd Lüdemann", "title": "The Resurrection of Jesus: History, Experience, Theology", "year": 1994, "level": "scholars", "why": "The fullest case for the vision hypothesis (German 1994)."}
]
}

CLOSING = {"title": "Your answer", "prompt": "", "practice": "", "music": "", "synthesis": [""], "exam": [], "next": {}}
try:
    from closing import CLOSING
except ImportError:
    pass
