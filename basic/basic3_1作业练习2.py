#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
题目1
1.编写如下程序
a.用户输入1-7七个数字，分别代表周一到周日
b.如果输入1~5，打印对应的“周一”~“周五”，如果输入的数字是6或7，打印输出“周末”
c.如果输入0，退出循环
d.输入其他内容，提示：“输入有误，请重新输入！”
提示：本题可以使用if和while循环，同时需要校验用户的输入是否正确
"""

# def week():
#     list_int = [1,2,3,4,5,6,7]
#     list_day = ["周一","周二",'周三','周四','周五','周末','周末']
#     i=1
#     while i<=7:
#         day = input("请输入数字1-7：")
#         day = int(day)
#         if day in list_int:
#             print(list_day[day-1])
#         elif day == 0:
#             break
#         else:
#             print("输入有误，请重新输入！")
#         i += 1
#
# week()


# 字典
# def week():
#     dict_day = {'1': "周一", "2": "周二", '3': '周三', '4': '周四', '5': '周五', '6': '周末', '7': '周末'}
#     i = 1
#     while i <= 7:
#         day = input("请输入数字1-7：")
#         if day in dict_day.keys():
#             print(dict_day[day])
#             i += 1
#         elif int(day) == 0:
#             break
#         else:
#             print("输入有误，请重新输入！")
#
# week()

# 老师的写法
def week(day):
    dict_day = {'1': "周一", "2": "周二", '3': '周三', '4': '周四', '5': '周五', '6': '周末', '7': '周末'}
    # 老师先判断不合法数据
    # if day not in '1234567':  # 老师这样写，12没有提示
    # if int(day) not in [1,2,3,4,5,6,7]:  # 我自己这样写，但是输入不是数字会报错
    #     print("输入有误，请重新输入！")
    # elif day in dict_day.keys():
    #     print(dict_day[day])
    if day in dict_day.keys():   # 我自己这样写感觉更好
        print(dict_day[day])
    else:
        print("输入有误，请重新输入！")

# while True:
#     day = input("请输入数字1-7：")
#     if day == '0':
#         break
#     else:
#         week(day)
'''
请输入数字1-7：7
周末
请输入数字1-7：4
周四
请输入数字1-7：hha 
输入有误，请重新输入！
请输入数字1-7：哈哈哈
输入有误，请重新输入！
请输入数字1-7：0

'''

'''
题目2
2.编写如下程序
输入一个人的身高(m)和体重(kg)，根据BMI公式（体重除以身高的平方）计算他的BMI指数
a.例如：一个65公斤的人，身高是1.62m，则BMI为 :  65 / 1.62 ** 2 = 24.8
b.根据BMI指数，给与相应提醒
低于18.5： 过轻
18.5-25：   正常
25-28：      过重
28-32：      肥胖
高于32：   严重肥胖
'''

def bmi(height,weight):
    height = float(height)
    weight = float(weight)
    BMI = weight/height**2
    # print('BMI是{}'.format(BMI))
    if BMI<18.5:
        print("过轻")
    elif BMI>=18.5 and BMI<=25:
        print("正常")
    elif BMI>25 and BMI<=28:
        print("过重")
    elif BMI>28 and BMI<=32:
        print("肥胖")
    elif BMI>32:
        print("严重肥胖")

# height = input("请输入身高m:")
# weight = input('请输入体重kg:')
# bmi(height,weight)


'''
题目3：
"""
从键盘输入一个用户名和密码，判断是否正确，如果正确则打印登录系统成功，否则显示用户名或密码错误。
a.定义一个函数，接收用户输入的用户名和密码作为参数
b.正确的账号，用户名为lemon，密码为best
"""
'''
def login(userName,pwd):
    user = {'userName':'lemon','pwd':'best'}
    if userName == user['userName'] and pwd == user['pwd']:
        print("登录成功")
    else:
        print("用户名或密码错误")

# userName=input("请输入用户名：")
# pwd=input("请输入密码：")
# login(userName,pwd)

'''
题目4
取出列表中最大的值
将列表[13, 20, 42, 85, 9, 45]中的最大值为85
'''
# 方法1
def get_max(list_num):
    max_num = 0
    for i in list_1:
        if i>max_num:
            max_num=i
    print(max_num)

list_1 = [13, 20, 42, 85, 9, 45]
get_max(list_1)

# 方法2
def get_max(list_num):
    for i in range(len(list_num)-1):
        if list_num[i]>list_num[i+1]:
            list_num[i],list_num[i+1]=list_num[i+1],list_num[i]
    print(list_num[-1])

list_1 = [13, 20, 42, 85, 9, 45]
get_max(list_1)

# 53fen