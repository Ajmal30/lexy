import subprocess
import os
import click
from lexy_helpers.fetch_lexy import LexyScraper
from lexy_helpers.config import load_config, build_fzf_command
from pathlib import Path


class LexyFinder:
    def __init__(self, language: str, languages: list, lexy: LexyScraper):
        self.language = language
        self.languages = languages
        self.lexy = lexy
        self.homedir = Path.home()
        self.directory = self.homedir / ".config/lexy/files"

    def language_finder(self):
        file_path = self.lexy.file_path
        if not any(
            self.language.lower() == d["language"].lower() for d in self.languages
        ):
            click.secho(f"Language {self.language} not found", fg="red")
            return exit(1)
        for lang in self.languages:
            language_name = lang["language"].lower()
            language_file = lang["language"] + lang["file_extension"]
            if language_name == self.language:
                with open(f"{file_path}/{language_file}", "r") as file:
                    full_path = os.path.abspath(file.name)
                    subprocess.run(["bat", full_path])

    def _get_language(self):
        config = load_config()
        fzf_command = build_fzf_command(config)
        subprocess.run(fzf_command, shell=True, cwd=self.directory)


class LexyInit:
    def __init__(self, lexy: LexyScraper):
        self.lexy = lexy

    def ensure_languages_file(self):
        json_path = self.lexy.json_path
        if not json_path.exists():
            self.lexy.fetch_language()
