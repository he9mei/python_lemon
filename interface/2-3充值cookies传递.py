#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
1.充值接口，先登录再充值，实现cookies赋值再传入请求
2.request底层，会从session层面自动传递cookie
    with sessions.Session() as session:
        return session.request(method=method, url=url, **kwargs)
也就是说，创建一个session，然后所有请求都使用这个session，会自动完成cookie的传递。
所有请求结束后，会自动关闭session。
目前来讲，我们请求一个接口，就会创建一个session，接口请求完毕后就会关闭。
我们现在要实现，所有请求使用一个session。
思路:
session的创建和关闭，写在setUp()和tearDown()? 每个类都要写太麻烦了。
--》我们统一写在HTTPRequest类中
--》目前我们每次实例化HTTPRequest类，只能完成一个请求。需要进程改造


'''