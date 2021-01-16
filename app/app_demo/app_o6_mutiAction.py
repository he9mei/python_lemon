#!/usr/bin/python3
# -*- coding: utf-8 -*-
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy
import time

from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
# from selenium import webdriver

# 你要在哪个系统上对哪个app进行操作！！
desired_caps = {}
desired_caps["platformName"] = "Android"
desired_caps["platformVersion"] = "5.1.1"
desired_caps["deviceName"] = "emulator-5554"
desired_caps["appPackage"] = "com.baidu.BaiduMap"
desired_caps["appActivity"] = "com.baidu.baidumaps.WelcomeScreen"
desired_caps["noReset"] = True
desired_caps["unicodeKeyboard"] = True  # 中文输入

# 与appium服务进行连接，并告诉appium我要干嘛。
driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
time.sleep(40)

# 获取屏幕大小
size = driver.get_window_size()
# 实例化
ma = MultiAction(driver)

# 放大操作
# 有2个动作链：先按住 - 再移动  -  再释放
ta1 = TouchAction(driver)
ta2 = TouchAction(driver)
ta1.press(x=size["width"]*0.5,y=size["height"]*0.5).wait(200).move_to(x=size["width"]*0.2,y=size["height"]*0.2).wait(200).release()
ta2.press(x=size["width"]*0.55,y=size["height"]*0.55).wait(200).move_to(x=size["width"]*0.88,y=size["height"]*0.88).wait(200).release()

# 加到ma当中
ma.add(ta1,ta2)
# 执行
ma.perform()

'''
# 以下是中文输入实例
loc = (MobileBy.ID,"com.baidu.BaiduMap:id/tv_searchbox_home_text")
WebDriverWait(driver,20).until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()

loc = (MobileBy.ID,"com.baidu.BaiduMap:id/tvSearchBoxInput")
WebDriverWait(driver,20).until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).send_keys("麓谷企业广场")

time.sleep(2)
# 按钮操作 - 回到主界面
driver.press_keycode(3)
'''