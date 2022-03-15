#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
from interface.interface_demo.common.http_request import HTTPRequest
from interface.interface_demo.common.do_excel import DoExcel
from ddt import ddt, data
from interface.interface_demo.common import contants
from interface.interface_demo.common.context import Context


# 注意：直接在这里右键执行时，定位class执行，而非定位用例执行。否则会报错。
# 如果要执行testCases中的所有用例，可以在testCases文件夹右键执行
@ddt
class TestLogin(unittest.TestCase):
    # excel = DoExcel("./data/cases.xlsx", "login")  # 此处路径需要绝对和相对结合，涉及到os模块
    excel = DoExcel(contants.cases_file, "login")
    cases = excel.get_cases()

    def setUp(self):
        pass

    @data(*cases)  # 解包
    def test_login(self, case):
        print("正在执行用例：{}".format(case["title"]))

        # 新增：正则替换实现参数化(excel中的数据，用配置文件中的数据替换)
        case['data'] = Context.replace(case['data'])

        data = eval(case["data"])  # 此处存放在excel的data是字符串，需要转换成字典
        request = HTTPRequest(method=case["method"], url=case["url"], data=data)
        actual = request.get_text()
        try:
            self.assertEqual(case["expected"], actual)
            self.excel.write_result(case["case_id"] + 1, actual, "PASS")
        except AssertionError as e:
            self.excel.write_result(case["case_id"] + 1, actual, "FAIL")
            print(e)
            raise e

    def tearDown(self):
        pass



