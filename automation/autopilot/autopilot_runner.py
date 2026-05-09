print("🔥 AUTOPILOT STARTED")

import os
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

        print("🚀 AUTOPILOT: single run...")

        plan = self.planner.create_plan()

        print("📦 PLAN:", plan)

        if not plan:

            print("⚠️ fallback plan attivo")

            plan = {
                "publish_date": "2026-01-01",
                "title": "Come imparare una lingua velocemente",
                "slug": "imparare-lingua-velocemente",
                "cluster": "metodo",
                "keyword": "imparare una lingua velocemente"
            }

        try:

            file_path = self.generator.create_file(plan)

            # 🔥 FIX: verifica reale file
            if file_path and os.path.exists(file_path):
                print(f"📄 FILE CREATED: {file_path}")
            else:
                print(f"❌ FILE NOT FOUND AFTER CREATION: {file_path}")

            return file_path

        except Exception as e:

            print(f"❌ ERROR CREATING FILE: {e}")
            return None

    # -------------------------
    # BATCH (STABILE DEFINITIVO)
    # -------------------------

    def run_batch(self, count=5):

        print(f"🤖 AUTOPILOT BATCH: {count} articles")

        plans = self.planner.generate_batch_plan(count)

        if not plans:

            print("❌ NO PLANS GENERATED")
            return []

        print(f"📦 PLANS RECEIVED: {len(plans)}")

        # 🔥 IMPORTANTE: NON rifare dedup qui (già fatto nel planner)
        files = self.generator.generate_batch(plans)

        print("🔍 VERIFYING FILES ON DISK...")

        valid_files = []

        for f in files:

            if f and os.path.exists(f):
                valid_files.append(f)
                print(f"✅ VALID: {f}")
            else:
                print(f"❌ MISSING: {f}")

        print(f"🏁 VALID FILES: {len(valid_files)}")

        return valid_files


# -------------------------
# ENTRYPOINT
# -------------------------

if __name__ == "__main__":

    autopilot = AutopilotRunner()

    result = autopilot.run_batch(5)

    print("📊 FINAL RESULT:", len(result))
