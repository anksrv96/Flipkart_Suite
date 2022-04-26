from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.base_page import BasePage


class LoginPage(BasePage):

    """By locators"""
    USERNAME = (By.CLASS_NAME, "_2IX_2- VJZDxU")
    PASSWORD = (By.CLASS_NAME, "_2IX_2- _3umUoc _3mctLh VJZDxU")
    LOGIN_BUTTON = (By.CLASS_NAME, "_2YsvKq o8qAfl")

    """Class Constructor"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    """Page Actions"""
    def get_visibility_of_username(self):
        return self.is_visible(self.USERNAME)

    def get_visibility_of_password(self):
        return self.is_visible(self.PASSWORD)

    def get_visibility_of_login_button(self):
        return self.is_visible(self.LOGIN_BUTTON)

    def perform_login_(self, username, password):
        self.do_send_keys(self.USERNAME, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)
