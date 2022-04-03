#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
字典的遍历
双重for循环
'''

# 字典的遍历
dict_1 = {'name':'huahua', 'age':18}

# 取到所有keys/values/
print(dict_1.keys())   # dict_keys(['name', 'age'])
print(dict_1.values())   # dict_values(['huahua', 18])
print(dict_1.items())   # dict_items([('name', 'huahua'), ('age', 18)])

# 用key遍历
for item in dict_1.keys():
    print(item)
    print(dict_1[item])

# 键值对遍历方式
for key,value in dict_1.items():
    print(key)
    print(value)


# ---老师的笔记---
# 双重for循环   代码的复杂度

# 抽奖活动
# 活动礼品： 行李箱  签字笔    水杯   零食

# 5个人：冰天、兰心、粽子、alex、八娃

# 每一个同学：每一样礼品都去领取 = 遍历了所有的礼品。
gifts = ["行李箱","签字笔","水杯","零食"]
# for gift in gifts:
#     print("领取礼品：{}".format(gift))

# 遍历每一个同学
stus = ["冰天","兰心","粽子","alex","八娃"]

# 每一位同学，去领取每一个奖励。
for stu in stus:   # 遍历学生
    print("======================")
    print("当前的领奖人：{}".format(stu))
    for gift in gifts:   # 遍历奖品
        print("领取礼品：{}".format(gift))
