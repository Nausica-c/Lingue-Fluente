import sys
from pathlib import Path

# 🔥 ROOT ROBUSTO (GitHub Actions SAFE)
ROOT_DIR = Path.cwd()
sys.path.append(str(ROOT_DIR))

from runtime.orchestrator import ArticleOrchestrator


class SiteBuilder:

    def __init__(self):

        # 🔥 usa working directory reale di Actions
        self.base_dir = Path.cwd()

        self.posts_path = self.base_dir / "_posts"
        self.output_path = self.base_dir / "_site"

        self.output_path.mkdir(parents=True, exist_ok=True)

        print(f"📍 BASE DIR: {self.base_dir}")
        print(f"📁 POSTS PATH: {self.posts_path}")
        print(f"📁 SITE PATH: {self.output_path}")

    # -------------------------
    # GET ARTICLES
    # -------------------------

    def get_articles(self):

        print("🔍 CHECKING _posts CONTENTS...")

        if not self.posts_path.exists():
            print("❌ _posts NON ESISTE")
            return []

        files = list(self.posts_path.glob("*.md"))

        print(f"📦 FILES FOUND: {len(files)}")

        # 🔥 DEBUG REALE
        for f in files:
            print(f" - {f.name}")

        return files

    # -------------------------
    # BUILD ARTICLE
    # -------------------------

    def build_article(self, article_path):

        print(f"✍️ BUILDING: {article_path.name}")

        orchestrator = ArticleOrchestrator(article_path)

        content = orchestrator.run()

        if not content:
            print(f"❌ EMPTY CONTENT: {article_path.name}")
            return None

        return content

    # -------------------------
    # SAVE OUTPUT
    # -------------------------

    def save_article(self, article_path, content):

        output_file = self.output_path / (article_path.stem + ".html")

        output_file.write_text(content, encoding="utf-8")

        print(f"✅ SAVED: {output_file}")

    # -------------------------
    # BUILD SITE
    # -------------------------

    def build(self):

        print("🚀 START BUILD")

        articles = self.get_articles()

        if len(articles) == 0:
            print("❌ NO ARTICLES FOUND → STOP")
            return

        built = 0

        for article in articles:

            try:

                content = self.build_article(article)

                if content:

                    self.save_article(article, content)
                    built += 1

            except Exception as e:

                print(f"❌ ERROR {article.name}: {e}")

        print(f"🏁 DONE → {built} articles built")
