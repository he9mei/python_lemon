#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 投资用例
'''
写自动化用例之前，先用excel写在手工测试用例（内容包括：名称、前置、步骤、断言）
用例1
名称：登录正常用例
前置：1.登录；2.有可以投资的标；3.有足够的钱（>投资标金额）
步骤：
1.首页-选择投资的标；
2.1.标页面-获取投资之前的余额；
2.2.标页面-获取投资之前标的余额；
3.标页面-投资操作（如投资300）；
4.标页面-点击“查看并激活”（存在该按钮即可代表进入投资成功流程）
断言：
1.用户的余额是否少了300块？（为了避免共用账号的影响，应该保持自动化账号独立---很容易）
 投资之前的余额-投资之后的余额=投资300
 1.1投资之后会进入个人页面，查看投资之后的余额
2.标的余额是否少了？ （为了避免别人投资同一个标的影响，只能尽量保证环境独立---很难，如果不行就晚上再跑）
 2.1投资之后会进入个人页面，点击投资记录第一条中的标名，进入标页面
 2.2标页面-查看投资之后的标的月余额
备注：
投资时，首页中如果有3个可以投资的标，应该使用“抢投标”按钮元素而不是标名。因为标名是会变的，按钮元素是不会变的。

补充:
1.投资成功后，不需要检验数据库，因为用户角度是从页面看的（如果是接口测试，是一定要检验数据库的）。不用搞混了。
2.自动化测试只能校验功能，不能检验页面的样式。如果要看样式，截图之后再人工查看，或者有更高级的图片比对？


# web-第4周-第2节课-38分钟
'''
