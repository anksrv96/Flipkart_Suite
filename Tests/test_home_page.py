from Config.config import TestData
from Pages.login_page import LoginPage
from Tests.test_base import BaseTest


class TestHomePage(BaseTest):
    def test_homepage_landing(self):
        self.login_page = LoginPage(self.driver)
        home_page = self.login_page.perform_login_(TestData.USERNAME, TestData.PASSWORD)
        flag = home_page.get_visibility_of_header()
        assert flag

    def test_search_button_visibility(self):
        self.login_page = LoginPage(self.driver)
        home_page = self.login_page.perform_login_(TestData.USERNAME, TestData.PASSWORD)
        flag = home_page.get_visibility_of_search_button()
        assert flag

    def test_search_bar_visibility(self):
        self.login_page = LoginPage(self.driver)
        home_page = self.login_page.perform_login_(TestData.USERNAME, TestData.PASSWORD)
        flag = home_page.get_visibility_of_search_bar()
        assert flag

    def test_grocery_button_visibility(self):
        self.login_page = LoginPage(self.driver)
        home_page = self.login_page.perform_login_(TestData.USERNAME, TestData.PASSWORD)
        flag = home_page.get_visibility_of_grocery_button()
        assert flag

    def test_fashion_section_visibility(self):
        self.login_page = LoginPage(self.driver)
        home_page = self.login_page.perform_login_(TestData.USERNAME, TestData.PASSWORD)
        flag = home_page.get_visibility_of_fashion_section()
        assert flag

