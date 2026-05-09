from pathlib import Path
import yaml


class ContextBuilder:

    def build(self, article_path):

        try:
            content = article_path.read_text(encoding="utf-8")

            if content.startswith("---"):

                parts = content.split("---")
                meta = yaml.safe_load(parts[1])

                return {
                    "article": {
                        "meta": meta
                    }
                }

        except Exception:
            pass

        return {
            "article": {
                "meta": {
                    "title": article_path.stem,
                    "cluster": "general",
                    "seo": {
                        "primary_keyword": "inglese"
                    }
                }
            }
        }
