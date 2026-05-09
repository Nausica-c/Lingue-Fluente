import random
from pathlib import Path

from automation.autopilot.analytics_feedback_loop import AnalyticsFeedbackLoop


class AutoRewriteEngine:

    def __init__(self, posts_dir="_posts"):

        self.posts_dir = Path(posts_dir)

        self.analytics = AnalyticsFeedbackLoop()

    # -------------------------
    # TROVA ARTICOLI DA MIGLIORARE
    # -------------------------

    def select_articles_to_improve(self):

        insights = self.analytics.analyze()

        # prende i cluster peggiori
        sorted_clusters = sorted(
            insights.items(),
            key=lambda x: x[1]
        )

        worst_clusters = [c[0] for c in sorted_clusters[:2]]

        articles = []

        for file in self.posts_dir.glob("*.md"):

            for cluster in worst_clusters:

                if cluster in file.name:

                    articles.append(file)

        return articles

    # -------------------------
    # CREA PROMPT DI MIGLIORAMENTO
    # -------------------------

    def build_rewrite_prompt(self, content):

        return f"""
Sei un editor SEO avanzato.

Rivedi e migliora questo articolo:

OBIETTIVI:
- aumentare chiarezza
- migliorare SEO
- aumentare CTR
- rendere più naturale e umano
- migliorare conversioni Babbel

REGOLE:
- mantieni tono semplice
- migliora esempi
- aggiungi chiarimenti
- elimina ripetizioni
- rendi più scorrevole

ARTICOLO:
{content}

OUTPUT: versione migliorata completa
"""

    # -------------------------
    # RISCRIVE ARTICOLO
    # -------------------------

    def rewrite_article(self, file_path, ai_generator):

        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        prompt = self.build_rewrite_prompt(content)

        improved = ai_generator.generate(prompt)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(improved)

        print(f"♻️ Riscritto: {file_path}")

    # -------------------------
    # CICLO COMPLETO
    # -------------------------

    def run(self, ai_generator):

        articles = self.select_articles_to_improve()

        if not articles:
            print("✅ Nessun articolo da migliorare")
            return

        for article in articles:

            self.rewrite_article(article, ai_generator)
