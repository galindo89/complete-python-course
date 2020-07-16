import requests
import logging
from pages.books_page import BooksPage

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S',
                    level=logging.DEBUG,
                    filename='logs.txt')

logger=logging.getLogger("scraping")

logger.info("Loading the books list")

page_content=requests.get("http://books.toscrape.com/").content


page=BooksPage(page_content)

books=page.books

for page_num in range(1,page.page_count):
    url=f"http://books.toscrape.com/catalogue/page-{page_num+1}.html"
    page_content=requests.get(url).content
    page=BooksPage(page_content)
    books.extend(page.books)









