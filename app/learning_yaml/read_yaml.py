#!/usr/bin/python3
# -*- coding: utf-8 -*-

import yaml   # 如果未安装，需要先pip install PyYaml

# 打开yaml文件
fs = open("demo_dict.yaml")  # 相同路径下课可以直接写相对路径
# 加载成python对象
# obj = yaml.load(fs)
obj = yaml.load(fs, yaml.FullLoader)
print(obj)
fs.close()

'''
读取结果：
{'platformName': 'Android', 'platformVersion': '7.1.1', 'deviceName': ['d1', True, 'hello'], 'info': {'name': basic6_2excel_and_config, 'sex': 222, 'age': 333}}

警告：
YAMLLoadWarning: calling yaml.load() without Loader=... is deprecated, as the default Loader is unsafe. Please read https://msg.pyyaml.org/load for full details.
  obj = yaml.load(fs)
根据网页说明，处理警告：改成
obj = yaml.load(fs, yaml.FullLoader)
处理结果：警告消失
'''
