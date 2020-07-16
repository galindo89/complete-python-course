"""-----------------------First implementation Too much complicated logic in the app---------------------------------"""

# from selenium import webdriver #import selenium's webdriver
# from pages.quotes_page import QuotesPage
#
# chrome=webdriver.Chrome(executable_path=r"C:\Users\Pablo Galindo\Coding\chromedriver.exe") #"""defines the object chrome that is returned by
#                                                                                               #selenium webdriver"""
# chrome.get("http://quotes.toscrape.com/search.aspx")
# page=QuotesPage(chrome) #chrome object contains the whole webpage


# author=input("Select please your Author: ")
# page.select_author(author)
# tags=page.get_available_tags()
# print("Select one of these tag: [{}]".format(" | ".join(tags)))
# selected_tag=input("Enter your tag: ")
# page.select_tag(selected_tag)
# page.search_button.click()
# print(page.quotes)

"""-----------------------Simplified implementation-----------------------------------------------------------------"""
from selenium import webdriver #import selenium's webdriver
from pages.quotes_page import QuotesPage

chrome=webdriver.Chrome(executable_path=r"C:\Users\Pablo Galindo\Coding\chromedriver.exe") #"""defines the object chrome that is returned by
                                                                                              #selenium webdriver"""
chrome.get("http://quotes.toscrape.com/search.aspx")
page=QuotesPage(chrome) #chrome object contains the whole webpage

author=input("Select please your Author: ")
tag=input("Enter your tag: ")
print(page.search_for_quotes(author,tag)) #Prints out the quotes based on the input of author and tag


