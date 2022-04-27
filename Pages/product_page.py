from selenium.webdriver.common.by import By

from Pages.base_page import BasePage


class ProductPage(BasePage):
    ADD_TO_CART = (By.XPATH, "//*[@id='container']/div/div[3]/div[1]/div[1]/div[2]/div/ul/li[1]/button")
    BUY_NOW = (By.XPATH, "//*[@id='container']/div/div[3]/div[1]/div[1]/div[2]/div/ul/li[2]/form/button")
    PRODUCT_TITLE = (By.XPATH, "//*[@id='container']/div/div[3]/div[1]/div[2]/div[2]/div/div[1]/h1/span")

    def __init__(self, driver):
        super().__init__(driver)

    def get_visibility_of_buy_now(self):
        return self.is_visible(self.BUY_NOW)

    def get_visibility_of_add_to_cart(self):
        return self.is_visible(self.BUY_NOW)