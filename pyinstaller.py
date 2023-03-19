import tkinter as tk
import tkinter.ttk as ttk
import webbrowser

class Browser:
    def __init__(self):
        # 创建窗口
        self.window = tk.Tk()
        self.window.geometry("800x600")

        # 创建地址栏和按钮
        self.url_entry = ttk.Entry(self.window, width=60)
        self.url_entry.pack(side="left", padx=10)

        self.go_button = ttk.Button(self.window, text="Go", command=self.load_url)
        self.go_button.pack(side="left")

        # 创建浏览器窗口
        self.browser_frame = tk.Frame(self.window, borderwidth=2)
        self.browser_frame.pack(fill="both", expand=True)

        # 进入主循环
        self.window.mainloop()

    def load_url(self):
        # 获取用户输入的URL
        url = self.url_entry.get()

        # 在浏览器窗口中打开URL
        webbrowser.open(url)

if __name__ == '__main__':
    browser = Browser()