#!/usr/bin/python3
# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By


class UserPageLocator:
    # 个人页面-查看账户余额
    loc_user_leftMoney = (By.XPATH, '')
    # 投资记录第一个标的标名
    loc_investRecord_bidName = (By.XPATH, '')
    # 投资记录TAB
    loc_investRecord_tab = (By.XPATH, '')