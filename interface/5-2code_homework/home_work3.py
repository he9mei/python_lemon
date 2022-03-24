# -*- coding:utf-8 _*-
""" 
@author:mongo
@time: 2019/6/21 19:13
@email:3126972006@qq.com
@function： 
"""
# 3）传入一个Json串，返回一个字典，字典只取出Json最底层的数据，
# 中间如果有字符串也要进行处理，请以下面的数据为例，请用递归方法实现
# Json：{"a":"aa","b":['{"c":"cc","d":"dd"}',{"f":{"e":"ee"}}]}
# 输出：
# Dic:{'a':'aa','c':'cc','d':'dd','e':'ee'}
#

"""
找出所有子元素的特征，根据特征进行判断，如果是重复的特征，只需要通过递归的调用自己就重复处理就行！
字典
字符串--》 json字符串--》 字典
列表
"""


def str_2_dict(j):
    new = {}
    if type(j) == str:  # 判断是否是字符串
        j = eval(j)  # 如果是字符串则转成字典，这会是json字符串！！！

    if type(j) == list:  # 判断是否是列表
        for item in j:  # 编列列表的元素，然后根据列表的里面的元素可能是字符串，字典，列表，所以再次调用自己处理
            d = str_2_dict(item)
            new.update(d)

    if type(j) == dict:  # 判断是否是字典
        for k, v in j.items():
            if type(v) == list or type(v) == dict:  # 如果字典中的子元素的value值是字典或者列表
                d = str_2_dict(v)  # 则调用自己处理相似的逻辑，并返回一个字典
                new.update(d)  # 两个字典的合并
            else:
                try:
                    eval(v)
                    d = str_2_dict(v)
                    new.update(d)
                except NameError as e:
                    new[k] = v  # 不是列表也不是字典，只是字符串

    return new


if __name__ == '__main__':
    s = '{"a":"aa","b":[\'{"c":"cc","d":"dd"}\',{"f":{"e":"ee"}}]}'
    # ss =  '{"a": "aa", "b": \'{"e": "ee"}\'}'
    d = str_2_dict(s)
    print(type(d), d)

    # 字典update的用法，将字典b里面的元素合并到字典a中
    # a = {"cc":"1222"}
    # b = {"zz":"6666"}
    # a.update(b)
    # print(a)
