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

===步骤===
1、先识别webview---APP元素定位时，发现页面是整个大红框，class是android.webkit.webview
2、要切换到webview所在的html当中，去操作元素。
---app自动化---
（1）得到所有的contexts列表 cons=driver.contexts   ---类似于driver.window_handles
（2）切换到webview对应的contexts driver.switch_to.context(context名字)
---web自动化---
（3）切换成功之后，就是在html页面当中。
（4）查找元素---在整个html页面当中，定位元素---借助工具得到html并定位
（5）安卓系统的webview版本（即chromedriver对应的chrome版本）---下载chromedriver

===定位web元素===
方式1：driver.page_source,写入文件用html打开。然后获取元素。
方式2：工具uc-devtools
下载：百度uc devtools---uc开发者调试工具
https://dev.ucweb.com/docs/pwa/docs-zh/xy3whu
下载安装后打开，设置-选中：本地 Inspector UI 资源
首页可以看到手机打开的webview；并且可以看到webview的名字，以及设备chrome的版本号，即可下载与之对应的chromedriver
前提是连接手机或模拟器
方式3:找到webview的url直接浏览器访问，然后进入调试模式。
方式4：谷歌自带的定位chrome://inspect。存在问题：如果不翻墙什么都看不到。

===下载chromedriver===
在uc devtools中咱们能够找到chrome版本，然后下载相应的chromedriver
应该将chromedriver放在哪里呢？
方式1：在appium server的配置界面当中，可以指定chromedriver的执行路径
appium---advanced---android---Chromedriver Binary Path
填写chromedriver的位置，具体到path/chromedriver.exe
方式2：在appium启动参数当中，可以指定chromedriver的执行路径===推荐，不同手机可以设置不同的路径
在appium官网-documents-caps中可以找到chromediverExcutable参数可以用例设置chromediver的路径，具体到chromedriver.exe。
如：caps["chromediverExcutable"] = "D:\\chromedriver\\chorme39-42\\chromedriver.exe"

===在html页面操作结束之后，要回到原生页面===即从html中跳出来，不一定在确定的哪个页面===
driver.switch_to.context("NATIVE_APP")


===注意===（PPT详见）
如果2.1得到contexts时，无法获取到webview，可能是app没有打开开关。---需要开发打包时打开
setWebContentDebuggingEnabled(true)
还有破解方式，见歪歪老师的博客。

===关于By和MobileBy===
可以用By,也可以用MobileBy，因为MobileBy继承了By所有的方式。如果是MobileBy特有的定位方式，则只能用MobileBy。
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
print("进入h5之后的cons:", cons)     # 打印结果：[NATIVE_APP,WEBVIEW_com.lemon.lemonban]

# 切换到webview
driver.switch_to.context(cons[-1])
# driver.switch_to.context("WEBVIEW_com.lemon.lemonban")

# 定位web元素,并操作（定位方式见以上笔记）
loc = (MobileBy.XPATH, "")
WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located(loc))
driver.find_element(*loc).click()
