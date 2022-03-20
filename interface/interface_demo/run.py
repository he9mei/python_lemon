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
from interface.interface_demo.testCases.test_login import TestLogin

root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print(sys.path)
sys.path.append(root)  # 把python_lemon的目录加到我们的Python编译环境下面
sys.path.append(root + '/interface')  # 把python_lemon/interface的目录加到我们的Python编译环境下面
print(sys.path)
# 在terminal路径interface_demo>执行python run.py----还是有问题,可能是因为我层数太多了（老师的可以了）

# 收集用例
discover = unittest.defaultTestLoader.discover(contants.testCases_dir, pattern="test_*py")

# 执行用例
unittest.TextTestRunner().run(discover)

# 执行用例并生成报告
# （导入HTMLTestRunnerNew这个文件，放在common中；这里需要导入这个文件）

# # 没有导入老师说的文件HTMLTestRunnerNew
# with open(contants.report_file, "wb+") as file:   # html二进制写入
#     runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file,
#                                      title="python-api-test",
#                                      description="前程贷",
#                                      tester='mongo')
#     runner.run(discover)


# 我自己导入了HTMLTestRunner.py
# runner = HTMLTestRunner(stream=contants.report_file,
#                         title="我的测试报告",
#                         description="运行环境：mac")
# runner.run(discover, rerun=1, save_last_run=True)
