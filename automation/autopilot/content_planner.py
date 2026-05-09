from automation.autopilot.content_planner import ContentPlanner
from automation.autopilot.frontmatter_generator import FrontmatterGenerator


print("🔥 AUTOPILOT RUNNING")


class AutopilotRunner:

    def __init__(self):

        self.planner = ContentPlanner()
        self.generator = FrontmatterGenerator()

    def run_batch(self, count=5):

        print(f"🚀 GENERATING {count} ARTICLES")

        plans = self.planner.generate_batch_plan(count)

        print(f"📦 PLANS: {len(plans)}")

        files = self.generator.generate_batch(plans)

        print(f"🏁 FILES CREATED: {len(files)}")

        return files


if __name__ == "__main__":

    AutopilotRunner().run_batch(5)
