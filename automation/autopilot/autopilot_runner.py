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

        print("📦 PLAN:", plan)

        if not plan:
            print("⚠️ Nessun piano generato → fallback attivo")

            plan = {
                "title": "Come imparare una lingua velocemente",
                "slug": "imparare-lingua-velocemente",
                "cluster": "metodo",
                "keyword": "imparare una lingua velocemente"
            }

        file_path = self.generator.create_file(plan)

        print(f"📄 File creato: {file_path}")

        return file_path

    # -------------------------
    # BATCH AUTOPILOT
    # -------------------------

    def run_batch(self, count=5):

        print(f"🤖 AUTOPILOT: avvio batch da {count} articoli...")

        # 1. genera piani
        plans = self.planner.generate_batch_plan(count)

        print("📦 PLANS GENERATI:", plans)

        # 2. fallback se vuoto
        if not plans:
            print("⚠️ Nessun plan generato → fallback attivo")

            plans = [
                {
                    "title": "Come imparare una lingua velocemente",
                    "slug": "imparare-lingua-velocemente",
                    "cluster": "metodo",
                    "keyword": "imparare una lingua velocemente"
                }
            ]

        # 3. genera file
        files = self.generator.generate_batch(plans)

        print("📄 FILE GENERATI:", files)

        if not files:
            print("❌ ERRORE: nessun file creato")
            return []

        for f in files:
            print(f"✅ Creato: {f}")

        print("🏁 Batch completato!")

        return files


# -------------------------
# ENTRYPOINT
# -------------------------

if __name__ == "__main__":

    autopilot = AutopilotRunner()

    autopilot.run_batch(5)
