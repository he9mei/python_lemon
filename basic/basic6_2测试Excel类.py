#!/usr/bin/python3
# -*- coding: utf-8 -*-

# ---老师的作业---

# 对excel类进行单元 测试

# 1、我要设计什么样的测试用例？
  # 用例1  读取第3行数据。断言：数据不空。
  # 用例2  读取单元格(2,3)的数据。断言：(2,3)与长沙是否相等。
  # 用例3  写入单元格(6,8)的值：666  断言：是否写入成功。

import unittest

class TestExcel(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 准备工作
        pass

    def test_read_row_datas(self):
        pass

    def test_read_cell_data(self):
        pass


# 运行方式2：unittest.main()入口
if __name__ == '__main__':
    unittest.main()


# TestSuite、TestLoader、ddt