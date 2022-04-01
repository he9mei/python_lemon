#!/usr/bin/python3
# -*- coding: utf-8 -*-

# 字符串
str_1 = 'hello,python!我来了!'

# 读取，通过索引来取。从0开始。
# 取某一个具体的值
print(str_1[4])
# 取区间值
# 字符串名[起始索引:结束索引]  取头不取尾
# 取前五个
print(str_1[0:5])
# 从第6个开始，取到最后
print(str_1[5:])
# 从头开始，取到下标为7
print(str_1[:8])
# 取最后两位
print(str_1[-2:])
# 截取整个字符串
print(str_1[:])  # hello,python!我来了!
# 字符串的逆序
# 步长为正，表示正向读取；步长为负，表示反向读取。
print(str_1[::-1])  # !了来我!nohtyp,olleh

# 字符串长度
print(len(str_1))

# 1.查找子字符串。
# 字符串.find(子字符串)  返回的是起始索引。如果找不到返回-1
print(str_1.find('python'))  # 6
print(str_1.find("pp"))  # -1
print(str_1.find('!'))  # 12  多个一样的，只匹配第一个
# 2.替换
# 字符串名.replace(old,new)
# 用#替换！
new_str1 = str_1.replace('!', '#')  # 默认全部替换
new_str2 = str_1.replace('!', '#', 1)  # 只替换1次
print(str_1)  # hello,python!我来了!
print(new_str1)  # hello,python#我来了#
print(new_str2)  # hello,python#我来了!

# 3.大小写转换
str_2 = 'PthOn'
print(str_2.upper())
print(str_2.lower())

# 4.删除字符串左右两边的空格，或者指定字符串
str_3 = ' python python   '
str_4 = '&&&python python&&&'
print(str_3.strip(" "))
print(str_4.strip('&'))
# 扩展：lstrip,rstrip 从左边删、从右边删

# 5.字符串截取，按照指定的分隔符。
# 字符串名.split('分隔符')
str_5 = "大家好，我是小简老师。今天天气真好，上课很开心。一会儿中场休息。"
print(str_5.split('。'))
# ['大家好，我是小简老师', '今天天气真好，上课很开心', '一会儿中场休息', '']
print(str_5.split('。', 1))  # 指定分隔次数
# ['大家好，我是小简老师', '今天天气真好，上课很开心。一会儿中场休息。']

# 6.拼成字符串（要求:列表当中每一个值都是字符串）
# 用连接符，将列表中的字符串拼成一个字符串。
# 连接符.join(列表)
list_1 = ['大家好，我是小简老师', '今天天气真好，上课很开心。一会儿中场休息。']
result_str = '*'.join(list_1)
print(result_str)
# 大家好，我是小简老师*今天天气真好，上课很开心。一会儿中场休息。

# 7.格式化字符串
# 用法1：%s字符串 %d数字 %f浮点数 ---了解即可
print('我叫%s,今年%d岁，数学考了%.2f分' % ('jackson', 18, 99.225))
# 我叫jackson,今年18岁，数学考了99.22分

# 用法2：format 占位符{}  ---常用
print("我叫{},今年{}岁，数学考了{}分".format('jackson', 18, 99.225))
# 我叫jackson,今年18岁，数学考了99.225分
print("我叫{1},今年{0}岁，数学考了{2}分".format(18, 'jackson', 99.2))
# 我叫jackson,今年18岁，数学考了99.2分
print('我今年{0}岁，我希望我每年都{0}岁'.format(18))  # 有序号可以替换多次
# 我今年18岁，我希望我每年都18岁


# =======================================
# 补充题目1：
# 输出：i'm ok
print("i'm ok")
print('i\'m ok')

# 补充题目2：
price = input("请输入价格：")
count = input("请输入数量：")
print("最后的价格是：%.2f" % (float(price) * float(count)))

# 补充题目3：
name = input("姓名：")
age = input("年龄：")
sex = input("性别：")
hobby = input("爱好：")

print('''
************
个人信息展示
姓名：{}
年龄：{}
性别：{}
爱好：{}
'''.format(name, age, sex, hobby))

# 三引号可以多行输出且保留格式
