from pathlib import Path
import os

class Paths:

    @staticmethod
    def repo_root():
        # GitHub Actions safe root
        return Path(os.getenv("GITHUB_WORKSPACE", Path.cwd()))

    @staticmethod
    def posts():
        return Paths.repo_root() / "_posts"

    @staticmethod
    def site():
        return Paths.repo_root() / "_site"
