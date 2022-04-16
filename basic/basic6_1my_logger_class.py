#!/usr/bin/python3
# -*- coding: utf-8 -*-
import logging
from logging.handlers import RotatingFileHandler


class Logger:
    def __init__(self,name='my_logger',filename='demo_rotating.log',encoding='utf-8'):
        self.name=name
        self.filename=filename

        self.logger = logging.getLogger('my_logger')
        self.logger.setLevel(logging.DEBUG)

        fmt = '%(asctime)s_%(filename)s_[line:%(lineno)d]_%(levelname)s_%(message)s'
        ft = logging.Formatter(fmt=fmt)

        handler_console=logging.StreamHandler()
        handler_console.setLevel(logging.INFO)
        handler_console.setFormatter(ft)

        handler_file=RotatingFileHandler(filename,encoding=encoding,maxBytes=1024*1024*10,backupCount=10)
        handler_file.setLevel(logging.ERROR)
        handler_file.setFormatter(ft)

        self.logger.addHandler(handler_console)
        self.logger.addHandler(handler_file)

    def debug(self,msg):
        self.logger.debug(msg)

    def info(self,msg):
        self.logger.info(msg)

    def warning(self,msg):
        self.logger.warning(msg)

    def error(self,msg):
        self.logger.error(msg)

    def critical(self,msg):
        self.logger.critical(msg)

    def exception(self,msg):
        self.logger.exception(msg)


logger = Logger()
# 注意：当我们把日志写在类中，要考虑实例化的问题：
# 如果有多个类调用我们的日志类，我们是要实例化一次？还是多次？----答案是一次。因为多个日志器操作同一个文件可能造成冲突。
# 如何实现多次被调用，但是只实例化一次？---在日志类所在的py文件内实例化。外部引入时，引入实例即可。


# 注意：
# 这样做有个问题，多个py文件调用my_logger_class.py中的logger
# 日志中所有的模块文件名都是：my_logger_class.py
# 所有老师更推荐：basicConfigd的方式