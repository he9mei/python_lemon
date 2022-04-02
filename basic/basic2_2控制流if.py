#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
控制流if
'''

# ----老师笔记------------------------

# 判断
"""
if 条件(True/False):
   条件为真时，执行的代码(要干的事情)
[elif 条件:
    条件为真时，执行的代码(要干的事情)
elif 条件:
    条件为真时，执行的代码(要干的事情)
else:
    以上条件全部不满足，要干的事情。]

"""
money = input("自动化学完之后，涨薪金额：")
city = input("所在的城市：")
# if money == "5000":
#     print("请全班同学喝奶茶！")
# elif money == "10000":
#     print("翻倍了！！")
#     print("请小简老师吃个大餐！")
# else:
#     print("继续学习！！")

if money == "5000" and city == "成都":
    print("请全班同学喝奶茶！")
elif money == "10000" and city in ["上海","深圳","北京"]:
    print("翻倍了！！")
    print("请小简老师吃个大餐！")
else:
    print("继续学习！！")

# 特殊的情况为假：[]、{}、None、0、{}
list_a = []
if list_a:
    print("11111")
else:
    print("2222222222")







