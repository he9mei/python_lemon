#!/usr/bin/python3
# -*- coding: utf-8 -*-

# ---老师的笔记---

# pandas- 读取操作
# 配置文件
import configparser  # 引入方式一
cp = configparser.ConfigParser()

# from configparser import ConfigParser  # 引入方式二
# cp = ConfigParser()

# 加载文件
# cp.read()

# section   [section]
# 和option  key=value
# item  [(key,value),(key,value)]

# get 得到某个section下面的，某个option的值(value)
# 字符串、数字、bool、列表/字典
# get   getint   getbool   先get再eval

# 更改配置文件的。---基本不这样用
# 添加/删除section、添加/更改option的值。
# 它还有哪些方法？？？

# 类 --- 写写写写







