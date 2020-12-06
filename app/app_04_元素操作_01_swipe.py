#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
app_第2周—第2課-1
'''

from appium import webdriver
from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# 要在哪个平台对哪个设备哪个app进行操作？
caps = {
    "automationName": "UiAutomator2",
    # Appium也可以，不过获取toast存在一些问题（以往经验）；官方建议Android6.0以上使用UiAutomator2。默认是Appium（老师没有写这个）
    "platformName": "Android",
    "platformVersion": "10",  # 如果不知道也可以先随便写一个，报错时，appium日志会提示可用的
    "deviceName": "GEY6R20507024610",  # 根据官方文档，这个字段填写错误也没有关系，必须有，但是没有使用---未验证
    "appPackage": "com.dangdang.reader",
    "appActivity": ".activity.GuideActivity",
    "noReset": True
}

# 与appium服务器建立连接，并向appium传入启动参数
driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)


# ==========滑动实例==========
# 先等待页面元素出现再滑屏
# loc = (By.ID, "resource-id")
loc = (MobileBy.ID, "resource-id")  # 这里用By或者MobileBy都没有区别
WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc))
sleep(1)

# 获取屏幕大小
size = driver.get_window_size()
# 从右向左滑动
start_x = size["width"]*0.9
start_y = size["height"]*0.5
end_x = size["width"]*0.1
end_y = size["height"]*0.5
duration = 500
driver.swipe(start_x, start_y, end_x, end_y, duration)

# 注意：如果是连续滑动，需要加sleep，因为手机反应会有点慢
# 如果需要封装连续滑动，可以用for循环


