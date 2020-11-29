#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
app_第1周—第2課
1.adb---Android调试桥梁
常用命令
adb devices
adb logcat
adb shell
adb pull 手机路径 电脑路径
adb push 电脑路径 手机路径
adb install path/package.apk
adb uninstall com.dangdang.reader
adb connect/disconect ---通过wifi进行手机连接---自行了解，扩展
adb kill-server ---终止adb服务
adb start-server ---启动adb服务，有问题时，与终止配合使用
adb shell pm list packages ---列出所有安装包
-f 列出所有apk路径和包名
-s 列出系统apk路径和包名
-3 列出用户apk路径和包名
aapt dump badging 本地apk全路径 ---通过apk文件来查看activity
adb shell dumpsys activity|findstr com.dangdang.reader |findstr LAUNCHER ---通过包名查看activity

举例：
-->adb shell
-->ls -l  ----查看所有文件夹
-->cd sdcard ---进入sd卡文件夹
-->cd Android
-->cd data
-->ls -l  ---可以看到这个目录下都是apk包名
补充：其实查看包名有更加简单的方式
-->adb shell
-->pm list package 或者 pm list package -3 （只显示第3方安装包）
注意：我们要pull或者push，如果在shell命令中，需要先退出shell。因为shell已经进入Linux系统，无法识别adb命令
退出shell使用exit
推送、拉取文件
-->adb pull /sdcard/android/data/com.dangdang.reader E:\test\dangdang\
-->adb push E:\mytest.txt /sdcard/mytest.txt

（老师给的adb shell dumpsys activity|find "mFocusdActivity"已失效，无结果）
然后老师用了另一种方法：
-->aapt dump badging 本地apk全路径

这里重新写一下我自己的查看pacakage和activity的方法：
--->adb shell pm list packages -3
--->adb shell dumpsys activity|findstr com.dangdang.reader |findstr LAUNCHER
结果中 cmp=com.dangdang.reader/.activity.GuideActivity
 .activity.GuideActivity即我们需要的activity

备注：adb shell monkey 单独练习下

2.appium实现第一个demo
（1）desires capabilities 启动参数
推荐查看appium官网英文文档：documents---write&run tests---desired capabilities
（2）具体实例见app_demo.py
from appium import webdriver

# 要在哪个平台对哪个设备哪个app进行操作？
caps = {
    "automationName": "UiAutomator2",
    # Appium也可以，不过获取toast存在一些问题（以往经验）；官方建议Android6.0以上使用UiAutomator2
    "platformName": "Android",
    "platformVersion": "10",  # 如果不知道也可以先随便写一个，报错时，appium日志会提示可用的
    "deviceName": "GEY6R20507024610",  # 根据官方文档，这个字段填写错误也没有关系，必须有，但是没有使用---未验证
    "appPackage": "com.dangdang.reader",
    "appActivity": ".activity.GuideActivity",
    "noReset": True
}

# 与appium服务器建立连接，并向appium传入启动参数
driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

（3）查看appium日志
要学会查看appium日志，在appium启动时可以进入advanced勾选Local Timezone和Log Timestamps给日志增加时间戳
appium的日志非常详细，每一个步骤都有。比如通过adb命令去获取设备版本、是否已安装启动配置中的安装包等。
确认启动数据没有问题后，会向设备push一个appium setting安装包，并判断是否已经安装。
[2020-11-29 05:35:59][AndroidDriver] Pushing settings apk to device...
[2020-11-29 05:35:59][ADB] Getting install status for io.appium.settings
[2020-11-29 05:35:59][ADB] Running 'C:\Users\lipan\AppData\Local\Android\Sdk\platform-tools\adb.exe -P 5037 -s GEY6R20507024610 shell dumpsys package io.appium.settings'
[2020-11-29 05:36:00][ADB] 'io.appium.settings' is installed
然后会回到首页，如果已经打开该APP会先关闭。
找到jar包,AppiumBoostrap.jar从电脑appium路径下push到手机中。
然后，socket通信已连接
之后就执行自动化操作指令
如果60s如果没有任何指令，也没有任务要执行，session就会关闭，socket通信也会关闭。
最后清清除session
'''
