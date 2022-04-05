#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
变量作用域
'''

# ---老师的笔记---

count = 50000  #全局变量 - 在当前的py文件当中，全局可用。


# def my():   # 在函数内部定义的变量，仅在函数内部有效。局部变量。
#     count = 5
#     count += 10
#     print(count)


# 想要在函数内部，改变全局变量的值。
def eat():
    # 用家庭基金请人吃饭。饭费为500
    global count   #函数内部，声明count是全局变量。后续逻辑，count都是对全局变量的处理。
    count = count - 500
    print(count)
    # pass   # 占位符

eat()
print(count)
'''
结果：
49500
49500
'''

# 如果只是把全局变量的值传进来，函数内部处理，不会改变全局变量的值
def eat(money):
    money = money - 500
    print(money)

eat(count)  # money = count
print(count)

'''
结果：
49500
50000
'''
