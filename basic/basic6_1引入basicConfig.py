#!/usr/bin/python3
# -*- coding: utf-8 -*-

from basic import basic6_1扩展_basicConfig
# 注意：这里引入的目的是为了执行basic6_1扩展_basicConfig这个文件，因为没有写入类中，都暴露在外面，引入即会执行
import logging
# 注意：这里在导入logging是因为我这里要用logging调用

# 老师是以Excel操作为例
# 我这里只是简单验证
logging.info("啦啦啦啦啦")
try:
    5/0
except:
    logging.exception("异常信息：被除数不能为0！")   # 注意：这里会打印完整的异常信息.级别是error

'''
2022-04-16 18:44:56,655_basic6_1引入basicConfig.py_[line:9]_INFO_啦啦啦啦啦
2022-04-16 18:44:56,655_basic6_1引入basicConfig.py_[line:13]_ERROR_异常信息：被除数不能为0！
Traceback (most recent call last):
  File "C:/Users/lipan/PycharmProjects/python_lemon/basic/basic6_1引入basicConfig.py", line 11, in <module>
    5/0
ZeroDivisionError: division by zero
'''