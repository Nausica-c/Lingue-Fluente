import random
from datetime import datetime

from automation.autopilot.keyword_engine import KeywordEngine


class ContentPlanner:

    def __init__(self):

        self.engine = KeywordEngine()

        self.clusters = [
    "beginner",
    "metodo",
    "speaking",
    "vocabolario",
    "business",
    "viaggio",
    "grammatica_pratica",
    "mindset",
    "errori",
    "curiosita",
    "lifelong-learner"
        ]

    def pick_cluster(self):

        return random.choice(self.clusters)

    def create_plan(self):

        cluster = self.pick_cluster()

        idea = self.engine.generate_idea(cluster)

        return {
            "title": idea["title"],
            "slug": idea["slug"],
            "keyword": idea["keyword"],
            "cluster": cluster,
            "publish_date": datetime.now().strftime("%Y-%m-%d")
        }

    def generate_batch_plan(self, count=5):

        return [self.create_plan() for _ in range(count)]
