#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
步骤1：Generating a new SSH key
-->ssh-keygen -t ed25519 -C "396167189@qq.com"
然后都默认，点击enter即可
执行结果：
Your identification has been saved in C:\Users\lipan/.ssh/id_ed25519.
Your public key has been saved in C:\Users\lipan/.ssh/id_ed25519.pub.
The key fingerprint is:
SHA256:idOL5deUd5zFXTjqATYFStA6nvqZJ0AF1cjLIRtVUhw 396167189@qq.com

步骤2：Adding your SSH key to the ssh-agent
---命令1---
-->ssh-agent -s
遇到问题
Windows 10 启动自带 ssh-agent
报错 ：unable to start ssh-agent service, error :1058
解决办法
用管理员权限打开Power Shell，执行
Set-Service -Name ssh-agent -StartupType automatic
---命令2---
$ ssh-add ~/.ssh/id_ed25519 命令2示例
-->ssh-add C:\Users\lipan\.ssh\id_ed25519
执行结果：Identity added: C:\Users\lipan\.ssh\id_ed25519 (396167189@qq.com)

步骤3：Add the SSH key to your account on GitHub
到Git网页，gitHub点击用户头像，选择setting，
新建一个SSH Key,取个名字id_ed25519，把id_ed25519.pub拷贝的秘钥复制进去，添加就好啦。
------------------------------
以前项目的地址：C:\Users\lipan\PycharmProjects\python_lemon
使用Git desktop之后，
克隆url: git@github.com:he9mei/python_lemon.git
克隆到地址： E:\GitHub\python_lemon

---------------------
问题：
push报错：
Push failed Unable to access 'https://github.com/he9mei/python_lemon.git/':
Unknown SSL protocol error in connection to github.com:44

解决1：
-->git config --global credential.helper store
-->git push
he9mei
8uhb*UHBhhm
错误：Support for password authentication was removed on August 13, 2021. Please use a personal access token instead
需要token代替密码登录,如何生成token？
进入Git后，头像下方Settings-->Developer settings-->personal access token
填写note，选择90天，勾选repo，Generate token-->
https://github.com/settings/tokens
token：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
再次push时，密码使用token即可
参考：https://blog.csdn.net/weixin_41010198/article/details/119698015


解决2：
1.-->git config --list
找到（如果没有需要添加）
user.name=he9mei
user.email=396167189@qq.com

2.生成key
-->ssh-keygen -t rsa -C "396167189@qq.com"
# （C:\Users\lipan\.ssh\id_rsa.pub）
生成后保存到输入：git_key
密码输入空
Your public key has been saved in git_key.pub.
The key fingerprint is:
SHA256:fCQoE6FtpaXHwudlfbzJlV0TfoeCxh0moSh0LzYFu+0 396167189@qq.com
The key's randomart image is:
+---[RSA 2048]----+
|    +.=.. o.o  oo|
|   = O * + * ..+o|
|  . @ @ * * = +.+|
|   . X O + o =  o|
|      o S . +    |
|       . .       |
|        E        |
|                 |
|                 |
+----[SHA256]-----+

3.找到git_key.pub拷贝秘钥

4.到Git网页，gitHub点击用户头像，选择setting，
新建一个SSH Key,取个名字，把之前拷贝的秘钥复制进去，添加就好啦。

5.使用
到git网页，找到项目code克隆的位置，切换到ssh
复制地址git@github.com:he9mei/python_lemon.git

然后到项目下，.git文件下config
修改url = https://github.com/he9mei/python_lemon.git
为git@github.com:he9mei/python_lemon.git

6.push可以了

注意：最后发现
C:\Users\lipan\.ssh\id_rsa.pub  这个秘钥可以
git_key.pub这个不行，说是public key

'''