#!/usr/bin/python3
# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from web.web_po.web_po_v2.PageLocators.login_page_locator import LoginPageLocator as loc
# 问题：在页面对象类调用driver的方法时，因为driver是外部传入的，这里写代码时无法自动弹起driver相关方法
# 解决-小技巧：
# （1）导入from selenium.webdriver.remote.webdriver import WebDriver
# （2）    def __init__(self, driver: WebDriver):
#         self.driver = driver
from selenium.webdriver.remote.webdriver import WebDriver


class LoginPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def wait(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    def locate_element(self, locator):
        return self.driver.find_element(*locator)

    def login(self, account, pwd):
        # 等待元素出现
        self.wait(loc.loc_input_account)
        # 输入用户名
        self.driver.find_element(*loc.loc_input_account).send_keys(account)
        # 输入密码
        self.locate_element(loc.loc_input_pwd).send_keys(pwd)
        # 点击登录按钮
        self.locate_element(loc.loc_bn_login).click()

    def get_error_msg(self):
        self.wait(loc.loc_errorMsg)
        return self.locate_element(loc.loc_errorMsg).text

    def get_error_toast(self):
        WebDriverWait(self.driver, 10, 0.1).until(EC.visibility_of_element_located(loc.loc_toast))
        return self.locate_element(loc.loc_toast).text






