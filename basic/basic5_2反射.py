#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
反射

反射机制是什么？
通过字符串--找到对应函数，并执行它。
通过字符串---对对象中的成员进行操作（查找、获取、删除、添加）
基于字符串的事件驱动

针对实例对象
hasattr(对象，'属性名或者方法名')
    ---判断对象有没有这个方法。返回布尔值
getattr(对象，'属性名或者方法名')
    ---获取对象的属性。传入属性名返回的是属性值，传入方法名返回的是方法的内存地址
setattr(对象，'属性名','属性值')
    ---动态添加对象的属性
delattr(对象，'属性名或者方法名')
    ---删除对象属性

'''


# ---老师的笔记---

mydict = {"name":"python","class":17}
#
mydict.keys()
mydict.values()

# 类和对象：类=属性+行为
# 判断对象有没有这个方法
has = hasattr(mydict,"keys")  # has attribute 有属性  # AttributeError:
print(has)

class Stu:
    # 初始化工作
    def __init__(self, name, stu_id, class_name, city="上海"):
        self.name = name  # 实例属性
        self.stu_id = stu_id
        self.class_name = class_name
        self.city = city
        self._protect_friend = "鸡腿"
        self.__private_money = 500
        print("初始化工作完成，我已经有了具体的名字、学号、班级、城市这四个属性。")

    # 行为  self就是我，我就是self。 类实例化之后，明确我是谁。
    def attend_course(self):
        # 300行  拆成四个小功能
        print("{}正在学习类和对象。".format(self.name))
        return

s = Stu("xj","11","py17")
# hasattr
print(hasattr(s,"name"))
print(hasattr(s,"attend_course"))
# 获取对象的属性  getattr
print(getattr(s,"name"))
print(getattr(s,"attend_course"))
print(getattr(s,"attend_coursesss")) # 报错：属性不存在
print(getattr(s,"attend_coursesss","没有找到对象对应的方法"))  # 加上默认值就不会报错

# 添加对象的属性 setattr
setattr(s,"age",18)
print(s.age)
# s.class_name = "py16"

# 删除 delattr
# delattr(s,"class_name")
# print(s.class_name)

aa = Stu("二狗","222","py17")
print(aa.class_name)
print(aa.age)  # 报错：属性不存在



