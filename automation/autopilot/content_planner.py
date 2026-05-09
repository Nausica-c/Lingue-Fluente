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
    # CLUSTER
    # -------------------------

    def pick_cluster(self):

        clusters = list(self.cluster_weights.keys())
        weights = list(self.cluster_weights.values())

        return random.choices(clusters, weights=weights, k=1)[0]

    # -------------------------
    # SAFE SLUG
    # -------------------------

    def safe_slug(self, text):

        text = text.lower()
        text = re.sub(r"[^a-z0-9\s-]", "", text)
        text = re.sub(r"\s+", "-", text)
        return text.strip("-")

    # -------------------------
    # FALLBACK
    # -------------------------

    def fallback_idea(self, cluster):

        keyword = f"imparare {cluster} inglese"

        return {
            "keyword": keyword,
            "title": f"Come migliorare il tuo {cluster} in inglese",
            "slug": self.safe_slug(keyword)
        }

    # -------------------------
    # CREATE PLAN
    # -------------------------

    def create_plan(self):

        cluster = self.pick_cluster()

        idea = self.keyword_engine.generate_idea(cluster)

        if not idea:
            print(f"⚠️ fallback attivo per {cluster}")
            idea = self.fallback_idea(cluster)

        # 🔥 FIX slug sempre sicuro
        slug = self.safe_slug(idea["slug"])

        publish_date = datetime.now() + timedelta(days=random.randint(0, 3))

        return {
            "publish_date": publish_date.strftime("%Y-%m-%d"),
            "cluster": cluster,
            "keyword": idea["keyword"],
            "title": idea["title"],
            "slug": slug,
            "priority": self.cluster_weights.get(cluster, 5)
        }

    # -------------------------
    # BATCH (NO DUPLICATI)
    # -------------------------

    def generate_batch_plan(self, count=5):

        plans = []
        seen = set()

        attempts = 0

        while len(plans) < count and attempts < count * 3:

            plan = self.create_plan()

            slug = plan["slug"]

            if slug not in seen:
                seen.add(slug)
                plans.append(plan)

            attempts += 1

        plans.sort(key=lambda x: x["publish_date"])

        return plans
