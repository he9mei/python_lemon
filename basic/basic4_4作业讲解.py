#!/usr/bin/python3
# -*- coding: utf-8 -*-

# ---老师的讲解---

# 1、基本逻辑
# 2、无效的数据：非数字  数字但不是123
# 3、退出游戏：用户输入0
"""
a.提示用户输入要出的拳 —— 石头（1）／剪刀（2）／布（3）
b.电脑随机出拳
c.比较胜负，显示用户胜、负还是平局
"""
import random
import os

def check_user_input(user_data):
    """
    :param user_data:
    :return:
    """
    try:
        user = int(user_data)
    except:
        print("用户输入的数据异常。请输入1、2、3来代表你的出拳。")
    else:
        if user not in [0,1,2,3]:
            print("用户输入的数据异常。请输入1、2、3来代表你的出拳。")
        else:
            return user


def play_game(user):
    """
    :param user: 用户出的拳。
    :return: 如果返回的是1，我赢了。如果是0，我输了。如果是2，平局。
    """
    # 随机 - 电脑出拳
    computer = random.randint(1,3)
    print("电脑出的拳：{}".format(computer))
    # 什么情况下才是我赢了？ 1、2    2、3    3、1
    # if (user == 1 and computer == 2) or (user == 2 and computer == 3) or (user == 3 and computer == 1):
    if (user,computer) in [(1,2),(2,3),(3,1)]:
        print("我赢了！")
        return 1
    elif user == computer:
        print("平局！")
        return 2
    else:
        print("我输了！")
        return 0

# 读取游戏历史记录。
def read_game_history_game():
    # 有没有历史记录？ 没有可能意味着文件不存在。有，我就打开文件去读取数据。
    if os.path.exists(os.path.join(os.getcwd(),"game_result.txt")):
        with open(os.path.join(os.getcwd(),"game_result.txt"),encoding="utf-8") as fs:
            datas = fs.read()

# 写入游戏结果
def write_game_result(res_data):
    # fs = open(os.path.join(os.getcwd(), "game_result.txt"),"a", encoding="utf-8")
    with open(os.path.join(os.getcwd(), "game_result.txt"),"a", encoding="utf-8") as fs:
        fs.write(res_data+"\n")

# .多次进行游戏，可以让用户选择退出游戏，退出后需要显示胜利情况，例如：用户5局胜、3局败、2局平
# 记数：计胜、计败、计平
# while内部要做什么？
# 0、用户输入拳
# 1、判断是否退出游戏？用户是否输入的为0
# 2、检查数据有效性。check_user_input
# 3、如果有效，开始玩猜拳游戏 。电脑出拳，然后比大小，显示输赢。play_game

win,lose,tie = 0,0,0
# 在玩游戏之前，读取历史记录。如果有的话。因为第一次玩，是没有历史记录的。
read_game_history_game()
# 多次游戏
while True:
    user = input("输入要出的拳 —— 石头（1）／剪刀（2）／布（3）:")
    if user == "0":
        break
    user_data = check_user_input(user)  # 判断数据有效性
    # 数据有效的情况下
    if user_data is not None:
        res = play_game(user_data)  # 玩游戏
        if res == 1:
            win += 1    # 计数。赢+1
        elif res == 0:
            lose += 1   # 计数。输+1
        else:
            tie += 1    # 计数。平+1

print("本次游戏：用户 {}胜{}败{}平".format(win,lose,tie))
# 玩完游戏之后，保存本次的游戏记录。
write_game_result("用户 {}胜{}败{}平".format(win,lose,tie))







