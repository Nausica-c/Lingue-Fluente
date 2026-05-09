import random
import re
from datetime import datetime, timedelta

from automation.autopilot.keyword_engine import KeywordEngine


class ContentPlanner:

    def __init__(self):

        self.keyword_engine = KeywordEngine()

        self.cluster_weights = {
            "beginner": 10,
            "metodo": 9,
            "speaking": 9,
            "vocabolario": 8,
            "mindset": 8,
            "business": 7,
            "viaggio": 7,
            "grammatica_pratica": 8,
            "errori": 7,
            "curiosita": 5,
            "lifelong-learner": 6
        }

    # -------------------------
    # CLUSTER PICK (SAFE)
    # -------------------------

    def pick_cluster(self):

        clusters = list(self.cluster_weights.keys())
        weights = list(self.cluster_weights.values())

        return random.choices(clusters, weights=weights, k=1)[0]

    # -------------------------
    # SLUG SAFE (FINAL VERSION)
    # -------------------------

    def safe_slug(self, text):

        if not text:
            return "no-slug"

        text = str(text).lower().strip()
        text = re.sub(r"[^a-z0-9\s-]", "", text)
        text = re.sub(r"\s+", "-", text)
        text = re.sub(r"-+", "-", text)

        slug = text.strip("-")

        return slug if slug else "no-slug"

    # -------------------------
    # FALLBACK IDEA
    # -------------------------

    def fallback_idea(self, cluster):

        keyword = f"imparare {cluster} inglese"

        return {
            "keyword": keyword,
            "title": f"Come migliorare il tuo {cluster} in inglese",
            "slug": self.safe_slug(keyword)
        }

    # -------------------------
    # CREATE PLAN (HARD SAFE)
    # -------------------------

    def create_plan(self):

        cluster = self.pick_cluster()

        idea = {}

        try:
            idea = self.keyword_engine.generate_idea(cluster)
        except Exception:
            idea = None

        if not isinstance(idea, dict) or not idea:
            idea = self.fallback_idea(cluster)

        keyword = str(idea.get("keyword", "imparare inglese"))
        title = str(idea.get("title", f"Guida su {keyword}"))
        slug = self.safe_slug(idea.get("slug", keyword))

        publish_date = datetime.now() + timedelta(days=random.randint(0, 3))

        return {
            "publish_date": publish_date.strftime("%Y-%m-%d"),
            "cluster": cluster,
            "keyword": keyword,
            "title": title,
            "slug": slug,
            "priority": self.cluster_weights.get(cluster, 5)
        }

    # -------------------------
    # BATCH PLAN (ROBUSTO DEFINITIVO)
    # -------------------------

    def generate_batch_plan(self, count=5):

        plans = []
        seen = set()

        max_attempts = count * 5
        attempts = 0

        while len(plans) < count and attempts < max_attempts:

            plan = self.create_plan()

            if not plan:
                attempts += 1
                continue

            slug = plan.get("slug")

            if slug and slug not in seen:
                seen.add(slug)
                plans.append(plan)

            attempts += 1

        # fallback assoluto
        if not plans:
            plans = [self.create_plan()]

        plans.sort(key=lambda x: x.get("publish_date", ""))

        return plans
