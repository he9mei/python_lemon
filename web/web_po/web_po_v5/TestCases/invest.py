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
-----------------------------
关于前置条件：
原则：
1.无限次执行用例的时候，代码不会出问题（前置都成立）
2.如果换一个电脑或者环境，不会出现环境依赖问题。
前置：
1.登录；
2.有可以投资的标；
   方案1：自己建标；---可以通过接口去做（也可以页面操作，但是接口更简单省时）。数据准备阶段借助接口甚至数据库都是可以的。
   方案2：使用已经建好的标的第一个---如果想更快捷的完成用例，可以先使用这个，之后再优化为方案1
3.有足够的钱（>投资标金额）
   方案1：每次投资之前先判断余额是否充足，不充足时，先充值---可以通过接口去做
   方案2：一次充值1亿即足够的钱---可以先用这个，之后再优化为方案1
-----------------------------
用例2：
名称：异常用例-账号余额不足
前置：1.账户余额<投资金额；2.标余额>投资金额
步骤：
断言：

用例3
名称：异常用例-标余额不足
前置：1.账户余额>投资金额；2.标余额<投资金额
步骤：
断言：

用例4
名称：输入非100整数
用例5
名称：输入小于100
用例6
名称：输入为空
用例7
名称：输入非数字

备注：分析用例2-7，参照自动化用例原则，决定---用例1、用例4、5、6、7做成自动化。用例2、3手工完成。
事实上这里只是表达一种思想，用例2、3实际是也不是特别麻烦，是可以自动化的。可以用接口创建新的用户、新的标即可。

问题：
接口测试的用例要与UI自动化测试用例放在一起吗？
不建议放在一起，可以在项目下创建一个API包，把所有用到的的接口都放进去。
可以定义成类也可以只定义成函数。只是调用而已，不会去校验结果正确与否。
-----------------------------

自动化用例原则
自动化用例设计和筛选原则：
1.不是所有手工用例都要转化为自动化测试用例
2.考虑大脚本开发成功，不要选择流程太复杂的用例。如果有必要，可以把流程拆分为多个用例来实现脚本。
3.选择的用例最好可以构建成场景。例如，一个功能模块，分多个用例，多个用例使用同一个场景。
4.选择的用例可以带有目的性。例如，这部分用例是做冒烟测试，那部分用例是回归测试等。当然会存在重叠的关系。
如果当前用例不能满足需求，那么唯有修改用例来适应脚本和需求。
5.选取的用例可以是你认为重复执行、很烦琐的部分。如字段验证、提示信息验证，这部分很适合自动化测试。
6.选取的用例可以是主体流程，这部分适用于冒烟测试。
7.自动化测试也可以用来做配置检查、数据库检查。这些可能超越了手工用例，但也算是用例拓展的一部分，项目负责人可以有选择的增加。
8.平时在手工测试时，如果需要构造一些复杂的数据或重复一些简单的机械式动作，则告诉自动化脚本，让他来帮你，或许你的效率会因此得到提高。

在编写自动化测试用例过程中应遵循以下几点原则：
1.一个用例为一个完整的场景，从用户登录系统到最终退出并关闭浏览器。
2.一个用例只验证一个功能点，不要试图在用户登录系统后把所有功能都验证一遍。
3.尽量少的编写逆向逻辑用例。一方面因为逆向逻辑的用例很多（例如手机号输入有十几种情况）；
另一方面自动化脚本本身比较脆弱，对于复杂的逆向逻辑用例实现麻烦且容易出错。
4.用例与用例之间尽量避免产生依赖。
5.一条用例完成测试之后需要对测试场景进行还原，以免影响其他用例的执行。
---数据清理（如果有权限测试环境可以通过接口或SQL清理数据，没有权限也可以不清理；线上环境不要动，风险太大，实在不行可以找开发操作；
   web自动化最基本的清理操作就是关闭浏览器）

补充：
关于第1-2点，复杂的流程可以拆分多个用例，再串起来执行。如果都写在一个用例，步骤太多容易出错。
关于第2-3点，结合1-5，复杂的逆向用例如果影响通过率，则可以拿出来手工测试，并标记好哪些自动化哪些手工。
关于第1-4点，冒烟的目的是能不能用，回归的目的是好不好用。
'''
