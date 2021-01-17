#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
一、web回顾
1、web页面
2、元素定位
3、元素操作
4、项目实战+web框架
面试问题：请描述你的框架结构设计？
a.框架当中应用了数据驱动思想和关键字封装思想
b.分层结构设计
数据驱动思想如何解释？即相同的流程不同的数据，可以通过参数化实现，也就是ddt

详细描述：***
框架当中应用了数据驱动思想和关键字封装思想。
    应用了PO模式，根据这个思想可以将测试过程分为四层：
        pagelocators：以页面为单位存储元素定位，以py文件。
        pageobjects: 以页面为单位封装页面操作。
        testcase: 以pytest框架，按照功能模块分层存放测试用例。
        testdatas: 管理测试数据，按照功能模块分层存放，以py文件。
    common层：basepage页面，实现了在框架当中，任何时候失败都能实时截图、输出异常日志、记录操作过程。且使用关键字封装，减少冗余。
    outputs层：存储截图文件、日志文件、测试报告
    run.py：框架入口。配置执行参数。



（1）po模式阶段
    功能测试角度来看，所有点点点=页面操作=测试用例，即不同页面操作组合起来。
    好处:修改一处，任何其他引用我的，全部都会自动同步；分层内容的修改和优化，并不影响其他层。
    分层设计---
    即测试用例与测试对象的分离。
    pageLocators/pageObjects/testCases/testDatas
    如何写断言？--在项目当中，功能测试用例怎么设计，自动化用例就怎么设计，思想是一样的。用例设计的能力始终是测试的核心。
    日志配置时，需要注意一个问题：任何路径的配置应该是相对路径，任何人拿到代码都可以运行，而不需要一堆配置
    测试框架：unittest/ddt

（2）basepage
    1.为什么要封装basepage？
    我们希望在测试过程中，无论哪个地方失败，都要有失败的异常日志、失败的截图、详细的记录操作过程。
    测试用例=页面对象操作+测试数据
        页面对象操作=selenium的基本操作方法---->所以我们应该在最底层的方法进行封装
        封装一次，哪个web系统都可以用
    目的：方便使用、减少冗余
    常见方法封装：等待元素可见、等待元素存在、元素查找、元素点击、元素输入、获取元素文本、获取元素属性、文件上传、windows切换、iframe切换等

    结果：在页面对象操作时，直接调用元素操作方法，不需要再单独写等待和查找元素。
    （如click封装中，会先等等元素出现、在查找元素、再点击与元素且做异常处理）

（3）pytest---特色：筛选测试用例更简单；和allure报告集成；失败重运行；
    面试问题：pyetest比unittest相比优势在哪里？
    1、编写测试用例特别简单（直接写def就可以，可以不写类；不需要继承）
    2、自动识别测试用例。
    3、断言更简单，assert表达式即可。
    4、4种fixture：session/module/class/function
    5、丰富的插件，600+

    自动识别？
    1、目录：pytest命令运行所在的目录。pytest.main()---这里需要再复习下pytest的执行方式
    2、文件：test_*.py或者*_test.py
    3、代码：test_开头的方法；Test开头的类（不能包含__init__）下，以test_开头的函数
    用例执行顺序？包名、文件名是以ADCII排序，文件内部是以代码先后顺序排序。

    运行所有测试用例：pytest.main()
    可以添加参数，如pytest.main(["-s","-v","test_demo.py"])

    筛选用例：
    1、注册标记 pytest.ini文件 [pytest] markers=标记名
    2、标记测试用例 @pytest.mark.标记名
    3、执行带标记的测试用例 -m 标记名

    html报告：--html=相对路径

    fixture：
    1、定义
        创建conftest.py---共享前置后置
        conftest.py可以存在于多个包下，作用范围就是包以内，就近原则

        定义一个函数（前置后置代码），装饰：@pytest.fixture
        @pytest.fixture(scope="function")  # session/module/class/function
        def myinit():
            #前置代码
            yield 返回值
            #后置代码

        scope即定义了夹心饼干中，夹的心是谁？

        fixture支持“继承”。
        一个fixture的前置后置，包含另外一个fixture的前置后置。
        def myinit2(myinit):
            #前置
            yield
            #后置

        执行顺序是：
        myinit前置

        myinit2前置
        myinit2后置

        myinit后置

    2、调用
    (1)测试类、测试用例前装饰：@pytest.mark.usefixtures("fixture函数名")
    (2)把fixture函数名，当做参数传入测试用例


    参数化：---详见笔记
    @pytest.mark.parametrize("参数名", 参数值)
    def test_demo(参数名)
        pass

    失败重运行：--reruns 2 --reruns-delay 5
    allure报告: --alluredir=相对路径

'''
