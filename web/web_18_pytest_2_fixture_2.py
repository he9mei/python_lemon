'''
web-第5周-第2节课-1 对应web_po_v5
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


web-第5周-第2节课-1 end  少看一节课
'''