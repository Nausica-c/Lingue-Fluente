from automation.generators.gemini_generator import GeminiGenerator


class AIContentWriter:

    def __init__(self):

        self.ai = GeminiGenerator()

    # -------------------------
    # COSTRUISCE PROMPT ARTICOLO
    # -------------------------

    def build_prompt(self, frontmatter):

        meta = frontmatter["article"]["meta"]
        seo = frontmatter["seo"]

        prompt = f"""
Sei un esperto content writer SEO per il sito Lingue-Fluente.

Scrivi un articolo completo in italiano.

TITOLO:
{meta.get("title")}

KEYWORD PRINCIPALE:
{seo.get("primary_keyword")}

CLUSTER:
{meta.get("cluster")}

REGOLE:
- Linguaggio semplice (A1-A2)
- Frasi brevi
- Tono motivazionale
- Esempi pratici
- Struttura chiara con H2
- Inserisci spiegazioni passo-passo

STRUTTURA OBBLIGATORIA:

1. Introduzione (hook)
2. Problema
3. Soluzione semplice
4. Esempi pratici
5. Routine giornaliera
6. Errori comuni
7. FAQ
8. Conclusione + CTA Babbel naturale

IMPORTANTE:
- Non sembrare un AI
- Scrivi come un insegnante amichevole
- Non essere troppo formale
"""

        return prompt

    # -------------------------
    # GENERA ARTICOLO
    # -------------------------

    def generate(self, frontmatter):

        prompt = self.build_prompt(frontmatter)

        article = self.ai.generate(prompt)

        return article

    # -------------------------
    # UNISCE FRONTMATTER + CONTENUTO
    # -------------------------

    def build_full_article(self, frontmatter, content):

        meta = frontmatter["article"]["meta"]

        final_article = f"""{self._extract_frontmatter_text(frontmatter)}

{content}
"""

        return final_article

    # -------------------------
    # ESTRAE FRONTMATTER TESTO
    # -------------------------

    def _extract_frontmatter_text(self, frontmatter):

        # semplificato: nel sistema reale leggerai il file .md
        return "FRONTMATTER_GIA_PRESENTE"
