import random
import time


fs = 0
fs_1 = 0
root_text = '1.进入游戏,2.更新日志，3.关于,4.退出'
game_text = '1.猜数字游戏，2.数字炸弹，3.返回'


while True:
    print(root_text)
    xz = int(input('请选择'))
    if xz == 1:
        print('欢迎进入游戏模式')
        time.sleep(0.5)
        print(game_text)
        xz_game = int(input('请选择玩什么游戏'))
        while True:
            if xz_game == 1:
                print('欢迎进入猜数字游戏')
                time.sleep(0.5)
                ran = random.randint(1, 50)
                guess = int(input('请输入数字：'))
                while True:
                    if guess == ran:
                        print('恭喜你，猜中了！！！')
                        time.sleep(0.5)
                        fs += 1
                        print('你的分数：' + fs)
                        if int(input('重来一把？' + '1是，2不是')) == 1:
                            continue
                        else:
                            break
                        pass
                    elif fs == 15:
                        print('你的游戏次数用完了')
                        time.sleep(0.2)
                        fs += 1
                        print('你的分数:' + fs)
                        if int(input('重来一把？' + '1是，2不是')) == 1:
                            continue
                        else:
                            break
                        pass
                    elif guess < ran:
                        print('小了')
                        fs += 1
                        pass
                    elif guess > ran:
                        print('大了')
                        fs += 1
                        pass
                    pass
                pass
            elif xz_game == 2:
                print('欢迎进入数字炸弹游戏')
                time.sleep(0.2)
                ran_2 = random.randint(1,20)
                while True:
                    guess_2 = int(input('请输入数字:'))
                    if guess_2 == ran_2:
                        print('boom！你被炸死了')
                        time.sleep(0.5)
                        fs_1 += 1
                        print('你的分数：' + fs_1)
                        if int(input('重来一把？' + '1是，2不是')) == 1:
                            continue
                        else:
                            break
                        pass
                    elif guess_2 != ran_2:
                        print('你逃过了一劫')
                        fs_1 += 1
                        pass
                    elif guess_2 > 20:
                        print('输入的数字超过了程序设定的最高数字！')
                        fs_1 += 1
                        pass
                    elif fs_1 == 15:
                        print('你的次数用完了')
                        time.sleep(0.2)
                        print('你的分数:' + fs_1)
                        if int(input('重来一把？' + '1是，2不是')) == 1:
                            continue
                        else:
                            break
                        pass
                    pass
                pass
            elif xz_game == 3:
                break
            pass
        pass
    elif xz == 2:
        while True:
            print('更新日志')
            print('''0.1 程序雏形完成
            1.0 加入猜数字游戏
            1.1 加入数字炸弹游戏
            1.2 加入更新日志和关于模块''')
            print('当前版本:1.2')
            if int(input('继续看？' + '1是，2不是')) == 1:
                continue
            else:
                break
            pass
        pass
    elif xz == 3:
        while True:
            print('关于本程序')
            print('''此程序是由dengrb1开发和编写
            开源地址和教程:https://github.com/dengrb1/pygk
            作者github：https://github.com/dengrb1
        
            @ 2023-2024由dengrb1拥有所有权''')
            print('1.退出，2.继续看')
            if int(input('请输入')) == 2:
                pass
            else:
                continue
            pass
        pass
    elif xz == 4:
        if int(input('是否要退出程序？' + '1是，2不是')) == 1:
            print('程序正在退出')
            time.sleep(0.5)
            exit()
            pass
        else:
            continue
        pass
            
