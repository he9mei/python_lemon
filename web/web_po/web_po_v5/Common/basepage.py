#!/usr/bin/python3
# -*- coding: utf-8 -*-
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import time
import os

from web.web_po.web_po_v4.Common.dir_config import screenshot_dir


# 目标：任务一个步骤都能实现-异常捕获、日志输出、失败截图
class BasePage:   # 页面对象类需要继承BasePage
    def __init__(self, driver: WebDriver):
        self.driver = driver

    # 等待元素可见/出现
    def wait_eleVisible(self, loc, timeout=10, frequncy=0.5, doc=""):
        start = time.time()
        try:
            WebDriverWait(self.driver, timeout, frequncy).until(EC.visibility_of_element_located(loc))
        except:
            logging.exception("等待元素{}出现，超时！".format(loc))   # 关于日志---之前在接口测试讲过了，这里只是简单输出
            # self.sava_png(doc="等待元素超时")  # 这里doc也可以继续从外层传入
            self.sava_png(doc)
            raise   # 异常抛出---这里是一定要抛出的，因为这里捕获后自己处理了，如果不抛出，就不会报错，代码会继续执行。
        else:
            end = time.time()
            duration = end - start  # 这里需要再转化为s，未写完整
            logging.info("等待元素{}出现，等待时间为{}秒。".format(loc, duration))

    # 等待元素存在
    def wait_elePresence(self, loc, timeout=10, frequncy=0.5, doc=""):
        start = time.time()
        try:
            WebDriverWait(self.driver, timeout, frequncy).until(EC.presence_of_element_located(loc))
        except:
            logging.exception("等待元素{}存在，超时！".format(loc))
            self.sava_png(doc)
            raise
        else:
            end = time.time()
            duration = end - start  # 这里需要再转化为s，未写完整
            logging.info("等待元素{}存在，等待时间为{}秒。".format(loc, duration))

    # 保存截图
    # 补充：
    # 1.webdriver的截图方法是仅针对web页面的，是无法截取windows截图的
    # 2.不要用特殊符号存储
    def sava_png(self, doc=""):   # doc是截图名字？类名？用例名？
        # 文件名=页面_操作_时间.png
        now = time.strftime("%Y_%m_%D-%H_%M_%S", time.time())
        # path = screenshot_dir  # 未实现截图，先用简单的路径的试试
        path = "./Outputs/screenshot"
        if not os.path.exists(path):    # 判断文件是否存在，可以单独写在一个函数中
            os.makedirs(path)
        filename = path + "/{}_{}.png".format(doc, now)
        # 截图操作本身也可能会出现失败的情况
        try:
            self.driver.save_screenshot(filename)
        except:
            logging.exception("截图失败！")
        else:
            logging.info("截图成功！保存为:{}".format(filename))

    # 查找元素
    def get_element(self, loc, doc=""):
        try:
            ele = self.driver.find_element(*loc)
        except:
            logging.exception("查找元素{}失败！".format(loc))
            self.sava_png(doc)
            raise
        else:
            # logging.info("查找元素{}，成功！".format(loc))
            logging.info("查找{}的元素{}成功！".format(doc, loc)) # 也可以通过doc具体到哪个页面的哪个元素
            return ele

    # 输入文本
    def input_text(self, loc, text, timeout=10, frequncy=0.5, doc=""):
        # 前提1：元素可见
        # 前提2：找到它
        self.wait_eleVisible(loc, timeout, frequncy, doc)
        ele = self.get_element(loc, doc)
        try:
            ele.send_keys(text)
        except:
            logging.exception("向元素{}输入:'{}'失败！".format(loc, text))
            self.sava_png(doc)
            raise
        else:
            logging.info("向元素{}输入:'{}'成功！".format(loc, text))

    # 点击元素
    def click(self, loc, timeout=10, frequncy=0.5, doc=""):
        self.wait_eleVisible(loc, timeout, frequncy, doc)
        ele = self.get_element(loc, doc)
        try:
            ele.click()
        except:
            logging.exception("点击元素{}失败！".format(loc))
            self.sava_png(doc)
            raise
        else:
            logging.info("点击元素{}成功！".format(loc))

    # 获取元素文本
    def get_element_text(self, loc, timeout=10, frequncy=0.5, doc=""):
        # 前提1：元素存在（不一定可见，建议这里改成存在-再写一个等待存在的方法；如果没有元素隐藏的情况，两种都可以）
        # 前提2：找到它
        self.wait_eleVisible(loc, timeout, frequncy, doc)
        # self.wait_elePresence(loc, timeout, frequncy, doc)
        ele = self.get_element(loc, doc)
        try:
            text = ele.text
        except:
            logging.exception("获取元素{}文本失败！".format(loc))
            self.sava_png(doc)
            raise
        else:
            logging.info("获取元素{}文本成功！".format(loc))
            return text

    # 获取元素属性
    def get_element_attr(self):
        pass

    # 不一定要把所有方法封装，可以需要的时候再封装；
    # 之后学习robotframework的时候，这块已经封装好了,可以再借鉴一下。
    # select
    # iframe
    # windows
    # upload

    # 以下举例说明：
    # 切换frame
    def switch_to_frame(self, locator, timeout=10):
        # 等待frame可见、切换
        try:
            WebDriverWait(self.driver, timeout).until(EC.frame_to_be_available_and_switch_to_it(locator))  # 等待+切换
        except:
            logging.exception("切换到frame元素{}失败！".format(locator))
            self.sava_png()
            raise
        else:
            logging.info("切换到frame元素{}成功！".format(locator))

    # 切换window  #new #main #index
    def switch_to_window(self, index):
        # 获取一次窗口列表、触发新窗口、获取所有窗口、再切换 （前2个步骤可以在函数之前实现，然后再调用函数）
        if index  == "new":  # 代表切换到新窗口
            pass
        elif index == "main":  # 代表切换到第一个窗口
            pass
        else:
            pass

