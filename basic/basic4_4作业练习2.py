#!/usr/bin/python3
# -*- coding: utf-8 -*-

#!/usr/bin/python3
# -*- coding: utf-8 -*-


'''
石头剪刀布
'''

import random
import os

def game(user_flag):
    data = {'1': '石头', '2': '剪刀', '3': '布'}  # 只是为了打印更清楚
    print("用户出：{}".format(data[str(user_flag)]))
    cp_flag = random.randint(1, 3)
    print("电脑出：{}".format(data[str(cp_flag)]))

    # 石头>剪刀，剪刀>布，布>石头
    # 1>2,2>3,3>1
    end = None
    if user_flag == cp_flag:
        print("平局！")
        end = '平局'
    elif (user_flag,cp_flag) in [(1,2),(2,3),(3,1)]:
        print("我赢了！")
        end = '赢'
    else:
        print("我输了！")
        end = '输'

    return end


def check_input_data(user_flag):
    try:
        user_flag = int(user_flag)
    except:
        print("输入的不是数字！")
    else:
        if user_flag not in [0,1,2,3]:
            print("请输入数字0、1、2、3，否则无效！")
        else:
            return user_flag

def do_game():
    i = 0
    j = 0
    k = 0
    while True:
        user_flag = input('请出拳（1石头2剪刀3布,0退出游戏）：')
        user_flag = check_input_data(user_flag)

        if user_flag == 0:
            print('结束游戏！')
            break
        else:
            end = game(user_flag)
            if end == '赢':
                i += 1
            if end == '输':
                j += 1
            if end == '平局':
                k += 1
    print("本次游戏结果：赢{},输{},平{}".format(i,j,k))

    with open('game.txt','a',encoding='utf-8') as fs:
        fs.write("赢{},输{},平{}\n".format(i,j,k))


def main():
    file = 'game.txt'
    if os.path.exists(file):
        with open(file,encoding='utf-8') as fs:
            result = fs.read()
            print('您的历史记录为：\n{}'.format(result))
    else:
        print('没有历史记录！')
    do_game()


main()


# ---25分钟---