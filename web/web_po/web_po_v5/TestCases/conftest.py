#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 定义一个函数级别的fixture，一个函数=前置+后置
# 函数名称前面 @pytest.fixture

from selenium import webdriver
import pytest
import logging


# @pytest.fixture  # 默认是function，可以不写
# scope级别：function、class、module、session、package（未实现）
from web.web_po.web_po_v5.PageObjects.login_page import LoginPage


@pytest.fixture(scope="function")
def access_web():
    # 前置：打开浏览器，访问网页
    driver = webdriver.Chrome()
    driver.get("http://120.78.128.25:8765/Index/login.html")
    driver.implicitly_wait(10)
    print("===打开浏览器，访问网页===")  # 自己添加的log，便于观察调用情况---log还有问题，灭有显示，改成print
    # yield   # yield作用1-相当于对前置和后置做一个分隔===问题：其他函数以及测试用例要用driver怎么办？需要返回呀
    yield driver  # yield作用2-返回，有return的作用===分界线+返回值===如果返回多个值，返回元组
    # 后置：关闭浏览器
    driver.quit()
    print("===关闭浏览器===")


'''
总结：
在测试用例中使用fixture
（1）测试类或者测试用例前面加上 @pytest.mark.usefixtures("access_web") 
（2）如果fixture有返回值，且测试用例中要用到返回值，那么fixture的函数名=返回值，作为测试用例的参数传入使用。
'''


@pytest.fixture
def refresh(access_web):   # aceess_web就相当于driver，直接拿来用 # 如果access_web没执行，先执行access_web，再执行refresh
    yield   # 这个函数是后置刷新操作，没有前置，直接以yield分隔
    access_web.refresh()
    print("==刷新页面==")
'''
补充：
在调用refresh时，
如果access_web还没有调用，则会去调用一次access_web；
如果access_web已经调用了，则不会重复调用access_web。
'''


# 再练习一下session和module级别的前置和后置
# @pytest.fixture(scope="session", autouse=True)  # 自动使用打开，如果没有返回值，则不需要再调用
@pytest.fixture(scope="session")  # 作用域整个会话，需要返回值,直接传参即可。整个会话只会被执行一次。
def my_session():
    print("====session级别的前置====")
    yield 888
    print("====session级别的后置====")


@ pytest.fixture(scope="module")  # 不打开自动使用时，如果要在整个模块使用，且不使用返回值，则在py文件第1个用例调用就可以---自己理解
def my_module():
    print("====module级别的前置====")
    yield
    print("====module级别的后置====")


# (注意：这里login_web是function级别的，login_web需要用到access_web，所以access_web也需要改成function级别的)
# (以上根据具体情况而定，不一定就要一样，可以尝试下不同的情况，只要能做到兼容就可以)
@pytest.fixture(scope="function")
def login_web(access_web):
    # 前置-登录操作（登录成功场景）
    LoginPage(access_web).login(user="18684720553", pwd="111111")    # 这里的账号和密码也可以从TestDatas中取
    yield access_web
    # 后置
    print("---我的后置---")

'''
谁的前置先执行？谁的后置后执行? ---access_web
执行顺序：
access_web的前置
login_web的前置
---测试用例---
login_web的后置
access_web的后置
'''


