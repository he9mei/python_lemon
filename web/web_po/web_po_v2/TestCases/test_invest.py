#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 投资用例
import unittest
from selenium import webdriver
from web.web_po.web_po_v2.TestDatas import Global_Datas as GD
from web.web_po.web_po_v2.TestCases.test_login import TestLogin


class TestInvest(unittest.TestCase):
    def setUp(self):
        # 启动driver，打开浏览器，访问网页
        # 登录（满足前置1，前置2和前置3可以暂时手动满足）
        self.driver = webdriver.Chrome()
        self.driver.get(GD.login_url)
        pass

    def tearDown(self):
        # 关闭浏览器
        self.driver.quit()

    def test_invest_success(self):
        '''
        步骤：
        1.首页-选择投资的标；
        2.1.标页面-获取投资之前的余额；
        2.2.标页面-获取投资之前标的余额；
        3.标页面-投资操作（如投资300）；
        4.标页面-投资成功弹出框-点击“查看并激活”（存在该按钮即可代表进入投资成功流程）
        断言：
        1.用户的余额是否少了300块？（为了避免共用账号的影响，应该保持自动化账号独立---很容易）
         投资之前的余额-投资之后的余额=投资300
         1.1投资之后会进入个人页面，查看投资之后的余额
        2.标的余额是否少了？ （为了避免别人投资同一个标的影响，只能尽量保证环境独立---很难，如果不行就晚上再跑）
         2.1投资之后会进入个人页面，点击投资记录第一条中的标名，进入标页面
         2.2标页面-查看投资之后的标的余额
        '''
        pass

