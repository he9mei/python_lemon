#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
数据类型之字典  关键字dict  用{}定义
字典 键值对  key:value
每一个值用,隔开
key:固定不变的。字符串、数字、布尔值、元组都是不变的。但是这里通用字符串
value；任意类型
字典是无序的，没有索引的概率。
'''
my_dict = {}
my_info = {"name":"huahua", "age": 18}
print(my_info)
# 字典的取值是根据key读取value，key必须是唯一的。
# 字典名[key]
# print(my_info["name"])
# 修改value  字典名[已经存在的key]=新的值
my_info["age"] = 28
# 新增key-value  字典名[新的key]=新的值
my_info['city'] = "长沙"
# 删除
my_info.pop("age")
# del my_info["age"]
print(my_info)
# 获取长度
print(len(my_info))


'''
老师的总结：
列表(可变)、元组(不可变)、字典(可变)
不能全是逗号，没有值。
数据类型的标识：
列表：[]    my_list = ["xiaojian",18]
元组：()    my_tuple = ("xiaojian",18)
字典：{}    my_dict = {"name":"xiaojian","sex":18}

中括号还出现的场景：
1、列表读取数据：my_list[0]
2、元组读取数据：my_tuple[0]
3、字典读取数据：my_dict["name"]

#获取元素的长度   len(集合对象)

列表的用法：增删改查
增：列表.append(值)
改：列表[索引] = 新的值   #重新赋值。
删：列表.remove(值)   del 列表[索引]
特征：有顺序的。值是可以重复的，可以是任意类型的数据。 单身狗

元组：查
创建方式：my_tuple = 1,2,3
只有1个元素：my_tuple = (1,)
不要往元组里面放可变类型的数据(列表、字典)

字典：增删改查
特征：key-value  成双成对出现   key:value  key要唯一
增加：myDict[不存在的key] = value
修改：myDict[已存在的key] = value
删除：字典.pop(key)

'''
