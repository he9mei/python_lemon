#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
web-第5周-第3节课-2
备注：
大部分情况，我们都是在自己电脑配置jenkins，
如果是在纯命令行的linux下，无法直接执行，需要分布式。

Jenkins配置manage jenkins：
1.全局配置
全局工具配置Global Tool Configuration，
（1）安装allure之后，这里就会增加allure commandline配置
（先安装allure插件）这里的allure commandline配置需要填写allure环境安装路径（到bin）。
（2）同理java也需要填写java环境的安装路径---可从环境变量查找java_home即可

2.然后新建任务new item
输入名字-选择自由风格-进入任务配置页面
genaral---jdk使用（system），代码源使用none（工作中需要在git和svn备份）
触发器和触发环境都没有设置
build---我们执行我们的main.py文件（main.py配置了执行的命令）先把工作目录切换到main.py文件
---构建步骤：windows选择excute windows batch command
--->cd （main.py所在的项目路径）
--->python main.py
post build actions---选择allure report
---这里需要填写已经生成的allure报告文件的路径allure-results。注意这个路径必须是相对于jenkins工作路径的相对路径，不可以是绝对路径。这样就有一个问题，报告的路径是在项目路径下，并不在jenkins工作空间。采取折中的办法，将jenkins工作空间切换到我的项目路径。
（general---Use custom workspace选中，填写项目路径，呈现名字可以不改）
然后allure-results路径填写项目下的报告相对路径即可，如outputs/allure_results
保存，然后即可看到allure标识。开始构建即可。

注意：如果出现无法识别allure命令的情况，可以到系统配置-Global properties下添加环境变量Environment variables。（Java的路径和allure的路径都写上，用分号隔开）

2.jenkins
(1)Jenkins的基本概念和运用（见ppt截图）
CI/CD持续集成、持续交付
（单元测试开发自己做；代码检查需要开发配合；其他的编译打包、自动部署、冒烟测试、回归测试都是可以做到持续集成的）代码检查目前比较好的工具是sonarQube
问题：写用例的时候需不需要尽早进入持续集成？
需要。因为单个执行没有问题，放在一起执行可能会存在问题。尽早集成，尽早发现问题。可以每天定时执行。比如加的等待不够，之后就会注意。不要等待200个用例写完了才开始集成，还不如写5个就开始集成。

(3)jenkins的文件管理
1）进入系统配置可以看到主目录
Home directory
C:\Users\lipan\.jenkins
所有的jenkins文件都在这个路径下。（不会存数据库，全部是文件管理）
可以查看下confg.xml和build.xml
2）workspace用来放啥?
工作空间用来放当前任务需要用到的数据文件，比如git下拉的代码、allure生成的报告等。
（直接在jenkins执行--alluredir=allure_results命令时，报告默认就是放在工作路径下的）
3）跟workspace相关的还有一个配置，在任务配置下，构建环境-构建之前删除工作空间
（比如构建之前先拉代码，想要重新拉代码，就可以选择清除工作空间以免影响）
4）构建记录会自己删除吗？
不会，如果自己不设置删除就会越来越多。怎么设置保留30天内的记录？怎么设置保留10个构建记录？
general-Discard old builds-Days to keep builds保留天数/Max # of builds to keep最大保留构建数。
比如，可以分别设置30

（4）补充pytest重运行机制
pip install pytest-rerunfailures
-->pytest --reruns 2 --reruns-delay 5   失败重运行2次，第1次和第2次之间延迟5秒

'''