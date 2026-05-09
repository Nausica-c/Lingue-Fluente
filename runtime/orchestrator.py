from runtime.context_builder import ContextBuilder
from automation.generators.smart_generator import SmartGenerator


class ArticleOrchestrator:

    def __init__(self, article_path):

        self.article_path = article_path
        self.context_builder = ContextBuilder()

        self.context = {}
        self.generator = SmartGenerator()

    # -------------------------
    # LOAD CONTEXT (SAFE)
    # -------------------------

    def load_context(self):

        print("📦 LOADING CONTEXT...")

        try:
            ctx = self.context_builder.build(self.article_path)

            if not isinstance(ctx, dict):
                print("⚠️ Context non valido → fallback empty dict")
                ctx = {}

            self.context = ctx

        except Exception as e:
            print(f"⚠️ Context error → fallback: {e}")
            self.context = {}

        print("📄 CONTEXT READY")
        return self.context

    # -------------------------
    # PROMPT BUILDER (SAFE)
    # -------------------------

    def build_prompt(self):

        article = self.context.get("article", {}).get("meta", {})
        cluster = self.context.get("cluster", {}).get("config", {})
        prompts = self.context.get("prompts", {})

        keyword = article.get("seo", {}).get("primary_keyword", "inglese")

        return f"""
Sei un content writer SEO per Lingue-Fluente.

CLUSTER:
{cluster.get('description', 'apprendimento lingue')}

KEYWORD:
{keyword}

REGOLE:
- Italiano semplice
- Struttura H2/H3
- Esempi pratici
- SEO ottimizzato
- Tono umano

OUTPUT:
Articolo completo HTML pronto per blog.
"""

    # -------------------------
    # GENERATE (ROBUST MODE)
    # -------------------------

    def generate_article(self):

        print("✍️ GENERATING ARTICLE...")

        prompt = self.build_prompt()

        article = ""

        try:
            article = self.generator.generate(prompt)
        except Exception as e:
            print(f"⚠️ AI ERROR: {e}")

        article = str(article or "").strip()

        # 🔥 GUARANTEED FALLBACK (ZERO FAILURE MODE)
        if len(article) < 200:

            print("🧱 USING GUARANTEED FALLBACK")

            title = self.context.get("article", {}).get("meta", {}).get(
                "title", "Imparare le lingue"
            )

            article = f"""
<h1>{title}</h1>

<p>Questo articolo è stato generato in modalità stabile del sistema Lingue-Fluente.</p>

<h2>Introduzione</h2>
<p>Imparare una lingua richiede costanza, esposizione e pratica quotidiana.</p>

<h2>Metodo pratico</h2>
<p>Usa esempi reali, ripetizione e immersione nel contesto.</p>

<h2>Consiglio</h2>
<p>Strumenti come Babbel possono aiutare a strutturare il percorso.</p>
"""

        print(f"📏 FINAL ARTICLE LENGTH: {len(article)}")

        return article

    # -------------------------
    # RUN PIPELINE
    # -------------------------

    def run(self):

        print("🚀 ORCHESTRATOR START")

        self.load_context()

        article = self.generate_article()

        print("✅ ORCHESTRATOR DONE")

        return article
