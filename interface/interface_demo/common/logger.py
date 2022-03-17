#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
日志输出
级别---大开关logger，渠道开关
渠道---console, file
格式---Formatter

'''

import logging
from logging.handlers import RotatingFileHandler
from interface.interface_demo.common import contants


class Logger:
    def __init__(self, name):
        self.log = logging.getLogger(name)
        self.log.setLevel('DEBUG')

        # 设置格式
        fmt = '%(asctime)s-%(message)s[ %(filename)s-%(lineno)d]'  # 格式根据自己需求定义，进Formatter查看即可
        formatter = logging.Formatter(fmt=fmt)

        # 输出渠道
        # 渠道1-控制台
        console_handler = logging.StreamHandler()
        console_handler.setLevel('DEBUG')  # 级别可以放到配置文件中
        console_handler.setFormatter(formatter)
        # 渠道2-文件
        file_handler = RotatingFileHandler(contants.logs_file,  maxBytes=1024*1024,
                                           backupCount=3, encoding='utf-8')
                        # maxBytes到达上限后自动分包；backupCount备份3份；utf-8支持中文
        file_handler.setLevel('INFO')
        file_handler.setFormatter(formatter)

        # 添加到日志实例
        self.log.addHandler(console_handler)
        self.log.addHandler(file_handler)

    def info(self, msg):
        self.log.info(msg)

    def debug(self, msg):
        self.log.debug(msg)

    def error(self, msg):
        self.log.error(msg)

'''
抛出问题：
我们的日志都写入一个文件，如果多个用例同时执行，都往同一个文件写入，可能出现错乱。
所以要保证，我们使用同一个实例来操作。
直接在类中实例化
'''
log = Logger("api")
# log.log.info()  # 这样调用不太好，最好是把log实例方法写在类中，外面就不要直接操作我的内部实例。
# log.info("日志信息")  # 之后就可以直接这样调用
# 然后在测试用例中引入即可
