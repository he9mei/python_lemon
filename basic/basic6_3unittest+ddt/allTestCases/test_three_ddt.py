
'''
ddt的用法
'''
# ---老师的笔记---

import unittest
import ddt
# ddt应用在测试用例当中。
# 如果一个测试类要用ddt，那么要用ddt装饰这个测试类。
# 1、装饰测试类  在类名前面 @ddt.ddt
# 2、在测试函数前面 @ddt.data(多组数据),每组之间用逗号隔开
#    测试函数增加一个参数，用来接收前每一组数据。
#    单组数据可以是任意类型数据。


@ddt.ddt    # 备注：被ddt装饰的测试类中的测试用例，不能单独执行
class TestCaculator(unittest.TestCase):
     # 流程：第一步：两数求和，第二步：与期望值进行比对。
     # 数据 (100,200,300) (100,0.02,100.02) (0.01,0.02,0.03)

    # 第一种---了解即可
    @ddt.data((100,200,300),(100,0.02,100.02),(0.01,0.02,0.03))
    def test_add(self,data):  # data是元组，用来接收每一组数据。
        res = data[0] + data[1]  # 流程第1步 相加
        self.assertEqual(data[2],res)  # 流程第2步 比对

    # 第二种：重点掌握此种方式。最最常用的方式  解包---必须会用
    # 完整的数据是一个列表，列表里面再嵌套列表。
    a = [(100,200,300),(100,0.02,100.02),(0.01,0.02,0.03)]
    @ddt.data(*a)
    def test_add_v2(self,data):
        res = data[0] + data[1]  # 流程第1步 相加
        self.assertEqual(data[2], res)  # 流程第2步 比对

    # 如果a是字典，data是什么？？请自己写代码来验证结果。

    # 第三种  unpack  把每一组数据，拆成孤零零的个体。---了解即可
    # 每一组：(A,B,C) 如果不unpack，那就是一个整体。在测试函数中，只要1个参数来接收。
    # 如果unpack,那就是解散，变成3个独立的数据。在测试函数中，要准备3个参数来接收。
    @ddt.data(*a)
    @ddt.unpack
    def test_add_v3(self,num1,num2,expected):
        res = num1 + num2  # 流程第1步 相加
        self.assertEqual(expected, res)  # 流程第2步 比对

    def test_minus(self):
        res = 100 * 10
        self.assertEqual(res,1000)

     # def test_add_2(self):
    #     res = 100 + 0.02  # 1 相加
    #     self.assertEqual(100.02, res)  # 2 比对
    #
    # def test_add_3(self):
    #     res = 0.01 + 0.02  # 1 相加
    #     self.assertEqual(0.03, res)  # 2 比对





