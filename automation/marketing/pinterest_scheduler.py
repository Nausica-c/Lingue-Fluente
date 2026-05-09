from datetime import datetime, timedelta
import random

from automation.marketing.pinterest_trend_detector import PinterestTrendDetector


class PinterestScheduler:

    def __init__(self):

        self.trend_detector = PinterestTrendDetector()

    # -------------------------
    # CREA CALENDARIO PIN
    # -------------------------

    def create_schedule(self, articles):

        schedule = []

        trending = self.trend_detector.recommend_boost_keywords()

        for i, article in enumerate(articles):

            keyword = article["seo"]["primary_keyword"]

            boost_priority = 10 if keyword in trending else random.randint(3, 7)

            publish_time = datetime.now() + timedelta(hours=i * 6)

            schedule.append({

                "article": article["article"]["meta"]["permalink"],

                "keyword": keyword,

                "priority": boost_priority,

                "publish_time": publish_time.strftime("%Y-%m-%d %H:%M"),

                "boost": keyword in trending

            })

        # ordina per priorità
        schedule.sort(key=lambda x: x["priority"], reverse=True)

        return schedule
