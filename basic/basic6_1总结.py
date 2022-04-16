#!/usr/bin/python3
# -*- coding: utf-8 -*-

# ---老师的笔记---

# 解释一个问题 == logging.warn()
"""
# rootlogger，日志收集器，handler,formatter,level
# 1、日志收集器
     logger = logging.getLogger("py17")
# 1.1  设置formatter
     # formatter
        fmt = '%(asctime)s  %(filename)s  %(funcName)s [line:%(lineno)d] %(levelname)s %(message)s'
        ft = logging.Formatter(fmt)

# 2、设置level

# 3、添加handler: 1）选择哪一种handler:StreamHandler,FileHandler
                                 RotatingFileHandler,TimedRotatingFileHandler
                     h1 = 实例化一个handler类
                  2）设置handler中的日志显示格式
                     h1.setFormatter(ft)
                  3) 可选：设置输出的日志级别。
                     h1.set_level(XXX)
                  4）将hander绑定到日志收集器。
                     logger.addHandler(h1)   # 可以添加 多个。


4、配置完成之后，就可以各种调用输出了。
info()..........


# 应用 -
1、设置rootlogger
2、定义自己的日志类。  --- 自己封装的日志类，必须提供info/debug/error/exception/warning/critical

1、设置rootlogger：
# 设置一下root logger
logging.basicConfig(level=logging.INFO,format=fmt,handlers=[h1,h2])
# 参考basicConfig.py文件的实现方式。
应用的时候：直接将此文件引入。代码会自动执行，会自动去设置rootlogger.
            再引入loggging
            在任何地方，使用logging.info/debug/error/exception/warning/critical即可。

"""

# 单元测试。