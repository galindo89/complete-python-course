from typing import List
from selenium.webdriver.support.ui import Select

from locators.quotes_page_locators import QuotePageLocators
from parsers.quote import QuoteParser

class QuotesPage:
    def __init__(self,browser):
        self.browser = browser

    @property
    def quotes(self) -> List[QuoteParser]:
        return [
            QuoteParser(e)
            for e in self.browser.find_elements_by_css_selector(
                QuotePageLocators.QUOTE
            )

        ]

    @property
    def author_dropdown(self):
        element=self.browser.find_element_by_css_selector(

            QuotePageLocators.AUTHOR_DROPDOWN
        )
        return Select(element)


    @property
    def tags_dropdown(self):
        element = self.browser.find_element_by_css_selector(

            QuotePageLocators.TAG_DROPDOWN
        )
        return Select(element)

    @property #Return clickable object "Search Button" after author and tag have been input by user
    def search_button(self):
        return self.browser.find_element_by_css_selector(
            QuotePageLocators.SEARCH_BUTTON
        )

    def select_author(self, author_name: str):
        self.author_dropdown.select_by_visible_text(author_name)

    def get_available_tags(self)-> List[str]:
        return [option.text.strip() for option in self.tags_dropdown.options]

    def select_tag(self,tag_name:str):
        self.tags_dropdown.select_by_visible_text(tag_name)


    def search_for_quotes(self,author_name:str,tag_name:str)->List[QuoteParser]:
        try:
            self.select_author(author_name)
            self.select_tag(tag_name)
            self.search_button.click()

        except:
            print("Author or tag do not exist")
        return self.quotes
