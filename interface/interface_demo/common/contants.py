#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os

'''
讲解绝对路径和相对路径
1小时10分钟
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

