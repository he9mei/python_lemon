#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
类和对象4
# 继承
'''

# ----老师的笔记---

# 1.1继承
# 你的是我的，我的还是我的
# 继承 - 完全继承。

class Animal:

    def __init__(self,name,private_v1):
        self.name = name
        self._private_v1 = private_v1   # 父类私有变量
        self.__private_v2 = "private_really"   # 父类深度私有变量

    def run(self):
        print("跑！！")

# a = Animal("cat")
# 狗 啃骨头
# class 子类名(父类名)   # Animal 基(base)类  Dog 多个派生类
class Dog(Animal):

    def __init__(self,name,kind):
        self.name = name
        self.kind = kind


    def eat(self):
        print("一只名叫 {} 的 {} 在啃骨头".format(self.name,self.kind))

    def run(self):
        print("我是一条狗，我有四条腿跑！！")

# 实例化
# dog = Dog("二狗")
dog = Dog("二狗","哈士奇")
dog.run()
dog.eat()


# 1.2继承-重写
# 父类：关闭修改、开放扩展
# 重写 和父类的方法名称一样。但是在子类里面，重新实现。
# 子类呢，需要父类里现有的功能，但是要在这个功能之外，还在再扩展。super  超级
# super   - 超类  父类
# 重写(第1种是完全重写、第2种是扩展(super) ) -- 前提：子类和父类函数名称是一样的。
# 1.3 私有继承
# 私有化的继承 _ 子类可以使用  __不对子类开放

# 狗 啃骨头
# class 子类名(父类名)   # Animal 基(base)类  Dog 多个派生类
class DogV2(Animal):

    def __init__(self,name,kind,private_v1):  # self是子类的实例对象
        # self.name = name
        # Animal.__init__(self,name)  # 父类的实例  子类的实例对象也是父类的实例对象
        super().__init__(name,private_v1)  # 调用父类现成的方法  # super()这种用法必须掌握
        # 方法二
        # super(DogV2,self).__init__(name)   # 不要求掌握

        self.kind = kind  # 扩展子类的特性

    def eat(self):
        print("一只名叫 {} 的 {} 在啃骨头".format(self.name,self.kind))

    def run(self):  # 完全颠覆父类的做法
        # super().run()
        print("我是一条狗，我有四条腿跑！！")
        print(self._private_v1)  # 父类的_私有可以调用；
        # print(self.__private_v1)  #父类__深度私有子类不可以访问

    def play(self):
        self.run()


#hsq = DogV2("小白","二哈")
#hsq.run()


# 1.4 isinstance类型判断
# 我们判断类型有两种方式：type()返回类型和isinstance()返回布尔值
# 语法：
# isinstance(实例对象,类)  # 谁是谁的实例。
# isinstance(实例对象,(类1,类2))
#print(isinstance(hsq,DogV2))  # hsq是DogV2实例来的
#print(isinstance(hsq,Animal))  # hsq也是父类Animal的实例
#print(isinstance(hsq,(Animal,DogV2)))

# 基本数据类型，如list,str,dict也可以用isinstance判断
mylist = [1,2,3]  # type
print(isinstance(mylist,list))


# 2.多继承---用的不多
# 人(super)  学生(init)   员工(init)  # 菱形继承 super
class Student:
    def study(self):
        print("我是学生，我爱学习，我爱柠檬班")


class Employee:
    def work(self):
        print("我要赚钱，我要工作，我爱工作！！")

class People(Student,Employee):

    def do_something(self):
        self.work()
        self.study()

    def work(self):
        pass

p = People()
p.do_something()


# 3.issubclass   子类
# issubclass(子类,(父类1，父类2....))
print(issubclass(People,Student))
issubclass(People,Employee)
issubclass(People,(Student,Employee))

# 总结  object是所有类的基类-py2中需要明确写出；py3不需要写
# 继承 - 完全继承，除了__开头的属性和方法之外，子类拥有父类的一切。
# 你的是我的，我的还是我的。
# 继承之后，在子类里可以像调用自己属性和方法一样，来调用父类的属性和方法。self.XXX

# 在完全继承之后，定义子类的特性。

# 如果你想对父类原有的行为进行改造、优化、扩展。可以重写父类的行为。
# 重写的要求：行为名称与父类的行为名称一样。
# 重写的两种方式：1、完全颠覆   2、保留父类的做法，在它的基础上再扩展其它的内容。
# 扩展方式来说：super - 超类。
# 子类当中，super的2种表达：super().方法(参数列表)
# super(子类名，self).方法(参数列表)

# isinstance(实例对象名,类名)
# issubclass(子类，父类)

# 多继承 - 可以有多个父类。
# 子类名(父类1，父类2....)

# 从excel操作 - 测试数据操作





