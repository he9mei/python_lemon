#!/usr/bin/python3
# -*- coding: utf-8 -*-

# -----老师的作业讲解----------

"""
1、补充缺失的代码：

用代码实现以下中文内容
 def print_directory_contents(sPath):
 #这个函数接受文件夹的路径作为输入参数， 返回该文件夹中文件的路径， 以及其包含文件夹中文件的路径。

备注：最多只考虑两层文件夹的处理。即sPath是第一层文件夹，其下的文件夹是第二层文件夹。
要求是文件的完整路径 ，而不仅仅是文件名。
"""
import os

# 非递归方式
def print_directory_contents(sPath):
    dir_conts = []
    # 如果sPath是路径 ,且存在
    if os.path.isdir(sPath) and os.path.exists(sPath):
        # 列出其下所有文件
        files = os.listdir(sPath)
        # 获取所有文件路径
        for file in files:
            file_path = os.path.join(sPath,file)  # 拼接路径
            dir_conts.append(file_path)   # 将文件添加到列表中
            if os.path.isdir(file_path):  # 如果是个文件夹
                # 列出其下所有文件
                sub_files = os.listdir(file_path)
                # 获取所有文件路径
                for sub in sub_files:
                    sub_file_path = os.path.join(file_path, sub)  # 拼接路径
                    dir_conts.append(sub_file_path)  # 将文件添加到列表中
    print(dir_conts)


print_directory_contents("D:\\4-小简")
print_directory_contents(r"D:\Pychram-Workspace\python17\class_20190420")



# 递归方式
# def print_directory_contents(sPath):
#     dir_conts = []
#     # 如果sPath是路径 ,且存在
#     if os.path.isdir(sPath) and os.path.exists(sPath):
#         # 列出其下所有文件
#         files = os.listdir(sPath)
#         # 获取所有文件路径
#         for file in files:
#             file_path = os.path.join(sPath,file)  # 拼接路径
#             dir_conts.append(file_path)   # 将文件添加到列表中
#             if os.path.isdir(file_path):
#                 subs = print_directory_contents(file_path)
#                 dir_conts += subs
#     print(dir_conts)
#     return dir_conts
#
# print_directory_contents("D:\\4-小简")
# print("=============================================")
# print_directory_contents(r"D:\Pychram-Workspace\python17\class_20190420")