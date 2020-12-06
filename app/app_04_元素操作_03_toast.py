#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
app_第2周—第2課-2
关于toast元素定位，因为很快会消失，稳定性可能不太高
（1）我们可以使用xpath来定位文本text
（2）还可以截图，然后进行图片比对
（关于图片比对，可以使用sikuli，还有airtest就是以图形比对为主的）

获取toast对appium、Java的安装版本，以及手机系统版本都有要求，而且启动时
automationName='UiAutomator2'
(这里填写Appium是实现不了toast获取的)

from ppt
toast注意事项
1.配置toast请注意：
1).desired_caps["automationName"]="UiAutomator2"
2).要求安装jdk1.8 64位及以上，配置其环境变量JAVA_HOME和path
3).Android系统5.0以上
4).appium server版本1.6.3以上

2.xpath表达式：
xpath = '//*[@text="文本内容"]'
xpath = '//*[contains(@text,"部分文本内容")]'
注意：
WebDriverWait方法中，请用presence_of_element_located(loc) 存在
不要用visibility_of_element_located(loc) 可见，它对toast的可见处理并不支持，会直接报错。

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

# ===获取toast操作===
# 用xpath定位toast文本
loc_toast = (MobileBy.XPATH, '//*[contains(@text, "手机号或密码不能为空")]')
# 等待toast存在
try:
    WebDriverWait(driver,10,0.1).until(EC.presence_of_element_located(loc_toast))
    text_toast = driver.find_element(*loc_toast).text
    print("找到toast,它的文本是:{}".format(text_toast))
except:
    print("没有找到toast!")



