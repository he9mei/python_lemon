#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
pandas暂时了解即可
pip install pandas
pip install xlrd
'''

# ---老师的笔记---

import pandas as pd

# DataForm 二维数据
# print(pd.read_excel("datas.xlsx"))

# 多行数据 - 加载表单
s = pd.read_excel("datas.xlsx")
print(s)

# 多行数据 - 随机
print(s.sample(2).values)

# 某一行数据
print(s.loc[0].values)   # 除表头以外，下标从0开始。

# 多行数据
print(s.loc[1:3])  # 1,2,3
print(s.loc[1:3].values)

# 某一个单元格的数据
print(s.iloc[1,0])  # 除表头以外数据，第二行第1列。


