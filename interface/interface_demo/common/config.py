#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 配置文件读取类
import configparser
from interface.interface_demo.common import contants


class ConfigHandler:
    def __init__(self):
        self.config_parser = configparser.ConfigParser()
        self.config_parser.read(contants.global_file, encoding="utf-8")  # 先加载global文件里面的配置项 #有中文需要指定编码格式
        switch = self.config_parser.getboolean("switch", "open")
        if switch:
            self.config_parser.read(contants.online_file)
        else:
            self.config_parser.read(contants.test_file)


config_handler = ConfigHandler()  # 直接在该py文件中实例化一次

# if __name__ == '__main__':
#     config_handler = ConfigHandler()
#     print(config_handler.config_parser.get("api", "pre_url"))

