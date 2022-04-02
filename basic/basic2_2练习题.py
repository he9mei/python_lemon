#!/usr/bin/python3
# -*- coding: utf-8 -*-

# ---------练习--------------
"""
登录功能：用户名和密码存在{'name':'huahua','pwd':'123456'}字典中，
通过控制台输入用户名和密码判读是否正确，
然后给出对应的提示消息：登录成功 OR 用户名或密码错误
"""
info = {'name': 'huahua', 'pwd': '123456'}

name = input("用户名：")
pwd = input("密码：")
if name == info['name'] and pwd == info['pwd']:
    print("登录成功")
elif name != info['name']:
    print('用户名错误')
else:
    print("密码错误")


# 1-100数字求和
# 写法1.用while循环
sum = 0
i = 1
while i<101:
    sum += i
    i += 1
print("1-100的和是：{}".format(sum))

# 1-100的和是：5050

# 写法2.用for循环
sum = 0
for i in range(1,101):
    sum += i
print("1-100的和是：{}".format(sum))


"""
2.一个足球队在寻找年龄在10岁到12岁的小女孩（包括10岁和12岁）加入。
编写一个程序，询问用户的性别（m表示男性，f表示女性）和年龄，
然后显示一条消息指出这个人是否可以加入球队，询问10次后，输出满足条件的总人数。
"""
count = 0
for i in range(2):
    sex = input("性别（男m，女f））：")
    age = input('年龄：')
    if sex == 'f' and int(age) in [10,11,12]:
        count += 1
        print("符合条件")
    else:
        print("不符合条件")
print("符合条件的总人数：{}".format(count))
