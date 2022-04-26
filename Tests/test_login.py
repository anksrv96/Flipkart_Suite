from Config.config import TestData
from Pages.login_page import LoginPage
from Tests.test_base import BaseTest


class TestLoginPage(BaseTest):
    def test_login_page_displayed(self):
        self.login_page = LoginPage(self.driver)
        assert self.login_page.get_visibility_of_header(TestData.LOGIN_PAGE_HEADER)

    def test_username_field_present(self):
        self.login_page = LoginPage(self.driver)
        assert self.login_page.get_visibility_of_username()

    def test_password_field_present(self):
        self.login_page = LoginPage(self.driver)
        assert self.login_page.get_visibility_of_password()

    def test_login_button_present(self):
        self.login_page = LoginPage(self.driver)
        assert self.login_page.get_visibility_of_login_button()

    def test_perform_login(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.perform_login_(TestData.USERNAME, TestData.PASSWORD)

