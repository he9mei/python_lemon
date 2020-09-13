'''
作业：练习百度登录弹出框
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")

# 点击登录
loc_login = (By.XPATH, '//div[@id="u1"]/a[text()="登录"]')
driver.find_element(*loc_login).click()
# 点击登录弹框中的，用户密码登录
loc_pw_login = (By.XPATH, '//p[@title="用户名登录"]')
WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc_pw_login))
driver.find_element(*loc_pw_login).click()

sleep(2)
driver.find_element(By.ID, 'TANGRAM__PSP_4__closeBtn').click()

sleep(5)
driver.quit()

