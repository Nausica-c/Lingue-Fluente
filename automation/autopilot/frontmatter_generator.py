from pathlib import Path


class FrontmatterGenerator:

    def __init__(self, output_dir="_posts"):

        # ROOT STABILE (NON cwd)
        self.base_dir = Path(__file__).resolve().parents[2]

        self.output_dir = self.base_dir / output_dir
        self.output_dir.mkdir(parents=True, exist_ok=True)

        print(f"📁 POSTS DIR: {self.output_dir}")

    # -------------------------
    # CREA FILE MD
    # -------------------------

    def create_file(self, plan):

        filename = f"{plan['slug']}.md"
        path = self.output_dir / filename

        content = f"""---
title: "{plan['title']}"
slug: "{plan['slug']}"
cluster: "{plan['cluster']}"
keyword: "{plan['keyword']}"
---

# {plan['title']}

Contenuto generato automaticamente.
"""

        path.write_text(content, encoding="utf-8")

        print(f"✅ CREATED: {path}")

        return path

    # -------------------------
    # BATCH
    # -------------------------

    def generate_batch(self, plans):

        files = []

        for plan in plans:
            files.append(self.create_file(plan))

        print(f"🏁 TOTAL FILES: {len(files)}")

        return files
