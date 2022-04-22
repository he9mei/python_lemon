# -*- coding:utf-8 _*-
""" 
@author:mongo
@time: 2019/6/21 19:13
@email:3126972006@qq.com
@function： 
"""

# 1）、搜索引擎中会对用户输入的数据进行处理，第一步就是词法分析，
# 分离字符串中的数字、中文、拼音、符号。
# 比如这个字符串：
# 我的是名字是ths,今年18岁。
# 语法分析后得到结果如下：
# 数字：18
# 中文：我的名字是 今年 岁
# 拼音：ths
# 符号：，。
# 请编写程序实现该词法分析功能。
# /d 数字 [a-zA-Z] [\ue400-\u9fff]
import re
import string
"""
字符串的解析：
1，常用正则表达式
\d 数字0-9 
\D 非数字
[a-zA-Z] 字母/拼音
[\u4e00-\u9fa5] 中文 
\w 字母，数字，下划线，汉字
\W 任意不是字母，数字，下划线，汉字的字符
+ 重复一次或多次，贪婪模式，即正常单个正则每次只能匹配一个字符，但是如果你想要在查找的时候，一次匹配多个字符就要使用这种模式

如果遇到其他不相同的字符串解析的题目，然后又记不住正则表达式的怎么去写思路呢？
可以模仿string模块里面的做法，根据字符串的类型进行分类定义成字符串，
比如说所有的数字字符串是"0123456789", 想要匹配数字就只需要判断单个字符是否在这数字字符串中即可，
一次类推~~~扩展思路

大家遇到编程面试题不要慌，不要一点都不写，冷静分析题目特点，及时不写代码也可将解题思路写上去。

"""

'''
# 老师写的
def analyze(s):
    pattern = {"数字": "\d+", "拼音": "[a-zA-Z]+", "中文": "[\u4e00-\u9fa5]+", "符号": "\W"}
    for k, v in pattern.items():
        # p = re.compile(v,s)
        # p.findall()
        ss = re.findall(v, s)  # eg:数组 [1,8]
        # print(ss)
        print(k + ":" + ' '.join(ss))
        # s = re.sub(v, '', s)

    # print("符号:{0}".format(s))


if __name__ == '__main__':
    s = '我的是名字是ths, 今年18岁。'
    # s = "柠檬班教育6666，python17班的666同学都！！！"
    # analyze(s)
    # for  ss in s:
    #     print(ss,ss in string.digits)

'''


# =========自己写的=======
# 分离字符串中的数字、中文、拼音、符号。
# 比如这个字符串：
# 我的是名字是ths,今年18岁。
# 语法分析后得到结果如下：
# 数字：18
# 中文：我的名字是 今年 岁
# 拼音：ths
# 符号：，。
def find(s):
    dict_data = {'数字': '\d+', '中文': '[\u4e00-\u9fa5]+', '拼音': '[a-zA-Z]+', '符号': '\W+'}
    for k, v in dict_data.items():
        # list_s = re.compile(v).findall(s)
        list_s=re.findall(v,s)   # 这两种写法作用一样
        # print(list_s)
        print('{}:{}'.format(k, ' '.join(list_s)))


if __name__ == '__main__':
    s='我的是名字是ths,今年18岁。'
    # p='\d+'
    # p='[\u4e00-\u9fa5]+'
    # p='[a-zA-Z]+'
    # p='\W+'
    # list_s = re.compile(p).findall(s)
    # print(list_s)
    find(s)
