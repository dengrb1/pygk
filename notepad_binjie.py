import tkinter as tk
from tkinter import filedialog
from tkinter.messagebox import askyesno

class TextEditor(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.root.title("Text Editor")
        self.file_path = None
        self.create_widgets()

    def create_widgets(self):
        self.text = tk.Text(self.root)
        self.text.pack(expand=True, fill='both')

        # 创建菜单栏
        menu_bar = tk.Menu(self.root)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="打开", command=self.open_file)
        file_menu.add_command(label="保存", command=self.save_file)
        menu_bar.add_cascade(label="文件", menu=file_menu)
        self.root.config(menu=menu_bar)

    def open_file(self):
        # 打开文件对话框
        file_types = [("Text Files", "*.txt"), ("All Files", "*.*")]
        file_path = filedialog.askopenfilename(title="打开文件", filetypes=file_types)
        if not file_path:
            return
        self.file_path = file_path

        # 读取文件内容
        with open(file_path, 'r', encoding=self.get_encoding()) as f:
            self.text.delete(1.0, tk.END)
            content = f.read()
            self.text.insert(tk.END, content)

    def save_file(self):
        # 如果没有打开过文件，调用另存为
        if not self.file_path:
            self.save_file_as()
            return

        # 存储文件
        with open(self.file_path, 'w', encoding=self.get_encoding()) as f:
            content = self.text.get(1.0, tk.END)
            f.write(content)

    def save_file_as(self):
        # 另存为文件对话框
        file_types = [("Text Files", "*.txt"), ("All Files", "*.*")]
        file_path = filedialog.asksaveasfilename(title="另存为", filetypes=file_types)
        if not file_path:
            return
        self.file_path = file_path
        self.save_file()

    def get_encoding(self):
        # 获取文件编码
        if not self.file_path:
            return 'utf-8'

        with open(self.file_path, 'rb') as f:
            header = f.read(4)
        if header.startswith(b'\xff\xfe'):
            return 'utf-16-le'
        elif header.startswith(b'\xfe\xff'):
            return 'utf-16-be'
        else:
            return 'utf-8'

    def confirm_save(self):
        # 文件有修改时，确认是否保存
        if not self.file_path:
            return True
        with open(self.file_path, 'r', encoding=self.get_encoding()) as f:
            old_content = f.read()
        new_content = self.text.get(1.0, tk.END)
        if old_content.strip() == new_content.strip():
            return True
        else:
            msg = "文件已修改，是否保存？"
            return askyesno("确认", msg)

root = tk.Tk()
app = TextEditor(root)
app.pack(expand=True, fill='both')
root.mainloop()