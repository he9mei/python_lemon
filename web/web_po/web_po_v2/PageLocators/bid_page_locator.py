#!/usr/bin/python3
# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By


class BidPageLocator:
    # 从输入框查看-账户余额
    loc_inputBox_leftMoney = (By.XPATH, '')
    # 标的余额
    loc_bid_money = (By.XPATH, '')
    # 输入框
    loc_inputBox = (By.XPATH, '')
    # 投标按钮
    loc_invest_btn= (By.XPATH, '')
    # 投资成功弹框-查看并激活按钮
    loc_active_btn = (By.XPATH, '//div[@class="layui-layer-content"]/div/div/button[text()="查看并激活"]')