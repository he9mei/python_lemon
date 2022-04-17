#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Name: my_config
# Author: 简
# Time: 2019/5/15
from configparser import ConfigParser
class MyConfig:

    def __init__(self,filenames,encoding="utf-8"):
        self.cp = ConfigParser()
        self.cp.read(filenames,encoding=encoding)


    def get(self,section,option):
        return self.cp.get(section,option)

    def getInt(self,section,option):
        return self.cp.getint(section,option)

    def getFloat(self,section,option):
        return self.cp.getfloat(section,option)

    def getBool(self,section,option):
        return self.cp.getboolean(section,option)

    def get_list_dict_tuple(self,section,option):
        temp = self.cp.get(section,option)
        return eval(temp)

