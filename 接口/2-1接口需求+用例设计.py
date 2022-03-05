#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests

'''
# 1.requests模块复习

# 如果返回的响应文本不是json字符串，可以调用接json()函数吗？会报错。JSONDecodeError
# url = "http://www.baidu.com"
# resp = requests.get(url)
# print(resp.text)
# print(resp.json())

# post请求，如果把参数放在url可以吗？可以。只是不符合规范

# headers使用
# 如果出现乱码，可以在headers里面设置
url = "http://test.lemonban.com/futureloan/mvc/api/member/register"
data = {"mobilephone": "18500000000", "pwd": "123456", "regname": "小可爱"}
headers = {"Content-Type": "application/x-www-form-urlencoded"}
resp = requests.post(url, data=data, headers=headers)
print(resp.json())
# {'status': 0, 'code': '20110', 'data': None, 'msg': '手机号码已被注册'}

'''

# 2.如果我们现在要判断接口的请求方式是否正确，所有接口都需要判断。我们需要写一个类。---22分钟
