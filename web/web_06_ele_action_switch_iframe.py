'''

元素操作：
二、切换
窗口切换、iframe切换、alter切换+弹出框

2.iframe切换
iframe---即html内部的html
（1）识别---你要操作的元素，在iframe中
如何知道一个元素是否在iframe中？
f12调试模式下，ctrl+f，输入表达式：可以看到表达式上方，即定位元素的结构
如果有两个html，则说明是在iframe中
以腾讯课堂-登录-账号密码登录框为例 https://ke.qq.com/

(2)进入iframe
有3种传参方式，见以下练习
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://ke.qq.com/")

driver.find_element(By.XPATH, '//a[@id="js_login"]').click()  # 点击登录
driver.find_element(By.XPATH, '//i[@class="icon-font i-qq"]').click()  # 点击QQ

# 进入iframe有3种传参方式---3种都验证通过
# time.sleep(2)
# driver.switch_to.frame('login_frame_qq')   # 用name，是字符串
# driver.switch_to.frame(2)   # 用iframe的index，比如第3个iframe的index是2，从0开始的。是数字
# driver.switch_to.frame(driver.find_element(By.NAME, 'login_frame_qq'))   # 用元素，是对象


# 切换高级版本（等待+切换一起搞定，传参以上3种都可以，还增加一种传入locator元祖）
loc = (By.NAME, "login_frame_qq")
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it(loc))


driver.find_element(By.XPATH, '//a[@id="switcher_plogin"]').click()  # 点击账号密码登录
driver.find_element(By.XPATH, '//input[@id="u"]').send_keys("12345678")  # 输入用户名

# 如果iframe当中还有iframe,同样的方法再切换一次就可以
# 如何从iframe回到主页面html？
driver.switch_to.default_content()  # 如果进入了多层iframe，则一步到位回到最外层html
# driver.switch_to.parent_frame()  # 如果进入了多层iframe，只会回到上层html，不一定是最外层html

time.sleep(2)
driver.find_element(By.ID, "login_close").click()  # 关闭登录框

time.sleep(5)
driver.quit()

'''
作业：腾讯课堂的登录流程
'''