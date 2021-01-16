#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
二、实际操作
APP框架
1.common层basepage新增APP特有的方法封装---具体封装见app_po_v1中common-basepage
2.pageObjects/PageLocators
 APP页面封装上与web区别：
    web端是严格的按照页面区分，但是app页面比较小，如果紧密联系的元素操作分散在不同的页面，可以写在同一个页面当中。
3.testCases
 APP会话启动上与web区别：
    web: webdriver.Chrome()
    app: desired_caps={}
         webdriver.Remote("http://localhost:4723/wd/hub",desired_caps)
         有很多参数需要配置
         按照我们web的框架逻辑，会话启动应该写在fixture中，但是配置经常改动，最好写在配置文件中
         待优化：
         启动参数写在配置文件中---yaml
         实现自动识别？自动识别系统版本？根据apk包识别包名和入口？

'''
