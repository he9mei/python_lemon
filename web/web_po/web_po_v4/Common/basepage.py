#!/usr/bin/python3
# -*- coding: utf-8 -*-
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import time


# 目标：任务一个步骤都能实现-异常捕获、日志输出、失败截图
class BasePage:   # 页面对象类需要继承BasePage
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def wait_eleVisible(self, loc, timeout=10, frequncy=0.5):
        start = time.time()
        try:
            WebDriverWait(self.driver, timeout, frequncy).until(EC.visibility_of_element_located(loc))
        except:
            logging.exception("等待元素{}出现，超时！".format(loc))   # 关于日志---之前在接口测试讲过了，这里只是简单输出
            self.sava_png()
            raise   # 异常抛出---这里是一定要抛出的，因为这里捕获后自己处理了，如果不抛出，就不会报错，代码会继续执行。
        else:
            end = time.time()
            duration = end - start  # 这里需要再转化为s，未写完整
            logging.info("等待元素{}，等待时间为{}秒".format(loc, duration))

    # 保存截图
    # 补充：
    # 1.webdriver的截图方法是仅针对web页面的，是无法截取windows截图的
    # 2.不要用特殊符号存储
    def sava_png(self, doc=""):
        # 文件名=页面_操作_时间.png

        pass


# web-第4周-第3节课 35分钟