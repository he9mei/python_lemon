#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
1.安装
安装python3.7和pycharm
配置环境变量：（安装时，勾选了环境变量配置，跳过此步骤）
（1）配置python.exe路径
将Python的安装目录配置到环境变量的path当中；
（2）配置pip.exe路径
pip命令在python目录下的script目录中，后续使用pip按照第三方库。

创建project时，需要选环境，不要选虚拟环境。
package和文件夹的区别在于：package会生产__init__.py文件
python中，单引号和双引号没有任何区别。三引号可以用于单行和多行输出，也可以用于多行注释。
引号都要成对出现。
Python中，换行代表语句结束，不需要分行。
Python中，不要随便缩进，特定场景才会缩进。

settings---editor---file encodig: utf-8
settings---editor---file and coding template---python script:
#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Name: ${NAME}
# Auther: ${USER}
# Time: ${DATE}

'''

print('hello world!')
print("hello world!")
print('''hello world!''')
# "D:\Program Files\Python38\python.exe" C:/Users/lipan/PycharmProjects/python_lemon/basic/basic1_1base.py
# hello world!
# 也可以直接在cmd輸出：
# -->python C:/Users/lipan/PycharmProjects/python_lemon/basic/basic1_1base.py

# 编写代码时一行写不下时，回车换行写，但是输出不换行（老师这里一行结尾用了\，实际编译不过）
print('hello world-----------'
      '换行了'
      'lalalalala')
# hello world-----------换行了lalalalala

# 单行注释 快捷键ctrl+/
'''
三个单引号多行注释
'''
"""
三个双引号多行注释
"""
print('''
111
222
333
''')

'''
标识符  就是名字，如：变量名、函数名、类名、文件名等
什么是变量？ 
存储数据的，可以理解为储物柜、购物篮等
语法 变量名 = 具体的数据即变量值

变量的命名规则？
1.字母、数字、下划线组成
2.不能以数字开头
也不要以下划线开头（下划线开头是有特殊意义的）
变量名一般以字母开头（类与对象除外）
3.见名知义
4.不要以关键字作为我自己定义的任何
（内置函数、内置模块、第三方库名称）
5.区分大小写 Person和person不是同一个变量
变量一般都是小写

变量怎么引用?  以后函数、类、自动化框架都会用到
'''
# 如果查看关键字？
import keyword
print(keyword.kwlist)

'''
数据类型：
1.字符串 String 缩写str 同时str是关键字
2.数字：整数和浮点数 关键字int float
3.布尔值boolean：True False 都是关键字，首字母大写
4.可变的数据类型：列表list、字典dict  支持增删改查
5.元组tuple（不可变）：支持查

type函数功能：识别数值的数据类型
'''
str_a = 'aaa'
int_a = 99
float_a = 99.999
print(type(float_a))  # <class 'float'>
bool_a = True
bool_b = False
print(type(bool_a))  # <class 'bool'>
