#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
读取单元格练习
'''
# import os
# print(os.getcwd())
import openpyxl
wb = openpyxl.load_workbook(r'C:\Users\lipan\PycharmProjects\python_lemon\basic\testData.xlsx')
# 遇到问题，
# 直接在pycharm新建的文件data.xlsx报错：ipfile.BadZipFile: File is not a zip file
# 从wps新建的文件可以
sh = wb['data']
cell_value = sh.cell(row=1,column=1).value
# print(cell_value)

for i in range(2,sh.max_row+1):  # 第1行作为表头，从第2行开始遍历
    case={}
    for j in range(1,sh.max_column+1):
        keys = sh.cell(1, j).value
        cell_value = sh.cell(i,j).value
        case[keys]=cell_value
    print(case)
'''
{'姓名': '何丫丫', '年龄': 20, '城市': '上海'}
{'姓名': '李晓霞', '年龄': 28, '城市': '北京'}
{'姓名': '王二狗', '年龄': 22, '城市': '重庆'}
'''

# 作业：
# 类中方法:读、写并保存操作

