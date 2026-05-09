from pathlib import Path
from datetime import datetime


class FrontmatterGenerator:

    def __init__(self, output_dir="_posts"):

        # 🔥 FIX: repo root stabile (NON cwd)
        self.base_dir = Path(__file__).resolve().parent.parent.parent

        self.output_dir = self.base_dir / output_dir
        self.output_dir.mkdir(parents=True, exist_ok=True)

    # -------------------------
    # CREA FRONTMATTER YAML
    # -------------------------

    def build_frontmatter(self, plan):

        return f"""---
article:
  meta:
    layout: "post"
    title: "{plan['title']}"
    slug: "{plan['slug']}"
    permalink: "/inglese/{plan['cluster']}/{plan['slug']}/"
    language: "it"
    target_language: "en"
    cluster: "{plan['cluster']}"
    publish_date: "{plan['publish_date']}"
    author: "Lingue-Fluente AI"
    publish: true
    indexed: true

seo:
  primary_keyword: "{plan['keyword']}"
  focus_keyword: "{plan['keyword']}"
  meta_description: "Scopri come migliorare {plan['keyword']} in modo semplice e veloce."

automation:
  generated_by: "autopilot"
  created_at: "{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
"""

    # -------------------------
    # CREA FILE MARKDOWN
    # -------------------------

    def create_file(self, plan):

        frontmatter = self.build_frontmatter(plan)

        filename = f"{plan['slug']}.md"

        path = self.output_dir / filename

        content = frontmatter + "\n# CONTENUTO DA GENERARE CON AI\n"

        # 🔥 DEBUG SERIO
        print(f"📁 BASE DIR: {self.base_dir}")
        print(f"📁 OUTPUT DIR: {self.output_dir}")
        print(f"📄 WRITING FILE: {path}")

        path.write_text(content, encoding="utf-8")

        print(f"✅ FILE SCRITTO: {path}")
        print(f"📂 EXISTS: {path.exists()}")

        return str(path)

    # -------------------------
    # CREA BATCH FILES
    # -------------------------

    def generate_batch(self, plans):

        files = []

        for plan in plans:

            file_path = self.create_file(plan)
            files.append(file_path)

        print(f"🏁 TOTAL FILES GENERATED: {len(files)}")

        return files
