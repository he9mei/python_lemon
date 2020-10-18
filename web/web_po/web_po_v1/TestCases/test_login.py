#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
from selenium import webdriver
from web.web_po.web_po_v1.PageObjects import LoginPage
from web.web_po.web_po_v1.PageObjects import IndexPage
from time import sleep


class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get("http://120.78.128.25:8765/Index/login.html")
        # 每个用例都有Page页面的实例化，可以写在前置中
        self.login_page = LoginPage(self.driver)
        self.index_page = IndexPage(self.driver)

    def tearDown(self):
        sleep(2)
        self.driver.quit()

    # @unittest.skip
    def test_login_scucess(self):
        # 前置条件：打开浏览器，进入登录页面
        # 步骤：登录页面-输入账号密码，点击登录
        # 断言：首页-登录账号信息存在
        # 测试数据：18684720553/python
        # login_page = LoginPage(self.driver)
        # index_page = IndexPage(self.driver)
        self.login_page.login(account="18684720553", pwd="python")
        self.assertIn("我的帐户", self.index_page.get_account_text())

    @unittest.skip
    def test_login_noPWD(self):
        # 前置条件：打开浏览器，进入登录页面
        # 步骤：登录页面-输入账号,不输入密码，点击登录
        # 断言：登录页面-错误信息:请输入密码
        # 测试数据：18684720553/空
        self.login_page.login(account="18684720553", pwd="")
        self.assertEqual(self.login_page.get_error_msg(), "请输入密码")

    @unittest.skip
    def test_login_wrongPWD(self):
        # 前置条件：打开浏览器，进入登录页面
        # 步骤：登录页面-输入账号,输入错误密码，点击登录
        # 断言：登录页面-错误信息:帐号或密码错误!
        # 测试数据：18684720553/111111
        self.login_page.login(account="18684720553", pwd="111111")
        self.assertEqual(self.login_page.get_error_toast(), "帐号或密码错误!")


if __name__ == "__main__":
    unittest.main()


'''
问题：为什么这里不用setUpClass和tearDownClass?
ui自动化测试用例编写原则（稳定性优先级最高）：
1.保持用例的独立性！无论其他用例成功与否，不影响我的运行。
比如我的前一个用例在中间某个页面报错，如果使用同一个浏览器，下一个用例就可能找不到页面或元素。

自己的理解：
以上至少对于WEB自动化是合理的，
如果对于APP的话，我自己做的是使用一个driver，但是每次用例执行完毕后无论是否成功都会回到主tab。
然后每个用例的开始也是从主tab。这样可以避免，用例失败，导致下一个用例找不到页面和元素的问题。
'''
