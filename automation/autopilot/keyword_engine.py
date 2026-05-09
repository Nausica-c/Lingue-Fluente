import random
import re


class KeywordEngine:

    def __init__(self):

        self.base_keywords = {
            "beginner": [
                "imparare inglese da zero",
                "inglese per principianti",
                "come iniziare inglese",
                "frasi base inglese"
            ],
            "metodo": [
                "imparare inglese velocemente",
                "metodo immersione linguistica",
                "come diventare fluente in inglese",
                "tecniche apprendimento lingue"
            ],
            "speaking": [
                "parlare inglese fluentemente",
                "migliorare speaking inglese",
                "come parlare inglese senza paura"
            ],
            "vocabolario": [
                "vocabolario inglese base",
                "parole inglesi utili",
                "frasi inglesi quotidiane"
            ],
            "business": [
                "inglese business",
                "email in inglese professionale",
                "inglese per lavoro"
            ],
            "viaggio": [
                "inglese per viaggiare",
                "frasi inglese aeroporto",
                "inglese hotel ristorante"
            ],
            "grammatica_pratica": [
                "grammatica inglese facile",
                "tempi verbali inglese",
                "regole inglese base"
            ],
            "errori": [
                "errori comuni inglese",
                "errori italiani inglese",
                "come evitare errori inglese"
            ],
            "mindset": [
                "come imparare lingue motivazione",
                "costanza nello studio lingue",
                "paura di parlare inglese"
            ],
            "curiosita": [
                "curiosità lingua inglese",
                "storia parole inglesi",
                "lingue strane nel mondo"
            ],
            "lifelong-learner": [
                "come imparare per sempre",
                "abitudini studio lingue",
                "crescita personale lingue"
            ]
        }

    # -------------------------
    # NORMALIZE CLUSTER
    # -------------------------

    def normalize_cluster(self, cluster):

        if not cluster:
            return "beginner"

        cluster = cluster.lower().strip()

        # fix accenti comuni o varianti
        replacements = {
            "curiosità": "curiosita",
            "grammatica pratica": "grammatica_pratica",
            "lifelong learner": "lifelong-learner"
        }

        return replacements.get(cluster, cluster)

    # -------------------------
    # GET RANDOM KEYWORD
    # -------------------------

    def get_keyword(self, cluster):

        cluster = self.normalize_cluster(cluster)

        keywords = self.base_keywords.get(cluster)

        if not keywords:
            print(f"⚠️ Cluster non trovato: {cluster} → fallback beginner")
            keywords = self.base_keywords["beginner"]

        return random.choice(keywords)

    # -------------------------
    # SLUG SAFE
    # -------------------------

    def make_slug(self, text):

        text = text.lower()

        # rimuove caratteri non URL-safe
        text = re.sub(r"[^a-z0-9\s-]", "", text)

        text = text.replace(" ", "-")

        return text

    # -------------------------
    # GENERATE IDEA
    # -------------------------

    def generate_idea(self, cluster):

        keyword = self.get_keyword(cluster)

        idea = {
            "cluster": self.normalize_cluster(cluster),
            "keyword": keyword,
            "title": f"Guida completa: {keyword}",
            "slug": self.make_slug(keyword)
        }

        return idea
