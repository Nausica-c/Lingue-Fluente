import os
from datetime import datetime


class FrontmatterGenerator:

    def __init__(self, output_dir="_posts"):

        self.output_dir = output_dir

        os.makedirs(self.output_dir, exist_ok=True)

    # -------------------------
    # CREA FRONTMATTER YAML
    # -------------------------

    def build_frontmatter(self, plan):

        fm = f"""---
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
        return fm

    # -------------------------
    # CREA FILE MARKDOWN
    # -------------------------

    def create_file(self, plan):

        frontmatter = self.build_frontmatter(plan)

        filename = f"{plan['slug']}.md"

        path = os.path.join(self.output_dir, filename)

        content = frontmatter + "\n# CONTENUTO DA GENERARE CON AI\n"

        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

        return path

    # -------------------------
    # CREA BATCH FILES
    # -------------------------

    def generate_batch(self, plans):

        files = []

        for plan in plans:

            file_path = self.create_file(plan)

            files.append(file_path)

        return files
