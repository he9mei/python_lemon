#!/usr/bin/python3
# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    # 账号输入框
    loc_input_account = (By.NAME, "phone")
    # 密码输入框
    loc_input_pwd = (By.NAME, "password")
    # 登录按钮
    loc_bn_login = (By.XPATH, "//button[text()='登录']")
    # 账号、密码为空时的错误提示，相同类型的提示都用这一个定位就可以了
    loc_errorMsg = (By.XPATH, '//div[@class="form-error-info"]')
    # 账号密码错误时，给出了toast提示
    # 定位toast方式：toast弹出之后，调试页面从element切换到source,然后点击pause on debugger停止
    # 然后再切换到到element，查看元素定位值
    loc_toast = (By.XPATH, '//div[@class="layui-layer-content"]')

    def __init__(self, driver):
        self.driver = driver

    def wait(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    def locate_element(self, locator):
        return self.driver.find_element(*locator)

    def login(self, account, pwd):
        # 等待元素出现
        self.wait(self.loc_input_account)
        # 输入用户名
        self.driver.find_element(*self.loc_input_account).send_keys(account)
        # 输入密码
        self.locate_element(self.loc_input_pwd).send_keys(pwd)
        # 点击登录按钮
        self.locate_element(self.loc_bn_login).click()

    def get_error_msg(self):
        self.wait(self.loc_errorMsg)
        return self.locate_element(self.loc_errorMsg).text

    def get_error_toast(self):
        WebDriverWait(self.driver, 10, 0.1).until(EC.visibility_of_element_located(self.loc_toast))
        return self.locate_element(self.loc_toast).text






