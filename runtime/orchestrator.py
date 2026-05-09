from runtime.context_builder import ContextBuilder
from automation.generators.smart_generator import SmartGenerator


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

        print("📄 CONTEXT TYPE:", type(self.context))

        if not isinstance(self.context, dict):

            raise Exception("❌ Context non valido (non dict)")

        print("✅ Context caricato")

        return self.context

    # -------------------------
    # INIT GENERATOR (SMART FIX)
    # -------------------------

    def init_generator(self):

        print("🤖 INIT SMART GENERATOR...")

        self.generator = SmartGenerator()

        print("✅ SmartGenerator attivo (Groq + fallback)")

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

            primary_keyword = article.get("seo", {}).get("primary_keyword", "")

            brand_voice = (
                prompts.get("prompts", {})
                .get("global", {})
                .get("brand_voice", "Chiaro e motivazionale")
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
Articolo completo pronto per pubblicazione.
"""

        except Exception as e:

            raise Exception(f"❌ PROMPT ERROR: {e}")

    # -------------------------
    # GENERATE ARTICLE
    # -------------------------

    def generate_article(self):

        print("✍️ GENERATING ARTICLE...")

        prompt = self.build_prompt()

        article = self.generator.generate(prompt)

        print("📄 GENERATED TYPE:", type(article))

        if article:
            print("📏 LENGTH:", len(str(article)))

        if not article or len(str(article).strip()) < 50:

            raise Exception("❌ Articolo vuoto o invalido")

        return article

    # -------------------------
    # RUN PIPELINE
    # -------------------------

    def run(self):

        print("🚀 START ORCHESTRATOR")

        self.load_context()
        self.init_generator()

        article = self.generate_article()

        print("✅ ARTICLE GENERATED")

        return article
