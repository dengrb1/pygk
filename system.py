from tkinter import *
from tkinter import messagebox
import time
import os


root = Tk()


pip_pyinstaller = Button(root, text="pyinstaller安装")
def pyinstaller(e):
    os.system("pip install pyinstaller")
    messagebox.showinfo("pip", "程序安装完成")
    pass
pip_pyinstaller.bind('<Button-1>', pyinstaller)


root_update = Button(root, text="pip检测升级")
def update(e):
    messagebox.showerror("pip update", "无法使用！（正在测试）")
    pass
    '''sc = Tk()
    text1 = Text(sc)
    sc.title("pip_update")
    sc.geometry('300x200+300+200')
    pip_update_1 = text1 + "-m pip install --upgrade pip"
    ok_update = Button(sc, text="确定")
    def ok(e):
        os.system(pip_update_1)
        messagebox.showwarning("pip更新完成")
        pass
    quit_update = Button(sc, text="返回")
    def exit_update(e):
        sc.destroy()
        pass
    text1.pack()
    ok_update.bind('<Button-1>', ok)
    quit_update.bind('Button-1>', exit_update)
    text1.pack()
    ok_update.pack()
    quit_update.pack()
    sc.mainloop()
    pass'''
root_update.bind('<Button-1>', update)


pip_pygame = Button(root, text="pygame库安装")
def pygame(e):
    os.system("pip install pygame")
    messagebox.showwarning("pygame install", "pygame安装完成")
    pass
pip_pygame.bind('<Button-1>', pygame)


pip_pyqt = Button(root, text="pyqt5安装")
def pyqt5(e):
    os.system("pip install pyqt5")
    messagebox.showwarning("pip pyqt5", "pyqt5安装成功")
    pass
pip_pyqt.bind('<Button-1>', pyqt5)


pip_quit = Button(root, text="exit")
def pip_exit(e):
    root.destroy()
    messagebox.showwarning("pip安装助手", "程序已退出")
    pass
pip_quit.bind('<Button-1>', pip_exit)


pip_update = Button(root, text='更新内容')
def update_root(e):
    update_window_1 = Tk()
    la_1 = Label(update_window_1, text='更新内容')
    la_2 = Label(update_window_1, text='''1.0 程序制作完成
    1.2 程序新增pyqt5、pygame、pyinstaller安装
    1.3 程序加入更新界面，里面只显示更新的内容，不会自动更新！
    1.4 新增Requests库安装和删除''')
    la_3 = Label(update_window_1, text="当前版本：1.4")
    la_1.pack()
    la_2.pack()
    la_3.pack()
    update_window_1.title('更新内容')
    update_window_1.geometry('400x200+500+400')
    update_window_1.mainloop()
    pass
pip_update.bind('<Button-1>', update_root)


'''remove_1 = Tk()
remove_open = Button(root ,text='删除库模式')
def remove(e):
    # def处理运行代码
    def pyinstaller_remove(e):
        os.system('pip uninstall pyinstaller')
        messagebox.showinfo('remove', '删除完成')
        pass
    def pygame_remove(e):
        os.system('pip uninstall pygame')
        messagebox.showinfo('remove', '删除完成')
        pass
    def pyqt_remove(e):
        os.system('pip uninstall pyqt5')
        messagebox.showinfo('remove', '删除完成')
        pass
    remove_pygame.bind('<Button-1>',pygame_remove)
    remove_pyinstaller.bind('<Button-1>', pyinstaller_remove)
    remove_pyqt5.bind('<Button-1>', pyqt_remove)
    remove_pygame.pack()
    remove_pyqt5.pack()
    remove_pyinstaller.pack()
    # 加载删除库的Gui
    remove_1.title('remove')
    remove_1.geometry('200x200+450+400')
    remove_1.mainloop()
    pass
remove_open.bind('<Button-1>', remove)'''

remove_pyinstaller = Button(root, text='删除pyinstaller库')
remove_pygame = Button(root, text='删除pygame')
remove_pyqt5 = Button(root, text='删除pyqt5')
remove_Requests = Button(root, text='删除Requests')
def pygame_remove(e):
    os.system('pip uninstall pygame')
    messagebox.showinfo('remove', '删除完成')
    pass
def pyinstaller_remove(e):
    os.system('pip uninstall pyinstaller')
    messagebox.showinfo('remove', '删除完成')
    pass
def pyqt_remove(e):
    os.system('pip uninstall pyqt5')
    messagebox.showinfo('remove', '删除完成')
    pass
def Requests_remove(e):
    os.system('pip uninstall Requests')
    messagebox.showinfo('remove', '删除完成')
    pass
remove_pygame.bind('<Button-1>', pygame_remove)
remove_pyinstaller.bind('<Button-1>', pyinstaller_remove)
remove_pyqt5.bind('<Button-1>', pyqt_remove)
remove_Requests.bind('<Button-1>', Requests_remove)    


pip_Requests = Button(root, text='Requests安装')
def Requests(e):
    os.system('pip install Requests')
    messagebox.showinfo('pip Requests', 'Requests安装完成')
    pass
pip_Requests.bind('<Button-1>', Requests)



# root_update.pack()
pip_pygame.pack()
pip_pyqt.pack()
pip_pyinstaller.pack()
pip_Requests.pack()
# remove_open.pack()
remove_pygame.pack()
remove_pyinstaller.pack()
remove_pyqt5.pack()
remove_Requests.pack()
pip_update.pack()
pip_quit.pack()


root.title('pip安装助手')
root.geometry('200x350+300+600')
root.mainloop()
