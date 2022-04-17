#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Name: main
# Author: 简
# Time: 2019/5/19

# TestSuite
import unittest

# 引入2个测试类
# from class_20190518.test_first import MyTestClass
# from class_20190518.test_two import TestCaculator

# 2、TestSuite实例化
# s = unittest.TestSuite()

# 3、加载用例
# 加载一个用例  s.addTest(测试类名("测试用例名称"))
# s.addTest(MyTestClass("test_who_bigger"))
# 加载多个用例   s.addTests([,])
# s.addTests([MyTestClass("test_who_bigger"),MyTestClass("test_upper_is_true")])

# TestLoader来完成加载用例
# 1、实例化TestLoader类
# t = unittest.TestLoader()
# t.loadTestsFromModule(test_first)
# t.loadTestsFromModule(test_two)

# 高级用法  # 指定一个目录 ，从目录 下去找用例测试，所有的测试用例都加载进来。
# t.discover(r"D:\Pychram-Workspace\python17\class_20190518\allTestCases")

# 1、TestSuite实例化
s = unittest.TestSuite()  # 1  套件实例化
t = unittest.TestLoader()   # 2 收集器实例化，收集用例的方式： discover方式
# 3  将收集到的用例，放到测试套件当中。
s.addTests(t.discover(r"C:\Users\lipan\PycharmProjects\python_lemon\basic\basic6_3unittest+ddt\allTestCases"))

# 高级版本：5、生成html测试报告  HtmlTestRunner()
# 将HTMLTestRunnerNew.py文件放到安装目录D:\Program Files\Python38\Lib下
from HTMLTestRunnerNew import HTMLTestRunner
# 打开一个html文件
fs = open("report.html","wb")
# 实例化html结果的用例运行器
runner = HTMLTestRunner(fs,title="unittest框架学习",description="体验html报告",tester="小简")
# 运行测试套件
runner.run(s)


# 备注：
# 加载用例的方式，最常用的就是discover其他的都不常用。
# 第4步被第5步高级版本替换

# 4  运行套件
# 4、1 实例化运行器
# runner = unittest.TextTestRunner()
# # 4.2  调用run方法，运行用例。
# runner.run(s)  # 参数为套件