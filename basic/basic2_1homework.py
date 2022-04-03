#!/usr/bin/python3
# -*- coding: utf-8 -*-

# ----老师笔记----

# 1.python中逻辑运算符有哪些? 它们之间有什么区别?
"""
and or not
"""

# 2.如下比较运算分别返回什么？
"""
如果a = 15，b = 9，
则a == b 、a != b 、a > b 、(a - 5) < b 、a >= b ** 2 、
(a + 13 - (10 * 2)) <= (b // 2 * 5 + 35 % 4)
"""

# 3、定义字符串I'm Lemon, I love Python automated testing！
# 提示：使用双引号还是单引号呢   \ 转义字符
str_a = 'I\'m Lemon, I love Python automated testing！'
str_b = "I'm Lemon, I love Python automated testing！"

# 4.把website = 'http://www.python.org'中的python字符串取出来
# 提示：可以使用字符串切片
website = 'http://www.python.org'
print(website[11:17])
start_index = website.find("python")
end_index = website.find("n")
print(website[start_index:end_index+1])


# 5.将给定字符串前后的空格除去，把PHP替换为Python
best_language = "     PHP is the best programming language in the world!      "

# 6.演练字符串操作
# 说明：“位置”指的是字符所处的位置（比如位置1，指的是第一个字符“N”），
# “索引”指的是字符的索引值（比如索引0， 代表的是第一个字符“N”）
my_hobby = "Never stop learning!"
# 截取从 位置2 ~ 位置6 的字符串  1 5+1
print(my_hobby[1:6])
# 截取从 位置2 ~ 末尾 的字符串
print(my_hobby[1:])
# 截取从 开始位置~ 位置6 的字符串
print(my_hobby[:6])
# 截取完整的字符串
print(my_hobby[:])
# 从 索引3 开始，每2个字符中取一个字符
print(my_hobby[3::2])  # 3 +2
# 截取从 索引2 ~ 末尾-1的字符串
print(my_hobby[2:-1])
# 截取字符串末尾两个字符
print(my_hobby[-2:])
# 字符串的逆序（拓展） #正向0  逆向-1
print(my_hobby[::-1])  # 步长为正，表示正向读取。步长为负，表示反向读取。


# 7.去生鲜超市买橘子
# 收银员输入橘子的价格，单位：元／斤
# 收银员输入用户购买橘子的重量，单位：斤
# 计算并且 输出 付款金额
price = input("橘子的价格:单位：元／斤")
count = input("用户购买橘子的重量:")
# int  float   只能输入数字
print(float(price) * float(count))



# 8.个人信息展示
# 在控制台依次提示用户输入：姓名、网名、年龄、性别、爱好、座右铭
# 按照以下格式输出：

# **************************************************
# 个人信息展示

# 姓名（网名）

# 年龄：年龄
# 性别：性别
# 爱好：爱好
# 座右铭：座右铭0
# **************************************************


name = input("名字")
age = input("年纪")
hobby = input("爱好")

person_info = """
**************************************************
个人信息展示

姓名:{}（网名）

年龄：{}
性别：性别
爱好：{}
座右铭：座右铭0
**************************************************
""".format(name, age, hobby)
print(person_info)
