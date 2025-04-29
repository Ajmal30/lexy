import subprocess
import os
import click
from lexy_helpers.fetch_lexy import LexyScraper


class LexyFinder:
    def __init__(self, language: str, languages: list, lexy: LexyScraper):
        self.language = language
        self.languages = languages
        self.lexy = lexy

    def _generate_output(self):
        for lang in self.languages:
            yield f"{lang['language']}\n"

    def language_finder(self):
        file_path = self.lexy.file_path
        for lang in self.languages:
            language_name = lang["language"].lower()
            language_file = lang["language"] + lang["file_extension"]
            if language_name == self.language:
                with open(f"{file_path}/{language_file}", "r") as file:
                    full_path = os.path.abspath(file.name)
                    subprocess.run(["bat", full_path])
            if not self.language:
                click.secho(f"Language not found: {self.language}", fg="red")


class LexyInit:
    def __init__(self, lexy: LexyScraper):
        self.lexy = lexy

    def ensure_languages_file(self):
        json_path = self.lexy.json_path
        if not json_path.exists():
            self.lexy.fetch_language()
