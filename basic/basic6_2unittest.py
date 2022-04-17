#!/usr/bin/python3
# -*- coding: utf-8 -*-


'''
unittest-1
'''

# ---老师的笔记---

# 组件测试

# 测试工作  要去设计测试数据，执行测试用例，看结果。
# 用代码来写测试用例：用例的组织，
# 自动执行用例，自动比对结果，直接展示结果。  前置后置

# unittest  --- 单元测试框架
# 100条用例 5个测试文件当中

# TestCase  测试用例
# runner    运行用例
# result    用例结果
# fixture   前置后置

# TestSuite  测试套件 -- 测试用例集
# TestLoader  加载用例  把TestCase加载到TestSuite,加载方式。

# 测试数据：IDO
# 1、步骤：是否为大写。 期望结果：大写
# 2、步骤-条件：它是大写。  期望结果：真
# 3、步骤：100 < 244(测试数据)   期望结果：小于

# 步骤1、引入单元测试库
import unittest

# 步骤2：定义测试类，继承TestCase类。
#  其中函数名称以test_开头的，是一个测试用例。函数名称以test_开头的，才是测试用例。
class MyTestClass(unittest.TestCase):

    # 在测试类当中，所有用例运行之前，执行的前置工作。不管有几个用例，且只运行一次。
    # 有3个用例，在第一个用例运行之前，运行一次。
    # setupClass
    # case1
    # case2
    # case3
    # teardownClass
    @classmethod
    def setUpClass(cls):
        print("====我是测试类级别的前置工作===整个测试类，只运行1次！在用例执行之前！====")

    @classmethod
    def tearDownClass(cls):
        print("====我是测试类级别的后置工作===整个测试类，只运行1次！在所有用例执行完成之后！====")

    # setup
    # case1
    # teardown
    # setup
    # case2
    # teardown
    # setup
    # case3
    # teardown
    # 每一条用例运行之前，前置工作(连接数据库，打开文件...)想要输出：=====开始运行  一条用例======
    def setUp(self):
        print("=====开始运行  一条用例======")

    # 每一条用例运行之后，后置工作(断开数据库连接，关闭文件...)。想要输出：=====一条用例  运行结束======
    def tearDown(self):
        print("=====一条用例  运行结束======")

    def test_upper(self):
        print("***************************")
        # 1、测试数据
        my_str = "iDo"
        # 2、步骤
        res = my_str.upper()
        # 期望结果(IDO) - 自动与实际结果(res)比对
        # 当期望结果与实际结果不匹配的时候，单元测试框架应该在结果当中，体现用例失败。
        # 3、断言 == 期望结果与实际结果比对。 英文：assert
        self.assertEqual(res,"IDO"," 不是大写")  # 如果期望与实际不符，那么AssertionError

    def test_upper_is_true(self):
        print("***************************")
        # 1、测试数据
        my_str = "iDo"
        # 2、步骤
        res = my_str.isupper()
        # 期望：True  实际的：res
        self.assertTrue(res)

    def test_who_bigger(self):
        print("***************************")
        # 1、测试数据
        a,b = 100,244
        # 期望：小于
        self.assertLess(a,b)

    def my_first_ope(self):
        pass




