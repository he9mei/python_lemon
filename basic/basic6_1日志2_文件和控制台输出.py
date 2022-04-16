#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
日志-file
'''

import logging
# 根据文件大小来设置的。一个日志最大多大。如果超了，则重新生成文件。
from logging.handlers import RotatingFileHandler
# 根据时间设置来决定 是否重新生成文件。到点就重新生成。
from logging.handlers import TimedRotatingFileHandler

logger = logging.getLogger('demo')
logger.setLevel(logging.DEBUG)

fmt='%(asctime)s_%(filename)s_[line:%(lineno)d]_%(levelname)s_%(message)s'
ft = logging.Formatter(fmt=fmt)    # fmt格式不用记住，ctr+b进Formatter源码看参数即可

# handler_file =logging.FileHandler(filename='demo.log',encoding='utf-8')
# 如果长期使用可能会导致文件越来越大，我们可以使用RotatingFileHandler或者TimedRotatingFileHandler
# 会先生成demo_rotating.log,超过1024字节生成demo_rotating.log.1,demo_rotating.log.2,demo_rotating.log.3
# demo_rotating.log中是最新的日志，其次是demo_rotating.log.1
handler_file = RotatingFileHandler(filename='demo_rotating.log',encoding='utf-8',maxBytes=1024,backupCount=3)
handler_file.setFormatter(ft)
handler_file.setLevel(logging.INFO)

# 控制台也输出
handler_consol = logging.StreamHandler()
handler_consol.setFormatter(ft)
handler_consol.setLevel(logging.DEBUG)

logger.addHandler(handler_file)
logger.addHandler(handler_consol)

logger.debug('debug日志')
logger.info('info日志')
logger.warning('warning日志')
logger.error('error日志')
