'''
web-第5周-第2节课-2 对应web_po_v5
一、继续fixture
1.fixture可以直接写在用例类当中，直接使用。比如某个测试类独有的前置。
实例见test_login_pytest_fixture.py
如果fixture是共用的则放在conftest.py中；如果只有自己用，可以放在测试类中。
2.session和module级别的前置和后置
实例见conftest.py

补充：执行顺序
unitest---
用例---ask码值（可以通过序号控制）
pytest---
先文件，再用例
文件名---ask码值（可以通过序号控制）；用例---代码顺序（不能通过序号控制，有插件order也可以控制）

二、参数化
1.数据写在用例中
测试用例前
（1）单个参数
@pytest.mark.parameterize("参数名",[参数值1，参数值2，参数值3])
（2）多个参数
@pytest.mark.parameterize("参数名1，参数名2",[(参数值1-1，参数值2-1),(参数值1-2，参数值2-2),(参数值1-3，参数值2-3)])
（3）多个参数化组合，会形成排列组合。
@pytest.mark.parameterize("a",[1,2])
@pytest.mark.parameterize("b",[11,22])
会产生4条用例。

2.引用外部数据，实例：
# 数据
wrong_data_1 = [
    {"user": "18684720553", "pwd": "", "check": "请输入密码"},
    {"user": "", "pwd": "python", "check": "请输入手机号"},
    {"user": "1868472055", "pwd": "python", "check": "请输入正确的手机号"},
    {"user": "186847205533", "pwd": "python", "check": "请输入正确的手机号"}
]

# 测试用例--不解包的方式
    @pytest.mark.parametrize("data", ld.wrong_data_1)
    def test_login_1_wrongData(self, data, access_web):
        LoginPage(access_web).login(data["user"], data["pwd"])
        assert LoginPage(access_web).get_error_msg() == data["check"]

# 测试用例--解包的方式
    @pytest.mark.parametrize("user,pwd,check", ld.wrong_data_1)
    def test_login_1_wrongData(self, user, pwd, check, access_web):
        LoginPage(access_web).login(user, pwd)
        assert LoginPage(access_web).get_error_msg() == check

三.改造测试用例---一部分前置写在测试用例中，一部分前置写在conftest.py中
查看我的截图，再消化消化

四.html报告
安装 -->pip3 install pytest-html
使用 命令 --html=Outputs/report/report.html  # 这个路径是相对路径，是相对于当前命令执行的路径
'''

'''
=======================================
web-第5周-第2节课-1 对应web_po_v5
补充：
一、关于basepage封装
1.basepage封装时，建议写注释
即，在函数写完之后，在函数下方打三引号，所有参数都会出来，给每个参数写上注释，函数的其他注释写在参数注释的上方即可。
没有返回值的话，return就写无
2.iframe切换封装再次讲解
可以不做页面封装，直接调用吗？可以
3.input_text封装
如果支持输入多个参数，则参数传入*args，send_keys也传入*args

二、pytest的优势
1、自动识别用例---确定目录（pytest在哪里运行，就以哪里为目录）->查找test_*.py/*_test.py->test_*或者Test*.test_*
2、assert 表达式 （非常自由；unittest更麻烦）
3、四个级别的前置后置：session/module/class/function  （unittest是不支持session级别的）
4、丰富的插件（比如allure插件）

mark功能---刷选用例
1、注册标签（pytest.ini文件-[pytest]-markers:）
2、使用标签（模块、类、用例）
类、用例：@pytest.mark.已注册标签  （可以有多个@标签）
模块、类：pytestmark=pytest.mark.已注册标签名  （多个标签时用列表）
3、运行时，利用标签名过滤用例
pytest -m 已注册标签名

fixture功能---共享前置后置
1.共享的方式：conftest.py；共享的范围：同级测试用例/所有子集测试用例（它爸爸下的所有测试用例）

2.实现前置后置？
@pytest.fixture(scope="session")
def access_web():
    # 前置
   driver=webdriver.Chrome()
   driver.get(url)
    # 分割线and返回值
   yield driver   # 如果返回多个值，可以用元组
    # 后置
   driver.quit()
补充：
1).有部分共用的前置后置，可以考虑放在一起写
举例：
登录---前置：打开浏览器-访问网址  后置:关闭会话
投资---前置：打开浏览器-访问网址-登录-选标  后置:关闭会话
充值---前置：打开浏览器-访问网址-登录  后置:关闭会话

思路：充值的前置后置，可以再写一个fixture，然后将登录的fixture传入
练习见：web_po_v5 的 conftest.py

2).有许多不同的前置后置，怎么办？
（1）层级的conftest.py
可以在不同层级，配置conftest.py文件。如果重名，优先使用自己的，如果自己没有就用爸爸的。
（2）只有自己的测试用例会用到的前置后置。---可以不做共享，直接测试用例py文件中定义fixture，写在类外面


3.如何运用在测试用例中？
---在测试应用中主动引用需要的fixture
（autouse的开关在module/class/function都是关闭的只有session级别酌情使用。大部分情况都是关闭的。）

（1）不需要返回值，通过装饰器直接使用：类、测试用例前 @pytest.mark.usefixtures("access_web")
     （如果同一个类、用例要使用多个装饰器，那大部分情况是因为要使用多个不同级别的fixture）
（2）需要返回值，将函数名当做参数传入（可以装饰也可以不装饰）：如access_web直接当做参数传入
举例：
# @pytest.mark.usefixtures("access_web")
class TestDemo:
    # @pytest.mark.usefixtures("access_web")
    def test_demo(access_web):
        pass
注意：
（1）可以使用多个前置后置，但是不能冲突。比如打开2次浏览器。
（2）如果测试类中，某个测试用例需要的前置后置不太一样，可以将该测试用例放在类外面单独装饰。
（3）如果某前置后置只有一个类或者用例会用到，fixture可以直接写在测试用例的py文件中（类外面），在该py文件中的用例可以直接使用，用法相同。

'''