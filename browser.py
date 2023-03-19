import tkinter as tk
import tkinter.ttk as ttk
import webbrowser

class Browser(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        # 创建地址栏
        self.address_bar = ttk.Entry(self.master)
        self.address_bar.pack(side='top', fill='x')
        self.address_bar.bind('<Return>', self.load_url)

        # 创建浏览器窗口
        self.browser_window = tk.Text(self.master, wrap='word')
        self.browser_window.pack(side='bottom', fill='both', expand=True)

        # 创建工具栏
        tool_bar = ttk.Frame(self.master, height=20)
        tool_bar.pack(side='top', fill='x')

        back_button = ttk.Button(tool_bar, text='<', command=self.back)
        back_button.pack(side='left')

        forward_button = ttk.Button(tool_bar, text='>', command=self.forward)
        forward_button.pack(side='left')

        refresh_button = ttk.Button(tool_bar, text='Refresh', command=self.refresh)
        refresh_button.pack(side='left')

    def load_url(self, event=None):
        url = self.address_bar.get()
        if '://' not in url:
            url = 'http://' + url
        webbrowser.open(url)
        self.browser_window.insert('end', f'Loading {url}...\n')

    def back(self):
        self.browser_window.event_generate('<<Back>>')

    def forward(self):
        self.browser_window.event_generate('<<Forward>>')

    def refresh(self):
        self.browser_window.event_generate('<<Refresh>>')

if __name__ == '__main__':
    root = tk.Tk()
    root.title('Tkinter Browser')
    root.geometry('640x480')

    browser = Browser(root)
    browser.pack(side='bottom', fill='both', expand=True)

    root.mainloop()