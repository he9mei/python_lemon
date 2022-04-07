#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
函数-1
'''

# ---老师的笔记---

# 函数
# 实现了某一特定功能。
# 可以重复使用。

# len() 功能:获取长度。
# input()  功能: 控制台输入
# print()  功能：输出

# 语法 关键字def
"""
def 函数名称():
    #实现功能的代码块。
"""

# 伞
# 定义功能。
def car():
    print("出行功能！！")

# 调用功能 = 执行函数的代码。
"""
函数名称()
"""
# car()   # 先定义再调用。
# car()   # 先定义再调用。
# car()   # 先定义再调用。
# car()   # 先定义再调用。
# car()   # 先定义再调用。
# car()   # 先定义再调用。

# 高铁、灰机。
# 出行功能：需要输入的数据：身份证、飞机票，起点，目的地。否则用不了功能。
# def out_going():
#     print("请出示身份证，飞机票")
#     id = "123456789001122"
#     ticket = "TTYYC12"
#     if id is not None and ticket is not None:
#         print("请上飞机。")
#
# # bear
# out_going()  #使用的时候，应该是把身份证和飞机票，传到这个函数里。
# # 寓次方
# out_going()

# 使用的时候，应该是把身份证和飞机票，传到这个函数里。
# 定义
def out_going_v2(id,ticket):   #形式参数,接收具体的数值。会变！！  变量来表示。用,隔开。
    print("请出示身份证，飞机票")
    # id = "123456789001122"
    # ticket = "TTYYC12"
    print(id,ticket)
    if len(id) != 18:
        print("身份证不符合要求！！")
    if id is not None and ticket is not None:
        print("请上飞机。")


# out_going_v2("123456789001122","TTYYC12")   #实参 = 具体的数值。
# out_going_v2("12345672233441112345","TTYYC33")
# out_going_v2("123456722334411",None)

# 1、位置参数(必传，定义的时候没有数值。)  形参和实参的参数顺序是一一对应的。


# 2、默认参数。定义函数时，给形参一个默认的具体数值。
# 可传可不传。  默认参数要放在所有的必传参数之后。
# 定义
def out_going_v3(id,ticket,enter="上海",gate=15):   #形式参数  变量来表示。用,隔开。
    enters = ["上海","北京","深圳"]
    print("请出示身份证，飞机票")
    # id = "123456789001122"
    # ticket = "TTYYC12"
    print(id,ticket,enter,gate)
    if len(id) != 18:
        print("身份证不符合要求！！")
    elif enter not in enters:
        print("当前城市 尚未开放 机场！！")
    elif id is not None and ticket is not None:
        print("请上飞机。")

out_going_v3("12345672233441112345","TTYYC33")  #不传默认参数
out_going_v3("12345672233441112345","TTYYC33","北京")  #传值
out_going_v3("12345672233441112345","TTYYC33",gate=25)  #指定参数

# 3、指定参数   调用的时候去指定  形参=数据。
# 调用的时候，全部参数，形参=值。可以不按位置的顺序来传参。
print("========================================")
out_going_v3(ticket="TTYYC33",id="12345672233441112345",gate=25)  #指定参数


# 4、可变参数\return
