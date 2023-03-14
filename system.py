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
    1.3 程序加入更新界面，里面只显示更新的内容，不会自动更新！''')
    la_3 = Label(update_window_1, text="当前版本：1.3")
    la_1.pack()
    la_2.pack()
    la_3.pack()
    update_window_1.title('更新内容')
    update_window_1.geometry('200x200+500+400')
    update_window_1.mainloop()
    pass
pip_update.bind('<Button-1>', update_root)


root_update.pack()
pip_pygame.pack()
pip_pyqt.pack()
pip_pyinstaller.pack()
pip_update.pack()
pip_quit.pack()


root.title('pip安装助手')
root.geometry('300x200+300+600')
root.mainloop()
