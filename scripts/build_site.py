import os
from pathlib import Path

from runtime.orchestrator import ArticleOrchestrator


POSTS_DIR = "_posts"
OUTPUT_DIR = "_site"


class SiteBuilder:

    def __init__(self):

        self.posts_path = Path(POSTS_DIR)
        self.output_path = Path(OUTPUT_DIR)

        self.output_path.mkdir(exist_ok=True)

    # -------------------------
    # GET ALL ARTICLES
    # -------------------------

    def get_articles(self):

        if not self.posts_path.exists():
            return []

        return [
            self.posts_path / f
            for f in os.listdir(self.posts_path)
            if f.endswith(".md")
        ]

    # -------------------------
    # BUILD SINGLE ARTICLE
    # -------------------------

    def build_article(self, article_path):

        orchestrator = ArticleOrchestrator(article_path)

        print(f"✍️ Generazione: {article_path.name}")

        content = orchestrator.run()

        return content

    # -------------------------
    # SAVE OUTPUT
    # -------------------------

    def save_article(self, article_path, content):

        output_file = self.output_path / article_path.name

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"✅ Salvato: {output_file}")

    # -------------------------
    # BUILD ALL SITE
    # -------------------------

    def build(self):

        print("🚀 Avvio build sito Lingue-Fluente...")

        articles = self.get_articles()

        if not articles:
            print("⚠️ Nessun articolo trovato")
            return

        for article in articles:

            try:

                content = self.build_article(article)

                self.save_article(article, content)

            except Exception as e:

                print(f"❌ Errore su {article.name}: {e}")

        print("🏁 Build completata!")


# -------------------------
# RUN SCRIPT
# -------------------------

if __name__ == "__main__":

    builder = SiteBuilder()

    builder.build()
