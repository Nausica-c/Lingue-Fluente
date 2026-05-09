from automation.autopilot.content_planner import ContentPlanner
from automation.autopilot.frontmatter_generator import FrontmatterGenerator


class AutopilotRunner:

    def __init__(self):

        self.planner = ContentPlanner()
        self.generator = FrontmatterGenerator()

    # -------------------------
    # RUN BATCH
    # -------------------------

    def run_batch(self, count=5):

        print("🚀 AUTOPILOT START")

        # 1. crea piani articoli
        plans = self.planner.generate_batch_plan(count)

        print(f"📦 PLANS: {len(plans)}")

        if not plans:
            print("❌ NO PLANS GENERATED")
            return []

        # 2. scrive file in _posts
        files = self.generator.generate_batch(plans)

        print(f"🏁 FILES CREATED: {len(files)}")

        return files


# -------------------------
# ENTRYPOINT
# -------------------------

if __name__ == "__main__":

    autopilot = AutopilotRunner()
    autopilot.run_batch(5)
