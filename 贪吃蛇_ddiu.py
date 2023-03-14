import pygame
import random

# 初始化pygame
pygame.init()

# 游戏窗口大小
window_width = 800
window_height = 600

# 创建游戏窗口
game_display = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('贪吃蛇')

# 颜色定义
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# 贪吃蛇的大小
snake_block_size = 10

# 游戏时钟
clock = pygame.time.Clock()

# 字体定义
font_style = pygame.font.SysFont(None, 30)


def our_snake(snake_block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(game_display, green, [x[0], x[1], snake_block_size, snake_block_size])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    game_display.blit(mesg, [window_width / 6, window_height / 3])


def game_loop():
    game_over = False
    game_close = False

    # 贪吃蛇的初始位置
    x1 = window_width / 2
    y1 = window_height / 2

    # 贪吃蛇的移动速度
    x1_change = 0
    y1_change = 0

    # 贪吃蛇的长度
    snake_list = []
    length_of_snake = 1

    # 食物的位置
    food_x = round(random.randrange(0, window_width - snake_block_size) / 10.0) * 10.0
    food_y = round(random.randrange(0, window_height - snake_block_size) / 10.0) * 10.0

    # 游戏循环
    while not game_over:
        
        # 游戏结束界面
        while game_close:
            game_display.fill(white)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        # 事件循环处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block_size
                    x1_change = 0

        # 判断是否触碰到边界
        if x1 >= window_width or x1 < 0 or y1 >= window_height or y1 < 0:
            game_close = True

        # 更新贪吃蛇的位置
        x1 += x1_change
        y1 += y1_change

        # 绘制游戏界面
        game_display.fill(white)
        pygame.draw.rect(game_display, red, [food_x, food_y, snake_block_size, snake_block_size])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(snake_block_size, snake_list)
        pygame.display.update()

        # 判断是否吃到食物
        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, window_width - snake_block_size) / 10.0) * 10.0
            food_y = round(random.randrange(0, window_height - snake_block_size) / 10.0) * 10.0
            length_of_snake += 1

        # 控制游戏帧率
        clock.tick(30)

    # 退出pygame
    pygame.quit()
    quit()


game_loop()
