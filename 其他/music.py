import tkinter as tk
from tkinter import filedialog
import pygame

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("300x150")

        self.music_file = None
        self.isPlaying = False

        self.create_ui()

    def create_ui(self):
        # 创建UI界面
        self.select_button = tk.Button(self.root, text="选择歌曲", command=self.select_music)
        self.play_button = tk.Button(self.root, text="播放", command=self.play_music)
        self.stop_button = tk.Button(self.root, text="停止", command=self.stop_music)

        self.select_button.pack(pady=10)
        self.play_button.pack(pady=10)
        self.stop_button.pack(pady=10)

    def select_music(self):
        # 选择歌曲文件
        self.music_file = filedialog.askopenfilename(defaultextension=".mp3", filetypes=[("MP3 Files", "*.mp3")])

    def play_music(self):
        # 播放歌曲
        if self.music_file is not None:
            if not self.isPlaying:
                pygame.mixer.init()
                pygame.mixer.music.load(self.music_file)
                pygame.mixer.music.play()
                self.isPlaying = True
            else:
                pygame.mixer.music.unpause()
        else:
            print("请选择歌曲文件！")

    def stop_music(self):
        # 停止歌曲
        if self.isPlaying:
            pygame.mixer.music.stop()
            self.isPlaying = False

if __name__ == "__main__":
    root = tk.Tk()
    player = MusicPlayer(root)
    root.mainloop()
