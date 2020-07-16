import requests
from bs4 import BeautifulSoup

# page = requests.get("http://www.example.com")
# soup = BeautifulSoup(page.content, "html.parsers")
#
# #print(soup.find("h1").string)
# print(soup.select_one("p a").attrs["href"])
# print(page.content)
# page_content=requests.get("http://quotes.toscrape.com").content
# soup = BeautifulSoup(page_content, "html.parser")
# print(soup.select("div .quote .text"))

page_content=requests.get("http://books.toscrape.com/").content
soup = BeautifulSoup(page_content, "html.parser")
item=soup.select_one("div.page_inner section div ul.pager li.current").get_text(strip = True)
print(item)


# def availabilty(self):
#     locator = BooksLocators.AVAILABILITY
#     item_availabilty = self.parent.select_one(locator).string
#     return item_availabilty