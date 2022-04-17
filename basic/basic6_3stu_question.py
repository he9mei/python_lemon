
# ---老师的笔记-完善解释---

# 问题：
# 在setupClass里设置cls.XX变量
# 在teardownClass里，引用时，提示找不到。

'''
解释：
@classmethod装饰的方法叫做类方式，cls代表类本身
cls.变量 也是类变量，是可以通用的。
以下方的测试用例为例，setUpClass定义的cls.a
在test_aaa中可以用self.a来调用；在tearDownClass中可以用cls.a来调用，
但是由于Python是非静态的代码，这里会提示找不到，但是运行到时是可以通过的。

'''


import unittest

class A(unittest.TestCase):

    aaa = 200

    @classmethod
    def setUpClass(cls):
        cls.a = 100
        print("==============")

    @classmethod
    def tearDownClass(cls):
        print(cls.a)
        print("1111111111111111111111")

    def test_aaa(self):
        # print(self.a)
        print("test")
