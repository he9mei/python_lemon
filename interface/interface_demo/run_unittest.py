#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
function: 统一的执行入口；收集用例、执行用例；生产报告
'''

import unittest
from interface.interface_demo.common import contants
import sys
import os

from interface.interface_demo.common.HTMLTestRunner import HTMLTestRunner
from interface.interface_demo.testCases.test_login2 import TestLogin

# root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# # print(sys.path)
# # sys.path.append(root)  # 把python_lemon的目录加到我们的Python编译环境下面
# # sys.path.append(root+'/interface')  # 把python_lemon/interface的目录加到我们的Python编译环境下面
# # print(sys.path)
# 在terminal路径interface_demo>执行python run_unittest.py----还是有问题,可能是因为我层数太多了（老师的可以了）

# 收集用例
suite = unittest.TestSuite()
# suite.addTest(TestLogin("test_login")) # 为什么找不到？
suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestLogin))
# discover收集
# suite = unittest.defaultTestLoader.discover(contants.testCases_dir, pattern="test_*py")

# 直接执行
# unittest.TextTestRunner().run(suite)
# 执行用例并生成报告
# （导入HTMLTestRunner.py这个文件，放在common中）
with open(contants.report_file, "wb+") as file:   # html二进制写入
    runner = HTMLTestRunner(stream=file,
                        title="我的测试报告",
                        description="运行环境：mac")
    runner.run(suite, rerun=1, save_last_run=True)
