from selenium.webdriver.common.by import By

from Pages.base_page import BasePage


class CartPage(BasePage):
    HEADER = (By.XPATH, "//*[@id='container']/div/div[2]/div/div/div/div/div[1]/div/div/div[1]")
    PRODUCT_LIST = [(By.XPATH, "//*[@id='container']/div/div[2]/div/div/div[1]/div/div")]

