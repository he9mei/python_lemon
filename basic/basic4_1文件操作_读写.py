#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
文件操作：文件的创建、读写
'''

# 一、文件的读取
# 1.打开文件
# mode：r代表读，w代表写，a代表追加；默认是r，可以不写
fs = open("read.txt", mode='r', encoding='utf-8')
# 2.读取
# 全部读取---常用
# file = fs.read()  # 默认是全部读取 n可以指定字节数
# print(file)
# print('==================')
# file2=fs.read()   # 读完之后再读就没有了
# print(file2)
'''
我是测试文件
练习文件的读取
不重要
==================
'''
# 按照行读取---不重要，基本用不到
# line1=fs.readline()  # 如果读到换行会空一行
# print(line1)
# print('===============')
# line2=fs.readline(3)   # 无法指定读多少行，只能指定读多少字符
# print(line2)
# print('===============')

'''
我是测试文件

===============
练习文
===============
'''

# 二、文件的写、追加
# 1.文件的写入
# w 代表写
# 如果文件存在，会覆盖之前的内容；如果文件不存在，会自动创建文件
# 如果有中文必须指定encoding='utf-8'，否则会乱码
# write不会主动换行，需要加上\n主动换行
# 在close之前多次调用wirte写入，是追加的；close之后重新打开再写入，是覆盖的
fs = open('write.txt',mode='w',encoding='utf-8')
fs.write("你好，Python\n") # ---常用
fs.write('拜拜,java\n加油呀\n')
# 写入多行，参数是列表（也需要\n来换行）---用的很少
fs.writelines(['学好Python基础\n','还要学习接口自动化\n','UI自动化'])
fs.close()   # 写完要关闭文件以免占用资源（只要打开文件，就尽量都要关闭）
'''
你好，Python
拜拜,java
加油呀学好Python基础
还要学习接口自动化、UI自动化
'''
# 2.文件的追加
# a 代表追加
# 如果文件不存在则创建文件再追加写；如果文件已经存在，则在文件末尾追加
fs = open('write.txt',mode='a',encoding='utf-8')
# 可以查看文件的属性
print(fs.encoding)  # utf-8
print(fs.closed)  # False
fs.write('再努力亿点点')
fs.close()


# 写完立即读取是读不到的；需要先关闭，再打开再读取
