#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
运算符
算数运算符
比较（关系）运算符
赋值运算符
逻辑运算符
成员运算符
'''

# ---老师的笔记---
# 运算符操作
# 算术运算符
num_a = 100
num_b = 5000

# 加法
print(num_a + num_b)
# 减法
print(num_a - num_b)
# 乘法 *
print(num_a * num_b)
# 除法 /
print(num_a / num_b)
# 取余数 %
print(num_a % num_b)

# 比较运算  结果：布尔值。True,False
# 比较相等  ==
print(num_a == num_b)
# 不相等
print(num_a != num_b)
# 大于等于
print(num_a > num_b)  # False
print(num_a >= num_b)
# 小于等于
print(num_a < num_b)
print(num_a <= num_b)  # True

# 赋值运算符。=
# += -=   在变量原来的基础，累加或者累减。
meat = 53
xia = 40
water = 2


count = 0   #总价是0
#count = count + meat   #牛肉  #0 + 53
count += meat

#count = count + xia   #虾   53 + 40
count += xia

#count = count + water  #水  53+40+2
count += water
print(count)

count -= xia
print(count)


# 逻辑运算符  and与  or或  not 非
#  条件(True/False) and 条件(True/False)    条件(True/False) or 条件(True/False)   not 条件(True/False)
# input函数  输入函数。
city = input("请输入你所在的城市：")   #字符串
sex = input("请输入你的性别：")    #字符串

# print(city == "上海" and sex == "女")  #同时都为真，才会真。
# print(city == "上海" or sex == "女")  #同时都为假，才会假。
print(not sex == "女")  # not 真 =假   not 假 =真


# 成员运算符   列表、字符串 、 字典 、 元组
# 成员 in 集合类型数据    成员 not in 集合类型的数据
c = [89,12,44,5,863,455]
print("科比" not in c)   #True False

# 比较运算符、逻辑运算符、成员运算符---结果为True和False












