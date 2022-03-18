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
（2）到项目目录下，按住shift(貌似不需要)，右键，点击git bash here
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

--30分钟

'''