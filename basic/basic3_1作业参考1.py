#!/usr/bin/python3
# -*- coding: utf-8 -*-

# ---老师的讲解-----
'''
3.求三个整数中的最大值
提示：三个整数使用input提示用户输入
12 47 3
'''
# max_num = None
# num1 = input("第一个数：")
# num2 = input("第二个数：")
# num3 = input("第三个数：")
# if int(num1) > int(num2):
#     max_num = num1
# else:
#     max_num = num2
#
# if int(max_num) < int(num3):
#     max_num = num3
# print("最大的数值为：{}".format(max_num))

'''

4.判断是否为闰年
提示:
输入一个有效的年份（如：2019），判断是否为闰年
如果是闰年，则打印“2019年是闰年”；否则打印“2019年不是闰年”
普通年能被4整除且不能被100整除的为闰年
世纪年能被400整除的是闰年
'''
# year = input("请输入一个有效年份：")
# if (int(year) % 4 == 0 and int(year) % 100 != 0) or int(year) % 400 == 0:
#     print("{}是闰年".format(year))
# else:
#     print("{}年不是闰年".format(year))


'''
5.分别使用for和while打印九九乘法表
提示：
输出九九乘法表，格式如下：（每项数据之间空一个Tab键，可以使用"\t"）

1 * 1 = 1
1 * 2 = 2    2 * 2 = 4
1 * 3 = 3    2 * 3 = 6      3 * 3 = 9
1 * 4 = 4    2 * 4 = 8      3 * 4 = 12    4 * 4 = 16
1 * 5 = 5    2 * 5 = 10    3 * 5 = 15    4 * 5 = 20    5 * 5 = 25
1 * 6 = 6    2 * 6 = 12    3 * 6 = 18    4 * 6 = 24    5 * 6 = 30    6 * 6 = 36
1 * 7 = 7    2 * 7 = 14    3 * 7 = 21    4 * 7 = 28    5 * 7 = 35    6 * 7 = 42    7 * 7 = 49
1 * 8 = 8    2 * 8 = 16    3 * 8 = 24    4 * 8 = 32    5 * 8 = 40    6 * 8 = 48    7 * 8 = 56    8 * 8 = 64
1 * 9 = 9    2 * 9 = 18    3 * 9 = 27    4 * 9 = 36    5 * 9 = 45    6 * 9 = 54    7 * 9 = 63    8 * 9 = 72    9 * 9 = 81
'''
"""
每一行：1，2，3，4，5，6，7，8，9
第一列：从1到行号 第一列1  第二列2  第三列3
列数：由行号来决定  是第几行就有几列。
"""
# #  for
# for index in range(1,10):
#     #print(index)
#     for sub in range(1,index+1):
#         print("{} * {} = {}".format(index,sub,index * sub),end="   ")
#         #print(sub)
#     print()
#     #print("====================")

#while
index = 1
while(index <= 9):
    sub = 1
    while(sub <= index):
        print("{} * {} = {}".format(index,sub,index * sub),end="   ")
        sub += 1
    print()
    index += 1