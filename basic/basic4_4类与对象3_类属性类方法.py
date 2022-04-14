#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
类与对象3
'''
# 通过调试可以看到，对象luoluo的内存地址，进入luoluo调用的类方法查看self的内存地址，是一样的。
# self就是对象本身，类实例化之前我们不知道具体的对象是谁，就用slef来表示对象本身。

# 实例属性和类属性、实例方法和类方法
# 实例属性，通常写在初始化方法中，如self.name = name。使用类名().属性名调用
# 类属性，写在类名下方，所有实例可以共享，不属于任何实例特征。可以直接使用类名.属性名调用；也可以使用类名().属性名调用
# 实例方法：需要传入self的方法都是实例方法。
# 类方法：装饰器@classmethod 参数是cls 表示类本身
# 一般与实例没有关系的属性和方法，才会写成类属性和类方法
# 类属性和类方法，了解即可，目前只有单元测试时会看到，其他暂时用不上。静态方法暂时也用不上。
# 以后做框架或者做测试开发，主要还是用实例方法和实例调用方式。

# 私有属性和私有方法
# _private_method 私有方法；类和子类的对象可以访问，提供api给你访问。
# __private_method_deep 深度私有；只有类的对象可以访问。
# 在类的内部，可以通过self访问
# 在类的外部，可以强行访问，但是最好不要这样做。类的内部可以提供访问的方法，类的外部通过调用该方法访问私有。

# ---老师的笔记---

# 封装  类=属性+行为   抽像 -
class StudentV2:

    # 类属性  所有的实例可以共享 。不属于任何实例的特性。
    is_people = True

    # 类方法  1、装饰器。2、参数是cls 表示类本身。
    @classmethod
    def pepole_aciton(cls):
        print("吃饭，睡觉！！")
        print(cls.is_people)


    # 初始化工作
    def __init__(self,name,stu_id,class_name,city="上海"):
        self.name = name   # 实例属性
        self.stu_id = stu_id
        self.class_name = class_name
        self.city = city
        self._protect_friend = "鸡腿"
        self.__private_money = 500
        print("初始化工作完成，我已经有了具体的名字、学号、班级、城市这四个属性。")

    # 行为  self就是我，我就是self。 类实例化之后，明确我是谁。
    def attend_course(self):
        # 300行  拆成四个小功能
        self._private_func()
        print("{}正在学习类和对象。".format(self.name))
        return

    def _private_func(self):
        pass
    def __private_func_deep(self):
        pass

    # 开放api，获取私有变量值。
    def get_counts(self):
        print("我有{} 个 {}".format(self.__private_money,self._protect_friend))


# 类属性的调用
# print(StudentV2.is_people)
# # print(StudentV2.name)  # 类是没有name属性
# StudentV2.pepole_aciton()

luoluo = StudentV2("罗罗","222222","python17","北京")
# print(luoluo.is_people)
# print(luoluo.name)
# print(luoluo._protect_friend) # 私有变量可以被外部强行访问
# print(luoluo.__private_money)  # 会报错
# print(luoluo._StudentV2__private_money)  #深度私有变量，改变了访问方式，才可以强行访问
luoluo.get_counts()


