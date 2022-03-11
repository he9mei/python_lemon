#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 2-3
import requests

'''
对HTTPRequest进行改造
改造需求：
1.实现自动报错cookies,传递cookies
2.一次实例化，完成多个请求
'''


class HTTPRequest:
    cookies = None

    def request(self, method, url, data=None, headers=None):
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

