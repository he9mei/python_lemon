'''
鼠标操作：
web鼠标操作---之后学习app的触屏操作，与之套路相同
类 ActionChains、TouchActions
鼠标常见操作---左键click、右键context_click、拖拽drag_and_drop、
悬停move_to_element、双击double_click
按住别动click_and_hold（对应释放release）
ppt未总结加入---课后；以及看源码

（1）调用方法，存储到行为列表当中。
（2）调用perform()，执行命令。真正执行鼠标操作。


'''
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("http://www.baidu.com")

# 鼠标悬停
# 实例化ActionChains
ac = ActionChains(driver)
# 找到要操作的元素
el = driver.find_element(By.XPATH, "//a[text()='更多']")  # 老师用的设置按钮
# 鼠标操作并执行
ac.move_to_element(el).perform()
# 补充：操作可以连续顺序调用，因为所有操作返回的都是ActionChains本身，看源码能看到return self
# ac.move_to_element(el).click(el).perform()   # 连续操作可以是同一个元素，也可以是不同元素

sleep(5)
driver.quit()

'''
作业：将以上操作补充完整---悬浮后，点击里面的元素，需要等待
'''
# 下次课程: web-第3周-第1节课
