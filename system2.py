# 初始化程序
import os
import time


# 定义变量
pyinstaller_setup = 'pip install pyinstaller'
pygame_setup = 'pip install pygame'
pyqt_setup = 'pip install pyqt5'
root_text = '1.pyinstaller安装，2.pygame安装，3.pyqt5安装，4.更新日志，5.删除库，6.退出,7.Requests安装'
setup_ok = '安装完成'
clean = 'cls'
root_2 = '1.删除pyinstaller，2.删除pygame，3删除pyqt5，4.Requests删除'
remove_pyinstaller = 'pip uninstall pyinstaller'
remove_pygame = 'pip uninstall pygame'
remove_pyqt5 = 'pip uninstall pyqt5'
remove = '删除完成'
remove_Requests = 'pip uninstall Requests'
Requests_setup = 'pip install Requests'


# 选择模块
while 1:
    print(root_text)
    xz = int(input('请选择:'))
    if xz == 1:
        os.system(pyinstaller_setup)
        print(setup_ok)
        time.sleep(1.2)
        pass
    elif xz == 2:
        os.system(pygame_setup)
        print(setup_ok)
        time.sleep(1.2)
        pass
    elif xz == 3:
        os.system(pyqt_setup)
        print(setup_ok)
        time.sleep(1.2)
        pass
    elif xz == 6:
        break
    elif xz == 7:
        os.system(Requests_setup)
        print(setup_ok)
        time.sleep(1.2)
        pass
    elif xz == 4: # 更新模块
        print('更新日志')
        print('''1.0 程序项目建立完毕
        1.1 新增pyinstaller、pygame、pyqt5安装
        1.2 新增更新日志显示
        1.3 删除库模式新增（暂未完成）
        1.3.1 删除库模式完成
        1.4 新增Requests库安装和删除
        1.5 新增关于选项''')
        print('当前版本：1.3')
        while 1:
            if int(input('是否退出？' + '1是，2不是')) == 2:
                continue
            else:
                break
            pass
        pass
    elif xz == 5: # 删除库模块
        os.system(clean)
        print(root_2)
        xz2 = int(input('请选择：'))
        if xz2 == 1:
            os.system(remove_pyinstaller)
            print(remove)
            time.sleep(1.2)
            pass
        elif xz2 == 2:
           os.system(remove_pygame)
           print(remove)
           time.sleep(1.2)
           pass
        elif xz2 == 3:
            os.system(remove_pyqt5)
            print(remove)
            time.sleep(1.2)
            pass
        elif xz2 == 4:
            os.system(remove_Requests)
            print(remove)
            time.sleep(1.2)
            pass
        else:
            print('格式不正确')
            time.sleep(1.2)
            pass
        pass
    else:
        print('没有这个选择')
        time.sleep(0.92)
        pass


# 程序退出模块
print('程序退出')
time.sleep(0.62)
exit()

