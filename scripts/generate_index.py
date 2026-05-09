from pathlib import Path

ROOT = Path.cwd()

SITE = ROOT / "_site"

SITE.mkdir(exist_ok=True)

articles = list(SITE.glob("*.html"))

links = []

for article in articles:

    if article.name == "index.html":
        continue

    links.append(
        f'<li><a href="{article.name}">{article.stem}</a></li>'
    )

html = f"""
<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <title>Lingue-Fluente</title>
</head>
<body>

<h1>Lingue-Fluente</h1>

<p>Articoli disponibili:</p>

<ul>
    {''.join(links)}
</ul>

</body>
</html>
"""

index_file = SITE / "index.html"

index_file.write_text(html, encoding="utf-8")

print("✅ index.html generated")
