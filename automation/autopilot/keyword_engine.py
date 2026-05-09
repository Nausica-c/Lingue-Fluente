import random


class KeywordEngine:

    def generate_idea(self, cluster):

        base_keywords = [
            f"inglese {cluster}",
            f"imparare inglese {cluster}",
            f"frasi inglesi {cluster}",
            f"come migliorare inglese {cluster}"
        ]

        keyword = random.choice(base_keywords)

        return {
            "keyword": keyword,
            "title": f"Guida pratica: {keyword}",
            "slug": keyword.replace(" ", "-")
        }
