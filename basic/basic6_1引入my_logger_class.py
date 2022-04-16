#!/usr/bin/python3
# -*- coding: utf-8 -*-

from basic.basic6_1my_logger_class import logger

logger.info("啦啦啦啦啦")
try:
    5/0
except:
    logger.exception("异常信息：被除数不能为0！")   # 注意：这里会打印完整的异常信息。级别是error

'''
2022-04-16 19:22:29,086_basic6_1my_logger_class.py_[line:42]_ERROR_异常信息：被除数不能为0！
Traceback (most recent call last):
  File "C:/Users/lipan/PycharmProjects/python_lemon/basic/basic6_1引入my_logger_class.py", line 8, in <module>
    5/0
ZeroDivisionError: division by zero
'''

# 注意：
# 这样做有个问题，多个py文件调用my_logger_class.py中的logger
# 日志中所有的模块文件名都是：my_logger_class.py
# 所有老师更推荐：basicConfigd的方式

