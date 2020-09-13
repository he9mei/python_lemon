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
'''

# web-第3周-第1节-50分钟