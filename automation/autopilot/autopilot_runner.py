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

            print(f"📄 FILE CREATED: {file_path}")

            return file_path

        except Exception as e:
            print(f"❌ ERROR CREATING FILE: {e}")
            return None

    # -------------------------
    # BATCH (STABILE)
    # -------------------------

    def run_batch(self, count=5):

        print(f"🤖 AUTOPILOT BATCH: {count} articles")

        plans = self.planner.generate_batch_plan(count)

        if not plans:

            print("❌ NO PLANS GENERATED")
            return []

        # 🔥 FIX DUPLICATI
        seen = set()
        clean_plans = []

        for p in plans:
            slug = p.get("slug")

            if slug and slug not in seen:
                seen.add(slug)
                clean_plans.append(p)

        print(f"📦 CLEAN PLANS: {len(clean_plans)}")

        files = self.generator.generate_batch(clean_plans)

        # 🔥 VERIFICA REALE
        print("🔍 VERIFYING FILES...")

        valid_files = []

        for f in files:
            try:
                import os
                if os.path.exists(f):
                    valid_files.append(f)
            except:
                pass

        print(f"🏁 VALID FILES: {len(valid_files)}")

        return valid_files


# -------------------------
# ENTRYPOINT
# -------------------------

if __name__ == "__main__":

    autopilot = AutopilotRunner()

    autopilot.run_batch(5)
