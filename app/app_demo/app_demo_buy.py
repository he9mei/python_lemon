#!/usr/bin/python3
# -*- coding: utf-8 -*-

from appium import webdriver
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# 要在哪个平台对哪个设备哪个app进行操作？
caps = {
    # "automationName": "UiAutomator2",
    # Appium也可以，不过获取toast存在一些问题（以往经验）；官方建议Android6.0以上使用UiAutomator2。默认是Appium（老师没有写这个）
    "platformName": "Android",
    "platformVersion": "10",  # 如果不知道也可以先随便写一个，报错时，appium日志会提示可用的
    "deviceName": "GEY6R20507024610",  # 根据官方文档，这个字段填写错误也没有关系，必须有，但是没有使用---未验证
    "appPackage": "com.dangdang.buy2",
    "appActivity": ".StartupActivity",
    "noReset": True
}

# 与appium服务器建立连接，并向appium传入启动参数
driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
driver.implicitly_wait(10)

# 1.点击“我的”
driver.find_element_by_id("com.dangdang.buy2:id/tab_personal_iv").click()
# 使用xpath写法---pass
# eles = driver.find_elements_by_xpath("//android.widget.TabWidget/android.widget.FrameLayout")
# eles[4].click()
# 2.点击“查看关注的宝贝”
# driver.find_element_by_id("com.dangdang.buy2:id/tv_agile_collect_more").click()
# driver.find_element_by_xpath("//*[contains(@text,'查看关注的宝贝')]").click()  # 还有点问题？
# 尝试点击订单
# driver.find_element_by_xpath("//*[contains(@text,'全部订单')]").click()
# driver.find_element_by_id("com.dangdang.buy2:id/tv_agile_order_title").click()

loc_order = (By.ID, "com.dangdang.buy2:id/tv_agile_order_title")
loc_favor = (By.ID, "com.dangdang.buy2:id/tv_agile_collect_more")

# 获取屏幕大小
size = driver.get_window_size()
# 从上向下滑动
start_x = size["width"]*0.5
start_y = size["height"]*0.2
end_x = size["width"]*0.21
end_y = size["height"]*0.5
duration = 500
driver.swipe(start_x, start_y, end_x, end_y, duration)
sleep(3)

try:
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc_favor))
    print("找到元素了")
except:
    print("没有找到元素")
# 找到元素了，但是不点击，一直卡住？原因未知---尝试：加个滑动触碰一下
# 先找到在滑动，容易点错。改成先滑动，再找元素，再点击。===可以了

driver.find_element(*loc_favor).click()


sleep(5)
driver.quit()
