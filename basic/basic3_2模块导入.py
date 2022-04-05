#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
模块导入
'''

# ---老师的笔记---

# 模块  .py文件就是模块。

# 想在当前py文件当中，调用其它模块里的函数

# 引入到当前文件当中，然后使用功能就好。

# 一、引入自定义模块(.py)
"""
引入的原则：相对路径  参照物：工程(project)名称对应的路径 。（---重点---）

包名 -> 包名 -> 模块名

from  从。。。。
import  导入 包/模块/变量
from  包  import 模块
"""
# 1、from  包[.包]  import 模块  #模块相对于工程的路径来说  #引入模块 （---常用方式1---）
# from class_20190418 import my_funcs
#
# print(my_funcs.class_name)
# my_funcs.eat()

from class_20190418.new_pack import my_model
print(my_model.my_model)

# 模块名有命名要求：
# 1、不要以数字、下划线开头、特殊符号。也不要以中文开头。
# 2、通常来说，都是以字母开头。
# 3、不要以关键字来命名、内置函数、内置模块、不要以第三方库来命名。

# 2、import 包名.模块名.类名 # import class_20190418.my_funcs---这种有问题，可以舍弃

# 3.import 模块名    # 在工程的根目录下 （---常用方式2---）
import my_func_two as tw
tw.minus()

# 给导入的模块 ，取个别名。
# from 包名 import 模块名 as 别名
# import 模块名 as 别名

# 如果是要将包下所有的模块引入 *
# from class_20190417 import *

# 二、第三方库的引入  包含内置的库、或者你要去额外安装的库。
# 固定好了的用法。
import os
# 内置的库在Python安装目录的lib目录下，自己安装的在site-package下
# 库一般存在形式有两种，一种是包（包含__init__.py的文件夹），一种是模块（即.py文件）

# 注意：
# 如果引入的模块中，有直接右键运行就能执行的代码，导入模块时，这些代码会自动执行
# 不过一般我们会导入具体的类或对象










