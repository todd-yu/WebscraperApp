"""This module contains the logic to extract the relevant text from a set of html
data."""

from bs4 import BeautifulSoup

#For Testing
import requests
page = requests.get("https://techcrunch.com/2019/12/06/elon-musk-found-not-liable-in-case-brought-against-him-by-british-diver/")


def extract_text(raw_html):
    """Extracts all relevant text from article"""
    soup = BeautifulSoup(raw_html)

    def get_title_data(html_soup):
        """Returns the title of the article from HTML_SOUP"""
        return str(soup.title.string)

    def get_paragraph_data(html_soup):
        """Returns the paragraph text of the article from HTML_SOUP"""
        polluted_text = str(soup.find_all("p"))
        text_soup = BeautifulSoup(polluted_text)
        return text_soup.get_text()

    return get_title_data(soup) + " " + get_paragraph_data(soup)

