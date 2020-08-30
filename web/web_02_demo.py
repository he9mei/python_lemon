
from selenium import webdriver

# 启动与浏览器的会话
driver = webdriver.Chrome()

# 浏览器操作
driver.get("http://www.baidu.com")
driver.maximize_window()   # 窗口最大化
# 如何去掉浏览器这一行“正在被自动化控制”的提示？---自己解决
driver.close()   # 关闭当前窗口
driver.quit()   # 关闭浏览器会话，整个浏览器关闭，关闭chromedriver进程




