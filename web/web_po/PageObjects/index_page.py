#!/usr/bin/python3
# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class IndexPage:
    loc_my_account = (By.XPATH, "//a[text()='我的帐户[python]']")

    def __init__(self, driver):
        self.driver = driver

    def wait(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    def locate_element(self, locator):
        return self.driver.find_element(*locator)

    def get_account_text(self):
        self.wait(self.loc_my_account)
        return self.locate_element(self.loc_my_account).text
