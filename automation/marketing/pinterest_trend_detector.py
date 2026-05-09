import random


class PinterestTrendDetector:

    def __init__(self):

        # simulazione trend (poi sostituibile con Pinterest API / scraping)
        self.trending_topics = {

            "imparare inglese velocemente": 95,
            "frasi inglesi viaggio": 78,
            "parlare inglese senza paura": 88,
            "inglese base principianti": 92,
            "metodo immersione linguistica": 85,
            "vocabolario inglese quotidiano": 70
        }

    # -------------------------
    # TROVA TREND MIGLIORI
    # -------------------------

    def get_top_trends(self, limit=3):

        sorted_trends = sorted(
            self.trending_topics.items(),
            key=lambda x: x[1],
            reverse=True
        )

        return sorted_trends[:limit]

    # -------------------------
    # SUGGERISCE CONTENUTI DA SPINGERE
    # -------------------------

    def recommend_boost_keywords(self):

        top = self.get_top_trends()

        return [t[0] for t in top]
