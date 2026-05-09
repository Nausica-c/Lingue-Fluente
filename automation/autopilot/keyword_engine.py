import random
import re


class KeywordEngine:

    # -------------------------
    # SAFE SLUG
    # -------------------------

    def safe_slug(self, text):

        text = text.lower()

        text = re.sub(r"[^a-z0-9\s-]", "", text)

        text = re.sub(r"\s+", "-", text)

        text = re.sub(r"-+", "-", text)

        return text.strip("-")

    # -------------------------
    # GENERA IDEA
    # -------------------------

    def generate_idea(self, cluster):

        keywords = [
            f"inglese {cluster}",
            f"imparare inglese {cluster}",
            f"frasi inglesi {cluster}",
            f"come migliorare inglese {cluster}",
            f"metodo inglese {cluster}",
            f"errori inglese {cluster}"
        ]

        keyword = random.choice(keywords)

        title_templates = [
            f"Guida pratica: {keyword}",
            f"Come migliorare con {keyword}",
            f"Metodo semplice per {keyword}",
            f"Strategie efficaci per {keyword}"
        ]

        title = random.choice(title_templates)

        return {
            "keyword": keyword,
            "title": title,
            "slug": self.safe_slug(title)
        }
