import random


class ContentEngine:

    def __init__(self):
        pass

    # -------------------------
    # HOOKS VARIABILI (semplici ma efficaci)
    # -------------------------

    def opening(self, keyword):
        return random.choice([
            f"Se vuoi migliorare {keyword}, devi partire da una cosa semplice:",
            f"Molti studenti sbagliano quando imparano {keyword}:",
            f"Imparare {keyword} non è difficile se usi il metodo giusto:",
            f"Ecco il segreto per padroneggiare {keyword}:"
        ])

    def closing(self):
        return random.choice([
            "La costanza batte sempre il talento.",
            "Pochi minuti al giorno fanno la differenza.",
            "Non serve studiare tanto, serve studiare bene.",
            "La pratica quotidiana è la vera chiave."
        ])

    # -------------------------
    # GENERAZIONE ARTICOLO (STABILE)
    # -------------------------

    def generate(self, data):

        title = data.get("title", "Articolo lingua inglese")
        keyword = data.get("keyword", "inglese")
        cluster = data.get("cluster", "base")

        return f"""<!doctype html>
<html lang="it">
<head>
    <meta charset="utf-8">
    <title>{title}</title>
</head>
<body>

<h1>{title}</h1>

<p>{self.opening(keyword)} {keyword} è una competenza fondamentale per comunicare meglio.</p>

<h2>Perché è importante</h2>
<p>Nel cluster <strong>{cluster}</strong>, l’obiettivo è imparare in modo pratico e veloce.</p>

<h2>Metodo semplice</h2>
<ul>
    <li>Impara frasi reali</li>
    <li>Ripeti ogni giorno</li>
    <li>Evita teoria inutile</li>
</ul>

<h2>Strategia quotidiana</h2>
<p>Dedica anche solo 10 minuti al giorno a {keyword} per vedere progressi reali.</p>

<h2>Conclusione</h2>
<p>{self.closing()}</p>

<p><strong>Consiglio:</strong> usa strumenti guidati come Babbel per accelerare il percorso.</p>

</body>
</html>"""
