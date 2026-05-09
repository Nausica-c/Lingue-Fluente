import os

os.makedirs("_posts", exist_ok=True)

from automation.autopilot.content_planner import ContentPlanner
from automation.autopilot.frontmatter_generator import FrontmatterGenerator


class AutopilotRunner:

    def __init__(self):

        self.planner = ContentPlanner()
        self.generator = FrontmatterGenerator()

    # -------------------------
    # SINGLE RUN (1 CICLO)
    # -------------------------

    def run_once(self):

        print("🚀 AUTOPILOT: generazione singolo ciclo...")

        plan = self.planner.create_plan()

        if not plan:
            print("⚠️ Nessun piano generato")
            return None

        file_path = self.generator.create_file(plan)

        print(f"📄 File creato: {file_path}")

        return file_path

    # -------------------------
    # BATCH AUTOPILOT
    # -------------------------

    def run_batch(self, count=5):

        print(f"🤖 AUTOPILOT: avvio batch da {count} articoli...")

        plans = self.planner.generate_batch_plan(count)

        files = self.generator.generate_batch(plans)

        for f in files:
            print(f"✅ Creato: {f}")

        print("🏁 Batch completato!")

        return files


# -------------------------
# ENTRYPOINT
# -------------------------

if __name__ == "__main__":

    autopilot = AutopilotRunner()

    # puoi scegliere:
    autopilot.run_batch(5)
