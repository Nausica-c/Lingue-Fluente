import random


class ContentEngine:

    def __init__(self):
        pass

    # -------------------------
    # VARIABILITÀ NATURALE
    # -------------------------

    def opening(self):
        return random.choice([
            "Molti studenti di inglese fanno questo errore:",
            "Se vuoi migliorare il tuo inglese, devi capire una cosa importante:",
            "Un metodo semplice ma potente per imparare è questo:",
            "La maggior parte delle persone fallisce perché:"
        ])

    def closing(self):
        return random.choice([
            "La costanza è più importante della perfezione.",
            "10 minuti al giorno valgono più di ore casuali.",
            "Imparare una lingua è un processo, non un evento.",
            "Se vuoi risultati, devi essere coerente."
        ])

    # -------------------------
    # GENERAZIONE ARTICOLO
    # -------------------------

    def generate(self, data):

        title = data.get("title", "Articolo")
        keyword = data.get("keyword", "inglese")
        cluster = data.get("cluster", "base")

        return f"""
<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <title>{title}</title>
</head>
<body>

<h1>{title}</h1>

<p>{self.opening()} {keyword} è una delle abilità più importanti oggi.</p>

<h2>1. Comprendere il metodo</h2>
<p>Nel cluster {cluster}, la chiave è la pratica quotidiana e la semplicità.</p>

<h2>2. Esempio pratico</h2>
<ul>
    <li>Ascolta contenuti semplici</li>
    <li>Ripeti frasi ogni giorno</li>
    <li>Non studiare troppo teoria</li>
</ul>

<h2>3. Strategia efficace</h2>
<p>La progressione lenta ma costante è la strategia migliore per {keyword}.</p>

<h2>Conclusione</h2>
<p>{self.closing()}</p>

<p><strong>Consiglio:</strong> usa strumenti guidati come Babbel per strutturare il tuo apprendimento.</p>

</body>
</html>
"""
