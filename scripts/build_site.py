import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

from runtime.orchestrator import ArticleOrchestrator


class SiteBuilder:

    def __init__(self):

        # 🔥 FIX: repo root stabile
        self.base_dir = Path(__file__).resolve().parent.parent

        self.posts_path = self.base_dir / "_posts"
        self.output_path = self.base_dir / "_site"

        self.output_path.mkdir(parents=True, exist_ok=True)

    # -------------------------
    # GET ARTICLES
    # -------------------------

    def get_articles(self):

        print(f"📁 CHECK POSTS DIR: {self.posts_path}")

        if not self.posts_path.exists():
            print("❌ _posts non esiste")
            return []

        articles = list(self.posts_path.glob("*.md"))

        print(f"📦 Articoli trovati: {len(articles)}")

        return articles

    # -------------------------
    # BUILD ARTICLE
    # -------------------------

    def build_article(self, article_path):

        print(f"✍️ Generazione: {article_path.name}")

        orchestrator = ArticleOrchestrator(article_path)

        content = orchestrator.run()

        # 🔥 FIX: blocca output vuoto
        if not content or len(content.strip()) < 50:
            print(f"❌ CONTENUTO NON VALIDO: {article_path.name}")
            return None

        return content

    # -------------------------
    # SAVE OUTPUT (HTML FIX)
    # -------------------------

    def save_article(self, article_path, content):

        # 🔥 FIX IMPORTANTE: HTML invece di MD
        output_file = self.output_path / (article_path.stem + ".html")

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"✅ Salvato: {output_file}")

    # -------------------------
    # BUILD SITE
    # -------------------------

    def build(self):

        print("🚀 Avvio build sito Lingue-Fluente...")

        articles = self.get_articles()

        if not articles:
            print("❌ NESSUN ARTICOLO → PIPELINE BLOCCATA")
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

        print(f"🏁 BUILD COMPLETATA → articoli generati: {built}")
