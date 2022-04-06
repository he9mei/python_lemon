#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
os模块
'''

import os

# 路径处理
# 1.获取当前工作路径
workspace=os.getcwd()
print(workspace)   # C:\Users\lipan\PycharmProjects\python_lemon\basic

# 2.列出当前路径下所有的文件和文件夹
files=os.listdir(workspace)   # 也可以不传参，就是当前文件夹；得到的是文件名称
print(files)
# ['basic1_1基础语法.py', 'basic1_2元组.py', 'basic1_2列表.py', 'basic1_2字典.py', 'basic2_1homework.py', 'basic2_1字符串.py', 'basic2_1运算符.py', 'basic2_2循环.py', 'basic2_2控制流if.py', 'basic2_2练习题.py', 'basic2_3函数.py', 'basic2_3双重for循环.py', 'basic3_1作业参考1.py', 'basic3_1作业参考2.py', 'basic3_1作业练习1.py', 'basic3_1作业练习2.py', 'basic3_1函数2.py', 'basic3_2内置函数.py', 'basic3_2变量作用域.py', 'basic3_2模块导入.py', 'basic3_3OS模块.py', 'basic3_3作业参考.py', 'basic3_3作业练习.py', 'basic3_3调试.py', '__init__.py']

# 3.文件名称和路径拼接 路径+路径/文件名
file1=os.path.join(workspace,files[0])
file2=os.path.join(workspace,'hhm',files[0])
print(file1)
# C:\Users\lipan\PycharmProjects\python_lemon\basic\basic1_1基础语法.py
# 会主动用连接符，不需要自己写

# 4.路径在系统中是否存在
# resp = os.path.exists(file1)   # True
resp = os.path.exists(file2)  # False
print(resp)

# 5.是不是路径，在判断路径是否存在
os.path.isdir(workspace)
# 6.是不是文件，再判断文件是否存在
os.path.isfile(file1)

# 7.路径分割
file_split = os.path.split(file1)   # 默认从后往前找到第一个\分割一次
print(file_split)
# ('C:\\Users\\lipan\\PycharmProjects\\python_lemon\\basic', 'basic1_1基础语法.py')
# python中路径用\\
# 转义：\将\转义为字符串的一部分

# 8.路径不存在怎么办？创建文件夹(如果存在，创建会报错)
# 比如路径C:\\Users\\lipan\\PycharmProjects\\python_lemon\\basic\\os_practice
# 创建1个文件夹（末尾文件夹前面的路径必须存在，只创建最后一个文件夹）
# os.mkdir('C:\\Users\\lipan\\PycharmProjects\\python_lemon\\basic\\os_practice')
# 创建一系列文件夹(给定目录中只要有不存在，都会创建)
# os.makedirs('C:\\Users\\lipan\\PycharmProjects\\python_lemon\\basic\\os_test\\os_test')

# 路径不存在时，才创建
path = 'C:\\Users\\lipan\\PycharmProjects\\python_lemon\\basic\\os_test\\os_test'
if not os.path.exists(path):
    os.makedirs(path)

'''
本节课总结：
debug小技巧  打断点，F7,F8

文件路径的操作
模块 ：os
1、获取当前的工作空间：os.getcwd()
2、列出指定目录下的文件和文件夹名称：os.listdir(目录)
3、将路径和文件拼接起来：os.path.join(a,b)
4、判断一下路径是否存在：os.path.exists(路径)
5、判断路径是一个目录呢，还是一个文件路径呢
   os.path.isdir(a)  os.path.isfile(a)
6、如果路径不存在，则创建路径。
   创建 最后一个路径   os.mkdir(a)
   创建  所有不存在的路径   os.makedirs(b)

'''