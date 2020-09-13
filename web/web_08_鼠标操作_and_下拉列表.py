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
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("http://www.baidu.com")
driver.maximize_window()

'''
# 知识点1：鼠标悬停（以百度-设置为例）
# (1)实例化ActionChains
'''
ac = ActionChains(driver)
# (2)找到要操作的元素
el = driver.find_element(By.XPATH, '//span[@id="s-usersetting-top"]')  # 设置按钮
# (3)鼠标操作并执行
ac.move_to_element(el).perform()
# 补充：操作可以连续顺序调用，因为所有操作返回的都是ActionChains本身，看源码能看到return self
# ac.move_to_element(el).click(el).perform()   # 连续操作可以是同一个元素，也可以是不同元素


'''
# 下次课程: web-第3周-第1节课
知识点2：悬浮下拉列表，如何操作？（以百度-设置，点击高级搜索为例）
（1）执行悬浮操作
（2）等待悬浮列表元素出现
（3）悬浮列表操作
补充1：对于悬浮才能看到的元素，如何定位：ctr+shift+c  或者  鼠标放在元素上-右键-检查
补充2：可以直接等待列表中某个元素出现；还有一种方法是找到父元素，然后再for循环，做比对，如果找到这个元素，则操作。
这里我们用第一种。
'''
loc = (By.XPATH, '//a[text()="高级搜索"]')
WebDriverWait(driver, 10).until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()

'''
知识点3：select/option下拉列表 （以百度-设置-高级搜索,文件格式为例）
以前的标签是：
<select name="ft">
    <option value>所有网页和文件</option>
    <option value="pdf">Adobe Acrobat PDF (.pdf)</option>
    <option value="doc">微软 Word (.doc)</option>
    <option value="xls">微软 Excel (.xls)</option>
</select>
现在是：
<div class="c-select-dropdown-list">
    <p data-for="ft">所有网页和文件</P>
    <p data-for="ft" data-value="pdf">Adobe Acrobat PDF (.pdf)</P>
    <p data-for="ft" data-value="doc">微软 Word (.doc)</p>
    <p data-for="ft" data-value="xls">微软 Excel (.xls)</P>
</div>

为了练习select下拉列表的操作，熟悉以下知识
但是实际以下操作是找不到元素的，因为该页面现在找不到select元素了
'''
# （1）导入Slect类
from selenium.webdriver.support.select import Select

loc = (By.XPATH, '//select[@name="ft"]')  # 找到select元素
WebDriverWait(driver,10).until(EC.visibility_of_element_located(loc))

# （2）实例化Select
s = Select(driver.find_element(*loc))  # Select需要传入的是webElement对象

# （3）有三种选择option方式：value属性、index下标、文本内容
s.select_by_value('pdf')   # value是指元素value属性的值，如果没有这个属性则不能用
s.select_by_index(2)    # 列表序号从0开始
s.select_by_visible_text('微软 Excel (.xls)')  # 可见文本

'''
以上两种下拉列表就讲完了，即select和非select
'''

# 关闭driver
sleep(5)
driver.quit()


