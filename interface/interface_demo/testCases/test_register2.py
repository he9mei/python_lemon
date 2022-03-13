#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
from interface.interface_demo.common.http_request import HTTPRequest
from interface.interface_demo.common.do_excel import DoExcel
from ddt import ddt, data
from interface.interface_demo.common import contants, mysql_handler


@ddt
class TestRegister(unittest.TestCase):
    excel = DoExcel(contants.cases_file, "register")
    cases = excel.get_cases()

    @classmethod
    def setUpClass(cls):
        cls.mysql = mysql_handler.MysqlHandler()  # 一个类实例化一次，即建立一次连接。测试用例中可以多次查询。

    @data(*cases)  # 解包
    def test_register(self, case):
        print("正在执行用例：{}".format(case["title"]))
        data = eval(case["data"])  # 此处存放在excel的data是字符串，需要转换成字典

        # 这里的改造是：将Excel中的注册手机号参数化，在excel中用register_phone占位
        # 参数化的方式是在数据库找到185最大手机号，然后+1，也就是得到未注册的手机号
        # 然后找到excel中的register_phone，替换为未注册的手机号
        if case['data'].find("register_phone") > -1:  # 找不到返回-1
            # max_phone="18518500001"
            sql = "select max(mobilephone) as maxphone from future.member where mobilephone like '185%'"
            result = self.mysql.query_one(sql)
            max_phone = int(result['maxphone'])+1000
            data = case["data"].replace("register_phone", max_phone)   # 找到后替换
            data = eval(data)

        request = HTTPRequest(method=case["method"], url=case["url"], data=data)
        actual = request.get_text()
        try:
            self.assertEqual(case["expected"], actual)
            self.excel.write_result(case["case_id"] + 1, actual, "PASS")
        except AssertionError as e:
            self.excel.write_result(case["case_id"] + 1, actual, "FAIL")
            print(e)
            raise

        # 需要增加数据库校验（自己实现）

    @classmethod
    def tearDownClass(cls):   # 一个类使用完成后一次关闭
        cls.mysql.close()



'''
直接在这里执行时，如果报错AttributeError: type object 'TestRegister' has no attribute 'test_register'
说明执行时应该定位到class而不是方法
'''