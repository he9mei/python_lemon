#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
web-第5周-第1节课-1 对应web_po_v5
问题1：如果有300个用例，冒烟70个，怎么选？
unittest需要先指定测试类-指定测试用例，加到suit中，用例很多时很麻烦。
pytest很简单。

===pytest简单介绍===
pytest是基于unittest之上的单元测试框架。
1.自动发现测试模块和测试方法。
2.断言使用assert+表达式即可。
3.可以设置会话级、模块级、类级、函数级的fixtures。
4.有丰富的插件库，母亲那在600个以上。===如支持allue报告

安装命令：
pip install pytest
pip install pytest-html  # 安装html插件

pytest插件地址：
http://plugincompat.herokuapp.com


详细解析：
1.自动发现测试用例
（cmd输入pytest，可以看到是从当前命令位置开始查找）

===pytest-收集测试用例===
pytest收集测试用例的规则：
1.默认从当前目录中搜索测试用例。即在哪个目录运行pytest命令，则从哪个目录当中搜索。
2.搜索规则：
（1）符合命名规则test_*.py或者*_test.py的文件
（2）以test_开头的函数名
（3）以Test开头的测试类（没有__init__函数）当中，以test_开头的函数

注意点：---未实践
1.引入的文件必须在python包里面（包内里面有__init__.py文件，如果删除__init__.py可能会报错）
2.工程目录，不能是pyton包，需要删除工程目录最外层的__init__.py文件
(也就是工程目录不能是python包，但是工程目录里面的py文件必须放在python包；如果不是py文件，可以用文件夹，比如截图、日志、报告等)
（有__init__.py文件就是python包；没有__init__.py文件，就是文件夹）
（补充：rootdir，命令所有目录，不能是包；其他都可以是包---老师这里rootdir就是工程目录）
3.使用pytest运行后会产生缓存文件，不仅仅是pycharm工程中看到的。
如果需要拿别人的工程来运行，需要把工程文件中的所有.pytest_cache缓存文件都删掉。因为别人执行的目录，换个电脑就灭有这个目录了。

2.测试用例打标记
pytest4.6之前的很简单，直接打标签；4.6之后的需要注册标签名
===pytest-mark===
对测试用例打标签，在运行测试用例的时候，可以根据标签名来过滤要运行的用例。
使用方法：
(1)注册标签名
(2)在测试用例、测试类前面加上：@pytest.mark.标记名
注册方式：
方法1：创建pytest.ini文件，在文件中按照如下格式添加标签名
[pytest]
markers=
    slow:marks tests as slow(deselected with '-m "not slow"')
    serial
    注：冒号之后,是可选的描述信息,可以不写

方法2：在conftest.py文件中，通过hook注册
def pytest_configure(config):
    config.addinivalue_line("markers","smoke1:标记只运行冒烟测试")
    config.addinivalue_line("markers","demo1:示例运行")

实际用法：
（1）注册-pytest.ini
[pytest]
markers=
    smoke
    demo

（2）标记
打标记范围：测试用例、测试类
@pytest.mark.smoke
@pytest.martk.demo  # 可以打多个标记；可以给测试用例打标记，也可以给测试类打标机
def test_hello():
    print("hello")

（3）执行
-->pytest test_study.py -m smoke
(-m 标记名）---注：支持多个标记名做逻辑运算，但是不推荐，可能出错

===pytest-mark-给用例打标签-方式2===
打标记范围：测试类、测试模块文件
（1）在测试类里，使用以下声明（测试类下，所有用例都被打上该标签）:
class TestClass(object):
    pytestmark=pytest.mark.已注册标签名
    pytestmark=[pytest.mark.标签1,pytest.mark.标签2]  # 多标签模式
（2）在模块文件里，同理（py文件下，所有测试函数和测试类里的测试函数，都有该标签）
import pytest
pytest=pytest.mark.已注册标签名
pytestmark=[pytest.mark.标签1,pytest.mark.标签2]  # 多标签模式

实践：
（1）注册
（2）标记
在py文件或者在class最前面：pytestmark = pytest.mark.demo
（3）执行
-->pytest test_study.py -m demo
补充：
1.模块可能用到的场景：如果做分布式，5台机器一台执行一个模块，可以用过标记来执行模块。也可以通过指定执行哪个py文件来控制模块。
2.如果没有注册标签名，会警告。

3、运行
可以命令行运行，也可以右键运行（老师的版本还可以识别单个用例和类，直接点击运行），还可以写在main文件运行。
main.py

'''