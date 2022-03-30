#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''

数据类型之列表 关键字list  用[]定义
数据之间用,隔开
列表中可以是任何数据，并且可以重复
'''
a = []
a = ['jackson', 0.99, 200, True, [1, 2, 3], (0, 1, 2), {'name': 'huahua', "age": '18'}]
# 增删改查
# 读取列表中的数据，利用索引，默认从0或者-1开始：列表[索引]
print(a[1])
print(a[-3])
# 增加数据
# 从列表最后追加数据：列表名.append(数据)
a.append("星星")
print(a)
# 插入数据：列表名.insert(索引，数据)
a.insert(2, "python")
print(a)
# 修改
a[1] = 999
print(a)
# 获取长度
print(len(a))
# 删除
# 列表名.remove(值)  # 删除具体的值
# 变量名.pop()  # 删除最后一个
# 变量名.pop(索引)   # 删除索引对应的数据
# del 列表名[索引]  # 删除索引对应的数据
# a.remove(999)
# a.pop()
a.pop(1)
# del a[2]
print(a)

# 排序函数
b=[333,0.99,30,4666]
# b.sort()  # 升序
# b.sort(reverse=True)  # 降序
b.reverse()  # 倒序,也叫做列表反转
print(b)

# 列表的合并：列表A+列表B
c = [True, False]
print(b+c)

# 奇葩面试题
f = []  # 数据长度是0
# f[0]='hello'   # 这种写法是错误的，因为f[0]不存在  IndexError: list assignment index out of range
f.append('hello')   # 这种情况只能用append
print(f)

