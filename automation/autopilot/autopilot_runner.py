print("🔥 AUTOPILOT STARTED")
from automation.autopilot.content_planner import ContentPlanner
from automation.autopilot.frontmatter_generator import FrontmatterGenerator


class AutopilotRunner:

    def __init__(self):

        self.planner = ContentPlanner()
        self.generator = FrontmatterGenerator()

    # -------------------------
    # SINGLE RUN
    # -------------------------

    def run_once(self):

        print("🚀 AUTOPILOT: generazione singolo ciclo...")

        plan = self.planner.create_plan()

        print("📦 PLAN:", plan)

        if not plan:

            print("⚠️ Nessun piano generato → fallback attivo")

            plan = {
                "publish_date": "2026-01-01",
                "title": "Come imparare una lingua velocemente",
                "slug": "imparare-lingua-velocemente",
                "cluster": "metodo",
                "keyword": "imparare una lingua velocemente"
            }

        file_path = self.generator.create_file(plan)

        print(f"📄 FILE CREATO: {file_path}")

        return file_path

    # -------------------------
    # BATCH (🔥 FIX IMPORTANTE)
    # -------------------------

    def run_batch(self, count=5):

        print(f"🤖 AUTOPILOT: batch {count} articoli...")

        plans = self.planner.generate_batch_plan(count)

        print(f"📦 PLANS GENERATI: {len(plans)}")  # 🔥 DEBUG CRITICO

        if not plans:
            print("❌ NESSUN PLAN GENERATO → STOP PIPELINE")
            return []

        files = self.generator.generate_batch(plans)

        print(f"🏁 FILE GENERATI: {len(files)}")

        return files


# -------------------------
# ENTRYPOINT (🔥 OBBLIGATORIO)
# -------------------------

if __name__ == "__main__":

    autopilot = AutopilotRunner()

    # 🔥 scegli UNA sola modalità reale
    autopilot.run_batch(5)
