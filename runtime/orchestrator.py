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
            raise Exception("❌ Context non valido")

        print("✅ Context caricato")

        return self.context

    # -------------------------
    # INIT GENERATOR (ROBUSTO)
    # -------------------------

    def init_generator(self):

        print("🤖 INIT SMART GENERATOR...")

        self.generator = SmartGenerator()

        if not hasattr(self.generator, "generate"):
            raise Exception("❌ SmartGenerator non valido")

        print("✅ SmartGenerator pronto")

        return self.generator

    # -------------------------
    # BUILD PROMPT
    # -------------------------

    def build_prompt(self):

        print("🧠 BUILD PROMPT...")

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

        structure = (
            prompts.get("prompts", {})
            .get("article_structure", {})
            .get("order", [])
        )

        return f"""
Sei un content writer SEO per Lingue-Fluente.

BRAND VOICE:
{brand_voice}

STILE:
{writing_style}

CLUSTER:
{cluster.get('description', '')}

OBIETTIVI:
{cluster.get('goals', [])}

STRUTTURA:
{structure}

KEYWORD:
{primary_keyword}

REGOLE:
- Italiano naturale
- H2/H3 strutturati
- Esempi concreti
- Zero ripetizioni
- SEO pulito

CTA:
Inserisci Babbel come soluzione consigliata.

OUTPUT:
Articolo completo HTML.
"""

    # -------------------------
    # GENERATE ARTICLE (HARD SAFE MODE)
    # -------------------------

    def generate_article(self):

        print("✍️ GENERATING ARTICLE...")

        prompt = self.build_prompt()

        article = None

        try:
            article = self.generator.generate(prompt)
        except Exception as e:
            print(f"⚠️ GENERATOR ERROR: {e}")

        print("📄 GENERATED TYPE:", type(article))

        if article:
            article = str(article).strip()

        # 🔥 HARD FALLBACK (CRITICO)
        if not article or len(article) < 200:

            print("⚠️ USING FALLBACK ARTICLE")

            article = f"""
<h1>{self.context.get('article', {}).get('meta', {}).get('title', '')}</h1>

<p>Contenuto non generato correttamente dall'AI.</p>
<p>Questo è un fallback automatico stabile del sistema Lingue-Fluente.</p>
"""

        print("📏 FINAL LENGTH:", len(article))

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
