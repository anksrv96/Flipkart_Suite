import time

from selenium.webdriver.common.by import By

from Pages.base_page import BasePage


class SearchPage(BasePage):
    BRAND_SECTION = (By.XPATH, "//*[@id='container']/div/div[3]/div[1]/div[1]/div/div/div/section[4]")
    HALDIRAM_CHECKBOX = (By.XPATH,
                         "//*[@id='container']/div/div[3]/div[1]/div[1]/div/div/div/section[4]/div[2]/div[1]/div[2]/div/label/input")

    def __init__(self, driver):
        super().__init__(driver)

    def get_visibility_of_brand_filter(self):
        return self.is_visible(self.BRAND_SECTION)

    def get_visibility_of_product_anchors(self):
        if len(self.PRODUCT_ANCHORS) > 0:
            return True
        else:
            return False

    def select_brand_filter(self):
        self.do_click(self.HALDIRAM_CHECKBOX)

    def get_applicability_of_filter(self):
        time.sleep(5)
        prod_list = []
        PRODUCT_ANCHORS = self.driver.find_elements(By.XPATH,
                                                    "//*[@id='container']/div/div[3]/div[1]/div[2]/div[2]/div/div)")
        for i in range(len(PRODUCT_ANCHORS)):
            prod_list.append(self.get_element_text(
                self.driver.find_element(By.XPATH, "//*[@id='container']/div/div[3]/div[1]/div[2]/div[2]/div/div[", i,
                                         "]/div/a[2]")))

        for i in prod_list:
            if "Haldiram" not in i:
                flag = False
        return flag

    def select_product(self):
        self.do_click(self.PRODUCT_ANCHORS[1])
