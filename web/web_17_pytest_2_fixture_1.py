#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
web-第5周-第1节课-2 对应web_po_v5
fixture---不能与unittest一起用
数据准备和数据清理，写在一个函数中；实现共享。
conftest.py文件，最好放在testCases包内，将所有前置后置放在这个文件中。同级目录下的用例和包内的用例，都可以共享。
重点：
test_study.py + pytest.ini + run.py 配合练习mark
conftest.py + test_login_pytest_fixture.py  + run.py 配合练习fixture
'''

'''
fixture笔记粘贴：
pytest - 定义fixture

fixture的参数中,有scope作用域：
function：每个test都运行，默认是function的scope。即unittest中的Setup和tearDown
class：每个class的所有test只运行一次。 即unittest中的setupClass和teardownClass
module：每个module的所有test只运行一次
session：每个session只运行一次

fixture中设置返回值：
有的时候，我们在测试环境初始化时，会对资源进行处理后，在测试用例中要使用这个资源。
yield 返回值

示例：
@pytest.fixture   #默认scope为function
def myfixture():
   driver = webdriver.Chrome()    #测试用例执行之前，执行的准备工作
   yield driver         #将driver作为返回值。在测试用例中需要使用driver
   driver.close()      #测试用例执行完成之后，要执行的清理操作
   driver.quit()        #测试用例执行完成之后，要执行的清理操作

2. 用fixture装饰器调用fixture：
   在测试用例/测试类前面加上@pytest.mark.usefixtures(“fixture函数名字”)
    ps: 定义conftest.py文件，在此文件中可定义多个fixture.pytest会自动搜索此文件

conftest.py
定义公共的fixture，多个测试类中都可以调用。
pytest提供了conftest.py文件，可以将fixture定义在此文件中。
运行测试用例时，不需要去导入这个文件，会自动去查找conftest.py文件，然后去找到对应的fixture。

补充：
我有许多不同的前置、后置，怎么办？
（1）层级的conftest.py
（2）有些前置后置，只有自己的测试用例要用，可以直接卸载测试用例文件中定义fixture函数。
3.fixture如果应用在测试用例上？---测试用例中主动引用需要的fixture
1）.通过装饰器直接使用
（1）用例不需要使用fixture的返回值：
 测试用例、测试类前 @pytest.mark.usefixture("fixtuer的函数名称")
（2）用例需要使用fixture的返回值：
第一步：测试用例、测试类前 @pytest.mark.usefixture("fixtuer的函数名称")
第二步：将fixture函数名称作为测试用例的参数传入。
2).可以使用多个前置后置，但是不能冲突。比如:打开2次浏览器
3).session级别的fixture可以将autouse设置为True
4).pytest用例的执行顺序：文件名称的顺序---测试用例的代码顺序

'''