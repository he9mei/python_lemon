#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 2-1
import requests


class HTTPRequest:
    def __init__(self, method, url, data=None, cookies=None, headers=None):
        method = method.upper()
        if method == "GET":
            self.resp = requests.get(url, params=data, cookies=cookies, headers=headers)
        elif method == "POST":
            self.resp = requests.post(url, data=data, cookies=cookies, headers=headers)

    def get_status_code(self):
        return self.resp.status_code

    def get_text(self):
        return self.resp.text

    def get_json(self):
        return self.resp.json()

    def get_cookies(self):
        return self.resp.cookies

    def get_headers(self):
        return self.resp.headers


if __name__ == "__main__":
    # 登录接口
    url = "http://test.lemonban.com/futureloan/mvc/api/member/login"
    data = {"mobilephone": "15814447890", "pwd": "123456"}
    request = HTTPRequest("get", url, data)
    # print(request.resp.text)
    print(request.get_text())

    # 充值接口
    url = "http://test.lemonban.com/futureloan/mvc/api/member/recharge"
    data = {"mobilephone": "15814447890", "amount": "100"}
    request = HTTPRequest("post", url, data, cookies=request.get_cookies())
    print(request.get_json())








