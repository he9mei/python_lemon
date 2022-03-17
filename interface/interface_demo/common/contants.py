#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os

'''
讲解绝对路径和相对路径
'''

# print(os.path.abspath(__file__))
# 当前文件的绝对路径
# C:\Users\lipan\PycharmProjects\python_lemon\interface\interface_demo\common\contants.py
# print(os.path.dirname(os.path.abspath(__file__)))
# 文件上一级目录路径
# C:\Users\lipan\PycharmProjects\python_lemon\interface\interface_demo\common
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 项目根目录
# data_path = base_dir+"/data"  # 不这样写？老师讲的下面的join方法
cases_file = os.path.join(base_dir, "data", "cases.xlsx")
global_file = os.path.join(base_dir, "config", "global.conf")
online_file = os.path.join(base_dir, "config", "online.conf")
test_file = os.path.join(base_dir, "config", "test.conf")
logs_file = os.path.join(base_dir, "logs", "api.log")
testCases_dir = os.path.join(base_dir, "testCases")
report_file = os.path.join(base_dir, "report", "api.html")
