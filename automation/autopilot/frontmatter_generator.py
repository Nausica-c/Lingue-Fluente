from pathlib import Path
from datetime import datetime


class FrontmatterGenerator:

    def __init__(self, output_dir="_posts"):

        # 🔥 ROOT STABILE (GitHub + locale)
        self.base_dir = Path.cwd()

        self.output_dir = self.base_dir / output_dir
        self.output_dir.mkdir(parents=True, exist_ok=True)

        print(f"📁 BASE DIR: {self.base_dir}")
        print(f"📁 OUTPUT DIR: {self.output_dir}")

    # -------------------------
    # SAFE VALUE HELPER
    # -------------------------

    def safe(self, value, default=""):

        if value is None:
            return default

        return str(value)

    # -------------------------
    # FRONTMATTER
    # -------------------------

    def build_frontmatter(self, plan):

        title = self.safe(plan.get("title"), "Titolo non disponibile")
        slug = self.safe(plan.get("slug"), "no-slug")
        cluster = self.safe(plan.get("cluster"), "general")
        keyword = self.safe(plan.get("keyword"), "")
        publish_date = self.safe(
            plan.get("publish_date"),
            datetime.now().strftime("%Y-%m-%d")
        )

        return f"""---
article:
  meta:
    layout: "post"
    title: "{title}"
    slug: "{slug}"
    permalink: "/inglese/{cluster}/{slug}/"
    language: "it"
    target_language: "en"
    cluster: "{cluster}"
    publish_date: "{publish_date}"
    author: "Lingue-Fluente AI"
    publish: true
    indexed: true

seo:
  primary_keyword: "{keyword}"
  focus_keyword: "{keyword}"
  meta_description: "Scopri come migliorare {keyword} in modo semplice e veloce."

automation:
  generated_by: "autopilot"
  created_at: "{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
"""

    # -------------------------
    # CREATE FILE
    # -------------------------

    def create_file(self, plan):

        if not plan:
            print("❌ PLAN VUOTO")
            return None

        slug = plan.get("slug", "no-slug")
        filename = f"{slug}.md"
        path = self.output_dir / filename

        content = self.build_frontmatter(plan) + "\n# CONTENUTO DA GENERARE CON AI\n"

        print(f"📄 WRITING FILE: {path}")

        try:
            path.write_text(content, encoding="utf-8")
        except Exception as e:
            print(f"❌ WRITE ERROR: {e}")
            return None

        return path

    # -------------------------
    # BATCH
    # -------------------------

    def generate_batch(self, plans):

        if not plans:
            print("❌ NESSUN PLAN")
            return []

        files = []

        for plan in plans:

            file_path = self.create_file(plan)

            if file_path:
                files.append(file_path)

        print(f"🏁 FILES CREATED: {len(files)}")

        return files
