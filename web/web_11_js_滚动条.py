'''

js 滚动条
说明：很多页面定位之后，会自动滚动到元素，不需要自己滚动（比如百度搜索结果翻页）；
所以滚动条并不是每次都需要用的。如果没有其他问题，报错元素不可见-不在可视区域，则应该考虑滚动。

滚动条操作：
当要操作的元素在页面可视范围之外，则需要将待操作的元素，滚动到可视区域中。
（1）先找到元素
element=driver.find_element_by_id("id")
（2）再将元素拖到可见区域
通过执行js语句实现
driver.execute_script("arguments[0].scrollIntoView();",element)   # 0即代表参数的序号，也就是element
还有一个方法是scrollIntoViewIfNeeded (如果需要才滚动，更智能，可以百度二者的区别)
（3）再操作元素
element.click()

在页面中，滚动元素到什么位置？
---有2个选择：可见区域最顶端、可见区域最底端
scrollIntoView()是默认 将元素滚动到可见区域最顶端
scrollIntoView(false) 将元素滚动到可见区域最底端
详细参数可以百度
https://developer.mozilla.org/zh-CN/docs/Web/API/Element/scrollIntoView

其他：
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")  移动到页面底部
driver.execute_script("window.scrollTo(document.body.scrollHeight,0)")  移动到页面顶部

'''

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("http://www.baidu.com")
# driver.maximize_window()

driver.find_element_by_id('kw').send_keys("柠檬班")
driver.find_element_by_id("su").click()

# 验证移动到页面底部、顶部
sleep(3)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")  # 移动到页面最底端
sleep(3)
driver.execute_script("window.scrollTo(document.body.scrollHeight,0)")  # 移动到页面最顶端

# driver.find_element_by_xpath('//a[text()=" - 主页"]').click()  # 不滑动也能找到
# 验证滑动到元素操作
loc = (By.XPATH, '//a[text()=" - 主页"]')
ele = driver.find_element(*loc)   # 老师这里写了显性等待，我没有写

js = '''
arguments[0].scrollIntoView(false);
'''
# arguments[0].scrollIntoView();  # 元素滑动到顶端（被挡住百度顶部悬浮框弹挡住了，所以还是找不到元素）
# arguments[0].scrollIntoView(false);  # 元素滑动到底端(成功找到元素了)

driver.execute_script(js, ele)
sleep(3)
ele.click()


sleep(3)
driver.quit()

'''
其他
老师的博客园
https://www.cnblogs.com/Simple-Small/p/11077120.html
以博客为例，博客详情的底部有评论框，查看元素时，看不到文本框textarea输入的内容，内容在哪里?
在value值中，不可见。
可能遇到问题，手动输入可以提交；但是自动化输入，不能提交
这个时候，就要去看一下value值
--> a = document.getElementById("id")
-->a.value
-->a.value = ""
'''

