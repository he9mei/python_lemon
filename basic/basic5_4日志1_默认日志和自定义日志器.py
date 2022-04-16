#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
一、logging是什么？作用是什么？
logging---是Python自带的一个日志模块。
它的作用主要有两个：
1.代替print，可以把大部分你想要进行调试的信息打印出来或者输出到指定文件。
2.可以对输出的调试信息分类输出，比如：DEBUG,INFO,WARNING,ERROR,CRITICAL 五个级别
DEBUG  调试用，比如对上一个结果进行打印确认没有问题，再执行下一步，有问题时更容易找到原因
INFO 正常流程打印信息
WARNING 警告，比如对于某些操作不建议这样用
ERROR 错误，比如打开文件时文件找不到
CRITICAL 重大错误，比如崩溃

我们最常用的是：info，error
# 日志的作用：记录了执行过程。程序干了什么，做了什么事情。

备注：如果是异常信息可以用logging.Exception('异常信息')打印全部异常报错信息

二、如何打印日志？
'''

# 标准库  - logging
import logging

# logging.debug("我是一条debug信息")
# logging.info('我是一条info信息')
# logging.error('我是一条error信息')
# logging.warning('我是一条warning信息')
# logging.critical('我是一条critical信息')
'''
执行结果：
ERROR:root:我是一条error信息
WARNING:root:我是一条warning信息
CRITICAL:root:我是一条critical信息

问题：为什么debug和info没有打印？
原因：需要设置显示的级别，来决定哪些日志需要输出。
默认的日志收集器rootLogger，默认显示的级别为warning
'''

# 自己定义日志器，我自己决定显示的日志级别
logger = logging.getLogger('py17')
# logger.setLevel("INFO")
logger.setLevel(logging.INFO)  # # 设置输出级别,这两种方式都可以

logger.info('我是一条info日志')
logger.error('我是一条error信息')
# 我是一条error信息
# 问题：单独执行以上两条，info还是不会输出？与最初版本的logging.*一起执行才会输出？
# 原因：没有指定任何输出渠道,就使用的默认输出渠道

# 想设置日志内容呈现的形式。
# 专门的类：Formatter
# logging.Formatter(fmt,datefmt)
fmt = '%(asctime)s  %(filename)s  %(funcName)s [line:%(lineno)d] %(levelname)s %(message)s'
ft = logging.Formatter(fmt=fmt)

# handler === 输出渠道。控制台？文件？日志输出到哪里.容器。
handler_console=logging.StreamHandler()    # 日志内容输出到控制台
handler_console.setFormatter(ft)  # 确定控制台当中，日志内容的呈现格式

logger.addHandler(handler_console)

logger.info('我是一条info日志')
logger.error('我是一条error信息')

# 2022-04-16 15:27:07,618  basic5_4日志1_默认日志和自定义日志器.py  <module> [line:58] INFO 我是一条info日志
# 2022-04-16 15:27:07,619  basic5_4日志1_默认日志和自定义日志器.py  <module> [line:59] ERROR 我是一条error信息

'''
总结
日志收集器-logger   handler - 输出渠道   formatter -- 日志内容的呈现样式
1、创建一个自己的日志收集器 - logger = logging.getLogger("py17")
2、设置显示的日志级别 - logger.setLevel()

如果你想改变默认的输出样式
3、创建一个handler - handler1 = logging.StreamHandler()   - 输出在哪里。
4、创建一个formatter - ft = logging.Formatter(fmt)   - 输出的日志样式
5、设置handler的日志输出样式 -  handler1.setFormatter(ft)
6、绑定到日志收集器当中。  logger.addHandler(handler1)
'''

# 下节课：日志输出到文件-处理。 --- 定义一个自己的日志类！！
# 如果与excel类结合使用。
# 两个类组合使用！！！

# 后续内容精彩预告：
# 单元测试 -- unitttest、ddt
# 数据库 -- 请作业里结合单元测试 ---