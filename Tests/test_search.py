import time

from Config.config import TestData
from Pages.login_page import LoginPage
from Tests.test_base import BaseTest


class TestSearch(BaseTest):
    def test_search_page_landing(self):
        self.login_page = LoginPage(self.driver)
        home_page = self.login_page.perform_login_(TestData.USERNAME, TestData.PASSWORD)
        time.sleep(2)
        home_page.populate_search_bar(TestData.SEARCH_QUERY)
        search_page = home_page.click_search_button()
        time.sleep(2)
        assert search_page.get_visibility_of_brand_filter()

    def test_visibility_of_search_results(self):
        self.login_page = LoginPage(self.driver)
        home_page = self.login_page.perform_login_(TestData.USERNAME, TestData.PASSWORD)
        time.sleep(2)
        home_page.populate_search_bar(TestData.SEARCH_QUERY)
        search_page = home_page.click_search_button()
        time.sleep(2)
        assert search_page.get_applicability_of_filter()
