#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
from interface.interface_demo.common.http_request import HTTPRequest
from interface.interface_demo.common.do_excel import DoExcel
from ddt import ddt, data
from interface.interface_demo.common import contants

cookies = None
# 注意：直接在这里右键执行时，定位class执行，而非定位用例执行。否则会报错。
# 如果要执行testCases中的所有用例，可以在testCases文件夹右键执行
@ddt
class TestRecharge(unittest.TestCase):
    # excel = DoExcel("./data/cases.xlsx", "login")  # 此处路径需要绝对和相对结合，涉及到os模块
    excel = DoExcel(contants.cases_file, "recharge")
    cases = excel.get_cases()

    @data(*cases)  # 解包
    def test_recharge(self, case):
        global cookies
        print("正在执行用例：{}".format(case["title"]))
        data = eval(case["data"])  # 此处存放在excel的data是字符串，需要转换成字典
        request = HTTPRequest(method=case["method"], url=case["url"], data=data, cookies=cookies)
        actual = request.get_json()["code"]  # str
        try:
            self.assertEqual(str(case["expected"]), actual)  # excel中的数字是int,需要转成str
            self.excel.write_result(case["case_id"] + 1, actual, "PASS")
            if request.get_cookies():   # 判断get_cookies()不为空，否则cookies会被空覆盖
                cookies = request.get_cookies()
        except AssertionError as e:
            self.excel.write_result(case["case_id"] + 1, actual, "FAIL")
            print(e)
            raise e



