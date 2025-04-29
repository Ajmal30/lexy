from lexy_helpers.fetch_lexy import LexyScraper
from lexy_helpers.output_helpers import LexyFinder
import click
import json

lexy_scraper = LexyScraper()


@click.command()
@click.version_option()
@click.argument("language", metavar="<FILENAME>")
def lexy(language):
    """Display <FILENAME> documentation using bat.

    <FILENAME> refers to the language name.

    Use 'list' to view all available languages.

    Use "update" to force update Lexy.
    """
    language = language.lower()
    with open(f"{lexy_scraper.json_path}/languages.json", "r") as f:
        languages = json.load(f)
        lexy_finder = LexyFinder(language, languages, lexy_scraper)
        if language == "list":
            click.echo_via_pager(lexy_finder._generate_output())
        elif language == "update":
            lexy_scraper.force_update()
        else:
            lexy_finder.language_finder()
