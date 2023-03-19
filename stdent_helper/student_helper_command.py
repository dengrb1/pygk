import os
import time

root_text = '1.全部操作，2.关闭极域，3.解除网络限制，4.解除U盘限制，5.更新内容，6.关于，7.退出'
student_killer = 'taskkill /f /t /im studentmain.exe'
student_net = 'sc stop tdnetfilter'
student_file = 'sc stop tdfilefilter'
ok = '操作成功'
cls = 'cls'


while 1:
    print(root_text)
    xz = int(input('请选择：'))
    if xz == 1:
        os.system(student_killer)
        os.system(student_net)
        os.system("taskkill /f /im GATESRV.exe")
        os.system("taskkill /f /im MasterHelper.exe")
        print(ok)
        time.sleep(1.2)
        os.system(cls)
        pass
    elif xz == 7:
        break
    elif xz == 2:
        os.system(student_killer)
        print(ok)
        time.sleep(1)
        os.system(cls)
        pass
    elif xz == 3:
        os.system(student_net)
        os.system("taskkill /f /im GATESRV.exe")
        os.system("taskkill /f /im MasterHelper.exe")
        print(ok)
        time.sleep(1)
        os.system(cls)
        pass
    elif xz == 4:
        os.system(student_file)
        print(ok)
        time.sleep(1)
        os.system(cls)
        pass
    elif xz == 5:
        while 1:
            print('更新内容')
            print('''1.0 程序制作完成
            1.1 新增关闭极域、解除网络限制、解除U盘限制
            1.2 更新内容显示
            1.3 关于模块制作完成，修复一些BUG
            1.7 新增一个小彩蛋''')
            print('1.退出，2.继续看')
            if int(input('请选择:')) == 2:
                os.system(cls)
                continue
            else:
                os.system(cls)
                break
            pass
        pass
    elif xz == 6:
        print('关于本程序')
        print('''此程序是由dengrb1开发和编写
        开源地址和教程:https://github.com/dengrb1/pygk
        作者github：https://github.com/dengrb1
        
        @ 2023-2024由dengrb1拥有所有权''')
        print('1.退出，2.继续看')
        if int(input('请输入')) == 2:
            os.system(cls)
            continue
        else:
            os.system(cls)
            break
        pass
    elif xz == 402:
        while 1:
            for i in range(50):
                print('梁子依是SB中的SB中的大大大SB')
                time.sleep(0.01)
                pass
            if int(input('请选择：' + '1.继续看，2.返回')) == 2:
                break
            else:
                continue
            pass
        pass
    else:
        print('请检查您输入的内容，本程序没有这个选项')
        time.sleep(1.2)
        os.system(cls)
        pass
    pass


        
        


print('程序退出中')
time.sleep(0.62)
exit()