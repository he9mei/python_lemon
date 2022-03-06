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

# 2.如果我们现在要判断接口的请求方式是否正确，所有接口都需要判断。
# 我们需要写一个类。HTTPRequest
# 见http_request.py文件

'''
3.接口文档
接口文档包含的信息：
接口名称、接口地址、请求方式、
请求参数（参数名、类型、参数说明、是否必须等）、
结果说明（参数名、类型、参数说明，如status、返回码code）、返回示例等

返回值-返回码code-服务器异常需要测试吗？不需要。自动化的前提是稳定的环境。

 4.用例的设计
一个类一个接口（方便维护易于理解）
一个测试点一个方法
（比如非必传，可以在一个用例中测试所有非必传参数）

接口自动化实际就是测试i/o
接口用例设计，就是不同参数的组合来设计，根据功能逻辑来设计
比如注册接口
1.注册成功
2.手机号已被注册
3.手机号格式不正确
3个用例的流程一样：传参、请求、响应、断言
可以进行数据驱动，参数化
测试数据当到哪里？怎么维护？
1.配置文件:数据库连接数据、共用的环境数据、公共数据如日志的级别配置
2.文件类：excel/CSV/json/xml/yaml
（测试用例，见老师写的excel用例。其他格式也可以。
但是参数很多时建议使用exxcel+json的形式，把参数单独写出来，这里写地址，需要自己实现。）
3.数据库：表，数据量超大的时候

作业：
1.用excel写用例
2.写一个类读取excel中的用例
'''

