#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
from interface.interface_demo.common.http_request2 import HTTPRequest
from interface.interface_demo.common.do_excel import DoExcel
from ddt import ddt, data
from interface.interface_demo.common import contants, mysql_handler
from interface.interface_demo.common.context import Context

# 注意：直接在这里右键执行时，定位class执行，而非定位用例执行。否则会报错。
# 如果要执行testCases中的所有用例，可以在testCases文件夹右键执行
@ddt
class TestInvest(unittest.TestCase):
    excel = DoExcel(contants.cases_file, "invest")
    cases = excel.get_cases()
    http_request = HTTPRequest()

    @classmethod
    def setUpClass(cls):
        cls.mysql = mysql_handler.MysqlHandler()

    @data(*cases)  # 解包
    def test_invest(self, case):

        # 新增：正则替换实现参数化(excel中的数据，用配置文件中的数据替换)
        case['data'] = Context.replace(case['data'])

        print("正在执行用例：{}".format(case["title"]))
        data = eval(case["data"])  # 此处存放在excel的data是字符串，需要转换成字典
        resp = self.http_request.request(method=case["method"], url=case["url"], data=data)
        try:
            self.assertEqual(str(case["expected"]), resp.json()["code"])  # excel中的数字是int,需要转成str
            self.excel.write_result(case["case_id"] + 1, resp.text, "PASS")

            # 如果加标成功，就去数据库根据menberid查询id，赋值给loan_id，并设置为context类属性值
            if resp.json('msg') == "加标成功":
                sql = 'select * from future.loan where MenberID={} order by CreatedTime desc limit 1'.format(data['memberId'])
                load_id = self.mysql.query_one(sql)['Id']
                setattr(Context, 'loan_id', str(load_id))  # 得到load_id 放到上下文中；然后在上下文中使用时再获取
                # 这里传入正则匹配的Excel的参数的值需要是str

        except AssertionError as e:
            self.excel.write_result(case["case_id"] + 1, resp.text, "FAIL")
            print(e)
            raise e

    @classmethod
    def tearDownClass(cls):
        cls.mysql.close()

'''
由于连接不上数据库
投资接口没有跑
学习目标是：
实现正则匹配和参数化，可以从配置文件拿参数值，也可以从数据库拿参数值（反射）
见Context类
'''