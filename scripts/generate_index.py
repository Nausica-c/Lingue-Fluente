from pathlib import Path


class IndexGenerator:

    def __init__(self):

        self.site_dir = Path.cwd() / "_site"
        self.posts_dir = Path.cwd() / "_posts"

    # -------------------------
    # GET ARTICLES
    # -------------------------

    def get_articles(self):

        articles = list(self.posts_dir.glob("*.md"))

        return sorted(articles)

    # -------------------------
    # BUILD INDEX HTML
    # -------------------------

    def build_index(self, articles):

        items = ""

        for a in articles:

            slug = a.stem.replace("-", " ")
            url = f"{a.stem}.html"

            items += f"""
            <li>
                <a href="{url}">{slug.title()}</a>
            </li>
            """

        html = f"""
<!doctype html>
<html lang="it">
<head>
    <meta charset="utf-8">
    <title>Lingue-Fluente - Home</title>
    <meta name="description" content="Impara le lingue velocemente con metodi pratici e semplici">
</head>
<body>

    <h1>🌍 Lingue-Fluente</h1>

    <p>Articoli per imparare le lingue in modo semplice e veloce</p>

    <h2>📚 Articoli</h2>

    <ul>
        {items}
    </ul>

</body>
</html>
"""

        return html

    # -------------------------
    # SAVE INDEX
    # -------------------------

    def save(self, html):

        self.site_dir.mkdir(parents=True, exist_ok=True)

        file_path = self.site_dir / "index.html"

        file_path.write_text(html, encoding="utf-8")

        print(f"✅ INDEX CREATED: {file_path}")

    # -------------------------
    # RUN
    # -------------------------

    def run(self):

        print("🌐 GENERATING INDEX...")

        articles = self.get_articles()

        html = self.build_index(articles)

        self.save(html)


# ENTRYPOINT
if __name__ == "__main__":

    IndexGenerator().run()
