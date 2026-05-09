import random


class KeywordEngine:

    def __init__(self):

        # seed base (puoi ampliarlo dopo con SEO tool reali)
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
    # GET RANDOM KEYWORD
    # -------------------------

    def get_keyword(self, cluster):

        keywords = self.base_keywords.get(cluster, [])

        if not keywords:
            return None

        return random.choice(keywords)

    # -------------------------
    # GENERATE NEXT ARTICLE IDEA
    # -------------------------

    def generate_idea(self, cluster):

        keyword = self.get_keyword(cluster)

        if not keyword:
            return None

        idea = {
            "cluster": cluster,
            "keyword": keyword,
            "title": f"Guida completa su: {keyword}",
            "slug": keyword.replace(" ", "-").lower()
        }

        return idea
