#!/usr/bin/python3
# -*- coding: utf-8 -*-

from appium import webdriver
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# 要在哪个平台对哪个设备哪个app进行操作？
caps = {
    "automationName": "UiAutomator2",
    # Appium也可以，不过获取toast存在一些问题（以往经验）；官方建议Android6.0以上使用UiAutomator2。默认是Appium（老师没有写这个）
    "platformName": "Android",
    "platformVersion": "7.1.1",  # 如果不知道也可以先随便写一个，报错时，appium日志会提示可用的
    "deviceName": "MJA68TGES4S4SKAY",  # 根据官方文档，这个字段填写错误也没有关系，必须有，但是没有使用---未验证
    "appPackage": "com.dangdang.buy2",
    "appActivity": ".StartupActivity",
    "noReset": True
}

# 与appium服务器建立连接，并向appium传入启动参数
driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
driver.implicitly_wait(10)

# 1.点击“我的”
driver.find_element_by_id("com.dangdang.buy2:id/tab_personal_iv").click()

# 2.点击“查看关注的宝贝”

# 获取屏幕大小
size = driver.get_window_size()
'''
# 这里滑动是为了解决，到新页面后找到元素不点击的情况
# 从上向下滑动
start_x = size["width"]*0.5
start_y = size["height"]*0.5
end_x = size["width"]*0.5
end_y = size["height"]*0.8
duration = 500
driver.swipe(start_x, start_y, end_x, end_y, duration)
'''
loc_favor = (By.ID, "com.dangdang.buy2:id/tv_agile_collect_more")
try:
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc_favor))
    print("找到元素了")
except:
    print("没有找到元素")

driver.find_element(*loc_favor).click()  # 非常奇怪---还是可能出现，找到元素点击卡死的情况。
sleep(2)


# =========重点--3.滑动列表=========
'''
page_src = driver.page_source  # 可以获得页面源码

swip来实现页面的滑动；
滑动的时候不能过度，要确保内容不会跳过；
如何确定，你找的元素，就在当前页面中？

while 没有滑到底部之前：---条件则为滑动前的页面和滑动后的页面不一致
    滑动一次，---会导致页面更新
    找一次
    当元素可见时，停止循环：break
'''
# 列表中的书籍元素ID是一样的，这里是等待所有书籍元素出现
loc_book_all = (By.ID, "com.dangdang.buy2:id/tv_product_name")
WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located(loc_book_all))

loc_book = (By.XPATH, "//*[contains(@text,'摆脱无力感，拿回你的人生主动权')]")

old = ""
new = driver.page_source

while old != new:
    # print("---没有滑到底部---")
    # 1.如果查找的是文本，还有一种方法
    # if new.find("摆脱无力感，拿回你的人生主动权") != -1:
    #     print("找到文本了")
    #     driver.find_element(*loc_book).click()
    #     break

    # 2.如果查找的是元素
    # ---这里的元素等待也可以写在前面，进页面的时候等待所有书籍元素出现，这样的话这里也可以不写等待
    # ---driver.find_element()配合try...except即可
    # （1）写等待
    # try:
    #     WebDriverWait(driver, 5).until(EC.visibility_of_element_located(loc_book))
    #     print("找到元素了")
    #     driver.find_element(*loc_book).click()
    #     break
    # except:
    #     print("没有找到元素")
    #（2）不写等待
    try:
        driver.find_element(*loc_book).click()
        print("找到元素了")
        # break  # 这里break也可以写在else中（也可以不写else）
    except:
        pass
    else:
        break

    # 从下向上滑动
    start_x = size["width"] * 0.5
    start_y = size["height"] * 0.5
    end_x = size["width"] * 0.5
    end_y = size["height"] * 0.2
    duration = 500
    driver.swipe(start_x, start_y, end_x, end_y, duration)

    old = new
    new = driver.page_source


sleep(5)
driver.quit()

# 列表滑动---
# 以上实例用oppo a83可以执行通过（包括appium和uiautomator2）
# （但是用华为play手机，uiautomator2存在找到元素不点击的情况）
