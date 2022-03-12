#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 2-3
import requests

'''
对HTTPRequest进行改造
改造需求：
1.实现自动报错cookies,传递cookies
2.一次实例化，完成多个请求

改造需求二：
与配置文件结合
'''
from interface.interface_demo.common import config


class HTTPRequest:
    cookies = None

    def request(self, method, url, data=None, headers=None):
        url = config.config_handler.config_parser.get("api", "pre_url") + url  # 完成拼接
        method = method.upper()
        resp = None
        if method == "GET":
            resp = requests.get(url, params=data, cookies=self.cookies, headers=headers)
        elif method == "POST":
            resp = requests.post(url, data=data, cookies=self.cookies, headers=headers)
        else:
            print("不支持该请求类型，请确认您的请求方式是否正确！")
        if resp.cookies:  # 判断响应cookies不为空，则存放在类属性cookies里面
            self.cookies = resp.cookies
        return resp


# 实例化一次，可以实现多个请求
# （以前实例化一次，只能实现一个请求）
if __name__ == "__main__":
    http_request = HTTPRequest()
    # 登录接口
    url = "http://test.lemonban.com/futureloan/mvc/api/member/login"
    data = {"mobilephone": "15814447890", "pwd": "123456"}
    resp_login = http_request.request("get", url, data)
    print(resp_login.text)

    # 充值接口
    url = "http://test.lemonban.com/futureloan/mvc/api/member/recharge"
    data = {"mobilephone": "15814447890", "amount": "100"}
    resp_register = http_request.request("post", url, data)
    print(resp_register.json())
