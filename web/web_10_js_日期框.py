'''
自动化过程中，我们一般不用js，但是实在搞不定时，也可以用js
js 日期框
（以12306为例：https://www.12306.cn/index/）
这里日期输入框有readonly属性，无法自己输入（如果日期可以自己输入的情况，也可以使用自己输入的方式）
<input type="text" class="input inp-txt_select" value="2018-07-21" id="train_date" readonly="">
问题：这里元素中value="2018-07-21"，并不是我选择的日期？实际的日期是隐藏的。
-->a = document.getElementById("train_date")
<input type=​"text" class=​"input inp-txt_select" value=​"2018-07-21" id=​"train_date" readonly>​
-->a.value
"2020-09-13"
以后如果遇到提交send_keys时数据为空时，首先要想到这个问题，查看一下value值。
-->a.readOnly = false
false
然后可以直接在输入框修改时间了。
或者修改a.value值，时间框会同步修改后的时间。
-->a.value = "2018-09-16"

总结1：但凡输入框，带有readonly，都可以先修改readonly=false，然后再输入。

以上是在页面调试模式下的执行。
然后我们将以上的调试代码，改成js。
'''

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://www.12306.cn/index/")

js = '''
a = document.getElementById("train_date")
a.readOnly = false
'''
# a.value = "2018-09-16"
# 修改时间可以放在js代码中，也可以在Python代码中输入

driver.execute_script(js)
sleep(2)

el_date_input = driver.find_element_by_id('train_date')
el_date_input.clear()
el_date_input.send_keys("2020-09-18")
# driver.find_element_by_id('search_one').click()
'''
以上是js的第1种用法---直接执行js代码
作业: 将12306查询流程补全
'''

'''
以下是js的第2种用法---带参数的js,参数来自Python代码（比如滚动条；比如，没有ID，需要通过xpath找元素的）
（如果要学习更多js参数的，百度js argumnets）
滚动条用法：
滚动条操作：
当要操作的元素在页面可视范围之外，则需要将待操作的元素，滚动到可视区域中。
（1）先找到元素
element=driver.find_element_by_id("id")
（2）再将元素拖到可见区域
通过执行js语句实现
driver.execute_script("arguments[0].scrollIntoView();",element)   # 0即代表参数的序号，也就是element
（3）再操作元素
element.click()

有多个参数时，示例：
ele1 = driver.find_element_by_xpath('')
ele1 = driver.find_element_by_xpath('')
driver.execute_script("arguments[0].readOnly=false;arguments[1].value='my_value';", ele1,ele2)
'''

# 运用---将之前的代码改写
# （1）可以先把元素定位写好，再当做参数传给JS，就不需要用JS代码中document来找元素了。
ele = driver.find_element_by_xpath('//input[@id="train_date"]')
driver.execute_script("arguments[0].readOnly=false;", ele)
# （2）如果想改写为外部传入的日期，也可以把日期当做参数传入
date = "2018-09-16"
js = '''
a = document.getElementById("train_date")
a.readOnly = false
a.value = arguments[0]
'''
driver.execute_script(js, date)


sleep(5)
driver.quit()
