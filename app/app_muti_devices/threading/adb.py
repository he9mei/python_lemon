#!/usr/bin/python3
"""
@File    : adb.py
@Time    : 2019/8/12 11:14
@Author  : 柠檬班-小简
@Email   : lemonban_simple@qq.com
@Company: 湖南省零檬信息技术有限公司
"""

import os
import subprocess
import chardet

class ADB:

    def __init__(self):
        self.devices_info_list = []

    # 获取adb能识别的所有设备的uuid和平台版本号
    def get_all_device_info(self):
        self._get_devices_uuid()
        for device in self.devices_info_list:  # 遍历所有的设备，获取每一个设备的平台版本信息
            platform_version = self._get_device_platform_vesion(device["device"])
            device["platform_version"] = platform_version


    # 获取可识别的所有移动端设备信息
    def _get_devices_uuid(self):
        # 终端命令行命令。
        command = "adb devices"
        result = self._run_command_and_get_stout(command)
        device_list = result.split("\r\n")  # ['List of devices attached', '08e7c5997d2a\tdevice', 'emulator-5554\tdevice', '', '']

        for item in device_list:  # 遍历adb devices 输出的内容
            if item.find("\t") != -1:  # 获取设备信息
                temp = item.split("\t")
                if temp[1] == "device":  # 设备为可识别状态。有些可能是offline、unauthorized等。
                    self.devices_info_list.append({"device":temp[0]})  # 添加到设备uuid列表当中。
        print(self.devices_info_list)

    # 获取设备的安卓版本
    def _get_device_platform_vesion(self,device_uuid):
        command = "adb -P 5037 -s {} shell getprop ro.build.version.release".format(device_uuid)
        print(command)
        s = self._run_command_and_get_stout(command)
        return s

    # 执行命令行并获取返回值。
    def _run_command_and_get_stout(self,command):
        # 执行command的，并获取命令执行之后的输出数据。
        stdout, stderror = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE,shell=True).communicate()
        # 编码处理
        encoding = chardet.detect(stdout)["encoding"]
        result = stdout.decode(encoding)
        result = result.strip("\r\n")   # 去掉首尾的换行回车
        return result


    def get_app_package_and_activity(self,apk_path):
        # apk_apth 示例：D:\1-课件目录\app自动化-appium\app包\lemon_app_webview_debug.apk
        app_info = {}  # 应用包名和activity
        command = ("aapt dump badging {}".format(apk_path))
        s = self._run_command_and_get_stout(command)
        for line in s.split("\r\n"):  # 对命令执行后的每一行数据进行处理。
            # 获取包名信息
            if line.startswith("package: name="):  # 如果是以package开头的行，则本行包含了app 包名信息
                print(line)
                #item = line.split(" ")  # ['package:', "name='com.lemon.lemonban'", "versionCode='20181113'", "versionName='2.1.2'", "platformBuildVersionName='2.1.2'"]
                for item in line.split(" "):  # 根据空格进行截断。
                    if item.startswith("name="): # 截断后的数据，以name=开头表示有app 包名信息
                        print(item)  # name='com.lemon.lemonban'
                        app_info["appPackage"] = item.lstrip("name='").strip("'")  # com.lemon.lemonban
                        # print(item.split("=")[1].strip("'"))  # com.lemon.lemonban
            # 获取activity的信息。
            if "appPackage" in app_info.keys() and line.startswith("launchable-activity: name='{}".format(app_info["appPackage"])):
                print(line)
                for item in line.split(" "):
                    if item.startswith("name="):
                        print(item)  # name='com.lemon.lemonban.activity.WelcomeActivity'
                        app_info["appActivity"] = item.lstrip("name='").strip("'")  # com.lemon.lemonban.activity.WelcomeActivity
            # 如果获取到了包名和activity名，则退出循环
            if "appPackage" in app_info.keys() and "appActivity" in app_info.keys():
                break
        return app_info

# # 获取要执行应用的包名和入口activity
# def get_app_package_and_activity(apk_path):
#     command = ("aapt dump badging {}".format(apk_path))
#     s = run_command_and_get_stout(command)
#     for item in s.split("\r\n")


# # 获取所有的设备以及对应的平台版本信息
# devices_uuid = get_devices_uuid()
# for uuid in devices_uuid:
#     get_device_platform_vesion(uuid)


# s = "111111111111"
# s.startswith()
# s.lstrip()