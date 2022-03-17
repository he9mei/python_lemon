#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
function: 统一的执行入口；收集用例、执行用例；生产报告
'''

import unittest
from interface.interface_demo.common import contants

# 收集用例
discover = unittest.defaultTestLoader.discover(contants.testCases_dir, pattern="test_*py")
# 执行用例并生成报告
# （导入HTMLTestRunnerNew这个文件，放在common中；这里需要导入这个文件）
'''
# 暂时未导入文件
with open(contants.report_file, "wb+") as file:   # html二进制写入
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                     title="python-api-test",
                                     description="前程贷",
                                     tester='mongo')
    runner.run(discover)
    
'''