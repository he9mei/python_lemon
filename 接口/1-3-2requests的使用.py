#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
2.requests模块
属于第三方模块，需要安装插件
-->pip install requests
'''

import requests

# get请求
url = "http://test.lemonban.com/futureloan/mvc/api/member/login"
data = {"mobilephone": "15814447890", "pwd": "123456"}
resp = requests.get(url, params=data)
print("响应码：{}".format(resp.status_code))
print("响应头：{}".format(resp.headers))
print("响应文本：{}".format(resp.text))
print("响应文本json：{}".format(resp.json()))
print("响应头中的cookie：{}".format(resp.cookies))   # <RequestsCookieJar[]>  # 目前没有cookie

# 响应文本和响应文本json有什么区别？返回的类型不同
print(type(resp.text))  # <class 'str'>
print(type(resp.json()))   # <class 'dict'>
# 如果要提取status等字段的值做断言，用json更方便
print(resp.json()['status'])   # 0

# get请求会直接把参数拼接在url
# 可以不传参数，直接把参数拼在在url吗？可以
# 也就是get有两种传参方式：
# 1是直接拼接在url中path？para1=value1&para2=value2的格式
# 2是get方法的params传入字典，参数放在字典中
print(resp.request.url)  # http://test.lemonban.com/futureloan/mvc/api/member/login?mobilephone=15814447890&pwd=123456

cookies = resp.cookies  # 登录接口返回的cookies

# post请求
url = "http://test.lemonban.com/futureloan/mvc/api/member/recharge"
data = {"mobilephone": "15814447890", "amount": "100"}
resp = requests.post(url, data=data, cookies=cookies)
print(resp.json())

# 接口好像有问题了，没有传cookie也充值成功了
# 正常的流程应该是登录接口拿到cookie再当做参数传给充值接口
# 之后讲了post调用的request函数参数的传入
# （可以百度requests,查看使用文档，查看里面的高级用法）
# https://docs.python-requests.org/zh_CN/latest/

