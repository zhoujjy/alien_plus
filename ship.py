# -*- coding = utf-8 -*-
# @Time: 2022/4/28 8:40
# @Author : zj
# @File : ship.py
# @Software: PyCharm
import pygame


class Ship:
    """飞船类"""

    def __init__(self, ai_game):
        """初始化飞船"""
        # 获取屏幕对象
        self.screen = ai_game.screen

        # 获取屏幕的rect对象
        self.screen_rect = ai_game.screen.get_rect()

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # 将飞船放在屏幕底部中央
        self.rect.midbottom = self.screen_rect.midbottom

    def blit_ship(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
