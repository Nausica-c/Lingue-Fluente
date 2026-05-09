from pathlib import Path
from datetime import datetime


class FrontmatterGenerator:

    def __init__(self, output_dir="_posts"):

        # 🔥 FIX ROBUSTO: supporto GitHub Actions + locale
        self.base_dir = Path.cwd()

        self.output_dir = self.base_dir / output_dir
        self.output_dir.mkdir(parents=True, exist_ok=True)

        print(f"📁 BASE DIR: {self.base_dir}")
        print(f"📁 OUTPUT DIR: {self.output_dir}")

    # -------------------------
    # CREA FRONTMATTER YAML
    # -------------------------

    def build_frontmatter(self, plan):

        # 🔥 FIX: safe get per evitare KeyError silenziosi
        title = plan.get("title", "Titolo non disponibile")
        slug = plan.get("slug", "no-slug")
        cluster = plan.get("cluster", "general")
        keyword = plan.get("keyword", "")
        publish_date = plan.get("publish_date", datetime.now().strftime("%Y-%m-%d"))

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
    # CREA FILE MARKDOWN
    # -------------------------

    def create_file(self, plan):

        frontmatter = self.build_frontmatter(plan)

        filename = f"{plan.get('slug', 'no-slug')}.md"

        path = self.output_dir / filename

        content = frontmatter + "\n# CONTENUTO DA GENERARE CON AI\n"

        print(f"📄 WRITING FILE: {path}")

        try:
            path.write_text(content, encoding="utf-8")

        except Exception as e:
            print(f"❌ ERRORE SCRITTURA FILE {path}: {e}")
            return None

        print(f"✅ FILE SCRITTO: {path}")
        print(f"📂 EXISTS: {path.exists()}")

        return path

    # -------------------------
    # CREA BATCH FILES
    # -------------------------

    def generate_batch(self, plans):

        files = []

        if not plans:
            print("❌ NESSUN PLAN RICEVUTO")
            return []

        for plan in plans:

            file_path = self.create_file(plan)

            if file_path:
                files.append(file_path)

        print(f"🏁 TOTAL FILES GENERATED: {len(files)}")

        return files
