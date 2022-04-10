#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
类与对象1
'''

# ---老师的笔记---

# 面向对象   python,java,c#
# 面向过程   C

# 类和对象
# 类 类型类别、类别 物以类聚   一类事物
# 班级、人类、动物类、车、学生类、老师类、手机、电脑
# 统称 == 共同特性
# 不具体、抽象  共同特性

# 对象   非常具体的。
# 对象就是类的一个实例化。  具体化

# 类 == N个对象

# 定义类  类名首字母大写 驼峰命名
# 学生的共性：
#属性：昵称、学号、性别、年龄、班级、联系方式、城市、工作
#行为(动作 - 逻辑处理)：上课、写作业、打卡、交学费、考试 、作笔记、提问



# 封装  类=属性+行为   抽像 -
class Student:

    # 属性  类内部全局通用。
    name = "小小"
    stu_id = "123456"
    class_name = "python17"
    city = "上海"

    # 行为  self就是我，我就是self。 类实例化之后，明确我是谁。
    def attend_course(self):
        # # 调用类的属性
        # self.name = "小简"
        # # 调用类的行为
        # self.do_homework()
        print("{}正在学习类和对象。".format(self.name))
        pass

    # 行为
    def do_homework(self):
        print("{}在写作业中。。".format(self.name))

    # 修改属性的行为
    def update_name(self,name):
        self.name = name

    def update_class_name(self,class_name):
        self.class_name = class_name

    def update_stu_id(self,stu_id):
        self.stu_id = stu_id

    def update_city(self,city):
        self.city = city


# 具体化 == 实例化 ==  具体的对象。有具体的属性和行为。
# 语法： 实例名称 = 类名()

# alex = Student()   # 实例化，具体化
# # print(alex)
# alex.update_name("alex")
# print(alex.name)   # 实例名称.属性值
# alex.attend_course()  # 实例名称.行为
# print(alex.class_name)
# print(alex.attend_course())  # 实例名称.行为

# # # 第二个实例化，具体化
# wanwan = Student()  # 实例化
# wanwan.update_name("wanwan")
# print(wanwan.name)
# wanwan.do_homework()

# 能不能在实例化的时候，就同时初始化某些属性。
# 初始化函数  在实例化的时候，初始化一些内容。

"""
类的初始化函数：
__init__   固定的名字。在类实例化的时候，会自动调用。
初始化函数不能写return。
"""


# 封装  类=属性+行为   抽像 -
class StudentV2:

    # 初始化工作
    def __init__(self,name,stu_id,class_name,city="上海"):
        self.name = name
        self.stu_id = stu_id
        self.class_name = class_name
        self.city = city
        print("初始化工作完成，我已经有了具体的名字、学号、班级、城市这四个属性。")

    # 行为  self就是我，我就是self。 类实例化之后，明确我是谁。
    def attend_course(self):
        print("{}正在学习类和对象。".format(self.name))
        return

    # 行为
    def do_homework(self):
        print("{}在写作业中。。".format(self.name))
        return

# 实例化类的同时，会主动调用init函数。
luoluo = StudentV2("罗罗","222222","python17","北京")
print(luoluo.stu_id)
luoluo.attend_course()  # 行为

hukai = StudentV2("胡凯","333111","python17","深圳")
hukai.do_homework()

# 中场休息：手机 -  类 实例化你们自己的手机。















