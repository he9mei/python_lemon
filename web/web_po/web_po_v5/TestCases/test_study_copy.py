#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pytest  # 如果没有安装，先导入，点击提示进行安装；也可以pip install pytest


# pytestmark = pytest.mark.demo  # 模块级别的标记


# @pytest.mark.smoke
@pytest.mark.demo
@pytest.mark.usefixtures("my_module")
def test_hello(my_session):
    print("hello")
    print("my_session的值是{}".format(my_session))


@pytest.mark.demo   # 标记类，会执行类里面的所有用例
class TestDemo:
    pytestmark = pytest.mark.demo   # 类级别的标记

    def test_demo1(self, my_session):
        print("test_demo1")
        print("my_session的值是{}".format(my_session))

    def test_demo2(self):
        print("test_demo2")


'''
执行：
terminal
默认目录：当前工程
-->cd web/web_po/web_po_v5
-->pytest test_study.py
-->pytest test_study.py -m smoke
-->pytest test_study.py -m demo
'''