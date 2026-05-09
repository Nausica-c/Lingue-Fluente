from runtime.context_builder import ContextBuilder
from automation.generators.gemini_generator import GeminiGenerator


class ArticleOrchestrator:

    def __init__(self, article_path):

        self.article_path = article_path

        self.context_builder = ContextBuilder()

        self.context = None
        self.generator = None

    # -------------------------
    # LOAD CONTEXT
    # -------------------------

    def load_context(self):

        print("📦 LOADING CONTEXT...")

        self.context = self.context_builder.build(self.article_path)

        # 🔥 DEBUG
        print("📄 CONTEXT TYPE:", type(self.context))

        if not self.context:

            raise Exception("❌ Context non caricato")

        print("✅ Context caricato")

        return self.context

    # -------------------------
    # INIT GENERATOR
    # -------------------------

    def init_generator(self):

        print("🤖 INIT GENERATOR...")

        # 🔥 FIX DEFINITIVO
        # bypass pipeline config mancante
        provider = "gemini"
        model = "gemini-1.0-pro"

        print(f"📡 PROVIDER: {provider}")
        print(f"🧠 MODEL: {model}")

        self.generator = GeminiGenerator(model=model)

        if not self.generator:

            raise Exception("❌ Generator non inizializzato")

        print("✅ Generator inizializzato")

        return self.generator

    # -------------------------
    # BUILD PROMPT
    # -------------------------

    def build_prompt(self):

        print("🧠 BUILD PROMPT...")

        try:

            article = self.context.get("article", {}).get("meta", {})

            cluster = self.context.get("cluster", {}).get("config", {})

            prompts = self.context.get("prompts", {})

            primary_keyword = article.get("seo", {}).get(
                "primary_keyword",
                ""
            )

            # 🔥 SAFE FALLBACKS
            brand_voice = (
                prompts.get("prompts", {})
                .get("global", {})
                .get("brand_voice", "Motivazionale e chiaro")
            )

            writing_style = (
                prompts.get("prompts", {})
                .get("global", {})
                .get("writing_style", "SEO semplice")
            )

            article_structure = (
                prompts.get("prompts", {})
                .get("article_structure", {})
                .get("order", [])
            )

            return f"""
Sei un content writer professionista per il sito Lingue-Fluente.

BRAND VOICE:
{brand_voice}

STILE:
{writing_style}

CLUSTER:
{cluster.get('description', '')}

OBIETTIVI:
{cluster.get('goals', [])}

STRUTTURA:
{article_structure}

KEYWORD:
{primary_keyword}

REGOLE:
- Scrivi in italiano naturale
- Usa H2 e H3
- Mantieni tono umano
- Inserisci esempi pratici
- Evita ripetizioni
- Ottimizza SEO

CTA:
Inserisci Babbel come soluzione consigliata.

OUTPUT:
Articolo HTML completo pronto per pubblicazione.
"""

        except Exception as e:

            raise Exception(f"❌ PROMPT BUILD ERROR: {e}")

    # -------------------------
    # GENERATE ARTICLE
    # -------------------------

    def generate_article(self):

        print("✍️ GENERATING ARTICLE...")

        prompt = self.build_prompt()

        article = self.generator.generate(prompt)

        # 🔥 DEBUG
        print("📄 GENERATED TYPE:", type(article))

        if article:
            print("📏 GENERATED LENGTH:", len(str(article)))

        if not article or len(str(article).strip()) < 50:

            raise Exception("❌ Articolo vuoto o non valido")

        return article

    # -------------------------
    # RUN PIPELINE
    # -------------------------

    def run(self):

        print("🚀 Avvio orchestrator Lingue-Fluente...")

        self.load_context()

        self.init_generator()

        article = self.generate_article()

        print("✅ Articolo generato")

        return article
