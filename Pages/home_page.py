import time
from appscript import app

from selenium.webdriver.common.by import By

from Pages.base_page import BasePage
from Pages.search_page import SearchPage


class HomePage(BasePage):
    HEADER = (By.XPATH, "//*[@id='container']/div/div[1]/div[1]/div[2]/div[1]/div/a[1]/img")
    SEARCH_BAR = (By.XPATH, "//*[@id='container']/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input")
    SEARCH_BUTTON = (By.XPATH, "//*[@id='container']/div/div[1]/div[1]/div[2]/div[2]/form/div/button")
    GROCERY_BUTTON = (By.XPATH, "//*[@id='container']/div/div[2]/div/div/div[2]/a")
    FASHION_SECTION = (By.XPATH, "//*[@id='container']/div/div[2]/div/div/div[4]/a/div[1]")
    CART_BUTTON = (By.XPATH, "//*[@id='container']/div/div[1]/div[1]/div[2]/div[6]/div/div/a")

    def __init__(self, driver):
        super().__init__(driver)

    def get_visibility_of_header(self):
        return self.is_visible(self.HEADER)

    def get_visibility_of_search_button(self):
        return self.is_visible(self.SEARCH_BUTTON)

    def get_visibility_of_search_bar(self):
        return self.is_visible(self.SEARCH_BAR)

    def get_visibility_of_grocery_button(self):
        return self.is_visible(self.GROCERY_BUTTON)

    def get_visibility_of_fashion_section(self):
        return self.is_visible(self.FASHION_SECTION)

    def populate_search_bar(self, query):
        self.do_send_keys(self.SEARCH_BAR, query)

    def click_search_button(self):
        time.sleep(1.5)
        try:
            self.do_click(self.SEARCH_BUTTON)
        except Exception as e:
            app('System Events').keystroke('\r')
        finally:
            return SearchPage(self.driver)
