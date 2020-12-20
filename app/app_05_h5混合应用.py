#!/usr/bin/python3
# -*- coding: utf-8 -*-
from appium import webdriver
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy

'''
app_第2周—第3課-01小时12分钟
h5混合应用---进行中
==============笔记=================
不是混合应用 原生控件 NATIVE_APP
有了混合应用 包含 NATIVE_APP 和 webview_com.lemon.lemonban # 增加html窗口
用context来表示，类似于窗口
切换的前提是得到当前所有的context(NATIVE_APP,webview)

步骤
1、先识别webview---APP元素定位时，发现页面是整个大红框，class是android.webkit.webview
2、要切换到webview所在的html当中，去操作元素。
---app自动化
（1）得到所有的contexts列表 cons=driver.contexts   ---类似于driver.window_handles
（2）切换到webview对应的contexts driver.switch_to.context(context名字)
---web自动化
（3）切换成功之后，就是在html页面当中。
（4）查找元素---在整个html页面当中，定位元素---借助工具得到html并定位
（5）安卓系统的webview版本（即chromedriver对应的chrome版本）---下载chromedriver
3、


注意：（PPT详见）
如果2.1得到contexts时，无法获取到webview，可能是app没有打开开关。---需要开发打包时打开
setWebContentDebuggingEnabled(true)
还有破解方式，见歪歪老师的博客。
'''

# ===============实例============
# 前面是进入h5页面之前的操作
caps = {
    "automationName": "UiAutomator2",
    "platformName": "Android",
    "platformVersion": "10",
    "deviceName": "GEY6R20507024610",
    "appPackage": "com.dangdang.buy2",
    "appActivity": ".StartupActivity",
    "noReset": True
}
driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
driver.implicitly_wait(10)

# 获取当前所有的contexts
cons = driver.contexts
print("进入h5之前的cons:", cons)

# 进入h5页面
loc = (MobileBy.ID, "")
WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located(loc))
driver.find_element(*loc).click()

# 等待webview元素可见
loc = (MobileBy.CLASS_NAME, "android.webkit.webview")
WebDriverWait(driver,10).until(EC.visibility_of_all_elements_located(loc))
sleep(1)

# 获取当前所有的contexts
cons = driver.contexts
print("进入h5之后的cons:", cons)
