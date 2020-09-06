# encoding = utf-8
'''
元素操作：
二、切换
窗口切换、iframe切换、alter切换+弹出框

3.alert弹框切换
（1）识别：没有任何标识，只要有导致弹框的操作，就需要处理
（2）切换：driver.switch_to.alert  返回一个Alert类对象alert
 (3) alert对象操作: 取消dismiss(), 接受accept(), 输入send_keys(keys), 获取文本text()

'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(10)
# 使用我自己写的myH.html文件，用绝对路径；注意\需要改成\\，否则报错
driver.get("C:\\Users\lipan\\PycharmProjects\\python_lemon\\web\\myH.html")

driver.find_element(By.ID, "press_me").click()

# sleep(2)
# alert = driver.switch_to.alert   # 注意不带括号
# alert.accept()    # 关闭弹框-确认


# 高级版本（等待+切换,until会继续返回EC的返回值）
# 可以用以下接受返回值的写法；也可以不接收，再写一次切换到alert也是没有问题的。
alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
alert.accept()


sleep(5)
driver.quit()

'''
补充1：
弹出框一般分为2种：
一种是以上的系统的alert弹出框；
还有一种是html自己的弹出框（如百度搜索页面的登录弹出框）
这种弹出框的套路：
（1）触发弹出框
（2）等待元素可见
（3）操作

作业：练习百度登录弹出框

补充2：
下拉列表
以百度搜索页面为例，更多-鼠标悬停，即可看到下拉列表
（需要先讲鼠标操作）
'''

