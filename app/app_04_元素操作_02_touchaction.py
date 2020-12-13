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
    action = TouchAction(driver)
    action \
        .press(x=start_x, y=start_y) \
        .wait(ms=duration) \
        .move_to(x=end_x, y=end_y) \
        .release()
    action.perform()
    return self

# (3)使用TouchAciton解锁九宫格手势密码
'''
一个点移动到另外一个点
如果每个点是单个元素，则传入元素
如果整个块是一个元素，只能使用坐标。终点左边减去起点坐标，得到元素的高和宽，再计算位置的坐标。
***
  *
'''
ele = driver.find_element(MobileBy.ID, "id")   # 整个九宫格元素
ele_loc = ele.location  # 元素的起点坐标（x,y）
ele_size = ele.size  # 元素的大小（高、宽）
start_x = ele_loc["x"]
start_y = ele_loc["y"]
step = ele_size["height"]/6  # 元素的高、宽均分为6份（其他地方的九宫格不一定是这样，老师举例的是这样）

# 计算每个点的坐标
p1 = (start_x+step, start_y+step)
p2 = (p1[0]+2*step, p1[1])
p3 = (p2[0]+2*step, p2[1])
p4 = (p3[0], p3[1]+2*step)

# 执行操作
action = TouchAction(driver)
action\
    .press(x=p1[0], y=p1[1]).wait(200)\
    .move_to(x=p2[0], y=p2[1]).wait(200)\
    .move_to(x=p3[0], y=p3[1]).wait(200)\
    .move_to(x=p4[0], y=p4[1]).wait(200)\
    .release()
action.perform()

'''
其他操作，比较简单就不讲了---见ppt截图
Android KEYCODE键值
可参考：https://blog.csdn.net/crisschan/article/details/50419963

'''