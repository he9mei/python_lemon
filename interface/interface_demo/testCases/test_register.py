#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
from interface.interface_demo.common.http_request import HTTPRequest
from interface.interface_demo.common.do_excel import DoExcel
from ddt import ddt, data
from interface.interface_demo.common import contants


@ddt
class TestRegister(unittest.TestCase):
    excel = DoExcel(contants.cases_file, "register")
    cases = excel.get_cases()

    @data(*cases)  # 解包
    def test_register(self, case):
        print("正在执行用例：{}".format(case["title"]))
        data = eval(case["data"])  # 此处存放在excel的data是字符串，需要转换成字典
        request = HTTPRequest(method=case["method"], url=case["url"], data=data)
        actual = request.get_text()
        try:
            self.assertEqual(case["expected"], actual)
            self.excel.write_result(case["case_id"] + 1, actual, "PASS")
        except AssertionError as e:
            self.excel.write_result(case["case_id"] + 1, actual, "FAIL")
            print(e)
            raise


