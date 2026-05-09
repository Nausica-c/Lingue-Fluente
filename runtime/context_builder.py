import yaml
import frontmatter
from pathlib import Path


class ContextBuilder:

    def __init__(self, config_path="config"):
        self.config_path = Path(config_path)

    # -------------------------
    # LOAD YAML CONFIG
    # -------------------------

    def load_yaml(self, filename):
        path = self.config_path / filename

        if not path.exists():
            return {}

        with open(path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)

    # -------------------------
    # LOAD ARTICLE
    # -------------------------

    def load_article(self, article_path):
        with open(article_path, "r", encoding="utf-8") as f:
            post = frontmatter.load(f)

        return {
            "meta": post.metadata,
            "content": post.content
        }

    # -------------------------
    # BUILD FULL CONTEXT
    # -------------------------

    def build(self, article_path):

        article = self.load_article(article_path)

        site_config = self.load_yaml("site.yaml")
        clusters = self.load_yaml("clusters.yaml")
        linking = self.load_yaml("linking_graph.yaml")
        offers = self.load_yaml("offers.yaml")
        prompts = self.load_yaml("prompts.yaml")
        pipeline = self.load_yaml("content_pipeline.yaml")

        cluster_name = article["meta"].get("cluster")

        cluster_config = clusters.get("clusters", {}).get(cluster_name, {})

        context = {

            "site": site_config.get("site", {}),

            "article": article,

            "cluster": {
                "name": cluster_name,
                "config": cluster_config
            },

            "linking": linking,

            "offers": offers,

            "prompts": prompts,

            "pipeline": pipeline,

        }

        return context

    # -------------------------
    # SIMPLE DEBUG OUTPUT
    # -------------------------

    def preview(self, article_path):

        context = self.build(article_path)

        print("\n===== CONTEXT PREVIEW =====\n")
        print(f"CLUSTER: {context['cluster']['name']}")
        print(f"TITLE: {context['article']['meta'].get('title')}")
        print(f"KEYWORD: {context['article']['meta'].get('seo', {}).get('primary_keyword')}")
        print("\n===========================\n")

        return context
