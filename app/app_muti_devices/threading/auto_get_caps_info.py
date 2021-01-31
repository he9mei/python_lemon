#!/usr/bin/python3
"""
@File    : 1111.py
@Time    : 2019/8/17 10:33
@Author  : 柠檬班-小简
@Email   : lemonban_simple@qq.com
@Company: 湖南省零檬信息技术有限公司
"""
# 执行命令行并获取返回值。

import os
import subprocess
import chardet

def _run_command_and_get_stout(command):
    # 执行command的，并获取命令执行之后的输出数据。
    stdout, stderror = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE,shell=True).communicate()
    # 编码处理
    print(stdout)
    encoding = chardet.detect(stdout)["encoding"]
    result = stdout.decode(encoding)
    print(result)
    result = result.strip("\r\n")   # 去掉首尾的换行回车
    print(result)
    return result

def get_device_uuid_list():
    device_uuid = []  # 设备uuid
    cmd = "adb devices"
    res = _run_command_and_get_stout(cmd)
    device_list = res.split("\r\n")
    print(device_list)
    for de in device_list:
        if de.find("\t") != -1:
            temp = de.split("\t")
            if temp[1] == "device":
                print(temp[0])
                device_uuid.append(temp[0])
    return device_uuid  # 需要考虑为空的情况，应该抛出异常

# adb -P 5037 -s {} shell getprop ro.build.version.release
def get_platform_version(device_uuid):
    comand = "adb -P 5037 -s {} shell getprop ro.build.version.release".format(device_uuid)
    res = _run_command_and_get_stout(comand)
    return res

# 暂时只考虑单设备
# 获取appPackage和appActivity自己实现---1.固定路径放apk包 2.aapt命令结果解析

# 把获取到的信息整合，然后conftest.py再引用这边的数据
def basedriver():
    #
    pass
