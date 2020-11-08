#!/usr/bin/python3
# -*- coding: utf-8 -*-

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from web.web_po.web_po_v2.PageLocators.index_page_locator import IndexPageLocator as loc
from selenium.webdriver.remote.webdriver import WebDriver


class UserPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def get_user_leftMoney(self):
        pass

    def click_first_bid_on_investRecord(self):
        pass
