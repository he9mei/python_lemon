#!/usr/bin/python3
# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By


class IndexPageLocator:
    # 我的账户
    loc_my_account = (By.XPATH, "//a[contains(text(),'我的帐户')]")
    # 首页按钮
    loc_home = (By.XPATH, "//a[text()='首页']")
    # 抢投标按钮
    loc_invest_enter_btn = (By.XPATH, '')
