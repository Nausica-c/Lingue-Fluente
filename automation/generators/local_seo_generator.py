import random


class LocalSEOGenerator:

    def __init__(self):
        pass

    # -------------------------
    # GENERAZIONE ARTICOLO
    # -------------------------

    def generate(self, prompt, context=None):

        title = self.extract(prompt, "KEYWORD") or "Imparare una lingua velocemente"
        cluster = self.extract(prompt, "CLUSTER") or "metodo"

        return self.build_article(title, cluster)

    # -------------------------
    # ESTRAI VALORI DAL PROMPT
    # -------------------------

    def extract(self, text, key):

        for line in text.split("\n"):
            if key in line:
                return line.split(":")[-1].strip()

        return None

    # -------------------------
    # GENERATORE SEO STATICO INTELLIGENTE
    # -------------------------

    def build_article(self, title, cluster):

        hooks = [
            "Molte persone pensano che imparare una lingua sia difficile, ma non è così.",
            "Il segreto non è studiare di più, ma studiare meglio.",
            "Puoi diventare fluente più velocemente di quanto immagini."
        ]

        sections = [
            ("Perché questo metodo funziona", "La chiave è la costanza quotidiana e l’esposizione naturale."),
            ("Errori da evitare", "Tradurre parola per parola rallenta il processo."),
            ("Metodo pratico", "Usa input quotidiano: ascolto, lettura e ripetizione."),
            ("Esempio reale", "20 minuti al giorno possono cambiare completamente il tuo livello.")
        ]

        article = f"<h1>{title}</h1>\n"

        article += f"<p>{random.choice(hooks)}</p>\n"

        for h, p in sections:
            article += f"<h2>{h}</h2>\n<p>{p}</p>\n"

        article += """
<h2>Conclusione</h2>
<p>La costanza è più importante della quantità. Anche pochi minuti al giorno fanno la differenza.</p>

<h2>Consiglio finale</h2>
<p>Strumenti come Babbel possono aiutarti a strutturare il percorso in modo più efficace.</p>
"""

        return article
