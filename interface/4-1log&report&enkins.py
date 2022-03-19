#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
1.log---见logger.py

2.report---见run.py

3.git
安装git，即源代码管理器，与svn作用相同，掌握简单命令
项目不要设置公开，创建时要设置为私有；绝对不能项目地址以及数据库信息，防止黑客攻击；config信息不要上传
1.新的项目上传git流程
（1）创建repository
（2）到项目根目录下，按住shift(貌似不需要)，右键，点击git bash here
输入命令：(创建之后，git页面就有以下命令提示)
-->git init
-->git add --all
-->git commit -m "first commit"
-->git branch -M main
-->git remote add origin git@github.com:he9mei/test.git
-->git push -u origin main
2.修改后push
到pycharm项目中，定位到项目或者单个文件右键也可以看到git了。如果是新的文件先add，如果不是commit和push就可以了。
3.本地没有，要从git拿到这个项目
git clone或者download
新拿到这个项目的人，如何指定需要哪些依赖的第三方库？
-->pip freeze  会直接将第三方库版本号输出在控制台
（Could not parse requirement: -ip 提示这个没有关系）
-->pip freeze > requirements.txt
当前目录下就会新增一个requirements.txt文件，可以看到所有第三方库的版本号。
可以将这个文件一起上传到git，告诉其他人。
--->pip install -r requirements.txt
将requirements.txt文件中的第三方库全部安装

4.jenkins
一、jenkins的安装（前提jdk1.8以上）
二、jenkins工作原理和配置介绍
三、jenkins常用的插件介绍
Jenkins的概念：
持续集成（continuous integration）,也就是我们常说的CI
持续集成是一种实践，可以让团队在持续的基础上收到反馈并进行改进，不必等到开发周期后期才开始寻找和修复缺陷。
解决以下困扰：
bug总是在最后才发现；
越到项目后期，问题越难解决；
软件交付时机无法保障；
程序经常需要变更；
无效的等待变多
--》其他概念见图片

---Jenkins使用---
1.安装jenkins,启动，然后网页访问ip:端口号，本地是localhost:8080
如果端口号被占用，可以到安装目录.jenkins下修改jenkins.xml文件arguments中的host

2.新建job并配置，注意：
代码来源：本地，Git（需要配置url和用户名密码）
build环境，选择delete worksapce before build stards 如果需要下拉代码，会清空重新下拉
build，选择windows批处理文件就是打开终端
-->(路径是相对于Jenkins工作空间/任务名，而言的)
pip install -r 项目名/requirements.txt
python 项目名/run.py

3.立即构建
出现问题：找不到路径---需要把根目录加入到编译环环境

4.插件管理
插件安装：如git
报告publish html report
邮件editable email notification

5.系统配置
Jenkins Location
Jenkins URL换成具体的IP:端口
System Admin e-mail address	系统管理员的邮箱
注意之后extended email notification配置发件人邮箱时，邮箱账号必须与上面的系统管理员邮箱一模一样

6.其他
节点管理：如果需要配置多台服务器需要用到
凭据管理：用户名和密码的管理

7.报告
安装插件publish html report
配置：任务配置-Post-build Actions
publish html
代码生成的报告的相对路径:项目名/report
代码生成的报告的报告的名字，如：api.html
report title：随便取的
keep past html reports 选中
构建后，可以在jenkins界面查看报告，但是遇到问题：格式丢失
解决办法：系统管理-脚本命令行-输入脚本

8.邮件
安装插件editable email notification
需要信息：邮件服务器、端口；发件人邮箱、密码；收件人邮箱
配置：系统管理-系统设置
editable email notification
引用
默认发件人
默认收件人
默认主题
默认内容
默认信息在哪里设置？--》extended email notification
以QQ邮箱为例，需要配置
smtp server: smtp.qq.com
默认邮箱后缀：不用填
use smtp Authentication 选中
username：发件人邮箱
password：发件人密码
advanced email properties：到QQ邮箱设置-账户-开启pop3/smtp和imap/smto服务，会发信息到手机授权码，粘贴到这里
use ssl 选中
smtp port: 465
carset: UTF-8
default content type: HTML(text/html)
Default recipients: 收件人邮箱
Default Subject: 默认主题
Default Content：默认内容模板（内部可以引用变量）

附件怎么发？
editable email notification
attachments（比如报告的路径文件）：项目名/report/api.html
（邮箱打开报告也没有格式）

9.build triggers
定时构建
输入后点击空白处，会给出预测来验证是否是我们想要的（不会写的话还是例子）

备注：
如果Git不上传配置文件，则需要收到将配置文件拷贝进去，或者执行copy 存在文件路径 目标文件路径
'''
