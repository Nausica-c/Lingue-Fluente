import random
from datetime import datetime, timedelta
from automation.autopilot.keyword_engine import KeywordEngine


class ContentPlanner:

    def __init__(self):

        self.engine = KeywordEngine()

        self.clusters = [
            "beginner",
            "metodo",
            "vocabolario",
            "viaggio",
            "business"
        ]

    def pick_cluster(self):
        return random.choice(self.clusters)

    def create_plan(self):

        cluster = self.pick_cluster()
        idea = self.engine.generate_idea(cluster)

        return {
            "cluster": cluster,
            "keyword": idea["keyword"],
            "title": idea["title"],
            "slug": idea["slug"],
            "publish_date": datetime.now().strftime("%Y-%m-%d")
        }

    def generate_batch_plan(self, count=5):

        return [self.create_plan() for _ in range(count)]
