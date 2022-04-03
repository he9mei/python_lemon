#!/usr/bin/python3
# -*- coding: utf-8 -*-

# ----老师的讲解-------
"""
1.编写如下程序
a.用户输入1-7七个数字，分别代表周一到周日
b.如果输入1~5，打印对应的“周一”~“周五”，如果输入的数字是6或7，打印输出“周末”
c.如果输入0，退出循环
d.输入其他内容，提示：“输入有误，请重新输入！”
提示：本题可以使用if和while循环，同时需要校验用户的输入是否正确
"""


def get_week_name(num):
    dict_week = {"1":"周一","2":"周二","3":"周三","4":"周四","5":"周五","6":"周末","7":"周末"}
    if num not in "01234567":
        print("输入有误，请重新输入！")
    elif num in dict_week.keys():
        print(dict_week[num])

while True:
    num = input("请输入1-7七个数字：")
    get_week_name(num)
    if num == "0":
        break

"""
2.编写如下程序
输入一个人的身高(m)和体重(kg)，根据BMI公式（体重除以身高的平方）计算他的BMI指数
a.例如：一个65公斤的人，身高是1.62m，则BMI为 :  65 / 1.62 ** 2 = 24.8
b.根据BMI指数，给与相应提醒
低于18.5： 过轻
18.5-25：   正常
25-28：      过重
28-32：      肥胖
高于32：   严重肥胖
"""


def get_BMI(height,weight):
    if type(height) is not float and type(weight) is not float:
        print("数据格式错误！")
    else:
        index = weight / height ** 2
        print(index)
        if index < 18.5:
            print("过轻")
        elif 18.5 <= index <= 25:
            print("正常")
        elif 25 < index <= 28:
            print("过重")
        elif 25 < index <= 32:
            print("肥胖")
        else:
            print("严重肥胖")


get_BMI(1.55,46)
get_BMI(1.75,85)

"""
3.编写如下程序
从键盘输入一个用户名和密码，判断是否正确，如果正确则打印登录系统成功，否则显示用户名或密码错误。
a.定义一个函数，接收用户输入的用户名和密码作为参数
b.正确的账号，用户名为lemon，密码为best
"""


def login(username,passwd):
    user = {"username":"lemon","passwd":"best"}
    if username == user["username"] and passwd == user["passwd"]:
        print("登陆成功")
    else:
        print("用户名密码错误！！")


"""
4.取出列表中最大的值
将列表[13, 20, 42, 85, 9, 45]中的最大值为85
"""
lista = [13, 20, 42, 85, 9, 45]
# for index in range(len(lista)-1):
#     if lista[index] > lista[index + 1]:
#         lista[index], lista[index+1] = lista[index+1], lista[index]
#     print(lista[index], lista[index+1])
# print(lista[-1])
# 函数版本


def get_maxNum_in_list(num_lists):
    for index in range(len(num_lists) - 1):
        if num_lists[index] > num_lists[index + 1]:
            num_lists[index], num_lists[index + 1] = num_lists[index + 1], num_lists[index]
    print(num_lists[-1])


get_maxNum_in_list(lista)
list_b = [88,96,12,108,33]
get_maxNum_in_list(list_b)

#方法二：
max_num = 0
for i in list_b:
    if max_num < i:
        max_num = i
    print("最大值为：{}".format(max_num))

#方法三：
print("最大值为：{}".format(max(list_b)))
