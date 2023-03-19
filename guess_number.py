import random
import time
import os


fs = 0
cls = 'cls'
lst = ['给' , '不给']
ran = random.choice(lst)
fs_1 = 0


while 1:
    print('1开始游戏，2.琳琳模式，3.更新日志，4.关于，5.退出,6.游戏2')
    xz = int(input('请选择：'))
    if xz == 1:
        a = int(random.randint(1, 20))
        while True:
            b = int(input('请输入数字:'))
            if b == a:
                print('boom！你被地雷炸死了！！')
                fs += 1
                time.sleep(1)
                print('当前分数：' + fs)
                time.sleep(0.2)
                print('炸弹位置:' + ran)
                if int(input('是否重生？' + '1.不，2.是')) == 2:
                    continue
                else:
                    print('Good Bye')
                    time.sleep(1)
                    break
                pass
            elif b != a:
                print('你躲过了一劫')
                fs += 1
                time.sleep(1)
                pass
            elif (b < 20):
                print('数字超过程序运算极限！！！')
                time.sleep(1)
                pass
            elif b == 16384:
                print(fs)
                time.sleep(1.56)
                pass
            elif fs == 12:
                print('游戏结束')
                time.sleep(0.65)
                print(fs)
                pass
            else:
                print('数字错误')
                time.sleep(1)
                pass
        pass
    elif xz == 2:
        print(ran)
        time.sleep(1)
        pass
    elif xz == 6:
        print('welcome to game')
        time.sleep(0.5)
        game_1 = random.randint(1, 50)
        while True:
            xz_game = int(input('请输入你的数字：'))
            if xz_game == game_1:
                print('恭喜你，成功赢到了游戏')
                time.sleep(1)
                fs_1 += 1
                print('当前分数：' + fs_1)
                time.sleep(1.5)
                if int(input('是否重新开始游戏？' + '1是，2不是')) == 1:
                    continue
                else:
                    break
                pass
            elif xz_game < game_1:
                print('大了')
                pass
            elif xz_game > game_1:
                print('小了')
                pass
            else:
                print('不支持这个数字')
                time.sleep(0.2)
                pass
            pass
    elif xz == 3:
        while 3:
            print('更新日志')
            print('''1.0 程序雏形完成
            1.1 程序新增选择界面
            1.1.1 程序选择界面重新更新
            1.2 新增妹妹模式
            1.3 新增彩蛋''')
            print('当前版本：1.3')
            if int(input('请选择：'+ '1返回，2继续看')) == 2:
                continue
            else:
                break
            pass
        pass
    elif xz ==4:
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
    elif xz == 402:
        print('恭喜你找到彩蛋！')
        if int(input('请选择:' + '1.观看，2.返回')) == 1:
            print('梁子依是SB中的SB中的大大大SB')
            time.sleep(1.99)
            pass
        else:
            break
    elif xz == 16384:
        while 1:
            print(ran)
            xz_gg = int(input('请选择：' + '1.不给，2.给，3.重新随机,4.返回'))
            if xz_gg == 1:
                ran = '不给'
                pass
            elif xz_gg == 3:
                ran = random.choice(lst)
                print(ran)
                time.sleep(0.422)
                pass
            elif xz_gg == 4:
                break
            else:
                ran = '给'
                pass
            pass
    elif xz == 5:
        break
    pass


print('程序正在退出')
time.sleep(0.6222)
pass

        