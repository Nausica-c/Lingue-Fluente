import random


class PinterestEngine:

    def __init__(self):

        self.styles = [
            "curiosity",
            "problem_solution",
            "quick_tip",
            "mistake_alert"
        ]

    # -------------------------
    # CREA TITOLO PIN
    # -------------------------

    def generate_pin_title(self, article):

        keyword = article["seo"]["primary_keyword"]

        templates = [
            f"Come imparare {keyword} velocemente",
            f"Il segreto per {keyword}",
            f"{keyword}: metodo semplice e veloce",
            f"Errori da evitare in {keyword}"
        ]

        return random.choice(templates)

    # -------------------------
    # CREA DESCRIZIONE PIN
    # -------------------------

    def generate_description(self, article):

        keyword = article["seo"]["primary_keyword"]

        return f"""
Scopri come migliorare {keyword} con un metodo semplice e pratico.

Impara in modo naturale e veloce senza stress.

Inizia oggi il tuo percorso linguistico.
"""

    # -------------------------
    # CREA PIN PACK
    # -------------------------

    def create_pin_package(self, article):

        return {
            "title": self.generate_pin_title(article),
            "description": self.generate_description(article),
            "style": random.choice(self.styles),
            "link": article["article"]["meta"]["permalink"]
        }
