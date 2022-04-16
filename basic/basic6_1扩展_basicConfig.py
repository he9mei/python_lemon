
'''
使用basicConfig实际是修改了root的Logger;---是一种偷懒的做法
另一种方式是定义自己的日志器
'''

import logging
from logging.handlers import RotatingFileHandler

fmt='%(asctime)s_%(filename)s_[line:%(lineno)d]_%(levelname)s_%(message)s'
ft = logging.Formatter(fmt=fmt)

handler_file = RotatingFileHandler(filename='basicConfig.log',encoding='utf-8',maxBytes=1024*1024*10,backupCount=10)
handler_file.setFormatter(ft)
handler_file.setLevel(logging.INFO)

handler_consol = logging.StreamHandler()
handler_consol.setFormatter(ft)
handler_consol.setLevel(logging.DEBUG)

# 设置一下RootLogger
# 格式这里不设置的话就用handler自带的格式
# 这里handlers必须是list格式，只有一个也需要用handlers=[handler_consol]
logging.basicConfig(level=logging.INFO,format=fmt,handlers=[handler_consol,handler_file])

logging.debug('debug日志')
logging.info('info日志')
logging.warning('warning日志')
logging.error('error日志')