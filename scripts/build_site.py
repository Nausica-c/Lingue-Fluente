from pathlib import Path
import yaml

class SiteBuilder:

    def __init__(self):
        self.root = Path.cwd()
        self.posts = self.root / "_posts"
        self.site = self.root / "_site"

        self.site.mkdir(exist_ok=True)

    # -------------------------
    # PARSER FRONTMATTER SEMPLICE
    # -------------------------

    def parse(self, content):
        if not content.startswith("---"):
            return {}

        parts = content.split("---")
        if len(parts) < 3:
            return {}

        try:
            return yaml.safe_load(parts[1]) or {}
        except:
            return {}

    # -------------------------
    # HTML GENERATOR BASE
    # -------------------------

    def to_html(self, meta):

        title = meta.get("title", "Articolo")
        keyword = meta.get("seo", {}).get("primary_keyword", "inglese")
        cluster = meta.get("cluster", "base")

        return f"""<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8">
<title>{title}</title>
</head>
<body>

<h1>{title}</h1>

<p>{keyword} è una competenza utile e importante.</p>

<h2>Metodo</h2>
<p>Nel cluster {cluster}, la chiave è la pratica costante.</p>

<h2>Esempio</h2>
<ul>
<li>Studia ogni giorno</li>
<li>Ripeti ad alta voce</li>
<li>Usa frasi reali</li>
</ul>

<h2>Conclusione</h2>
<p>La costanza è tutto.</p>

</body>
</html>"""

    # -------------------------
    # BUILD SITE
    # -------------------------

    def build(self):

        print("🚀 BUILD START")

        files = list(self.posts.glob("*.md"))

        print(f"📦 POSTS: {len(files)}")

        for f in files:

            print(f"✍️ {f.name}")

            content = f.read_text(encoding="utf-8")
            meta = self.parse(content)

            html = self.to_html(meta.get("article", {}).get("meta", meta))

            out = self.site / f"{f.stem}.html"
            out.write_text(html, encoding="utf-8")

            print(f"✅ SAVED {out.name}")

        print("🏁 DONE")


if __name__ == "__main__":
    SiteBuilder().build()
