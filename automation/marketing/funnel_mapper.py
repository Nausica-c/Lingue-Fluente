class FunnelMapper:

    def __init__(self):

        self.cta_position = {
            "top": True,
            "middle": True,
            "bottom": True
        }

    # -------------------------
    # INSERISCE CTA BABBEL
    # -------------------------

    def inject_cta(self, article_content):

        cta = """

👉 Vuoi imparare davvero questa lingua?

Prova Babbel: lezioni brevi, pratiche e pensate per farti parlare subito.

"""

        if self.cta_position["top"]:
            article_content = cta + article_content

        if self.cta_position["middle"]:
            article_content = article_content.replace("</h2>", "</h2>\n" + cta, 2)

        if self.cta_position["bottom"]:
            article_content += cta

        return article_content
