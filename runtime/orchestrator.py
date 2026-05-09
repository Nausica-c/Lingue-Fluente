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

        self.context = self.context_builder.build(self.article_path)

        return self.context

    # -------------------------
    # INIT AI GENERATOR
    # -------------------------

    def init_generator(self):

        provider = self.context["pipeline"]["generation"]["provider"]
        model = self.context["pipeline"]["generation"]["model"]

        if provider == "gemini":
            self.generator = GeminiGenerator(model=model)

        return self.generator

    # -------------------------
    # BUILD PROMPT
    # -------------------------

    def build_prompt(self):

        article = self.context["article"]["meta"]
        cluster = self.context["cluster"]["config"]
        prompts = self.context["prompts"]

        primary_keyword = article.get("seo", {}).get("primary_keyword", "")

        prompt = f"""
Sei un content writer per il sito Lingue-Fluente.

BRAND VOICE:
{prompts['prompts']['global']['brand_voice']}

STILE:
{prompts['prompts']['global']['writing_style']}

CLUSTER:
{cluster.get('description', '')}

OBIETTIVI:
{cluster.get('goals', [])}

STRUTTURA ARTICOLO:
{prompts['prompts']['article_structure']['order']}

KEYWORD PRINCIPALE:
{primary_keyword}

REGOLE:
- Scrivi in italiano semplice
- Usa esempi pratici
- Inserisci sezioni chiare
- Mantieni tono motivazionale
- Evita linguaggio artificiale

CTA:
Inserisci in modo naturale Babbel come soluzione per imparare lingue.

OUTPUT:
Articolo SEO completo pronto per pubblicazione.
"""

        return prompt

    # -------------------------
    # GENERATE ARTICLE
    # -------------------------

    def generate_article(self):

        prompt = self.build_prompt()

        article = self.generator.generate(prompt)

        return article

    # -------------------------
    # RUN FULL PIPELINE
    # -------------------------

    def run(self):

        print("🚀 Avvio orchestrator Lingue-Fluente...")

        self.load_context()

        self.init_generator()

        print("✍️ Generazione articolo in corso...")

        article = self.generate_article()

        print("✅ Articolo generato")

        return article
