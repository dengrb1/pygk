import random
import time

num = random.randint(1, 15)

guess = int(input("请输入一个 1-15 之间的整数："))

while guess != num:
    if guess < num:
        print("你猜的数字太小了！")
    else:
        print("你猜的数字太大了！")
    
    guess = int(input("请重新输入一个整数："))

print("恭喜你猜对了！")
time.sleep(3) # 程序会在这里暂停三秒
