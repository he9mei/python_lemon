#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
web-第4周-第3节课 对应web_po_v4
今天目标：1.主要是对页面对象的优化 2.测试用例层面优化
分析：
1、基本操作反复写，很烦琐----基本操作封装
2、异常捕获（目的：捕获测试用例中每个步骤的报错--->捕获页面对象每个操作的报错--->捕获selenium基本操作的报错）
----基本操作封装时，完成try...except异常捕获的动作，之后则无需在页面对象和测试用例层面捕获异常。
创建common层，即别人拿去用不需要修改的文件，就放在common层

补充：
关于引入，包与包之前只允许单向引入，不能双向引入。如pageLocators和pageObjects

# web-第4周-第3节课 做的事情
1.在Common中的basepage封装常用的方法，我们称这种思想为关键字封装，见basepage.py
2.改造PageObjects中的页面以及页面操作，见login_page_2.py
3.执行测试用例，检查basepage封装是否有问题，检查页面操作是否OK---用test_login.py验证，可以通过，但是没有截图，没有日志

备注：
unittest没有全局级别的setup和teardown
'''