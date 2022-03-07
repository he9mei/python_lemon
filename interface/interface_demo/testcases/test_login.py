#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
from interface.interface_demo.common.http_request import HTTPRequest
from interface.interface_demo.common.do_excel import DoExcel
from ddt import ddt, data


@ddt
class TestLogin(unittest.TestCase):
    excel = DoExcel("./datas/cases.xlsx", "login")  # 此处路径需要绝对和相对结合，涉及到os模块
    cases = excel.get_cases()

    @data(*cases)  # 解包
    def test_login(self, case):
        data = eval(case["data"])  # 此处存放在excel的data是字符串，需要转换成字典
        request = HTTPRequest(method=case["method"], url=case["url"], data=data)
        actual = request.get_text()
        try:
            self.assertEqual(case["expected"], actual)
            self.excel.write_result(case["case_id"] + 1, actual, "PASS")
        except AssertionError:
            self.excel.write_result(case["case_id"] + 1, actual, "FAIL")


