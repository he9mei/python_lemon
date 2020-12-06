#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
app_第2周—第2課-2
from PPT
appium-模拟触屏
TouchAction类
将一系列动作放在一个链条中，然后将该链条传递给服务器。
服务器接收到该链条后，解析各个动作，逐个执行。
短按-press，与release组合使用
长按-longPress，默认1000ms，与release组合使用
点击-tap
移动到-move_to
等待-wait
释放-release
执行-perform
取消-cancel

需要引入from appium.webdriver.common.touch_action import TouchAction
'''
from appium import webdriver
from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from appium.webdriver.common.touch_action import TouchAction

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


# ===模拟触屏实例===
# (1)查看TouchAction的源码，进一步理解相关操作
# (2)swipe实际就是用TouchAction来实现封装的
# 查看driver.swipe()的源码
def swipe(self, start_x, start_y, end_x, end_y, duration=None):
    action = TouchAction(self)
    action \
        .press(x=start_x, y=start_y) \
        .wait(ms=duration) \
        .move_to(x=end_x, y=end_y) \
        .release()
    action.perform()
    return self
# (3)使用TouchAciton解锁九宫格手势密码---还没讲

# app_第2周—第2課-2 01小时15分钟