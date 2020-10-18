#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
from selenium import webdriver
from time import sleep
import ddt

from web.web_po.web_po_v2.PageObjects.login_page import LoginPage
from web.web_po.web_po_v2.PageObjects.index_page import IndexPage
from web.web_po.web_po_v2.TestDatas import Global_Datas as gd
from web.web_po.web_po_v2.TestDatas import login_datas as ld


@ddt.ddt
class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get(gd.login_url)
        # 每个用例都有Page页面的实例化，可以写在前置中
        self.login_page = LoginPage(self.driver)
        self.index_page = IndexPage(self.driver)

    def tearDown(self):
        sleep(2)
        self.driver.quit()

    # @unittest.skip
    def test_login_1_scucess(self):
        # 前置条件：打开浏览器，进入登录页面
        # 步骤：登录页面-输入账号密码，点击登录
        # 断言：首页-登录账号信息存在
        # 测试数据：18684720553/python

        self.login_page.login(ld.success_data["user"], ld.success_data["pwd"])
        # self.assertIn("我的帐户", self.index_page.get_account_text())   # 我自己写法的断言
        self.assertTrue(self.index_page.check_user_ele_exists())   # 老师写法的断言

    # @unittest.skip
    @ddt.data(*ld.wrong_data_1)
    # @ddt.unpack # 注意：这里不需要再解包---待研究
    def test_login_2_wrongData(self, data):
        # 密码为空
        # 前置条件：打开浏览器，进入登录页面
        # 步骤：登录页面-输入账号,不输入密码，点击登录
        # 断言：登录页面-错误信息:请输入密码
        # 测试数据：18684720553/空
        # 步骤相同，其他场景：
        # 账号名为空，""/"python" "请输入手机号"；
        # 账号格式错误，10位"1850000000"或者12位"185000000000"/"python" "请输入正确的手机号"；

        self.login_page.login(data["user"], data["pwd"])
        self.assertEqual(self.login_page.get_error_msg(), data["check"])

    # @unittest.skip
    @ddt.data(*ld.wrong_data_2)
    # @ddt.unpack
    def test_login_3_wrongData(self, data):
        # 密码错误
        # 前置条件：打开浏览器，进入登录页面
        # 步骤：登录页面-输入账号,输入错误密码，点击登录
        # 断言：登录页面-错误信息:帐号或密码错误!
        # 测试数据：18684720553/111111
        # 步骤相同，其他场景：
        # 账号未注册，"18500000000"/"python" "此账号没有经过授权，请联系管理员!"

        self.login_page.login(data["user"], data["pwd"])
        self.assertEqual(self.login_page.get_error_toast(), data["check"])


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

补充：
对于setUpClass和tearDownClass，这里也可以用，但是需要调换一下执行顺序，先执行wrongData再执行success,
因为success涉及2个页面，会影响后面用例的执行。
结论：这里可以这么做，但是还是应该尽量保持用例的独立性，每个用例使用一次setUp和TearDown是最好的做法。
改写，见test_login_ddt_setUpClass.py
'''

# @ddt.unpack # 注意：这里不需要再解包---待研究