#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
from interface.interface_demo.common.http_request2 import HTTPRequest
from interface.interface_demo.common.do_excel import DoExcel
from ddt import ddt, data
from interface.interface_demo.common import contants
from interface.interface_demo.common.context import Context
from interface.interface_demo.common.logger import log


# 注意：直接在这里右键执行时，定位class执行，而非定位用例执行。否则会报错。
# 如果要执行testCases中的所有用例，可以在testCases文件夹右键执行
@ddt
class TestLogin(unittest.TestCase):
    excel = DoExcel(contants.cases_file, "login")
    cases = excel.get_cases()
    http_request = HTTPRequest()  # 实例化一次可以执行多个接口

    def setUp(self):
        pass

    @data(*cases)  # 解包
    def test_login(self, case):
        # print("正在执行用例：{}".format(case["title"]))
        log.info("正在执行用例：{}".format(case["title"]))

        # 新增：正则替换实现参数化(excel中的数据，用配置文件中的数据替换)
        case['data'] = Context.replace(case['data'])

        data = eval(case["data"])  # 此处存放在excel的data是字符串，需要转换成字典
        resp = self.http_request.request(method=case["method"], url=case["url"], data=data)
        try:
            # self.assertEqual(case["expected"], resp.get_text())
            self.assertEqual(str(case["expected"]), resp.json()["code"])
            self.excel.write_result(case["case_id"] + 1, resp.text, "PASS")
        except AssertionError as e:
            self.excel.write_result(case["case_id"] + 1, resp.text, "FAIL")
            print(e)
            raise e

    def tearDown(self):
        pass



