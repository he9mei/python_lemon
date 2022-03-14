#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
1.a接口参数需要b接口返回拿到，如果实现参数的传递？
用cookies传递的方式可以吗？

2.关于用户信息
根据用户角色准备一套数据，如果需要切换环境，则需要多套数据
如：
管理员--加标、审核
投资人---充值、投资、体现
借款人---借款
每个角色统一使用一个用户即可
问题：
我们之前参数化是用的找到再替换的方法。但是如果太多了，这样做太麻烦了。
引入新的知识点：正则表达式
'''

import re   # 引入正则模块
from interface.interface_demo.common.config import config_handler

# 正则表达式：(如果要检测表达式写的是否正确可以百度搜正则在线编译器)
# 原义符+元字符
data = '{"mobilephone": "#user#", "pwd": "#pwd#"}'   # 怎么才能更容易找到？加上标志
# 写一个正则表达式（需要记住常用的元字符和限定符）
# p = "#.#"  # 只能匹配一个字符，所以a.c能找到，但是多个字符找不到
# p = "#.*#"  # 需要加上限定符。不加?需要匹配多次时，会最大范围匹配。 # {"mobilephone": "18500000000"}
# p = "#.*?#"  # {"mobilephone": "18500000000", "pwd": "18500000000"}
p = "#(.*?)#"   # 加上()就是加组group
# 编译成这个pattern对象
pattern = re.compile(p)
# 通过patter对象去查找，找到返回match对象，没找到返回None
# match是从开头开始找；search是从任意位置开始找（这里match找不到任何东西，因为开头不是#）
match = pattern.search(data)   # search任意位置开始找，找到一个就返回
print(match)   # <re.Match object; span=(17, 23), match='#user#'>
print(match.group(1))  # user  传参，就返回指定组匹配字符
print(match.group())   # #user# 不传参返回全部
all = pattern.findall(data)  # findall找到全部，返回列表
print(all)  # ['#user#', '#pwd#']

# 替换
# sub第一个参数是替换的值，第二个参数是目标字符串)
# sub会重新生成一个新的字符串；
# sub是全部找到;可以通过count值控制替换几次
user = '18500000000'
pwd = '123456'
# new_data = pattern.sub(user, data)  # {"mobilephone": "18500000000", "pwd": "18500000000"}
new_data = pattern.sub(user, data, count=1)  # {"mobilephone": "18500000000", "pwd": "#pwd#"}
new_data = pattern.sub(pwd, new_data, count=1)  # {"mobilephone": "18500000000", "pwd": "123456"}
print(new_data)

while pattern.search(data):
    print(data)
    key = pattern.search(data).group(1)  # 拿到参数化的key
    value = config_handler.config_parser.get('userdata', key)   # 根据key拿到value值
    data = pattern.sub(value, data, count=1)

print(data)

# {"mobilephone": "#user#", "pwd": "#pwd#"}
# {"mobilephone": "18500000000", "pwd": "#pwd#"}
# {"mobilephone": "18500000000", "pwd": "123456"}
