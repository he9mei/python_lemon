
from selenium import webdriver

'''
元素操作：
一、3种等待方式
1.傻等，即强制等待
等待时间是固定的，一般5s以内，否则就是浪费时间
与显性等待、隐性等待结合使用；起到辅助作用，比如显性等待后元素出现了但是没有渲染完，就可以再加1s强制等待

'''
import time
# time.sleep(5)

'''
智能等待
下一行代码中要用到的元素，设置等待极限;
在这个极限范围内，任意时间点元素出现了，就不等了，去执行下一行代码。
如果超过极限范围，没有等到，则不等了，抛出异常。
隐性等待、显性等待，的属于智能等待。

2.隐性等待
主要作用是：等待元素存在，或者命令执行完成。比如find_element、click等命令都算
注意整个session只需要调用一次。之后如果再遇到比如find_element它会自己偷偷调用。
不确定要等待哪个元素，只要是find_element都会去等待。

'''

'''
driver = webdriver.Chrome()
driver.implicitly_wait(10)  # 隐性等待
driver.get("http://www.baidu.com")
# 搜索
input_box = driver.find_element_by_id("kw")
input_box.send_keys("selenium")
search_bn = driver.find_element_by_id("su")
search_bn.click()
# 查看搜索结果---隐性等待元素出现
# （定位搜索结果时，需要搜索结果加载出来，才能定位到。但是这里不需要再写等待，它会自己去调用隐性等待10s）
result = driver.find_element_by_xpath('//a[text()="自动化测试工具" and text()="-新手入门宝典-实战性强"]')
result.click()

time.sleep(5)
driver.quit()
'''

'''
3.显示等待
等待某一元素可见、等待url发生变化、等待元素可用等等条件成立。
各种条件都适用；只适用于当前条件，每个条件都要调用一次
（比如百度页面的登录框，在页面一直是存在的，但是没有弹起时是不可见的。）

显示等待的2个重点：（1）等待操作 （2）条件：可见

ppt描述：
明确等到某个条件满足有，再去执行下一步操作。
程序每隔几秒看一眼，如果条件成立了，则执行下一步，否则继续等待；
直到超过等待时间，则抛出TimeOutException

WebDriverWait()类，即显示等待类。
WebDriverWait(driver,等待时间，轮询时间).until()/until_not()

expected_conditions模块：提供了一系列期望发生的条件
presence_of_element_located  元素存在
visibility_of_element_located  元素可见
element_to_be_clickable  元素可点击
还要很多判断方法，可自行了解。
'''

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
# driver.implicitly_wait(10)
driver.get("http://www.baidu.com")
# 搜索
input_box = driver.find_element_by_id("kw")
input_box.send_keys("selenium")
search_bn = driver.find_element_by_id("su")
search_bn.click()
# 查看搜索结果---显性等待元素出现
# By元素定位
loc_result = (By.XPATH, '//h3[@class="t c-gap-bottom-small"]//em[text()="Selenium"]')
# 条件
print(EC.visibility_of_element_located(loc_result))
# 显性等待
WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc_result))
# 操作
driver.find_element(*loc_result).click()

'''
# 以下是以百度登录框为例，涉及到iframe，之后再用，暂时先用搜索结果为例
ele_login_enter = driver.find_element_by_xpath('//div[@id="u1"]//a')
ele_login_enter.click()
# 切换到iframe
# 等待登录框出现-用户名登录
loc_login_user_login = (By.ID, '//p[text()="用户名登录"]')
WebDriverWait(driver, 10, 1).until(EC.visibility_of_element_located(loc_login_user_login))
# 轮询时间可以不写，默认是0.5s
driver.find_element(*loc_login_user_login).click()
'''

time.sleep(5)
driver.quit()
