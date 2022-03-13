#!/usr/bin/python3
# -*- coding: utf-8 -*-
from interface.interface_demo.common.config import config_handler
import pymysql


# 数据库交互封装类
class MysqlHandler:
    # 1.建立连接；建立游标
    def __init__(self):
        self.mysql = pymysql.connect(host=config_handler.config_parser.get('db', 'host'),
                                     user=config_handler.config_parser.get('db', 'user'),
                                     password=config_handler.config_parser.get('db', 'pwd'),
                                     charset='utf-8', autocommit=True,
                                     port=config_handler.config_parser.getint('db', 'port'))
        self.cursor = self.mysql.cursor(pymysql.cursors.DictCursor)

    # 2.查询并返回结果
    def query_one(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    def query_all(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    # 3.关闭游标；关闭连接
    def close(self):
        self.cursor.close()
        self.mysql.close()


# 调用思想：一次实例化，一次连接；多次查询；一次关闭
if __name__ == '__main__':
    mysql = MysqlHandler()
    sql = "select max(mobilephone) as maxphone from future.member where mobilephone like '185%'"
    result = mysql.query_one(sql)
    # print(type(result[0]), result[0])  # str  # 不指定DictCursor，只能通过index取
    print(result["maxphone"])  # 指定DictCursor，通过key取
    mysql.close()
