# coding=utf-8
'''
File: test16.py
Project: test16
File Created: Monday, 23rd April 2018 4:26:56 pm
Author: <<dpj>> (<<idle0423@126.com>>)
'''

import pygame
import sys
import random
from pygame.color import THECOLORS
import math

# pygame.init()
# screen = pygame.display.set_mode([640, 480])
# screen.fill([255, 255, 255])
# # 画圆
# # pygame.draw.circle(screen, [0, 0, 255], [320, 240], 30, 0)

# # 画矩形，rect()矩形参数是个列表
# # pygame.draw.rect(screen, [0, 0, 255], [250, 150, 300, 200], 0)

# # 画矩形，rect()矩形参数是个列表变量
# # my_list = [250, 150, 300, 200]
# # pygame.draw.rect(screen, [0, 0, 255], my_list, 0)

# # 画矩形，rect()矩形参数是个矩形对象变量
# my_rect = pygame.Rect(250, 150, 300, 200)
# pygame.draw.rect(screen, [0, 0, 255], my_rect, 2)
# pygame.display.flip()
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running =False

# pygame.quit()

# 画随机颜色的矩形
# pygame.init()
# screen = pygame.display.set_mode([640, 480])
# screen.fill([255, 255, 255])

# for i in range(100):
#     width = random.randint(0, 250)
#     height = random.randint(0, 100)
#     top = random.randint(0, 400)
#     left = random.randint(0, 500)
#     color_name = random.choice(THECOLORS.keys())
#     print random.choice(THECOLORS.keys())
#     color = THECOLORS[color_name]
#     line_width = random.randint(1, 3)
#     pygame.draw.rect(screen, color, [left, top, width, height], line_width)

# pygame.display.flip()
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
# pygame.quit()

# 画正弦曲线（小矩形，未连接）
# pygame.init()
# screen = pygame.display.set_mode([640, 480])
# screen.fill([255, 255, 255])
# for x in range(0, 640):
#     y = int(math.sin(x / 640.0 * 4 * math.pi) * 200 + 240)
#     pygame.draw.rect(screen, [0, 0, 0], [x, y, 1, 1], 1)

# pygame.display.flip()
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
# pygame.quit()

# 画正弦曲线（点连接）
# pygame.init()
# screen = pygame.display.set_mode([640, 480])
# screen.fill([255, 255, 255])
# plotPoints = []
# for x in range(0, 640):
#     y = int(math.sin(x / 640.0 * 4 * math.pi) * 200 + 240)
#     plotPoints.append([x, y])
# pygame.draw.lines(screen, [0, 0, 0], False, plotPoints, 2)
# pygame.display.flip()
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
# pygame.quit()

# 画树叶，将点连接起来
# pygame.init()

# dots = [[221, 432], [225, 331],  [133, 342], [141, 310],
#         [51, 230],   [74, 217],  [58, 153],  [114, 164],
#         [123, 135], [176, 190], [159, 77],  [193, 93],
#         [230, 28],  [267, 93],  [301, 77],  [284, 190], 
#         [327, 135], [336, 164], [402, 153], [386, 217], 
#         [409, 230],  [319, 310], [327, 342], [233, 331],  
#         [237, 432]]

# screen = pygame.display.set_mode([640, 480])
# screen.fill([255, 255, 255])
# pygame.draw.lines(screen, [255, 0, 0], True, dots, 2)
# pygame.display.flip()
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
# pygame.quit()

# 显示一个沙滩球
# pygame.init()
# screen = pygame.display.set_mode([640, 480])
# screen.fill([255, 255, 255])
# my_ball = pygame.image.load("beach_ball.png")
# screen.blit(my_ball, [50, 50])
# pygame.display.flip()
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
# pygame.quit()

# 沙滩球移动
# pygame.init()
# screen = pygame.display.set_mode([640, 480])
# screen.fill([255, 255, 255])
# my_ball = pygame.image.load("beach_ball.png")
# screen.blit(my_ball, [50, 50])
# pygame.display.flip()
# pygame.time.delay(2000)
# screen.blit(my_ball, [150, 50])
# pygame.display.flip()
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
# pygame.quit()

# 沙滩球移动后，擦掉原来位置的球
# pygame.init()
# screen = pygame.display.set_mode([640, 480])
# screen.fill([255, 255, 255])
# my_ball = pygame.image.load("beach_ball.png")
# screen.blit(my_ball, [50, 50])
# pygame.display.flip()
# pygame.time.delay(2000)
# screen.blit(my_ball, [150, 50])
# pygame.draw.rect(screen, [255, 255, 255], [50, 50, 90, 90], 0)
# pygame.display.flip()
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
# pygame.quit()

# 循环移动沙滩球
# pygame.init()
# screen = pygame.display.set_mode([640, 480])
# screen.fill([255, 255, 255])
# my_ball = pygame.image.load("beach_ball.png")
# x = 50
# y = 50
# screen.blit(my_ball, [x, y])
# pygame.display.flip()
# for looper in range(1, 100):
#     pygame.time.delay(20)
#     pygame.draw.rect(screen, [255, 255, 255], [x, y, 90, 90], 0)
#     x = x + 5
#     screen.blit(my_ball, [x, y])
#     pygame.display.flip()

# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
# pygame.quit()

# 让沙滩球在边界处左右来回反弹
# pygame.init()
# screen = pygame.display.set_mode([640, 480])
# screen.fill([255, 255, 255])
# my_ball = pygame.image.load("beach_ball.png")
# x = 50
# y = 50
# x_speed = 10

# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     pygame.time.delay(20)
#     pygame.draw.rect(screen, [255, 255, 255], [x, y, 90, 90], 0)
#     x = x + x_speed
#     if x > screen.get_width() - 90 or x < 0:
#         x_speed = - x_speed
#     screen.blit(my_ball, [x, y])
#     pygame.display.flip()
# pygame.quit()

# 让沙滩球在边界处上下左右来回反弹
# pygame.init()
# screen = pygame.display.set_mode([640, 480])
# screen.fill([255, 255, 255])
# my_ball = pygame.image.load("beach_ball.png")
# x = 50
# y = 50
# x_speed = 10
# y_speed = 10

# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     pygame.time.delay(20)
#     pygame.draw.rect(screen, [255, 255, 255], [x, y, 90, 90], 0)
#     x = x + x_speed
#     y = y + y_speed
#     if x > screen.get_width() - 90 or x < 0:
#         x_speed = - x_speed
#     if y > screen.get_height() - 90 or y < 0:
#         y_speed = - y_speed
#     screen.blit(my_ball, [x, y])
#     pygame.display.flip()
# pygame.quit()

# 让沙滩球移动到右边界后，再从左边开始移动
pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill([255, 255, 255])
my_ball = pygame.image.load("beach_ball.png")
x = 50
y = 50
x_speed = 10

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.time.delay(20)
    pygame.draw.rect(screen, [255, 255, 255], [x, y, 90, 90], 0)
    x = x + x_speed
    if x > screen.get_width():
        x = 0
    screen.blit(my_ball, [x, y])
    pygame.display.flip()
pygame.quit()
