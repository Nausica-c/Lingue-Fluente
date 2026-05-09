class ConversionOptimizer:

    def optimize(self, article):

        content = article["content"]

        seo = article["seo"]

        # aggiunge trigger psicologici semplici
        triggers = [
            "senza stress",
            "risultati veloci",
            "metodo pratico",
            "solo 15 minuti al giorno"
        ]

        for t in triggers:

            if t not in content:
                content += f"\n\n✔ {t}"

        return content
