#!/usr/bin/python3
# -*- coding: utf-8 -*-

# ---老师的讲解---

import random

class GussingGame:

    def __init__(self):
        self._game_res = [0,0,0] # win,fail,tie

    def select_role(self,role_num):
        roles = {"1":"曹操","2":"张飞","3":"刘备"}
        if str(role_num) in roles.keys():
            print("本轮游戏，您选的角色为：{}".format(roles[str(role_num)]))

    def _user_finger_punch(self):
        # 用户输入数据
        num = input("角色猜拳1剪刀 2石头 3布 玩家输入一个1-3的数字:")
        # 用户的数据是否有效  1，2，3
        if num in ("1","2","3"):
            # 有效的情况下，才去pk
            return int(num)
        else:
            print("猜拳数据错误，玩家输入一个1-3的数字!")
            return

    def _computer_finger_punch(self):
        # 生成随机数
        computer_num = random.randint(1,3)
        return computer_num

    def battle(self):
        # 用户拳
        user_num = self._user_finger_punch()
        # 电脑拳
        computer_num = self._computer_finger_punch()
        # 同时都有出拳的情况下，再pk
        if user_num is not None and computer_num is not None:
           # 赢局
           if (user_num,computer_num) in [(1,3),(2,1),(3,2)]:
               self._game_res[0] += 1
               print("哇哈哈，我赢了！！666！")
           elif user_num == computer_num:
               self._game_res[2] += 1
               print("看来我们实力相当吗？")
           else:
               self._game_res[1] += 1
               print("噢嚯，我失败了！！")


    def show_game_result(self):
        # self.game_res[0],self.game_res[1],self.game_res[2]
        print("本轮游戏结果为：角色{}胜，电脑{}胜，{}平局".format(*self._game_res))


# if __name__ == "__main__":
# 选角
gs = GussingGame()
gs.select_role(2)
while True:
    # pk
    gs.battle()
    # 才去确认，是否需要继续？？
    is_go_on = input("是否继续？按y继续，按n退出。")
    if is_go_on == "n":
        break
    elif is_go_on == "y":
        continue


# 显示本轮游戏
gs.show_game_result()




# 用户出拳
# 电脑出拳
# pk
# 才去确认，是否需要继续？？
# 用户出拳
# 电脑出拳
# pk
# 。。。。
# 最终游戏结果展示。