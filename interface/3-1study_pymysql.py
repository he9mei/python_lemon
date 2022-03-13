#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
pymysql
python一个用于与mysql数据库进行交互的库。
1.通过客户端进行连接 IP：port/域名  用户名&密码  （mysql默认端口3306）
2.新建一个查询页面
3.编写sql
4.执行sql
5.查看、获取结果集
6.关闭查询页面
7.关闭连接
'''

from interface.interface_demo.common.config import config_handler
import pymysql

# -->pip install pymysql  #安装失败
# -->pip install pymysql --trusted-host=pypi.org --trusted-host=files.pythonhosted.org  #安装成功


# 1.通过客户端进行连接 IP：port/域名  用户名&密码  （mysql默认端口3306）
mysql = pymysql.connect(host=config_handler.config_parser.get('db', 'host'),
                        user=config_handler.config_parser.get('db', 'user'),
                        password=config_handler.config_parser.get('db', 'pwd'),
                        charset='utf-8', autocommit=True, cursorclass=dict,
                        port=config_handler.config_parser.getint('db', 'port'))
# charset='utf-8'表示编码格式
# autocommit=True自动提交，防止操作后，数据库数据未更新
# cursorclass=dict指定返回格式为字典

# 2.新建一个查询页面
cursor = mysql.cursor()  # 建立游标，保存查询结果
# cursor = mysql.cursor(pymysql.cursors.DictCursor)  指定返回格式为字典。与cursorclass=dict作用一样

# 3.编写sql
sql = "select max(mobilephone) from future.member where mobilephone like '185%'"
# sql = "select * from future.member where mobilephone like '185%' order by Id"

# 4.执行sql
cursor.execute(sql)

# 5.查看、获取结果集 （游标每次取到结果之后，指标就会往下走）
mobilephone = cursor.fetchone()  # 获取当前结果集里面最近的一条
print(type(mobilephone), mobilephone)
print(mobilephone[0])   # 我们要使用查到的185最大手机号时，按照index取就可以，然后再转为int
# mobilephone = cursor.fetchone()  # 如果有多条数据，第二次调用fetchone取的就是第2条，游标往下走
# print(type(mobilephone), mobilephone)
# all = cursor.fetchall()  # 获取当前结果集全部的数据
# print(type(all), len(all), all)   # 长度是387,实际应该全部是389条，因为是游标目前的位置以下全部（如果先fetchall，后面再获取就是None）
# for a in all:
#     print(type(a), a, a['id'])
# 注意：查询结果为多条多列时，是以元组嵌套元组的形式，只能用index取，不方便。
# 那么可以返回字典吗？指定为dictCursor
# 两种方式：可以在建立连接时，指定cursorclass=dict；
# 也可以在建立游标时指定cursor = mysql.cursor(pymysql.cursors.DictCursor)
# dictCursor时，返回多条数据时是列表嵌套字典。（单条返回的就是字典）
# 然后就可以根据key来取了。

# 6.关闭查询页面
cursor.close()

# 7.关闭连接
mysql.close()
