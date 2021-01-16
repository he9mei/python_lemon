#!/usr/bin/python3
# -*- coding: utf-8 -*-

from appium import webdriver
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy

# 要在哪个平台对哪个设备哪个app进行操作？
caps = {
    "automationName": "UiAutomator2",
    # Appium也可以，不过获取toast存在一些问题（以往经验）；官方建议Android6.0以上使用UiAutomator2。默认是Appium（老师没有写这个）
    "platformName": "Android",
    "platformVersion": "7.1.1",  # 如果不知道也可以先随便写一个，报错时，appium日志会提示可用的
    "deviceName": "MJA68TGES4S4SKAY",  # 根据官方文档，这个字段填写错误也没有关系，必须有，但是没有使用---未验证
    "appPackage": "com.dangdang.reader",
    "appActivity": ".activity.GuideActivity",
    "noReset": True
}

# 与appium服务器建立连接，并向appium传入启动参数
driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

driver.implicitly_wait(10)

# 常用元素定位
# driver.find_element_by_id()
# driver.find_element_by_class_name()
# driver.find_element_by_accessibility_id()
# driver.find_element_by_android_uiautomator()
# driver.find_element_by_xpath()
# uiautomator用法
# locator_fuli = 'new UiSelector().text("福利")'     # 注意：单引号里面是java代码，在java中字符串必须使用双引号
# locator_fuli = 'new UiSelector().text("福利").resourceId("resource-id")'  # 方法返回的的都是UiSelector，可以直接组合定位
# driver.find_element_by_android_uiautomator(locator_fuli)

# 书架
'''
driver.find_element_by_id("com.dangdang.reader:id/new_shelf_iv").click()
sleep(2)
driver.find_element_by_id("com.dangdang.reader:id/self_my_bought_btn").click()  # 原生的，能找到
# driver.find_element_by_id("com.dangdang.reader:id/search").click()
sleep(2)
driver.press_keycode(4)
sleep(2)
'''

# 个人中心---可以先通过text进入到内部页面即原生页面，再操作。可以实现部分自动化
# driver.find_element_by_id("com.dangdang.reader:id/tab_personal_iv").click()
driver.find_element_by_xpath("//*[contains(@text,'我的')]").click()
sleep(2)
# driver.find_element_by_xpath("//*[contains(@text,'任务')]").click()  # flutter,用text能找到
# driver.find_element_by_xpath("//*[contains(@text,'资产')]").click()
driver.find_element_by_xpath("//*[contains(@text,'何九妹')]").click()
loc_reading = (MobileBy.ID,'com.dangdang.reader:id/book_iv')
WebDriverWait(driver,10).until(EC.visibility_of_element_located(loc_reading))
driver.find_element(*loc_reading).click()
driver.press_keycode(4)

sleep(5)
driver.quit()


# 前提条件：
# 1.appium server已启动
# 2.模拟器、真机已连接,adb devices能识别到

# 老师演示，投屏工具：ApowerMirror
# 注意通过WiFi投屏，以免影响自动化
