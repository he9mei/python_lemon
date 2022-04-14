#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
类与对象2
'''

# ----老师的笔记---

"""
总结：
类和对象：类是抽象的，一类事物的共性的体现。  有共性的属性和行为。
对象：具体化，实例化。有具体的属性值，有具体做的行为。
类 ---- N多个对象。

定义：
class 类名：
    # 属性 - 变量
    # 行为 - 函数
    def 行为1(self):
     # self是我 self是指的实例化对象本身。定义的时候不知道对象到底是谁，用self
     self.属性
     self.行为N

     # 初始化 - 在实例化的同时，执行初始化工作。没有return的用法。
     def __init__(self,[参数1，参数2.。])
        ### 初始化工作
        ###

# 具体化实例化
实例名 = 类名([参数1，参数2.。。])
# 通过实例名称来访问实例的属性、做行为
实例名.属性
实例名.行为
"""
import os


# 文件操作 -- 文件是一类事物。有读写关闭行为。
class FileOperator:
    # 属性 文件的编码、文件路径、文件类型
    # 行为  读所有内容、按行读所有内容、写入、关闭文件、追加
    # 有没有初始化工作？  打开文件。
    def __init__(self, file_path, acess_mode="r", encoding="utf-8"):
        # 标记
        # self.flag = 0
        # 判断文件要是不存在，咱就创建一个。
        if not os.path.exists(file_path):
            # 再判断目录不存在？-创建目录。文件不存在？-创建文件
            path, file = os.path.split(file_path)
            if os.path.exists(path) is False:  # 如果目录不存在，则创建目录
                os.makedirs(path)
            if os.path.exists(file_path) is False:  # 如果文件不存在，则创建文件
                with open(file_path, "w", encoding="utf-8") as fs:
                    fs.write("=======================================")
        try:
            self.fs = open(file_path, mode=acess_mode, encoding=encoding)
        except:
            print("打开文件失败")
            # self.flag = 1 # 这里只是学生的提议的一种通过标记的方式
            raise  # 实际我们是需要抛出的，抛出后之后的代码也不会执行了，所以不需要再判断

    # 行为1
    def read_all(self):
        return self.fs.read()

    # 行为2
    def read_all_by_line(self):
        return self.fs.readlines()

    # 行为3
    def write_data_to_file(self, data):
        self.fs.write(data)

    # 行为4
    def close_file(self):
        self.fs.close()


# 实例化
my_ope1 = FileOperator("read.txt")
data = my_ope1.read_all()
print(data)

# # 实例化2
# my_ope2 = FileOperator("datas.txt")
# contents = my_ope2.read_all()
# print(contents)
# my_ope2.close_file()
#
# # 实例化3
# my_ope3 = FileOperator("datas.txt","a")
# my_ope3.write_data_to_file("今天学的好开心啊，感觉又涨知识了！！")
# my_ope3.close_file()