#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests

'''

'''
# 注册接口
# 1.先设计测试用例写到excel，如注册接口、登录接口
url = "http://test.lemonban.com/futureloan/mvc/api/member/register"
data = {"mobilephone": "18500000001", "pwd": "123456", "regname": "小可爱"}
headers = {"Content-Type": "application/x-www-form-urlencoded"}
resp = requests.post(url, data=data, headers=headers)
print(resp.text)

# 2.读取excel并写入实际结果和断言结果
# 见do_excel.py文件
# 实际基本的用例执行

# 3.搭建框架
# 分层---数据层、用例层、逻辑层（用3个package）
# 使用unittest框架
# 新建包interface_demo
