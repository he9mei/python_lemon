#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
之前学习的知识总结：

1、基础语法
2、数据类型：
   字符串、数字、布尔值、字典、列表、元组
   str  int float  boolean  dict list tuple
   len()
   字符串操作：find\strip\split\replace\join\
   字典操作：赋值、更新键值对、添加键值对、读取   key是唯一，不可变的。 {}
             keys()  values()  items()
   列表操作：取值、修改值、插入值、追加值  []
   元组操作：读取  ()

   可变类型：字典、列表

3、运算符：
   算术运算符
   赋值运算符  =   +=  -=
   比较  ==  !=   <= >= < >
   成员  in    not in
   逻辑运算  and  or  not
   XXx is True
   XXX is not None
   XXX is False

4、控制流：判断和遍历
   if XXX：
      *****
   elif XXX:
      ***
   else:
      ***

   while  设置退出循环的条件。 在while内部，能够使条件达到不满足的满足。
   while 条件：
       条件成立时干的事儿。
       一定要有：条件不成立时，退出while。  break
       一定要有：改变条件，导致条件不成立。

   for： 从头到尾，都要去访问一下。每一个元素，都要去干点啥。
         当我们要对列表当中每一个元素，都要做同样的逻辑处理的时候。
   # 列表
   第一种：直接取值
   for item in list:
        每一个元素，都要去执行的代码。都要做的逻辑处理。

   第二种：遍历下标，通过下标取值。
   range(起始、终止、步长)   起始默认为0，步为默认为1. 不包含终止值。
   range(10)
   range(1,10)
   range(1,10,2)
   for index in range(len(列表))：
       每一个元素，都要去执行的代码。都要做的逻辑处理。

   # 字典
   # 通过键名
   for key in 字典.keys():
      每一个元素，都要去执行的代码。都要做的逻辑处理。
   # 直接取键值对
   for key,value in 字典.items():
      每一个元素，都要去执行的代码。都要做的逻辑处理。

   # 字符串、元组
   for item in [(1,2),(3,4),(5,6)]:


5、函数：
   实现了某一功能：功能尽量单一
   重复使用

   定义：
   def 函数名称([arg1,arg2,arg3....]):   # 函数名称都是小写，用下划线拼接
       函数体==实现函数功能的代码块
       [return [值]]

   # 参数  形参-占坑。定义的时候，用来接收数据的。实参-调用的时候，真正的实际数据。
   # 位置参数：形参与实参位置一一对应。1VS1
   # 默认参数：定义的时候，直接给形参赋默认值。默认值建议是不可变类型的数据。列表、字典等，不要设置为默认参数。
               定义的时候，要求默认值放在最后。
               调用的时候，可传可不传。
   # 指定参数：在调用的时候，形参=实参
              用的最多场景：当有多个默认值时候，想只传其中部分。
   # 可变参数：
              *args  不确定个数的值。在函数内部，以元组的形式呈现。
                     数值1，数值2
              **kwargs  不确定个数的键值对。在函数内部，以字典的形式呈现。
                     key1=value1,key2=value2

              两个一起用的时候，*args   **kwargs

   # return
   1、退出函数。函数调用函数。
   2、可以返回内部处理后的数据。输出。可以是任意类型的数据
   3、也可以不返回任何值。返回None
   4、如果函数里边没有return，函数默认返回None
   5、用变量主动接收函数的返回值。

# 调试 debug  F7 F8

6、 导入
   from 包名[.包名...] import 模块名 [as 别名]   # 以项目路径作为参照物。相对路径。
   import 模块名 [as 别名]

# 以下最近才学习，就不总结了，回看笔记。
7、os-文件系统
8、文件操作 - 读写
9、异常处理

'''