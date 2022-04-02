#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
循环：
while循环
for循环
'''

# ---老师的笔记---
# while for
# 循环和遍历
# 遍历：从头到尾，一个个都去访问一下。 for
# 循环：
"""
while 条件：
    条件满足时，干的事情。
如果条件一直满足，一直去重复的执行代码。
直接条件不满足为止，停止循环。
"""
# salary = "0"
# while int(salary) < 40000:
#     salary = input("我想要的薪资：")
#     print("继续学习！！！")

# salary = 7000
# while salary < 40000:  # 只要条件满足，就重复运行缩进的代码。直到条件不满足为止。
#     print("继续学习！！！")
#     salary += 5000
#     print(salary)
#     # 如果我的月薪达到2万，我就退出循环。
#     if salary >= 20000:
#         print("月薪达到2万!不学了，嗨一下！！！")
#         break    # 退出整个循环的关键字。

# 发生变化，达到停止循环的条件 。 避免死循环。

#for 遍历 遍历：从头到尾，一个个都去访问一下。
# 集合类型的数据：列表、字典、字符串、元组
"""
for 变量名 in 列表/字典:
    每访问到一个值(集合)，都要执行的代码。
"""
movies = ["魔道祖师","铁甲钢拳","泰坦尼克号","复联4","变形金刚"]
#列表遍历方式一
for item in movies:
    print(item)
    if item == "复联4":
        print("我最想看的电影，出来了！！我要买票！！")
        break   # 退出当前循环

# 列表 == 遍历索引 0，1，2，3，4 = [0,1,2,3,4]
# range() 生成整数序列。
# range(起始整数,终点整数,步长) 起始整数默认是0，步长默认是1。不包含终点整数。
# range(终点整数)  range(5)  #[0,1,2,3,4]
# range(2,10)   #[2,3,4,5,6,7,8,9]
# range(2,10,2) #[2,4,6,8]
# range(10,2,-2) #[10,8,6,4]
print(len(movies))
#len(movies) = 5
# range(len(movies)) = range(5) = [0,1,2,3,4]
for index in range(len(movies)):
    print(index)
    print(movies[index])


