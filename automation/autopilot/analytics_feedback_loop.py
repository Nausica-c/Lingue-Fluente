import random


class AnalyticsFeedbackLoop:

    def __init__(self):

        # simulazione analytics (poi verrà da GA4 / Pinterest / Search Console)
        self.mock_data = {

            "beginner": {
                "traffic": 1200,
                "ctr": 4.2,
                "conversion": 1.1
            },

            "metodo": {
                "traffic": 900,
                "ctr": 6.5,
                "conversion": 2.3
            },

            "speaking": {
                "traffic": 1500,
                "ctr": 3.8,
                "conversion": 1.8
            },

            "vocabolario": {
                "traffic": 700,
                "ctr": 5.0,
                "conversion": 1.2
            }
        }

    # -------------------------
    # ANALIZZA PERFORMANCE
    # -------------------------

    def analyze(self):

        insights = {}

        for cluster, data in self.mock_data.items():

            score = (
                data["traffic"] * 0.4 +
                data["ctr"] * 0.3 +
                data["conversion"] * 0.3
            )

            insights[cluster] = score

        return insights

    # -------------------------
    # TROVA PRIORITÀ
    # -------------------------

    def get_priority_clusters(self):

        insights = self.analyze()

        sorted_clusters = sorted(
            insights.items(),
            key=lambda x: x[1],
            reverse=True
        )

        return [c[0] for c in sorted_clusters]

    # -------------------------
    # MIGLIORA STRATEGIA
    # -------------------------

    def optimize_strategy(self):

        priority = self.get_priority_clusters()

        strategy = {

            "top_clusters": priority[:2],

            "boost_clusters": priority[2:],

            "deprioritize": [c for c in self.mock_data.keys() if c not in priority[:3]],

            "action": "update_content_planner_weights"
        }

        return strategy

    # -------------------------
    # SIMULA LEARNING LOOP
    # -------------------------

    def run_cycle(self):

        strategy = self.optimize_strategy()

        print("📊 ANALYTICS INSIGHT:")
        print(strategy)

        return strategy
