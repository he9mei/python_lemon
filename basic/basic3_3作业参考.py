#!/usr/bin/python3
# -*- coding: utf-8 -*-

# ---老师的讲解---

'''
#自动贩卖机：
# 允许用户投币，但投币总数不能超过10块钱(币总只支持1元，5元，10元)。 如果10块以上，则直接退出贩卖机功能使用。
# 贩卖机中饮料只有橙汁、椰汁、矿泉水、早餐奶，售价分别是3.5，4.2，4.5 ，2
# 用户需要通过： 投钱和选择饮料，来使用贩卖机。
# 如果饮料是没有的，则直接退出贩卖机功能使用。
# 并通过判断之后，给用户吐出饮料和找零。
# 请写函数实现贩卖机的功能。并调用此函数，调用时要用不同的数据来测试函数的功能是否正确实现。

ps：不需要考虑重复投币。贩卖机只需要知道总的投币数量即可。

一次只取一个饮料
'''


def vending_machine(money, drink):
    # 饮料
    drinks = {"橙子": 3.5, "椰汁": 4.2, "矿泉水": 4.5, "早餐奶": 2}

    # 判断参数格式
    if type(money) is not int and type(money) is not float:
        print("您的金额格式不正确。退出贩卖机使用！！")
        return
    # 判断参数格式
    if type(drink) is not str:
        print("您的饮料名称格式不正确，退出贩卖机使用！！")
        return
    # 饮料不在范围内
    if drink not in drinks.keys():
        print("贩卖机暂时无此饮料，敬请期待！！")
        return

    # 满足money 是否满足条件
    if 0 < money <= 10 and (money % 1 == 0 or money % 5 == 0 or money % 10 == 0):
        change = money - drinks[drink]
        # 判断是否买得起
        if change >= 0:
            print("您选中的饮料 {} 价格为：{}元，您的金额为：{}元，找零：{}元".format(drink, drinks[drink], money, change))
            return change
        else:
            print("您的金额不够，买不起！！")
    else:
        print("贩卖机只支持1元、5元、10元币种。您的金额不合格！！")


vending_machine(5, "橙子")
vending_machine("111", "椰汁")
vending_machine(9, "椰汁")
vending_machine(9.5, "早餐奶")
vending_machine(9, "怡宝")
vending_machine(2, "椰汁")


