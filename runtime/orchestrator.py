from runtime.context_builder import ContextBuilder
from automation.generators.smart_generator import SmartGenerator


class ArticleOrchestrator:

    def __init__(self, article_path):

        self.article_path = article_path
        self.context_builder = ContextBuilder()

        self.context = {}
        self.generator = None

    # -------------------------
    # LOAD CONTEXT
    # -------------------------

    def load_context(self):

        print("📦 LOADING CONTEXT...")

        try:
            self.context = self.context_builder.build(self.article_path)

        except Exception as e:
            print(f"⚠️ Context build error: {e}")
            self.context = {}

        if not isinstance(self.context, dict):
            self.context = {}

        print("📄 CONTEXT LOADED (SAFE MODE)")

        return self.context

    # -------------------------
    # INIT GENERATOR
    # -------------------------

    def init_generator(self):

        print("🤖 INIT SMART GENERATOR...")

        try:
            self.generator = SmartGenerator()
        except Exception as e:
            print(f"❌ Generator init failed: {e}")
            self.generator = None

        return self.generator

    # -------------------------
    # PROMPT
    # -------------------------

    def build_prompt(self):

        article = self.context.get("article", {}).get("meta", {})
        cluster = self.context.get("cluster", {}).get("config", {})
        prompts = self.context.get("prompts", {})

        primary_keyword = article.get("seo", {}).get("primary_keyword", "lingua inglese")

        brand_voice = prompts.get("prompts", {}).get("global", {}).get(
            "brand_voice", "Chiaro e semplice"
        )

        writing_style = prompts.get("prompts", {}).get("global", {}).get(
            "writing_style", "SEO base"
        )

        return f"""
Sei un copywriter SEO per Lingue-Fluente.

BRAND:
{brand_voice}

STILE:
{writing_style}

CLUSTER:
{cluster.get('description', '')}

KEYWORD:
{primary_keyword}

ISTRUZIONI:
- Italiano semplice
- Struttura con H2 e H3
- Esempi pratici
- Nessuna ripetizione
- Ottimizzato SEO

CTA:
Inserisci Babbel in modo naturale.

OUTPUT:
Articolo completo.
"""

    # -------------------------
    # GENERATE (STABILE + FALLBACK)
    # -------------------------

    def generate_article(self):

        print("✍️ GENERATING ARTICLE...")

        prompt = self.build_prompt()

        article = ""

        try:
            if self.generator and hasattr(self.generator, "generate"):
                article = self.generator.generate(prompt)
        except Exception as e:
            print(f"⚠️ AI ERROR: {e}")

        # normalizzazione
        if article:
            article = str(article).strip()

        # 🔥 FALLBACK ASSOLUTO (NON SI BLOCCA MAI)
        if not article or len(article) < 200:

            print("🧱 USING SAFE FALLBACK")

            title = self.context.get("article", {}).get("meta", {}).get("title", "Articolo")

            article = f"""
<h1>{title}</h1>

<p>Questo articolo è stato generato in modalità fallback.</p>

<h2>Introduzione</h2>
<p>Imparare una lingua richiede pratica costante e metodo.</p>

<h2>Consiglio pratico</h2>
<p>Usa contenuti quotidiani e ripetizione attiva.</p>

<h2>Strumento consigliato</h2>
<p>Babbel può aiutarti a strutturare lo studio in modo efficace.</p>
"""

        print(f"📏 FINAL LENGTH: {len(article)}")

        return article

    # -------------------------
    # RUN
    # -------------------------

    def run(self):

        print("🚀 START ORCHESTRATOR")

        self.load_context()
        self.init_generator()

        result = self.generate_article()

        print("✅ DONE")

        return result
