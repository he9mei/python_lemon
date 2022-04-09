#!/usr/bin/python3
# -*- coding: utf-8 -*-

# ---老师的讲解---

# # 按行读取数据
# # 打开文件，readlines(列表)
# fs = open("my_datas.txt",encoding="utf-8")
# # 数据列表
# all_data_list = []
# # 遍历每一行
# for line in fs.readlines():  # 每一行
#     # 每一行是一个字典
#     data_dict = {}
#     # 去掉首尾的换行符
#     line = line.strip("\n")
#     print(line)
#     data_list = line.split("@") # 每一行根据@分割
#     print(data_list)
#     for data in data_list:   # 根据:进行分割。只分割1次
#         temp = data.split(":",1)
#         print(temp)   # ['mobile'-key, '18866668888'-value]
#         data_dict[temp[0]] = temp[1]
#     print(data_dict)
#     all_data_list.append(data_dict)
#
# print(all_data_list)

import os
def check_file(file_path,encoding="utf-8"):
    # 文件存在与否
    if os.path.exists(file_path):
        fs = None
        # 文件打开
        try:
            fs = open(file_path,encoding=encoding)
            #return fs
        except Exception as e:
            print("打开文件失败：")
            print(e)
            return False
        else:
            return fs.readlines()
        finally:
            if fs is not None:
                fs.close()
        # except FileNotFoundError:
        #     print("文件找不到！！")
        # except OSError:
        #     print("操作系统异常！！")
        # except UnicodeError:
        #     print("编码格式错误！！")



def get_datas_from_file(file_path,encoding="utf-8"):
    # 打开文件，readlines(列表)
    data_lines = check_file(file_path,encoding)
    if data_lines is not None and data_lines is not False:
        # 数据列表
        all_data_list = []
        # 遍历每一行
        for line in data_lines:  # 每一行
            # 每一行是一个字典
            data_dict = {}
            # 去掉首尾的换行符
            line = line.strip("\n")
            print(line)
            data_list = line.split("@")  # 每一行根据@分割
            print(data_list)
            for data in data_list:  # 根据:进行分割。只分割1次
                temp = data.split(":", 1)
                print(temp)  # ['mobile'-key, '18866668888'-value]
                data_dict[temp[0]] = temp[1]
            print(data_dict)
            all_data_list.append(data_dict)
        return all_data_list

# 检测你写的代码逻辑是否都能够处理。 --- 测试工作
# print(get_datas_from_file("my_datas.txt"))
# print(get_datas_from_file("my_datassss.txt"))
# print(get_datas_from_file("D:\\1-课件目录\\python编程基础"))


# 另外两种异常场景
"""
try：
    可能会出错的代码
except 具体异常类(KeyError):
    捕获异常后的处理
except 具体异常类(OSError):
    捕获异常后的处理
except 具体异常类(FileNotFoundError):
    捕获异常后的处理


方式四：
try：
    可能会出错的代码
except Exception as e:
    捕获异常后的处理
    print(e)
"""

# 文件打开异常处理方式二：上下文管理
"""
# 打开文件(无论有没有出现异常)，都会关闭文件对象。
with open() as fs:
    # 没有出现异常的情况下，执行的代码。
    # fs 文件对象 fs = open()
"""
with open("my_datasssss.txt") as fs:
    datas = fs.read()
    print(datas)


