#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
1、补充缺失的代码：

用代码实现以下中文内容
 def print_directory_contents(sPath):
 #这个函数接受文件夹的路径作为输入参数， 返回该文件夹中文件的路径， 以及其包含文件夹中文件的路径。

备注：最多只考虑两层文件夹的处理。即sPath是第一层文件夹，其下的文件夹是第二层文件夹。
要求是文件的完整路径 ，而不仅仅是文件名。
"""
import os

# 只做2层文件夹的遍历
def print_directory_contents(sPath):
    all_files_path=[]
    if os.path.isdir(sPath):
        files = os.listdir(sPath)
        for itme in files:
            file_path = os.path.join(sPath,itme)
            # all_files_path.append(file_path)  # 第1层的文件和文件夹都打印的情况
            if os.path.isdir(file_path):
                files2 = os.listdir(file_path)
                for i in files2:
                    file_path2 = os.path.join(file_path, i)
                    if os.path.isfile(file_path2):   # 第2层只打印文件的情况（如果是空文件夹不会打印）
                        all_files_path.append(file_path2)
            else:
                all_files_path.append(file_path)   # 第1层只打印文件的情况
    return all_files_path

spath = 'E:\\柠檬班Python自动化加密课程\\py17期-加密\\第四周\\20190423_文件操作+异常处理' # 注意Python中路径都是双斜杠，除非特殊处理
all_files_path = print_directory_contents(spath)
for itme in all_files_path:
    print(itme)

print('==============================')

# 递归写法---文件和文件夹都要的情况
# def print_directory_contents(sPath):
#     all_files_path = []
#     if os.path.isdir(sPath) and os.path.exists(spath):
#         files = os.listdir(sPath)
#         for itme in files:
#             file_path = os.path.join(sPath, itme)
#             all_files_path.append(file_path)  # 第1层的文件和文件夹都打印的情况
#             if os.path.isdir(file_path):
#                 sub_file_path = print_directory_contents(file_path)
#                 all_files_path += sub_file_path  # 第2层的文件和文件夹列表，拼接到第1层的列表
#     return all_files_path

# 递归写法---只要文件的情况
def print_directory_contents(sPath):
    all_files_path = []
    if os.path.isdir(sPath) and os.path.exists(spath):
        files = os.listdir(sPath)
        for itme in files:
            file_path = os.path.join(sPath, itme)
            if os.path.isfile(file_path):
                all_files_path.append(file_path)
            elif os.path.isdir(file_path):
                sub_file_path = print_directory_contents(file_path)
                all_files_path += sub_file_path
    return all_files_path

spath = 'E:\\柠檬班Python自动化加密课程\\py17期-加密\\第四周\\20190423_文件操作+异常处理' # 注意Python中路径都是双斜杠，除非特殊处理
all_files_path = print_directory_contents(spath)
for itme in all_files_path:
    print(itme)