#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests

'''

'''
# 注册接口
# 1.先设计测试用例写到excel
url = "http://test.lemonban.com/futureloan/mvc/api/member/register"
data = {"mobilephone": "18500000001", "pwd": "123456", "regname": "小可爱"}
headers = {"Content-Type": "application/x-www-form-urlencoded"}
resp = requests.post(url, data=data, headers=headers)
print(resp.text)
# 2.读取excel
# 见do_excel.py文件
