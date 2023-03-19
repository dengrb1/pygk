import os
from tkinter import *
from tkinter import messagebox

root = Tk()
student_net = Button(root)
student_net["text"] = '解除网络控制'
def del_net(e):
    os.system("taskkill /f /im GATESRV.exe")
    os.system("taskkill /f /im MasterHelper.exe")
    os.system("sc stop TDnetfilter")
    messagebox.showinfo("Student killer", "极域断网程序以破解")
    pass
student_net.bind("<Button-1>", del_net)


student_killer = Button(root)
student_killer['text'] = "关闭极域"
def studentmain_killer(e):
    os.system("taskkill /f /t /im studentmain.exe")
    messagebox.showinfo("student Killer", "程序已关闭")
    pass
student_killer.bind('<Button-1>', studentmain_killer)


py_exit = Button(root)
py_exit['text'] = '退出'
def exit_student(e):
    root.destroy()
    messagebox.showwarning("Student Helper", "程序已退出")
    pass
py_exit.bind('<Button-1>', exit_student)


student_file = Button(root)
student_file['text'] = "解除U盘控制"
def student_sc_file(e):
    os.system("sc stop TDfilefilter")
    messagebox.showinfo("Student File", "已解除")
    pass
student_file.bind('<Button-1>', student_sc_file)


student_e = Button(root)
student_e['text'] = "全部操作"
def student_e_everyone(e):
    os.system("taskkill /f /t /im studentmain.exe")
    os.system("taskkill /f /im GATESRV.exe")
    os.system("taskkill /f /im MasterHelper.exe")
    os.system("sc stop TDnetfilter")
    os.system("sc stop TDfilefilter")
    messagebox.showinfo("Student everyone", "已全部操作完成！")
    pass


student_update = Button(root, text="更新内容")
def update(e):
    update_window = Tk()
    update_window.title('程序更新')
    la_update = Label(update_window, text="更新内容")
    la_update_1 = Label(update_window, text="""1.0 程序制作完成
    1.1 新增关闭极域、解除网络限制、解除U盘限制
    1.2 更新内容显示
    1.3 关于模块制作完成，修复一些BUG
    1.7 新增一个小彩蛋""")
    la_sudent_helper_system = Label(update_window, text="当前版本是：1.2.1")
    la_update.pack()
    la_update_1.pack()
    la_sudent_helper_system.pack()
    update_window.geometry('300x300+500+400')
    update_window.mainloop()
    pass
student_update.bind('<Button-1>', update)


student_gk = Button(root, text='关于')
def gk(e):
    gk_window = Tk()
    gk_1 = Label(gk_window, text='student helper')
    gk_2 = Label(gk_window, text='''此程序是由dengrb1开发和编写
    开源地址和教程:https://github.com/dengrb1/pygk
    作者GitHub：https://github.com/dengrb1

    @ 2023-2024 由pygk团队的dengrb1拥有所有权''')
    gk_1.pack()
    gk_2.pack()
    gk_window.title('关于')
    gk_window.geometry('310x300')
    gk_window.mainloop()
    pass
student_gk.bind('<Button-1>', gk)


# 彩蛋程序
student_cd = Button(root , text='彩蛋解锁')
def cd(e):
    messagebox.showinfo('彩蛋', '梁子依是sb中的sb中的大大大sb')
    pass
student_cd.bind('<Button-1>', cd)


student_e.pack()
student_killer.pack()
student_net.pack()
student_file.pack()
student_cd.pack()
student_update.pack()
student_gk.pack()
py_exit.pack()


root.geometry('200x200+500+500')
root.title("student Helper")
root.mainloop()