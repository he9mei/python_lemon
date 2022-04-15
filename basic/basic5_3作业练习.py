#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random


class PlayGame:
    dic_game ={'1':'剪刀','2':'石头','3':'布'}
    res_game = [0,0,0]  # 平 赢 输

    def check_input_data(self, input_data):
        try:
            input_data = int(input_data)
        except:
            print("输入不合法，请输入数字1、2、3！")
        else:
            if input_data in [1, 2, 3]:
                return input_data
            else:
                print("输入不合法，请输入数字1、2、3！")

    def choose_role(self):
        dict_role = {'1': '曹操', '2': '张飞', '3': '刘备'}
        role_input = input("请选择您的角色（1曹操，2张飞，3刘备）:")
        role_flag = self.check_input_data(role_input)
        if role_flag is not None:
            role_value = dict_role[str(role_flag)]
            print('您的角色是：{}'.format(role_value))
            return role_value

    def player_do(self):
        player_input = input('请出拳（1剪刀2石头3布）：')
        player_flag = self.check_input_data(player_input)
        if player_flag is not None:
            print('您出拳为：{}'.format(self.dic_game[str(player_flag)]))
            return player_flag

    def computer_do(self):
        computer_flag = random.randint(1,3)
        print('电脑出拳为：{}'.format(self.dic_game[str(computer_flag)]))
        return computer_flag

    def play_game(self):
        # role = self.choose_role()
        player_flag = self.player_do()
        if player_flag is not None:
            computer_flag = self.computer_do()
            '''
            1剪刀 2石头 3布
            1剪刀>3布 2石头>1剪刀  3布>2石头
            '''
            if player_flag == computer_flag:
                print("本局对战结果:不好意思是平局！".format())
                # return 0
                self.res_game[0] += 1
            elif (player_flag, computer_flag) in [(1, 3), (2, 1), (3, 2)]:
                print("本局对战结果:恭喜你赢了！".format())
                # return 1
                self.res_game[1] += 1
            else:
                print("本局对战结果:很遗憾你输了！".format())
                # return 2
                self.res_game[2] += 1

    def read(self):
        try:
            fs = open('game_record.txt', encoding='utf-8')
            file_data = fs.read()
            print('历史记录:\n{}'.format(file_data))
            fs.close()
        except:
            print('没有历史记录！')

    def write(self,data):
        with open('game_record.txt','a',encoding='utf-8') as fs:
            fs.write(data)


if __name__ == '__main__':  # 只在本模块运行，被外部引入时这里不会执行
    '''
    play = PlayGame()
    play.read()
    role = play.choose_role()
    i, j, k = 0, 0, 0  # 可以写在类里面
    if role is not None:
        while True:
            res = play.play_game()
            if res is not None:
                if res==0:
                    i += 1
                if res==1:
                    j += 1
                if res==2:
                    k += 1
                flag = input('是否继续？（y继续，n退出）：')
                flag = flag.upper()
                if flag not in ['Y', 'N']:
                    print('输入不合法！自动退出！')
                    break
                elif flag == 'N':
                    print('退出游戏！')
                    break
            else:
                continue

        print('{}，你的对战结果是：赢{} 输{} 平局{}'.format(role,j,k,i))
        play.write('角色是：{},对战结果是：赢{} 输{} 平局{}\n'.format(role,j,k,i))
'''
    play = PlayGame()
    play.read()
    role = play.choose_role()
    if role is not None:
        while True:
            play.play_game()
            flag = input('是否继续？（y继续，n退出）：')
            flag = flag.upper()
            if flag not in ['Y', 'N']:
                print('输入不合法！自动退出！')
                break
            elif flag == 'N':
                print('退出游戏！')
                break
            else:
                continue

        print('{}，你的对战结果是：平局{} 赢{} 输{} '.format(role, *play.res_game))
        play.write('角色是：{},对战结果是：平局{} 赢{} 输{}\n'.format(role, *play.res_game))