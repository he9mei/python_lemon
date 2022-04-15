#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
1.首先新建一个配置文件，conf或者ini结尾，配置文件的格式如下：
[student]
name=小黑
age=16
sex=girl

[student]---section,是标签的符号，里面是标签名
name,age,sex---options
右边的值就是value

那么我们如何对这个配置文件进行读取？需要利用Python自带的ConfigParser
掌握一些基础用法：【跟file一样，要先打开才能进行读取操作】
1）实例化ConfigParser对象：cf=configparser.ConfigParser()
2) 打开配置文件；cf.read(配置文件的地址和名称)  # 返回文件名列表
3）获取我们的标签名：cf.sections() #返回的数据类型是列表
4) 获取options: cf.options(section_name)
5) 获取键值对items：cf.items(section)  # 得到该section的所有键值对，列表相形式返回
6) 获取到某个具体的值
<1>.get(section,option)   # 得到section中option的值，返回为str类型
两种具体获取方式：
cf.get('section_name','option_name')
cf['section_name']['option_name']
<2>getint(section,option)   #得到section中option的值，返回为int类型
还有cp.getboolean()、cp.getfloat()
问题：如果存入的是列表或者字典怎么办？
    用eval()函数从str恢复其原本的类型
'''

import configparser

cp = configparser.ConfigParser()
# fs = cp.read('data.conf',encoding='utf-8')
# print(fs)  # ['data.conf']

cp.read('data.conf',encoding='utf-8')

print(cp.get('student','name'))
print(cp.getint('student','age'))
print(cp.getfloat('student','weight'))
print(cp.getboolean('testdata','res'))

dict_data=cp.get('testdata','data')
print(dict_data,type(dict_data))
dict_data=eval(dict_data)  # str转dict
print(dict_data,type(dict_data))
list_name=cp.get('testdata','list_name')
print(list_name,type(list_name))
list_name=eval(list_name)    # str转list
print(list_name,type(list_name))

print(cp.sections())
print(cp.options('student'))
print(cp.items('student'))

'''
小黑
16
52.52
True
{'mobile':'11850000000','pwd':'111111'} <class 'str'>
{'mobile': '11850000000', 'pwd': '111111'} <class 'dict'>
['huahua','xiaojian','jsckson'] <class 'str'>
['huahua', 'xiaojian', 'jsckson'] <class 'list'>
['student', 'testdata']
['name', 'age', 'sex', 'weight']
[('name', '小黑'), ('age', '16'), ('sex', 'girl'), ('weight', '52.52')]
'''