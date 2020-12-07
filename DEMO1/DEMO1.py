import pygame
import sys

clock = pygame.time.Clock()
from pygame.locals import *
pygame.init() # 初始化pygame

pygame.display.set_caption('Demo1') # 标题栏名称

WINDOW_SIZE = (400,400) # 设定窗口的尺寸

screen = pygame.display.set_mode(WINDOW_SIZE,0,32) # 创建窗口

player_img = pygame.image.load('./img/player_idl.png') # 加载玩家图像

moving_right = False
moving_left = False

player_location = [50,50]

while True: #循环游戏
    screen.fill((255,255,255))
    screen.blit(player_img,player_location) # 在屏幕上显示玩家图像

    if moving_right == True:
        player_location[0] += 2
    if moving_left == True:
        player_location[0] -= 2

    for event in pygame.event.get(): # 事件循环
        if event.type == QUIT: #检测窗口是否退出
            pygame.quit() # 停止pygame
            sys.exit() # 停止脚本
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                moving_right = True
            if event.key == K_LEFT:
                moving_left = True
        if event.type == KEYUP:
            if event.key == K_RIGHT:
                moving_right = False
            if event.key == K_LEFT:
                moving_left = False

    pygame.display.update() # 更新显示
    clock.tick(60) #60fps
