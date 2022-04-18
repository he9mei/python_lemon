#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Name: main
# Author: liyuan
# Time: 16:58

import unittest
import os

# 1、TestSuite实例化
s = unittest.TestSuite()  # 1  套件实例化
t = unittest.TestLoader()   # 2 收集器实例化，收集用例的方式： discover方式
# 3  将收集到的用例，放到测试套件当中。
s.addTests(t.discover(os.path.join(os.getcwd(),"test_cases")))

# 高级版本：5、生成html测试报告  HtmlTestRunner()
from HTMLTestRunnerNew import HTMLTestRunner
# 打开一个html文件
fs = open("report.html","wb")
# 实例化html结果的用例运行器
runner = HTMLTestRunner(fs,title="unittest框架学习",description="体验html报告",tester="小简")
# 运行测试套件
runner.run(s)