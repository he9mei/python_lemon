#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Name: my_logger
# Author: 简
# Time: 2019/5/14

"""
1、日志文件当中有很多参数：
0、日志收集器名称  1、日志输出级别；2、文件渠道下有：1）文件路径 2）文件个数 3）文件大小

请利用配置文件，来配置以上参数。
并在日志文件中，读取这些参数来设置日志。
"""

from configparser import ConfigParser
import logging
from logging.handlers import RotatingFileHandler
# 使用rootlogger来输出日志，输出到文件，按文件大小。

# 配置数据读取
cp = ConfigParser()
cp.read("my_logger.conf",encoding="utf-8")
level = cp.get("log_level","level")
log_name = cp.get("log_RotatingFileHandler_conf","log_file")
maxMB = cp.getint("log_RotatingFileHandler_conf","maxMB")
backupcounts = cp.getint("log_RotatingFileHandler_conf","backupcounts")


# 设置2个handler
fmt = '%(asctime)s  %(filename)s  %(funcName)s [line:%(lineno)d] %(levelname)s %(message)s'
# handle file
h1 = RotatingFileHandler(log_name,maxBytes=1024*1024*maxMB,backupCount=backupcounts,encoding="utf-8")
# 设置handler2
h2 = logging.StreamHandler()
# 设置一下root logger
logging.basicConfig(level=level,format=fmt,handlers=[h1,h2])

logging.info("1111111111111111")



