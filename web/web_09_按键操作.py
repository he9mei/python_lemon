'''
按键操作：
大部分用send_keys即可
本次主要讲组合键：这里可以再根据书籍总结一下常用的按键

'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")

# driver.find_element(By.ID, "kw").send_keys("柠檬班")
# driver.find_element(By.ID, "su").click()
# 此处确认搜索，可以点击百度一下确认按钮，也可以直接点击enter

# (1) 导入Keys类
from selenium.webdriver.common.keys import Keys
#（2）输入keys按键（是建立在元素基础上的）
driver.find_element(By.ID, "kw").send_keys("柠檬班", Keys.ENTER)  # send_keys可以有多个参数


sleep(5)
driver.quit()