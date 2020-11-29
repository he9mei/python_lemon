#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
app_第1周—第1課_2
1.原理
pc端python代码--->Chromedriver.exe--->Chrome浏览器
客户端python代码-->appium server-->模拟器/真机
appium server和chromedriver.exe的作用一样，都是一个中间通信人。
环境安装
第1步：客户端python代码-->appium server === 通过HTTP通信，需要node.js、appium server、appium的python插件
第2步：appium server-->模拟器/真机 === 通过adb连，需要jdk环境、安装开发工具ADT、模拟器
        Android/iOS系统自带自动化框架api
        appium是js写的，Android是java写的/iOS是Object c写的，可以直接通信吗？
        实际上，是往模拟器/真机传了一个jar包，会与appium服务器实时通信，是这个jar包在调用系统自带自动化框架api。
        这个过程是tcp通信
移动端自带框架
iOS9.3及以上：苹果XCUITest
Android4.2及以上：谷歌UiAutomator
提问：为什么不直接使用移动端自带的自动化框架？
原因：以Android为例
1）必须学习java代码，熟悉UiAutomator的api
2）需要把写好的Java测试代码放到手机上，才能调用UiAutomator的api

具体原理下节课会再讲。
小简老师博客：https://www.cnblogs.com/Simple-Small
歪歪老师博客：https://www.cnblogs.com/yyoba

'''