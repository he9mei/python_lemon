#!/usr/bin/python3
"""
@File    : main.py
@Time    : 2019/8/12 16:16
@Author  : 柠檬班-小简
@Email   : lemonban_simple@qq.com
@Company: 湖南省零檬信息技术有限公司
"""

# 1、获取当前连接的所有设备
# 2、获取每一个设备的平台信息
# 3、获取app的信息 - app固定存储在某一个目录下面。去指定目录下面取apk
# 4、根据每一个设备，启动一个appium server。并启动会话

from app.app_muti_devices.threading.adb import ADB
from app.app_muti_devices.threading.appium_server import *
from threading import Thread
import time
# 设备平台信息
a = ADB()
a.get_all_device_info()
# [{'device': '08e7c5997d2a', 'platform_version': '8.1.0'}, {'device': 'emulator-5554', 'platform_version': '5.1.1'}]
print(a.devices_info_list)

# app信息
# D:\1-课件目录\app自动化-appium\app包\lemon_app_webview_debug.apk
apk_path = r"D:\1-课件目录\app自动化-appium\app包\lemon_app_webview_debug.apk"
app_info = a.get_app_package_and_activity(apk_path)
print(app_info)
# 起始端口叼
port = 4723
# 根据设备数，启动对应个数的appium server  --- 多线程
for dev_info in a.devices_info_list:
    print(port)
    th = Thread(target=start_appium_server,args=(port,))  # 启动appium server
    th.start()
    time.sleep(2)
    th2 = Thread(target=start_appium_session,args=(dev_info,app_info,port))  # 启动appium会话
    th2.start()
    port += 3





