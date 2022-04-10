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
import os
def open_file(file,encoding):
    if os.path.exists(file):
    # if os.path.isfile(file)  # 也可以即判断是否存在，也判断是不是文件
        try:
            fs = open(file, encoding=encoding)
        # except FileNotFoundError:  # 异常模式3：精准捕获异常。不常用。
        #     print('文件找不到')
        # except OSError:
        #     print('操作系统异常')
        # except UnicodeError:
        #     print('编码异常')
        # except Exception as e:   # 异常模式4：不用。做框架不用这种写法。
        #     print("文件打开失败!")
        #     print(e)
        #     return False
        except:
            print('文件打开失败')
            raise
        else:
            # return fs
            return fs.readlines()   # 写法2：不返回文件流，直接返回读取的内容
        finally:
            if fs is not None:
                fs.close()   # 如果是返回文件流，这里先不要关，否则无法读取。如果返回读取后的内容，可以关闭


def do_data(file,encoding='utf-8'):
    # fs = open(file, 'r',encoding=encoding)
    # fs = open_file(file,encoding=encoding)  # 接收的是文件流
    file_lines= open_file(file,encoding=encoding)   # 接收的读取的文件行
    if file_lines is not None:
        list_dict = []
        # for line in fs.readlines():
        for line in file_lines:
            line_list = line.strip('\n').split('@')
            dict_data = {}
            for i in line_list:
                l = i.split(':', 1)  # 指定分隔次数
                key = l[0]
                value = l[1]
                dict_data[key] = value
            list_dict.append(dict_data)
        print(list_dict)
        # fs.close()  # 接收的是文件读取结果，文件就可以提前关闭，无需在这里关闭

do_data('my_datas.txt')
