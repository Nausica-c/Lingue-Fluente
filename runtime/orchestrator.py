from runtime.context_builder import ContextBuilder
from automation.generator.content_engine import ContentEngine


class ArticleOrchestrator:

    def __init__(self, article_path):

        self.article_path = article_path
        self.context_builder = ContextBuilder()

        self.context = {}
        self.engine = ContentEngine()

    # -------------------------
    # LOAD CONTEXT (SAFE)
    # -------------------------

    def load_context(self):

        print("📦 LOADING CONTEXT...")

        try:
            self.context = self.context_builder.build(self.article_path)
        except Exception as e:
            print(f"⚠️ Context error: {e}")
            self.context = {}

        if not isinstance(self.context, dict):
            self.context = {}

        print("📄 CONTEXT READY")

        return self.context

    # -------------------------
    # EXTRACT DATA
    # -------------------------

    def extract_data(self):

        article = self.context.get("article", {}).get("meta", {})

        seo = article.get("seo", {})

        return {
            "title": article.get("title", "Articolo Lingue-Fluente"),
            "slug": article.get("slug", "articolo"),
            "keyword": seo.get("primary_keyword", "inglese"),
            "cluster": article.get("cluster", "base")
        }

    # -------------------------
    # GENERATE ARTICLE
    # -------------------------

    def generate_article(self):

        print("✍️ GENERATING ARTICLE (NO AI)...")

        data = self.extract_data()

        html = self.engine.generate(data)

        print("📏 GENERATED LENGTH:", len(html))

        return html

    # -------------------------
    # RUN PIPELINE
    # -------------------------

    def run(self):

        print("🚀 ORCHESTRATOR START")

        self.load_context()

        result = self.generate_article()

        print("✅ DONE")

        return result
