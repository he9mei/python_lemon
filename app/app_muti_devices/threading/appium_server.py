#!/usr/bin/python3
"""
@File    : appium_ser.py
@Time    : 2019/8/12 14:57
@Author  : 柠檬班-小简
@Email   : lemonban_simple@qq.com
@Company: 湖南省零檬信息技术有限公司
"""

# 命令行的形式启动appium desktop
# 找到appium desktop下的appium 服务启动文件　（appium安装路径下 resources\app\node_modules\appium\build\lib的main.js文件）
#　C:\Users\MyPC\AppData\Local\Programs\Appium\resources\app\node_modules\appium\build\lib
# 跳转到此目录下，运行命令：node main.js -p 端口号，则会启动一个appium。
# 查看所有参数：node main.js --help

import os
import subprocess
from appium import webdriver

# 启动appium server服务
def start_appium_server(port=4723):
    appium_server_path = r'C:\Users\MyPC\AppData\Local\Programs\Appium\resources\app\node_modules\appium\build\lib\main.js'
    command = "node {0} -p {1} -g D:\\appium_server_{1}.log".format(appium_server_path,port)
    os.system(command)

# for port in [5010,5013,5017]:
#     start_appium_server(port)

# 与appium建议连接，启动与appium的会话
def start_appium_session(device_info,app_info,port=4723,server_params=None):
    # 设备uuid得到平台版本号  # app信息
    desired_caps = {}
    desired_caps["platformName"] = "Android"
    desired_caps["platformVersion"] = device_info["platform_version"]
    desired_caps["deviceName"] = device_info["device"]
    desired_caps["appPackage"] = app_info["appPackage"]
    desired_caps["appActivity"] = app_info["appActivity"]
    desired_caps["noReset"] = True
    desired_caps["unicodeKeyboard"] = True
    # 其它的启动参数
    if server_params is not None:
        desired_caps.update(server_params)
    # 启动会话
    driver = webdriver.Remote('http://127.0.0.1:{}/wd/hub'.format(port),desired_caps)
    return driver
