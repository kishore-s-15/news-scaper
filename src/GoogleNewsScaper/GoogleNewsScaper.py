# Importing the required libraries

import sys
import pprint
import logging
from datetime import datetime
from typing import List, Dict, Union

import requests
from bs4 import BeautifulSoup

# Return type of articles
Articles = Dict[str, Union[str, datetime]]


class GoogleNewsScraper:
    """
    GoogleNewsScraper scrapes articles from google news rss feeds.
    """

    # Constants
    DATE_TIME_FORMAT = "%a, %d %b %Y %H:%M:%S %Z"
    BASE_URL = "https://news.google.com/rss/search"

    def __init__(self, query: str):
        """
        Constuctor method initializes GoogleNewsScraper object
        to scrape google news rss feeds for the given query.

        Args:
            query (str): Query to scrape.
        """

        self._query = query
        self.url = f"{self.BASE_URL}?q={query}"

        self.setup_logger()

        self.pretty_printer = pprint.PrettyPrinter()

    @property
    def query(self):
        """
        Getter method for _query attribute.
        """

        return self._query

    @query.setter
    def query(self, query_string: str):
        """
        Setter method for _query attribute.

        Args:
            query_string (str): Query to scrape.
        """

        query_string_list = query_string.split(" ")
        query_string_list = list(map(lambda x: x.lower(), query_string_list))

        query_string = "+".join(query_string_list)

        self._query = query_string

    def setup_logger(self):
        """
        Method sets up the logger.
        """

        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)

        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(logging.DEBUG)

        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        handler.setFormatter(formatter)

        self.logger.addHandler(handler)

    def parse_string_to_datetime(self, date_time_str: str) -> datetime:
        """
        Method parses string to python datetime object.

        Args:
            date_time_str (str): Datetime string.

        Returns:
            date_time_obj (datetime): Parsed python datetime object.
        """

        date_time_obj = datetime.strptime(date_time_str, self.DATE_TIME_FORMAT)
        return date_time_obj

    def scrape_articles(self) -> List[Articles]:
        """
        Method scrapes google news rss feed articles.

        Returns:
            articles (List[Articles]): List of scraped articles of type Article.
        """

        self.logger.info(f"Started scraping {self.url}...")

        xml_content = requests.get(self.url).content
        soup = BeautifulSoup(xml_content, features="xml")
        items = soup.find_all("item")

        self.logger.info(f"Scraped {len(items)} articles.")

        articles: List[Articles] = []

        for item in items:
            article = {}

            # Articles Info
            article["link"] = item.find("link").text
            article["title"] = item.find("title").text
            article["description"] = item.find("description").text

            # Publisher info
            article["publisher"] = item.find("source").text
            article["published_date"] = self.parse_string_to_datetime(
                item.find("pubDate").text
            )

            articles.append(article)

        return articles

    def print_articles(self, articles: List[Articles]):
        """
        Method pretty prints scraped articles.

        Args:
            articles (List[Articles]): Scraped Articles.
        """

        self.pretty_printer.pprint(articles)


if __name__ == "__main__":
    query = "Carbon Net Zero"

    google_scaper = GoogleNewsScraper(query)

    articles = google_scaper.scrape_articles()

    google_scaper.print_articles(articles)
