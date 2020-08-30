
'''
元素定位
chrome进入调试模式（我的Windows fn+f12）
两种查看方式：
1.点击方框加箭头的图标，然后点击要定位的位置；
2.直接右键要定位的位置，选择检查

8种定位方式：6种针对单一属性；2种各种组合定位-万能
定位1个元素
find_element_by_id("id")   # 如果是动态ID则不能用此定位
find_element_by_name("name")
find_element_by_class_name("class")
find_element_by_tag_name("tag_name")    # 只针对链接文本-a标签的全部文本
find_element_by_link_text("text")   # 只针对链接文本-a标签的部分文本
find_element_by_partial_link_text("partial_text")

find_element_by_xpath("xpath")
find_element_by_cssSelector("cssSelector")

定位一组元素---同理，也有以上8中元素定位方式
find_elements_by_id("id")
区别：
find_element_by_id("id")---定位1个元素，第一个匹配到的元素，HTML页面从上往下按照顺序
find_elements_by_id("id")---定位1组元素，返回的是列表，列表中是WebElement对象

'''

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://wwww.baidu.com")
ele = driver.find_element_by_id("kw")
# 元素的操作、元素的属性-WebElement类；
# 实际上是类与对象的关系。
# 在find_element_by_id()函数内部，进行实例化（怎么实例化的？不知道），返回的是一个WebElement对象，并赋值给ele
# ele.click()
# ctr+b可以看到click()方法是写在class WebElement(object)类中；还有一些属性
print(ele.tag_name)   # 打印元素属性
ele.send_keys("selenium")   # 对元素进行操作
# 验证码的用途：防止人为或者自动化恶意操作，以阻拦服务器没有必要的压力。
# 在实际自动化过程中，验证码是不做处理的，可以让开发提供万能验证码，或者先拿掉，上线之前再加上。
# 总之没有必要浪费时间在验证码上。应该把更多的时间用在内部功能上。

# 其他方式练习
ele1 = driver.find_element_by_id("kw")
ele1 = driver.find_element_by_name("wd")
ele1 = driver.find_element_by_class_name("s_ipt")
ele1 = driver.find_element_by_tag_name("input")
ele2 = driver.find_element_by_link_text("新闻")
ele2 = driver.find_element_by_partial_link_text("新")

'''
7.xpath---万能；重点学习---两种都用也可以，但是可能混淆
（1）找到元素定位到的element下的html代码-箭头放上去-右键-copy-xpath
以百度页面为例
//*[@id="kw"]
//*[@id="s-top-left"]/div/a
//*[@id="bottom_layer"]/div[1]/p[2]/a
以该前程贷页面手机号输入框为例:http://120.78.128.25:8765/index/login.html
/html/body/div[2]/div/form/div[1]/input

说明：
实际项目中，我们不用copy的xpath，如果层级太多，又找不到唯一属性，可能会特别长。层级结构有变动时，修改量很大。

分析：
绝对定位：以/开头
从根目录开始；严格按照路径；要注意同级元素的位置。如果div[2]表示同级目录下的第2个div，从1开始的。
这种定位方式，页面结构不能动，否则位置就不对了。
尽量不要用绝对定位和下标，实在没有其他办法时才会用。

相对定位：以//开头
以整个html为参照物，不考虑路径和位置，只考虑有还是没有，只要能唯一定位就可以。

补充：
验证表达式是否正确：
找到元素定位到的element下的html代码-箭头放上去-ctr+f
输入表达式如 //input[@name="phone"] 如果找到，会自动标黄；是1/1则是唯一（还是以前程贷手机号输入框为例）

（2）自己写xpath
---相对路径与属性结合---
1.拼自己（属性、文本内容等）
》简单写法 //标签名[@属性名=属性值]
如表达式//input[@name="phone"] 

》如果1个属性找不到，要用多个属性也可以，使用逻辑元素符and 、or连接
如表达式//input[@name="phone" and @placeholder="手机号"]

》如果属性值太长，可以用包含，函数表达  //标签名[contains(@属性名，被包含的属性值)]
class="form-control username" value="">
如表达式//input[contains(@class,"username")]
//input[contains(@class,"username") and @name="phone"]

》*表示全部匹配，可以匹配任意标签名和属性名
如表达式//*[@*="phone"]

》text是文本内容，独立于属性之外，不需要@标识，函数表达 //标签名[text()=文本值]
附加：a链接不要使用href来定位，因为会变，要考虑稳定性和灵活性
如表达式//a[text()="关于百度"]
如果文本太长，可以只取一部分
如表达式//a[contains(text(),"关于")]

2.拼关系
》层级定位
从父元素开始查找
（以百度页面的登录入口为例）
如表达式//div[@id="u1"]/a[@name="tj_login"]    # 父元素之后，以/之后表示子元素
//div[@id="u1"]//a[@name="tj_login"]    父元素之后，以//之后表示所有子孙都可以，是以父元素为参照物
备注：层级定位中用//更多，能用//就不要用/，也就是说能用相对定位就不要用绝对定位

》轴定位---通过兄弟来定位，在表格中很常见，因为自身属性和父元素属性可能都是一样的
轴名称：
ancestor 祖先节点，包括父节点（直系祖先）
parent 父节点 
preceding 当前节点标签之前的所有节点 （html先后顺序，只要在我之前出生的都是）
preceding-sibling 当前节点标签之前的所有兄弟节点 （html先后顺序，同级下的比我先出生的才算，有亲生血缘关系）
following 当前节点标签之后的所有节点
following-sibling 当前节点标签之后的所有兄弟节点

轴定位语法：
/轴名称::节点名称[@属性名=值]     # 此处用/更好，//可能会扩大范围
例如//div//table//td[@name=""]/preceding-sibling::td[@name=""]//input
实际情况轴定位是与之前学的定位是需要结合使用的，不会单独使用。
如表达式---搜索结果第1条---这个例子不是很恰当，因为很容易定位到，只是为了练习该语法
//div[@class="s_tab"]/following-sibling::div[@id="wrapper_wrapper"]//div[@id="content_left"]/div[@id="1"]

使用场景：
页面显示为表格样式的数据列

轴定位总结：明确参照物、与参照物的关系

8.css_selector---效率更高；但是理解有难度；某些xpath可以实现，它实现不了
文本定位表达式，是css_selector不支持的
contains，也是css_selector不支持的

'''

'''
作业---百度页面登录入口按钮
//a[contains(@class,"s-top-login-btn")]
//a[@name="tj_login" and contains(@class,"s-top-login-btn")]
//div[@id="u1"]/a[@name="tj_login"]

柠檬班社区
Jack老师关于web元素定位的博客

'''

'''
xpath定位简单总结:
1.拼自己
表达式：//标签名[@属性名=值]
//input(@name="" and contains(@*="") or text()="")  # 包含5个知识点
2.拼爹、拼关系
（1）层级关系（祖先-后代）
（2）轴定位
爸爸parent  祖先嫡系：ancestor
亲生哥哥们 preceding-sibling  亲生弟弟们following-sibling
表达式：.../轴名称::标签名[@属性名=值]

'''