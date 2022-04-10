#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
异常处理
'''

# ---老师的笔记---
# 常见异常类型
# NameError    变量名找不到异常
# IndexError   下标越界异常
# KeyError   字典形式，键不存在异常
# AssertionError   断言异常。
# AttributeError  属性异常。对象的属性不存在。
# SyntaxError   语法错误
# IndentationError   缩进异常
# FileExistsError   文件存在异常，当要创建目录或者文件时
# PermissionError   权限异常。没有操作权限。

# mydict = {"key":"value"}
# print(mydict["hello"])


# 进一步对异常进行处理。出现了异常，我还要干啥干啥！
# 常用的两种模式：---重要
"""  模式一：
try:
    XXXX   # 认为这一段代码会出异常
except:
    捕获异常之后，我想自己干的事情。 # 写到日志里 #截图  
    raise   # 抛出异常。（可选；如果是必须要程序知道的异常，一定要抛出；如果不抛出，相当于异常被偷偷处理了，程序不知道）
finally: （可选）
    无论有没有出现异常，最终都会执行的代码。 # 收尾工作，比如关闭数据库连接、关闭文件等  
"""

"""  模式二：
try:
    XXXX   # 认为这一段代码会出异常
except:
    捕获异常之后，我想自己干的事情。 # 写到日志里 #截图  
    raise   # 抛出异常。
else: （可选）
    没有异常，接着try里的代码里，继续执行。  （这里的代码也可以写在try里面，但是这样写需要try的代码会更明确）
[finally:]
"""

# 实例1
# fs = None
# try:
#     fs = open("moviessss.txt",encoding="utf-8")
#     print(fs.read())
# except:
#     print("文件读取失败")
#     raise   # 抛出异常
# finally:
#     print("我是必定会执行的工作！！")
#     if fs is not None:
#         fs.close()

# print("我还会执行吗吗吗吗！！！")   # 如果异常没有抛出，这行代码还会继续执行

# 实例2
# try  except  else
str_a = input("请输入一个数字：")

try:
    b = int(str_a)
except:
    print("输入的数据不合格，非数字！！！")
else:
    print(b + 22)   # try没有异常的情况下
finally:
    print("heheheheh")


# 另外两种异常场景---不常用
"""模式3：
try：
    可能会出错的代码
except 具体异常类(KeyError):
    捕获异常后的处理
except 具体异常类(OSError):
    捕获异常后的处理
except 具体异常类(FileNotFoundError):
    捕获异常后的处理


模式四：
try：
    可能会出错的代码
except Exception as e:
    捕获异常后的处理
    print(e)
"""

# 文件打开异常处理方式二：上下文管理---常用，重要
"""
# 打开文件(无论有没有出现异常)，都会关闭文件对象。
with open() as fs:   ----可以代替try except finally处理
    # 没有出现异常的情况下，执行的代码。
    # fs 文件对象 fs = open()
"""
with open("write.txt",encoding='utf-8') as fs:
    datas = fs.read()
    print(datas)



