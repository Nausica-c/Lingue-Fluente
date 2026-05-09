import sys
from pathlib import Path

# 🔥 ROOT ULTRA STABILE (GitHub Actions safe)
ROOT_DIR = Path.cwd().resolve()
sys.path.append(str(ROOT_DIR))

from runtime.orchestrator import ArticleOrchestrator


class SiteBuilder:

    def __init__(self):

        # 🔥 FIX: sempre cwd (unica fonte affidabile in Actions)
        self.base_dir = Path.cwd().resolve()

        self.posts_path = self.base_dir / "_posts"
        self.output_path = self.base_dir / "_site"

        self.output_path.mkdir(parents=True, exist_ok=True)

        print("🚀 SITE BUILDER INIT")
        print(f"📍 BASE DIR: {self.base_dir}")
        print(f"📁 POSTS PATH: {self.posts_path}")
        print(f"📁 SITE PATH: {self.output_path}")

    # -------------------------
    # GET ARTICLES
    # -------------------------

    def get_articles(self):

        print("🔍 SCANNING _posts...")

        if not self.posts_path.exists():
            print("❌ _posts NON ESISTE")
            return []

        articles = sorted(self.posts_path.glob("*.md"))

        print(f"📦 FILES FOUND: {len(articles)}")

        for a in articles:
            print(f" - {a.name}")

        return articles

    # -------------------------
    # BUILD ARTICLE (HARD VALIDATION)
    # -------------------------

    def build_article(self, article_path):

        print(f"\n✍️ BUILDING: {article_path.name}")

        try:

            orchestrator = ArticleOrchestrator(article_path)
            content = orchestrator.run()

            if not content:
                print("❌ EMPTY CONTENT")
                return None

            content = str(content).strip()

            # 🔥 HARD CHECK (IMPORTANTISSIMO)
            if len(content) < 100:
                print("❌ CONTENT TOO SHORT → SKIP")
                return None

            print(f"📏 LENGTH: {len(content)}")

            return content

        except Exception as e:

            print(f"❌ ORCHESTRATOR FAILED: {article_path.name}")
            print(f"   → {e}")

            return None

    # -------------------------
    # SAVE OUTPUT
    # -------------------------

    def save_article(self, article_path, content):

        output_file = self.output_path / f"{article_path.stem}.html"

        html = f"""<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8">
<title>{article_path.stem}</title>
</head>
<body>
{content}
</body>
</html>"""

        output_file.write_text(html, encoding="utf-8")

        print(f"✅ SAVED: {output_file}")

        return output_file

    # -------------------------
    # BUILD SITE
    # -------------------------

    def build(self):

        print("\n🚀 START BUILD")

        articles = self.get_articles()

        if not articles:
            print("❌ NO ARTICLES FOUND")
            return

        built = 0
        failed = 0

        for article in articles:

            content = self.build_article(article)

            if not content:
                print(f"⚠️ SKIPPED: {article.name}")
                failed += 1
                continue

            self.save_article(article, content)
            built += 1

        print("\n🏁 BUILD FINISHED")
        print(f"✅ BUILT: {built}")
        print(f"❌ FAILED: {failed}")

        # 🔥 FINAL CHECK
        files = list(self.output_path.glob("*"))

        print("\n📂 _site CONTENTS:")

        if not files:
            print("❌ _site VUOTA (PROBLEMA ORCHESTRATOR O AI)")
        else:
            for f in files:
                print(f" - {f.name}")


if __name__ == "__main__":

    SiteBuilder().build()
