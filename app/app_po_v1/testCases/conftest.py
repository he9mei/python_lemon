#!/usr/bin/python3
# -*- coding: utf-8 -*-
import pytest
from appium import webdriver
import yaml
from time import sleep
from app.app_po_v1.common import dir_config


@pytest.fixture(scope="session")
# def start_app():
def driver():
    # desired_caps = {}    # 启动参数用yaml配置替代
    # desired_caps["automationName"] = "uiAutomator2"
    # desired_caps["platformName"] = "Android"
    # desired_caps["platformVersion"] = "7.1.1"
    # desired_caps["deviceName"] = "MJA68TGES4S4SKAY"
    # desired_caps["appPackage"] = "com.dangdang.reader"
    # desired_caps["appActivity"] = ".activity.GuideActivity"
    # desired_caps["noReset"] = True

    # 打开yaml文件
    # fs = open("desired_caps.yaml")  # 放在相同路径下（都放在testcases下）---pass
    # caps_dir = "../caps"   # 这里路径先写在这里尝试是否读取成功(之后会写在common中dir_config中)---pass
    caps_dir = dir_config.caps_dir   # 路径写在common中dir_config中
    print(caps_dir)  # C:\Users\lipan\PycharmProjects\python_lemon\app\app_po_v1\caps
    fs = open(caps_dir+"/"+"desired_caps.yaml")
    # 加载成python对象
    desired_caps = yaml.load(fs, yaml.FullLoader)
    fs.close()

    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
    driver.implicitly_wait(10)
    yield driver
    sleep(5)
    driver.quit()


# 如果特殊用例需要不同的caps配置,可以用以下方法；无特殊要求用以上即可。
# def basedriver(noRest=True, **kwargs):
#     fs = open(dir_config.caps_dir + "/" + "desired_caps.yaml")
#     desired_caps = yaml.load(fs, yaml.FullLoader)
#     fs.close()
#
#     if noRest == False:
#         desired_caps["noRest"] == False
#     if kwargs:
#         for key,value in kwargs.items():
#             desired_caps[key] == value
#
#     driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
#     return driver


# 是否已登录判断
# 可以用文本判断，文本是“未登录用户”则未登录，进行登录操作，否则已登录，pass
def is_logined():
    pass
