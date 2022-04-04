#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
函数2
'''
# ---老师的笔记--------------

# 4、可变参数\return
# 可变参数：参数个数不固定 。调用的时候来确定有几个参数。
# 第一种：*args  在函数内部，是以元组的形式来表示。
def my_args(*args):   # 放在位置参数，默认参数之后。#arguments
    print(args)

# my_args(12,34,True,False,[1,2])
# my_args("hello",True)
# my_args()

# 第二种：**kwargs 在函数内部，是以字典的形式来表达。
def my_kwargs(**kwargs):
    print(kwargs)

# my_kwargs(name="xj")  # key=value
# my_kwargs(name="xj",sex="female",city="changsha")

#一个函数的定义当中，都有*args,**kwargs.先*args，再**kwargs

def my_all_args(num,*args,**kwargs):
    print(num,args,kwargs)
    if "my_class" in kwargs:
        if kwargs["my_class"] == "python17":
            print("正确！")

# my_all_args(12,23,34,45,hello="world",my_class="python17")
#
# # 解包   *元组 *(23,34,45) = 23,34,45
# my_all_args(12,*(23,34,45),hello="world",my_class="python17")
# 解包以后做框架还会用到

# return   函数返回
# 取钱ATM
#      取钱功能(ATM) == 吐出来==返回
# 输入数据：银行卡(8)、密码(6)、金额(3000)
# 输出数据：人民币、卡、凭证
# 有进有出


# return
# 1、代表函数返回数据
# 2、终止函数调用 。
# 在执行函数内部代码的时候，如果遇到了return关键字，意味着函数调用结束。不管后面还有没有逻辑处理。

# def get_money_from_atm(cardNo,passwd,count):
#     # 判断数据是否符合要求，如果不符合，不能取钱。
#     if len(cardNo) == 8 and len(passwd) == 6 and 100 < count < 3000:
#         print("可以取钱,取钱金额为{}".format(count))
#         return count   # return 返回值

#3、return 后面可以不用跟任何的数据。实际上代表的是返回的None 。return None


def get_money_from_atm(cardNo,passwd,count):
    # 判断数据是否符合要求，如果不符合，不能取钱。直接退出函数调用
    if len(cardNo) != 8 or len(passwd) != 6 or (count > 3000 or count < 100):
        return

    # print("可以取钱,取钱金额为{}".format(count))
    # 符合取钱的条件下，返回取款金额
    return count,cardNo

# 4、调用函数的时候，如果函数有返回值，要主动用变量接收函数的返回值。
# 5、return 任意类型的数据。
# 6、定义函数的时候，没有用到return.请问调用函数，有返回值？有，为None
# money = get_money_from_atm("12345678","123456",500)
# print(money)
# money,cardNo = get_money_from_atm("12345678","123456",500)
# print(money,cardNo)
# money = get_money_from_atm("123456","123456",500)
# print(money)

def buy_somethings(price,money): #price是物品的价格。money是你的钱。
    if money >= price:
        print("可以买！")
    else:
        print("买不起！！")

# 调用函数。
# buy_somethings(600,money)

# 这里只是演示无return返回值为None的情况
# def get_maxNum_in_list(num_lists):
#     for index in range(len(num_lists) - 1):
#         if num_lists[index] > num_lists[index + 1]:
#             num_lists[index], num_lists[index + 1] = num_lists[index + 1], num_lists[index]
#     print(num_lists[-1])
#
#
# list_b = [88,96,12,108,33]
# res = get_maxNum_in_list(list_b)
# print("1111111111111111111111111111111111")
# print(res)

# 版本2：用控制台输入的场景，串联取钱和买东西
def get_money_from_atm_v2(cardNo,passwd,count):
    # 判断数据是否符合要求，如果不符合，不能取钱。直接退出函数调用
    if len(cardNo) != 8 or len(passwd) != 6 or (count > 3000 or count < 100):
        return

    # print("可以取钱,取钱金额为{}".format(count))
    # 符合取钱的条件下，返回取款金额
    return count,cardNo

def buy_somethings_v2(price,money): #price是物品的价格。money是你的钱。
    if money >= price:
        print("可以买！")
    else:
        print("买不起！！")

cardNo = input("卡号：")
passwd = input("密码：")
gkd = input("取钱金额：")
price = input("物品价格为：")
# 1、取钱
res = get_money_from_atm_v2(cardNo,passwd,int(gkd))
print(res)
if res is not None:
    # 2、拿着你取的钱，去买东西
    buy_somethings_v2(int(price),res[0])