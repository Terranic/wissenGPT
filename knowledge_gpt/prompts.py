# flake8: noqa
from langchain.prompts import PromptTemplate

## Use a shorter template to reduce the number of tokens in the prompt
template = """Create a final answer to the given questions using the provided document excerpts(in no particular order) as references. ALWAYS include a "SOURCES" section in your answer including only the minimal set of sources needed to answer the question. If you are unable to answer the question, simply state that you do not know. Do not attempt to fabricate an answer and leave the SOURCES section empty.

---------

QUESTION: What  is the purpose of ARPA-H?
=========
Content: More support for patients and families. \n\nTo get there, I call on Congress to fund ARPA-H, the Advanced Research Projects Agency for Health. \n\nIt’s based on DARPA—the Defense Department project that led to the Internet, GPS, and so much more.  \n\nARPA-H will have a singular purpose—to drive breakthroughs in cancer, Alzheimer’s, diabetes, and more.
Source: 1-32
Content: While we’re at it, let’s make sure every American can get the health care they need. \n\nWe’ve already made historic investments in health care. \n\nWe’ve made it easier for Americans to get the care they need, when they need it. \n\nWe’ve made it easier for Americans to get the treatments they need, when they need them. \n\nWe’ve made it easier for Americans to get the medications they need, when they need them.
Source: 1-33
Content: The V.A. is pioneering new ways of linking toxic exposures to disease, already helping  veterans get the care they deserve. \n\nWe need to extend that same care to all Americans. \n\nThat’s why I’m calling on Congress to pass legislation that would establish a national registry of toxic exposures, and provide health care and financial assistance to those affected.
Source: 1-30
=========
FINAL ANSWER: The purpose of ARPA-H is to drive breakthroughs in cancer, Alzheimer’s, diabetes, and more.
SOURCES: 1-32

---------

QUESTION: {question}
=========
{summaries}
=========
FINAL ANSWER:"""


## Use a shorter template to reduce the number of tokens in the prompt
template2 = """
Erzeuge eine endgültige Antwort zur den angegebenen Fragen mit Hilfe des angegebenen Dokuments als Referenz für Auszüge (in beliebiger Reihenfolge). 
Füge immer einen "QUELLEN" Abschnitt in deiner Antwort einschliesslich einer minimalen Anzahl von QUELLEN, um die Frage zu beantworten. 
Wenn Gesetzesangaben, Paragraphen, Verordnungen, Verweise genannt sind, gib sie immer auch an. 
Wenn du die Frage nicht sicher beantworten kannst, sage dies und zeige auch keine QUELLE an. Antworten dürfen nicht ohne QUELLE fabriziert sein.

FRAGE: Wie werden Gewinne/Verluste aus dem Krypto-Trading besteuert?
=========
Inhalt: Wird der An- und Verkauf von Kryptowährungen als Privatperson unternommen, sind § 22 Nr. 2, § 23 Abs. 1 Nr. 2 EStG einschlägig. Es handelt sich hierbei um ein privates Veräußerungsgeschäft von „anderen Wirtschaftsgütern“. Gemäß § 23 Abs. 3 Satz 1 EStG ist der Gewinn oder Verlust der Unterschied zwischen Veräußerungspreis einerseits und den Anschaffungs- und Werbungskosten andererseits. Es muss also nur der Anschaffungspreis vom Veräußerungspreis abgezogen werden. Die Gebühren beim Handel auf den Börsen sind Werbungskosten und damit abzugsfähig.
Quelle: § 22 Nr. 2, § 23 Abs. 1 Nr. 2 EStG
Inhalt: In § 23 Abs. 3 Satz 5 EStG ist zudem eine Freigrenze von 600 € vorgesehen, bis zu deren Erreichen alle privaten Veräußerungsgeschäfte des Veranlagungszeitraums steuerfrei bleiben. Wird die Grenze überschritten, muss allerdings der gesamte Betrag ab dem ersten Euro versteuert werden. Die Einkommensteuer fällt dabei nicht erst beim Umtausch von Kryptowährungen in Euro oder eine andere Fremdwährung an, sondern bereits bei einem Tausch in eine beliebige andere Kryptowährung oder auch beim Kauf von Waren oder Dienstleistungen mit einer solchen. Vergeht aber zwischen Anschaffung und Veräußerung mehr als ein Jahr, greift die Haltefrist des § 23 Abs. 1 Nr. 2 Satz 1 EStG. In diesen Fällen ist der gesamte Veräußerungsgewinn nicht steuerbar.
Quelle: § 23 Abs. 3 Satz 5 EStG
Inhalt: Zur Bestimmung der Anschaffungskosten und des Veräußerungsgewinns sowie zur Bestimmung der Einhaltung der Haltefrist wird in der Regel die sogenannte FIFO-Methode aus § 23 Abs. 1 Nr. 2 Satz 3 EStG herangezogen. Zwar schreibt das Gesetz diese First-In-First-Out-Methode nicht für Kryptowährungen vor, in der Praxis wird sie aber weitgehend angewendet. Auch das BMF hat sich für die Anwendung der FIFO-Methode innerhalb des BMF-Schreibens ausgesprochen. Es werden allerdings auch andere Meinungen vertreten und eine Berechnung nach der LIFO-Methode oder – zur Bestimmung der Anschaffungskosten – nach Durchschnittswerten vorgeschlagen.
Wird der Handel mit Kryptowährungen gewerblich durchgeführt (z.B. durch Anbieten einer Webseite zum Umtausch von Kryptowährungen) sind die Erträge als solche aus Gewerbebetrieb gem. § 15 EStG zu versteuern. In diesem Rahmen gibt es insbesondere keine Haltefrist. Neben der Einkommensteuer muss in dem Fall auch Gewerbesteuer gezahlt werden. Allerdings sieht § 11 Abs. 1 Satz 3 Nr. 1 GewStG einen Freibetrag in Höhe von 24.500 Euro vor. Zudem hat sich der Händler mit Fragen der Umsatzsteuerbarkeit seiner Tätigkeit zu beschäftigen.
Quelle: 1-31
=========
FINALE ANTWORT: Gewinne und Verluste aus Kryptowährungen gehören zu den Privaten Veräußerungsgeschäften, wie z.B. auch der Verkauf von Antiquitäten.
Der Gewinn unterliegt nicht der Abgeltungssteuer, sondern wird mit dem persönlichen Steuersatz bei der Einkommensteuer versteuert.
Es gibt eine Freigrenze von 600 Euro im Jahr, wird diese überschritten, ist für die gesamten Gewinne Steuer zu zahlen, nicht nur für den Betrag, der die Freigrenze überschreitet!
Liegt zwischen Kauf und Verkauf mehr als ein Jahr, sind die Gewinne steuerfrei. Verluste können dann allerdings auch nicht angesetzt werden. Gewinne aus dem Verkauf von Kryptowährungen können mit Verlusten aus anderen privaten Veräußerungsgeschäften verrechnet werden.
Es gibt eine Freigrenze von 600 Euro, alle Gewinne unter dieser Grenze sind steuerfrei. Durch geschickte Nutzung der FIFO- oder LIFO-Methode kann der Gewinn optimiert werden, falls im Laufe der Zeit mehrmals Bitcoins gekauft wurden.
QUELLEN: § 22 Nr. 2, § 23 Abs. 1 Nr. 2 EStG, § 23 Abs. 3 Satz 5 EStG, 1-31
---------

FRAGE: {question}
=========
{summaries}
=========
FINALE ANTWORT:"""

STUFF_PROMPT = PromptTemplate(
    template=template2, input_variables=["summaries", "question"]
)

