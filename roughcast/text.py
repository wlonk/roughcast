from bs4 import BeautifulSoup
from markdown import markdown


def unmark(text):
    return BeautifulSoup(markdown(text), 'html.parser').get_text()
