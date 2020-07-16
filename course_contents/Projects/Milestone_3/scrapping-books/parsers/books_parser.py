import re
import logging
from locators.books_locators import BooksLocators

logger=logging.getLogger("scraping.books_parser")

class BooksParser:

    RATINGS={
        "One":1,
        "Two":2,
        "Three":3,
        "Four":4,
        "Five":5

    }



    """
    Given  one of the specific books divs, find out the data about the book (name , price, link, rating).

    """

    def __init__(self,parent):
        logger.debug(f"Parsing information from the following book {parent}")
        self.parent = parent


    def __repr__(self):
        return f"<Book name is {self.name},its price is {self.price}, its rating is {self.rating} and it is {self.availabilty}>"

    @property
    def  name(self):
        logger.debug("Finding book name}")
        locator=BooksLocators.NAME
        item_name=self.parent.select_one(locator).attrs["title"]
        logger.debug(f"Found book name, {item_name}")
        return item_name

    def  link(self):
        logger.debug("Finding book link")
        locator=BooksLocators.NAME
        item_link=self.parent.select_one(locator).attrs["href"]
        logger.debug(f"Found book name, {item_link}")
        return item_link

    @property
    def price(self):
        logger.debug("Finding book price")
        locator = BooksLocators.PRICE
        item_price = self.parent.select_one(locator).string
        pattern="£([0-9]+\.[0-9]+)"
        matcher=re.search(pattern,item_price)
        logger.debug(f"Found book name, {item_price}")
        return matcher.group(1)

    @property
    def rating(self):
        logger.debug("Finding book rating")
        locator = BooksLocators.RATING
        item_rating=self.parent.select_one(locator).attrs["class"] #it will return for example ["star-rating","Three"]
        rating_classes=[r for r in item_rating if r !="star-rating"]
        logger.debug(f"Found book name, {item_rating}")
        return BooksParser.RATINGS.get(rating_classes[0])

    @property
    def availabilty(self):
        logger.debug("Finding book availability}")
        locator = BooksLocators.AVAILABILITY
        item_availabilty= self.parent.select_one(locator)
        logger.debug(f"Found book availability, {item_availabilty}")
        return item_availabilty.get_text(strip = True)

