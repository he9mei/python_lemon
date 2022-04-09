#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
题目1：
从文件读取数据，然后处理后，输出为列表套字典的格式
数据为：
url:http://test.lemonban.com/futureloan/mvc/api/member/register@mobile:18866668888@pwd:123456
url:http://test.lemonban.com/futureloan/mvc/api/member/recharge@mobile:18866668888@amount:1000
'''


fs = open('my_datas.txt', 'r')
# line1 = fs.readline()
# line2 = fs.readline()
# fs.close()
# print(line1)
# print(fs.readlines())  # 结果是一个列表
list_dict=[]
for line in fs.readlines():
    # print(line)

    line_list = line.strip('\n').split('@')
    # print(line1_list)

    dict_data = {}
    for i in line_list:
        l = i.split(':', 1)  # 指定分隔次数
        # print(l)
        key = l[0]
        value = l[1]
        #     if key == 'url':   # 这里是因为:把http后面也分隔了。这个问题可以用指定分隔次数来解决
        #         value = ':'.join([l[1], l[2]])
        #     else:
        #         value = l[1]
        dict_data[key] = value
    # print(dict_data)
    list_dict.append(dict_data)
print(list_dict)

fs.close()


'''
[{'url': 'http://test.lemonban.com/futureloan/mvc/api/member/register', 'mobile': '18866668888', 'pwd': '123456'}, 
{'url': 'http://test.lemonban.com/futureloan/mvc/api/member/recharge', 'mobile': '18866668888', 'amount': '1000'}]

'''

# 定义为函数
def do_data(file,encoding='utf-8'):
    fs = open(file, 'r',encoding=encoding)
    list_dict = []
    for line in fs.readlines():
        line_list = line.strip('\n').split('@')
        dict_data = {}
        for i in line_list:
            l = i.split(':', 1)  # 指定分隔次数
            key = l[0]
            value = l[1]
            dict_data[key] = value
        list_dict.append(dict_data)
    print(list_dict)
    fs.close()

do_data('my_datas.txt')

# 33分钟