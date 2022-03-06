#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
1.关于接口?
接口主要用于外部系统与系统之间以及内部各个子系统之间的交互点，定义特定的交互点，然后通过这些交互点，通过一些特殊的规则也就是协议，
来完成数据之间的交互。

接口的分类?
按照归属区分：外部接口和内部接口  （外部接口就是不属于我们公司的接口；内部接口就是公司内部各子系统之间以及模块与模块直接的接口）
按照协议区分：HTTP接口，Webservice接口等等

2.什么是接口测试？
接口测试就是测试系统组件间接口的一种测试
（测试的重点是检查数据的交换，传递和控制的过程，以及系统间的相互逻辑依赖关系）

如何做好接口测试？
1.了解好系统各个模块组件之间的逻辑交互 （功能）
2.了解接口的I/O（输入输出）
3.了解协议（协议类型，报文构成，传输方式，常见状态码，url构成等）
4.常用接口测试工具
5.数据库基础（数据校验，提取测试数据等）

3.HTTP协议？
hyper text transfer protocol 超文本传输协议
浏览器作为HTTP客户端通过url向HTTP服务端即web服务器发送所有请求。
web服务器根据接受到的请求，向客户端发生相应信息。

4.HTTP请求包含?
请求体
1.url构成（协议名称://ip:port/path） ip:port也可用域名代替
2.请求头
3.请求数据
4.请求方式

响应体
1.响应码
2.响应头
3.响应正文

5.状态码？
1开头：指示信息---表示请求已接收，继续处理
2开头：成功---表示请求已被成功接收，理解、接受
3开头：重定向---要完成请求必须进行更进一步操作
4开头：客户端错误---请求有语法错误或请求无法实现
5开头：服务端错误---服务器未能实现合法的请求
常见的状态码
200 ok   ---客户端请求成功
400 bad request   ---客户端请求有语法错误
401 unauthorized  ---请求未经授权
403 forbidden  ---服务端收到请求，但是拒绝
404 not found  ---请求资源不存在
500 internal server error  ---服务器发生不可预期的错误
503 server unavailabel ---服务端当前不能处理请求，过段时间可能恢复

//
补充
swagger开发可以用这个工具自动生成接口文档。可以了解下。
状态码、业务码---状态码是Http协议定义的；业务码是开发自己定义的，如点赞时遇到帖子不存在给一个业务码10010等
数据库需要掌握基本的增删改查、联查、分组、排序、基本的函数如max/count/sum/统计等
HTTPS也是属于HTTP协议，但是HTTPS是加密的，更加安全
最常用的请求方式是get和post，一般查询获取信息用get，修改和发生数据用post。登录用post，查询个人信息用get。
但是用get还是post是由开发这个接口的人来定义的，并不绝对。如果接口定义的是用get请求可以用post吗？不行，要按照接口定义来测试
请求方式还有put/delete/option不常用
常见状态码需要记住几个，面试官会问
请求头中user-agent有一个用法是如果测试请求设置为test，就能知道哪些请求是test
http接口用的http协议，webservice用的soap协议。soap协议就是封装好的http的post协议
还有ftp协议，是专门管理文件的
请求头常见的内容，比如Accept,即接收的类型，有application/json、text、xml、html等类型（到公司再确认下公司接口的请求头）
响应头常见内容，比如content-type也是类型，还有content-length等

请求头示例
Accept: */*
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
Connection: keep-alive
Content-Length: 56
Content-Type: application/json
Cookie:
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)
响应头示例
Access-Control-Allow-Credentials: true
Access-Control-Allow-Headers: Content-Type
Access-Control-Allow-Methods: POST, GET
Access-Control-Allow-Origin: https://www.baidu.com
Content-Length: 130
Content-Type: application/json

练习：
浏览器f12查看网络下接口请求信息
使用postman进行请求
//
'''