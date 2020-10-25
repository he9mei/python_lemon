#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
web-第4周-第1节课
深入分层应用
对应练习：web_po_v2这个包
优化1：
对于页面对象，将页面元素提取出来放到另外一个包下，还是以页面区分。
那页面对象类中就只放页面操作函数。然后导入页面元素的类就可以了。
分层：Pagelocators，与PageObjects结构是对应的。

补充小技巧：
# 问题：在页面对象类调用driver的方法时，因为driver是外部传入的，这里写代码时无法自动弹起driver相关方法
# 解决-小技巧：
# （1）导入from selenium.webdriver.remote.webdriver import WebDriver
# （2）    def __init__(self, driver: WebDriver):
#         self.driver = driver

优化2：
测试数据单独管理：
1、数据共用、模块级共用、全局级共用。
2、测试环境、预发布环境、生产环境。---不同环境的数据应该分开管理。
基于以上原因，结论：所有数据全部拿出来统一管理。
分层：TestDatas，与TestCases模块结构是对应的。可以区分为模块数据和全局数据。

目前优化后有四层：PageLocators, PageObjects, TestCases, TestDatas
'''

'''
web-第4周-第2节课
复杂用例的设计和实现
以投资用例来讲解，对应：invest.py文件以及test_invest.py
关于自动化测试用例原则，在invest.py中
自己总结-这节课的学习收获：写用例之前先分析，先把手工用例写出来（用例名称、前置、步骤、断言），筛选可以自动化的用例，然后再写。
在写的过程中，先把架子搭起来，然后再具体化。
搭架子步骤：
（1）testCases-class/setUP/tearDown/用例（细节先用pass代替） 
（2）理清用例的步骤和断言，明了需要哪些页面-哪些操作
（3）pageObects-补充页面需要的操作（细节先用pass代替） 
（4）PageLocatir-补充页面需要的元素
（5）补充细节，调试用例
'''
'''
web-第4周-第3节课

'''