from pathlib import Path

SITE_DIR = Path("_site")

def generate_index():
    files = list(SITE_DIR.glob("*.html"))

    links = "\n".join([
        f'<li><a href="./{f.name}">{f.stem}</a></li>'
        for f in files
        if f.name != "index.html"
    ])

    html = f"""
    <html>
    <body>
        <h1>Lingue-Fluente</h1>
        <ul>
            {links}
        </ul>
    </body>
    </html>
    """

    (SITE_DIR / "index.html").write_text(html, encoding="utf-8")

if __name__ == "__main__":
    generate_index()
