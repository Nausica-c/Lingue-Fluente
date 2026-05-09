import sys
from pathlib import Path

# 🧠 ROOT STABILE
ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

from runtime.orchestrator import ArticleOrchestrator


POSTS_DIR = Path("_posts")
OUTPUT_DIR = Path("_site")


class SiteBuilder:

    def __init__(self):

        self.posts_path = POSTS_DIR
        self.output_path = OUTPUT_DIR

        self.output_path.mkdir(exist_ok=True)

    # -------------------------
    # GET ALL ARTICLES (FIXED)
    # -------------------------

    def get_articles(self):

        if not self.posts_path.exists():
            print("❌ _posts non esiste")
            return []

        articles = list(self.posts_path.glob("*.md"))

        print(f"📦 Articoli trovati: {len(articles)}")

        return articles

    # -------------------------
    # BUILD SINGLE ARTICLE
    # -------------------------

    def build_article(self, article_path):

        print(f"✍️ Generazione: {article_path.name}")

        orchestrator = ArticleOrchestrator(article_path)

        content = orchestrator.run()

        # 🔥 FIX CRITICO
        if not content:
            print(f"❌ CONTENUTO VUOTO: {article_path.name}")
            return None

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

        built = 0

        for article in articles:

            try:

                content = self.build_article(article)

                if content:

                    self.save_article(article, content)
                    built += 1

            except Exception as e:

                print(f"❌ Errore su {article.name}: {e}")

        print(f"🏁 Build completata! Articoli generati: {built}")


# -------------------------
# RUN
# -------------------------

if __name__ == "__main__":

    builder = SiteBuilder()
    builder.build()
