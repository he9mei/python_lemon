#!/usr/bin/python3
# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from web.web_po.web_po_v2.PageLocators.index_page_locator import IndexPageLocator as loc
from selenium.webdriver.remote.webdriver import WebDriver


class IndexPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def wait(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    def locate_element(self, locator):
        return self.driver.find_element(*locator)

    # 我自己的写法
    def get_account_text(self):
        self.wait(loc.loc_my_account)
        return self.locate_element(loc.loc_my_account).text

    # 老师的写法
    def check_user_ele_exists(self):
        # 先等待首页按钮元素出现，表达另外一种思路：如果首页元素出现，理论上讲页面已经加载完了，我的账户也应该出现。
        self.wait(loc.loc_home)
        # 获取我的账户这个元素
        try:
            self.driver.find_element(*loc.loc_my_account)
        except:
            return False
        else:
            return True
