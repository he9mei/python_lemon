
'''
元素操作：
二、切换
窗口切换、iframe切换、alter切换+弹出框

1.窗口切换
需求：要操作新窗口的元素
（1）driver.window_handles  # 所有窗口
handle实际就是窗口的ID，会一直变化。windows中叫做句柄。
返回的是一个list列表
最后打开的页面，位于列表的末尾；最开始打开的页面，位于列表第1个。
最新的窗口即是 window_handles[-1]

（2）driver.switch_to.window/iframe/altert（切换对象）   #切换
如切换到最新的窗口即 driver.switch_to.window(window_handles[-1])

（3）driver.current_window_handle  # 当前窗口


'''

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")
driver.find_element_by_id("kw").send_keys("柠檬班")
driver.find_element_by_id("su").click()
wins1 = driver.window_handles  # 新增
driver.find_element_by_xpath('//a[text()="腾讯课堂官网"]').click()  # 触发新窗口
time.sleep(2)
WebDriverWait(driver,10).until(EC.new_window_is_opened(wins1))  # 新增

# 获得所有窗口
wins = driver.window_handles
print(wins)
# 获得当前窗口
handle1 = driver.current_window_handle
print(handle1)
# 切换窗口
driver.switch_to.window(wins[-1])
print(driver.current_window_handle)

# 操作新窗口
# driver.find_element_by_xpath('//ul[@id="js-tab"]//h2[contains(text(),"老师")]').click()
# 增加显性等待
loc = (By.XPATH, '//section//h2[contains(text(),"老师")]')
WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()
# 拓展：关于window的EC判断条件
# EC.new_window_is_opened   # 触发新窗口之前获取所有窗口，然后传入，与触发之后获取的所有窗口做比对
# EC.number_of_windows_to_be

# 切回老窗口
time.sleep(2)
driver.switch_to.window(handle1)
# driver.switch_to.window('main')  # main是主窗口，但是不会切换？

time.sleep(5)
driver.quit()