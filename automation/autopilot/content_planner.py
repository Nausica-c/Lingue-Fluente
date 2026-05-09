import random
from datetime import datetime, timedelta

from automation.autopilot.keyword_engine import KeywordEngine


class ContentPlanner:

    def __init__(self):

        self.keyword_engine = KeywordEngine()

        # peso dei cluster (più alto = più pubblicato)
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
    # SCEGLIE CLUSTER
    # -------------------------

    def pick_cluster(self):

        clusters = list(self.cluster_weights.keys())
        weights = list(self.cluster_weights.values())

        return random.choices(clusters, weights=weights, k=1)[0]

    # -------------------------
    # CREA SCHEDA ARTICOLO
    # -------------------------

    def create_plan(self):

        cluster = self.pick_cluster()

        idea = self.keyword_engine.generate_idea(cluster)

        if not idea:
            return None

        # data pubblicazione simulata
        publish_date = datetime.now() + timedelta(days=random.randint(0, 3))

        plan = {

            "publish_date": publish_date.strftime("%Y-%m-%d"),

            "cluster": cluster,

            "keyword": idea["keyword"],

            "title": idea["title"],

            "slug": idea["slug"],

            "priority": self.cluster_weights.get(cluster, 5)

        }

        return plan

    # -------------------------
    # GENERA CALENDARIO
    # -------------------------

    def generate_batch_plan(self, count=5):

        plans = []

        for _ in range(count):

            plan = self.create_plan()

            if plan:
                plans.append(plan)

        # ordina per data
        plans.sort(key=lambda x: x["publish_date"])

        return plans
