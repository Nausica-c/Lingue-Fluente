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
    # CLUSTER PICK
    # -------------------------

    def pick_cluster(self):

        return random.choices(
            list(self.cluster_weights.keys()),
            weights=self.cluster_weights.values(),
            k=1
        )[0]

    # -------------------------
    # SAFE SLUG (ROBUSTO)
    # -------------------------

    def safe_slug(self, text):

        if not text:
            return "no-slug"

        text = text.lower().strip()
        text = re.sub(r"[^a-z0-9\s-]", "", text)
        text = re.sub(r"\s+", "-", text)
        text = re.sub(r"-+", "-", text)

        return text.strip("-") or "no-slug"

    # -------------------------
    # FALLBACK IDEA (ROBUSTO)
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

        # 🔥 FIX: fallback totale se engine fallisce
        if not idea or not isinstance(idea, dict):
            print(f"⚠️ KeywordEngine fallback: {cluster}")
            idea = self.fallback_idea(cluster)

        # 🔥 FIX: protezione campi mancanti
        keyword = idea.get("keyword", "imparare inglese")
        title = idea.get("title", f"Guida su {keyword}")
        slug_raw = idea.get("slug", keyword)

        slug = self.safe_slug(slug_raw)

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
    # BATCH PLAN (ANTI DUPLICATI + SAFE)
    # -------------------------

    def generate_batch_plan(self, count=5):

        plans = []
        seen = set()

        attempts = 0
        max_attempts = count * 5

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

        # fallback finale se troppo pochi
        if len(plans) == 0:
            plans.append(self.create_plan())

        plans.sort(key=lambda x: x["publish_date"])

        return plans
