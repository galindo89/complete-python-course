from bs4 import BeautifulSoup
import re
import logging
from locators.books_page_locators import BooksPageLocator
from parsers.books_parser import BooksParser

logger=logging.getLogger("scraping.books_page")

class BooksPage:
    def __init__(self,page):
        logger.debug("Parsing page content with BeautifulSoup HTML parser...")
        self.soup=BeautifulSoup(page,"html.parser")

    @property
    def books(self):
        logger.debug(f"Finding all books in the page using `{BooksPageLocator.BOOKS}´.")
        locator=BooksPageLocator.BOOKS
        books_content=self.soup.select(locator)
        return [BooksParser(e) for e in books_content]

    @property
    def page_count(self):
        logger.debug("Finding all number of cataloge pages available....")
        content=self.soup.select_one(BooksPageLocator.PAGER).get_text(strip = True)
        logger.info(f"Found number of catalogue pages available `{content}`.")
        pattern="Page [0-9]+ of ([0-9]+)"
        matcher=re.search(pattern,content)
        pages=int(matcher.group(1))
        logger.debug(f"Extracted number of pages `{pages}`.")
        return pages