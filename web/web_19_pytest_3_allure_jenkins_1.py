#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
web-第5周-第3节课-1 对应web_po_v5
html报告:
可以统计执行通过、失败、跳过等状态；
可以查看错误时的控制台输出和日志；
可以根据执行结果、用例、执行时间排序；---可以利用执行时间排序，找到执行事件最长的10个用例，进行调优。

一、allure报告：
官网：https://docs.qameta.io/allure/#_pytest
1、安装
（1）先安装allure软件
# https://docs.qameta.io/allure/#_installing_a_commandline
# 手动安装，并配置环境变量
# 2.1.4. Manual installation
# Download the latest version as zip archive from Maven Central.
# Unpack the archive to allure-commandline directory.
# Navigate to bin directory.
# Use allure.bat for Windows or allure for other Unix platforms.
# Add allure to system PATH.
# 问题：Maven Central页面报错

直接下载zip文件：
https://dl.bintray.com/qameta/maven/io/qameta/allure/allure-commandline/2.13.0/allure-commandline-2.13.0.zip
解压到E盘，到bin目录下找到allure.bat
配置环境变量：
ALLURE_HOME E:\allure-2.13.0
path加入：%ALLURE_HOME%\bin

（2）再安装pytest的allure插件
-->pip install allure-pytest
(pip提示升级-->python -m pip install --upgrade pip)
安装完成
 pyparsing>=2.0.2 in d:\program files\python38\lib\site-packages (from packaging->pytest>=4.5.0->allure-pytest) (2.4.7)

2、使用
-->pytest --alluredir=/tmp/my_allure_results  # 生成报告
-->allure serve /tmp/my_allure_results  # 打开报告
自己补充：转换为index.html文件---转换后不用每次命令打开，直接打开即可
-->allure generate ./report/allure_result/ -o ./report/allure_report/ --clean
或者
-->allure generate ./report/allure_result/ -c -o ./report/allure_report/

3、allure报告讲解
平时没有注意的点：
时刻表，可以拖动，可以看某个时刻跑了哪些用例；
如果没有jenkins集成，没有趋势图、没有执行器；
test defects---测试用例本身的问题
功能---也可以按照执行时间排序；点击切换展示某类型（如通过的用例）再点击不展示
图表---执行时间范围划分

二、jenkins集成
Jenkins插件安装，jenkins可以在线安装插件，
也可以离线安装，
下载：百度搜索“jenkins allure plugin index”，点击Index of /jenkins/plugins/allure-jenkins-plugin/
    即可看到下载列表，下载最新的即可 http://mirrors.xmission.com/jenkins/plugins/allure-jenkins-plugin/

安装：到manage jenkins-advanced-upload plugins，Jenkins插件文件后缀都是.hpi


# 进度：web-第5周-第3节课-1 45分钟
# jenkins插件已下载，未安装；本地Jenkins未配置

'''