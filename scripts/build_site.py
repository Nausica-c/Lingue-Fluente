import sys
from pathlib import Path

# 🔥 ROOT STABILE PER GITHUB ACTIONS
ROOT_DIR = Path.cwd().resolve()
sys.path.append(str(ROOT_DIR))

from runtime.orchestrator import ArticleOrchestrator


class SiteBuilder:

    def __init__(self):

        # 🔥 DIRECTORY PRINCIPALI
        self.base_dir = ROOT_DIR

        self.posts_path = self.base_dir / "_posts"
        self.output_path = self.base_dir / "_site"

        # 🔥 CREA _site SEMPRE
        self.output_path.mkdir(parents=True, exist_ok=True)

        print("🚀 SITE BUILDER INIT")

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

        articles = list(self.posts_path.glob("*.md"))

        print(f"📦 FILES FOUND: {len(articles)}")

        for article in articles:
            print(f" - {article.name}")

        return articles

    # -------------------------
    # BUILD SINGLE ARTICLE
    # -------------------------

    def build_article(self, article_path):

        print(f"\n✍️ BUILDING ARTICLE: {article_path.name}")

        try:

            orchestrator = ArticleOrchestrator(article_path)

            content = orchestrator.run()

            # 🔥 DEBUG CONTENUTO
            print("📄 CONTENT TYPE:", type(content))

            if content:

                print("📏 CONTENT LENGTH:", len(str(content)))

            else:

                print("❌ CONTENT IS EMPTY")
                return None

            return content

        except Exception as e:

            print(f"❌ BUILD ARTICLE ERROR: {e}")
            return None

    # -------------------------
    # SAVE OUTPUT
    # -------------------------

    def save_article(self, article_path, content):

        try:

            output_file = self.output_path / f"{article_path.stem}.html"

            output_file.write_text(str(content), encoding="utf-8")

            print(f"✅ SAVED: {output_file}")

            return output_file

        except Exception as e:

            print(f"❌ SAVE ERROR: {e}")
            return None

    # -------------------------
    # BUILD FULL SITE
    # -------------------------

    def build(self):

        print("\n🚀 START BUILD")

        articles = self.get_articles()

        if not articles:

            print("❌ NO ARTICLES FOUND")
            return

        built = 0

        for article in articles:

            content = self.build_article(article)

            if not content:

                print(f"⚠️ SKIPPED: {article.name}")
                continue

            saved = self.save_article(article, content)

            if saved:
                built += 1

        print("\n🏁 BUILD FINISHED")
        print(f"✅ ARTICLES BUILT: {built}")

        # 🔥 DEBUG FINALE
        print("\n📂 FINAL _site CONTENTS:")

        files = list(self.output_path.glob("*"))

        if not files:

            print("❌ _site È VUOTA")

        else:

            for f in files:
                print(f" - {f.name}")


# -------------------------
# ENTRYPOINT
# -------------------------

if __name__ == "__main__":

    builder = SiteBuilder()

    builder.build()
