#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Name: test_two
# Author: 简
# Time: 2019/5/19

import unittest

class TestCaculator(unittest.TestCase):

    def test_add(self):
        res = 100 + 200  # 1 相加
        self.assertEqual(300,res)  # 2 比对

    def test_add_2(self):
        res = 100 + 0.02  # 1 相加
        self.assertEqual(100.02, res)  # 2 比对

    def test_add_3(self):
        res = 0.01 + 0.02  # 1 相加
        self.assertEqual(0.03, res)  # 2 比对

    def test_minus(self):
        res = 100 * 10
        self.assertEqual(res,1000)




