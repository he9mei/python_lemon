#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
app_第1周—第1課_1
1.allure的更多用法可以去查看allure report官網下pytest裏面的内容
https://docs.qameta.io/allure/#_pytest

2.web自动化的并行模式
一台电脑只希望打开一个浏览器，如果需要并行，则需要3台机器来打开3个浏览器
如何实现呢？
第1种---grid---以后老师出文章具体讲
第2种---jenkins
manage nodes节点管理-进去可以看到目前的master机器信息
如果Jenkins是安装在linux机器上，但是linux是纯命令行，无法打开浏览器，怎么办？
大部分情况，我们不会在linux机器执行，我们会选择在windows机器执行
===jenkins-master/slave模式===
分担jenkins服务器的压力，任务分配到其他自执行机器来执行。
master：jenkins服务器
slave：执行机，执行master分配的任务，并返回任务的进度和结果。
master---对应多个slave
master---1.管理节点、2.分配任务
slave---1.反馈状态、2.反馈任务进度、3.反馈任务结果
1.slave向master注册
2.slave的状态：空闲/忙碌
3.slave的能力：可并行执行

具体见ppt
提问：master即安装Jenkins的机器，slave需要安装Jenkins吗？---不需要

可以拿云服务器当做master，自己电脑当做slave，尝试

具体操作：
1.slave---管理员账号
（1）到manage nodes页面，new node新建节点,输入节点名字，选中Permanent Agent
（2）配置节点，填写slave的相关信息
Description---描述，可以填写该slave需要做的事情，以及该slave的机器类型等
# of executors---并行能力，如果机器一般就填写1，如果机器特别好可以填写2，即可以同时做几件事？
Remote root directory---slave机器上用于存放文件的地址，可以自己指定，如新建一个地址E://jenkins_slave_home
Labels---给该slave打个标记，在配置任务的时候，可以根据标记来选择。也就是给执行机分类。机器特别少的时候，可以不填。
Usage---两个选项。选项1.尽可能的使用（必须保证所有任务我都能做，都有相关的环境，否则可能执行失败）
        选项2，只做明确指定给我的事情（我们一般推荐使用这个）
Launch method---slave向master报道的方式，如果选项没有Windows向linux连接的选项，需要先配置（有个SSH是linux直接的连接）
        到全局安全配置下-agent-原本是disable，切换到random随机模式，保存
        再到节点配置去查看，是否多了选项Launch agent by connecting it to the master
        （如果jenkins安装在Windows本身就有这个选项）
Availability---3个选项，我们一般选择尽可能的在线
Node Properties---环境变量、工具路径。之后用的时候在来配置。
保存。会看到是打叉的，表示该slave是离线模式。

2.slave
进入slave详情，会看到展示了连接的几种方式：
（1）.Launch agent from browser
（2）.Run from agent command line:
java -jar agent.jar -jnlpUrl
http://localhost:8080/computer/1%E5%8F%B7%E5%B0%8F%E5%BC%9F-%E5%93%AA%E5%90%92/slave-agent.jnlp
-secret 1883ebf1264845ffc76127d5c0cec0b986a58d9cd3dad313a54b72fd4ab62d54 -workDir "E:\jenkins_slave_home"
说明：
第2种方式，需要先下载agent.jar包。
我们这里采用第一种方式，点击launch图标，即可下载slave-agent.jnlp文件
老师这里会进入运行jenkins remoting agent页面（我这里是jenkins用的本机地址，没有进入下一步流程）
点击运行，会进入连接，打开连接窗口

3.slave
刷新后，如果连接完成，可以看到，已经不是离线状态，显示已连接。
再去节点管理查看，有个时钟差表示主从之间的时间差。
连接窗口，就相当于是连接的桥梁，关闭这个窗口，连接就断了。
连接之后，连接窗口这时候有个file，点击有个install as a service，也就是安装成一个Windows服务，开机即打开。
但是存在一个问题，如果使用windows服务的形式连接，执行web自动化时，看不到打开浏览器，是默默执行的。
如果使用窗口连接，可以看到打开浏览器。

4.slave-管理员账户
新建任务-general-adwanced，选择Restrict where this project can be run
Label Expression---可以输入label标签名、也可以直接输入从机的名字。（注意不要使用中文，命名时需要注意）
其他配置与之前相同。
这里举例，在构建时，只是输入windows命令，打印环境变量。
输入-->echo %WORKSPACE%

补充：
1.从机必须具备相应的环境，如执行自动化，python/selenium/pytest/allure这些环境都得有。
2.从机需要执行自动化，那么自动化所需要的数据都是放在从机上的，比如说自动化的代码。如果从git下载，那么代码是默认
下载到从机的E:\jenkins_slave_home路径下的。（这个路径是之前做节点配置的）

主从模式的作用：
1.通过Jenkins实现分布式，多机器并发。
2.如果Jenkins需要做很多事，则可以分一些压力给从机。

进度：未练习
jenkins发送邮件，成功发给谁？失败发给谁？---之前讲过，得看之前的
'''