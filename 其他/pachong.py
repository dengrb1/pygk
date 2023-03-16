import tkinter as tk
from tkinter import filedialog
import requests
from bs4 import BeautifulSoup
import urllib.request

class Crawler:
    def __init__(self, root):
        self.root = root
        self.root.title("Crawler")
        self.root.geometry("300x150")

        self.url = None
        self.file_path = None

        self.create_ui()

    def create_ui(self):
        # 创建UI界面
        self.url_label = tk.Label(self.root, text="请输入URL：")
        self.url_entry = tk.Entry(self.root)

        self.music_button = tk.Button(self.root, text="爬取音乐", command=self.crawl_music)
        self.video_button = tk.Button(self.root, text="爬取视频", command=self.crawl_video)

        self.url_label.pack(pady=10)
        self.url_entry.pack(pady=5)
        self.music_button.pack(pady=5)
        self.video_button.pack(pady=5)

    def crawl_music(self):
        # 爬取音乐
        self.url = self.url_entry.get()
        if self.url is not None:
            response = requests.get(self.url)
            soup = BeautifulSoup(response.text, "html.parser")
            songs = soup.find_all("a", {"class": "download-link"})
            for song in songs:
                url = song["href"]
                file_name = url.split("/")[-1]
                self.download_file(url, file_name)
        else:
            print("请输入URL！")

    def crawl_video(self):
        # 爬取视频
        self.url = self.url_entry.get()
        if self.url is not None:
            response = requests.get(self.url)
            soup = BeautifulSoup(response.text, "html.parser")
            videos = soup.find_all("source")
            for video in videos:
                url = video["src"]
                file_name = url.split("/")[-1]
                self.download_file(url, file_name)
        else:
            print("请输入URL！")

    def download_file(self, url, file_name):
        # 下载文件
        if self.file_path is None:
            self.file_path = filedialog.askdirectory()
        file_path = self.file_path + "/" + file_name
        urllib.request.urlretrieve(url, file_path)

if __name__ == "__main__":
    root = tk.Tk()
    crawler = Crawler(root)
    root.mainloop()
