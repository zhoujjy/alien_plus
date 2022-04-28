# -*- coding = utf-8 -*-
# @Time: 2022/4/28 8:14
# @Author : zj
# @File : main.py
# @Software: PyCharm

import sys
import pygame

from ship import Ship
from settings import Settings


class AlienMain:
    """游戏主类"""

    def __init__(self):
        """初始化游戏"""
        self.settings = Settings()

        # 初始化屏幕
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)  # 全屏
        pygame.display.set_caption("Alien Invasion")
        self.bg_color = self.settings.bg_color

        # 创建飞船
        self.ship = Ship(self)


    def check_events(self):
        """响应按键和鼠标事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:  # 按下键盘
                if event.key == pygame.K_ESCAPE:  # 按下esc键退出
                    sys.exit()
                if event.key == pygame.K_RIGHT:  # 右移
                    self.ship.move_right = True
                if event.key == pygame.K_LEFT:  # 左移
                    self.ship.move_left = True
            elif event.type == pygame.KEYUP:  # 松开键盘
                if event.key == pygame.K_RIGHT:
                    self.ship.move_right = False
                if event.key == pygame.K_LEFT:
                    self.ship.move_left = False

    def update_screen(self):
        """更新屏幕上的图像，并切换到新屏幕"""

        # 每次循环时都重绘屏幕
        self.screen.fill(self.bg_color)
        self.ship.blit_ship()

        # 更新屏幕
        pygame.display.flip()

    def run_game(self):
        """开始游戏"""
        # 主循环
        while True:
            # 检测事件
            self.check_events()
            self.ship.move()
            # 重绘屏幕
            self.update_screen()


if __name__ == '__main__':
    # 创建游戏对象
    alien_main = AlienMain()
    # 启动游戏
    alien_main.run_game()
