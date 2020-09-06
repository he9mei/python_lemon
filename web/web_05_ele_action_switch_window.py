
'''
元素操作：
二、切换
窗口切换、iframe切换、alter切换+弹出框

1.窗口切换
需求：要操作新窗口的元素
（1）driver.window_handles  # 所有窗口
handle实际就是窗口的ID，会一直变化。windows中叫做句柄。
返回的是一个list列表
最后打开的页面，位于列表的末尾；最开始打开的页面，位于列表第1个，即window_handles[0]
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
handles = driver.window_handles  # 新增：测试EC.new_window_is_opened
driver.find_element_by_xpath('//a[text()="腾讯课堂官网"]').click()  # 触发新窗口
# time.sleep(2)
# 这里的等待是为了新窗口出来需要一点时间。可以强制等待，也可以用以下方式等待新窗口出现
WebDriverWait(driver,10).until(EC.new_window_is_opened(handles))  # 新增
# print(f"是否打开新窗口：{re}")  # 新增---实际无需赋值打印，如果等不到会报错

# 获得所有窗口
handles = driver.window_handles
print(f"所有窗口：{handles}")
# 获得当前窗口
handle_1 = driver.current_window_handle
print(f"切换前的当前窗口：{handle_1}")
# 切换窗口
driver.switch_to.window(handles[-1])   # -1就是最新打开的窗口
print(f"切换后的当前窗口：{driver.current_window_handle}")

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
# driver.switch_to.window(handle_1)  # 以下方式更方便，无需赋值
driver.switch_to.window(handles[0])  # 回到主窗口，也就是第1次进来的窗口。0即代表第1个打开的窗口
print(f"切换回主窗口：{driver.current_window_handle}")

time.sleep(5)
driver.quit()


'''
***不重要***
根据书籍自己补充：
切换到哪个窗口？老师讲的是根据所有窗口的下标来获取的。
# 还有一种方式是通过遍历的方式---但是根据这种方式没有下标方便
for handle in handles:
    if handle != handle_1:
        driver.switch_to.window(handle)
'''
