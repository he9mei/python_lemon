#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
作业练习
'''

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

def auto_buyer(money,drink):
    dict_drink = {'橙汁':3.5,'椰汁':4.2,'矿泉水':4.5,'早餐奶':2}
    if money<1 or money>10:
        print('金额不符合要求！')
        return
    elif drink not in dict_drink.keys():
        print("没有你要的饮料！")
        return
    elif money-dict_drink[drink]<0:
        print("金额不足，无法购买！")
        return money
    else:
        print("取走饮料：{}；找零：{}".format(drink, money-dict_drink[drink]))
        return drink,money-dict_drink[drink]


# money = input("请投币（1元，5元，10元）：")
# drink = input("请选择饮料（橙汁、椰汁、矿泉水、早餐奶）：")
# money = int(money)
# resp = auto_buyer(money,drink)

# 改成不用手动输入，直接传值验证
# resp=auto_buyer(0.5,'矿泉水')
# resp=auto_buyer(10,'可乐')
# resp=auto_buyer(2,'橙汁')
resp=auto_buyer(10,'矿泉水')
print(resp)

