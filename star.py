# -*- coding = utf-8 -*-
# @Time: 2022/5/19 8:11
# @Author : zj
# @File : star.py
# @Software: PyCharm
import random

import pygame


class Star:
    def __init__(self, ai_game):
        """初始化属性"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # 设置属性
        self.font = pygame.font.SysFont(None, 80)
        self.G = random.randint(0, 255)
        self.B = random.randint(0, 255)
        self.R = random.randint(0, 255)

        # 定义星星坐标
        self.x = []
        self.y = []

    def draw_stars(self):
        """绘制星星"""
        # 随机星星坐标
        if len(self.x) < 100:

            for i in range(0, 100):
                self.x.append(random.randint(0, self.screen_rect.width))
                self.y.append(random.randint(0, self.screen_rect.height))

        # 绘制星星
        for i in range(len(self.x)):
            self.fontRead = self.font.render("*", True, (self.R, self.G, self.B))
            self.screen.blit(self.fontRead, (self.x[i], self.y[i]))
