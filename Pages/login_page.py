from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Config.config import TestData
from Pages.base_page import BasePage
from Pages.home_page import HomePage


class LoginPage(BasePage):

    """By locators"""
    USERNAME = (By.XPATH, "/html/body/div[2]/div/div/div/div/div[2]/div/form/div[1]/input")
    PASSWORD = (By.XPATH, "/html/body/div[2]/div/div/div/div/div[2]/div/form/div[2]/input")
    LOGIN_BUTTON = (By.XPATH, "/html/body/div[2]/div/div/div/div/div[2]/div/form/div[4]/button")
    HEADER = (By.XPATH, "/html/body/div[2]/div/div/div/div/div[1]/span/span")

    """Class Constructor"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.delete_all_cookies()
        self.driver.get(TestData.BASE_URL)

        # WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(self.HEADER))

    """Page Actions"""
    def get_visibility_of_username(self):
        self.log_info("Validating username field")
        return self.is_visible(self.USERNAME)

    def get_visibility_of_password(self):
        self.log_info("Validating password field")
        return self.is_visible(self.PASSWORD)

    def get_visibility_of_login_button(self):
        self.log_info("Validating login button")
        return self.is_visible(self.LOGIN_BUTTON)

    def perform_login_(self, username, password):
        self.do_send_keys(self.USERNAME, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)
        self.log_info("PERFORMING LOGIN")
        return HomePage(self.driver)

    def get_visibility_of_header(self, header_text):
        if self.is_visible(self.HEADER):
            if self.get_element_text(self.HEADER) == header_text:
                return True
            else: return False
        else:
            return False

