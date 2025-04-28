from bs4 import BeautifulSoup
import requests
import json
import re


# FIX: I want to be able to add a dict to the existing json file if the language does not exist in the file. Check this: https://www.geeksforgeeks.org/append-to-json-file-using-python/
# TODO: Separate fetching and parsing logic into functions
#
class XnyScraper:
    def __init__(self):
        self.XNY_URL = "https://learnxinyminutes.com"
        self.response = requests.get(self.XNY_URL)
        self.soup = BeautifulSoup(self.response.text, "html.parser")
        self.languages = self.soup.select("tr td.name a")
        self.pattern = r"\.(?<=\.)[\w]+"
        self.languages_list = []

    def fetch_language(self):
        for language in self.languages:
            language_name = language.text.strip()
            if not language.get("href") or language_name == "AWK":
                language_url = None
                language_full_url = None
            else:
                language_url = language.get("href")
                language_full_url = self.XNY_URL + language_url
                language_response = requests.get(language_full_url)
                language_soup = BeautifulSoup(language_response.text, "html.parser")
                language_file = language_soup.select("p.filelink a")
            try:
                language_file_url = language_file[0].get("href")
                file_extension = re.search(self.pattern, language_file_url).group()
                language_file_full_url = self.XNY_URL + language_file_url
                language_dict = {
                    "language": language_name,
                    "language_url": language_full_url,
                    "language_file_url": language_file_full_url,
                }
                self.languages_list.append(language_dict)
                self.create_file(language_file_full_url, file_extension, language_name)

            except (IndexError, AttributeError):
                file_extension = ".txt"

    def save_to_json(self):
        with open("data/json/languages.json", "w") as f:
            json.dump(self.languages_list, f)

    def create_file(self, language_full_file_url, file_extension, language_name):
        content_response = requests.get(language_full_file_url)
        content_soup = BeautifulSoup(content_response.text, "html.parser")
        with open(f"data/files/{language_name}{file_extension}", "w") as file:
            file.write(content_soup.text)


if __name__ == "__main__":
    xny_scraper = XnyScraper()
    xny_scraper.fetch_language()
