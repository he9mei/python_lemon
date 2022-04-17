#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Name: homework_0509_challenge
# Author: 简
# Time: 2019/5/15

"""
1、将配置文件的读取操作，封装成自己的类；
2、利用上节课的excel操作类。

主函数当中(应用场景)：
1、读取给定的行的数据 - 可以是单行、也可以是多行。由配置文件决定。
2、读取给定的(行号、列号)数据 - 可以是一个，也可以是多个。由配置文件决定。

使用配置类中的方法，读取配置数据，并传递到excel实例当中，去使用。
ps：配置化的数据的section可以是以下四个：excel路径、sheet表单、行下标、行和列下标。
"""
from class_20190516.homework_0509_challenge.my_config import MyConfig
# 1 读取配置数据
mc = MyConfig("conf.ini")
excel_path = mc.get("excel","file_path")  # 文件路径
sheet_name = mc.get("sheet","sheet_name")  # 表单名称
rows = mc.get_list_dict_tuple("row","row")  # 读取第几行、第几行的数据
cords = mc.get_list_dict_tuple("coordinate","cors")

# 2、操作excel
from class_20190516.homework_0509_challenge.my_excel import MyExcel
me = MyExcel(excel_path)  # 使用配置文件中的，文件路径
me.select_sheet_by_name(sheet_name)  # 使用配置文件中的，表单名称
for row in rows:
    datas = me.get_dada_by_row(row)  # 使用配置文件中的，第几行，第几行。
    print(datas)

for cord in cords:
    cell_data = me.get_data_by_cell(*cord) # 使用配置文件中的，单元格坐标点。
    print(cell_data)