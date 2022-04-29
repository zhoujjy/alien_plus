# -*- coding = utf-8 -*-
# @Time: 2022/4/28 8:14
# @Author : zj
# @File : main.py
# @Software: PyCharm

import sys
import pygame

from ship import Ship
from settings import Settings
from bullet import Bullet
from alien import Alien


class AlienMain:
    """游戏主类"""

    def __init__(self):
        """初始化游戏"""
        self.settings = Settings()

        # 初始化屏幕
        pygame.init()
        # self.screen = pygame.display.set_mode((1200, 800))
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)  # 全屏
        pygame.display.set_caption("Alien Invasion")
        self.bg_color = self.settings.bg_color

        # 创建飞船
        self.ship = Ship(self)
        # 创建一个用于存储子弹的精灵组
        self.bullets = pygame.sprite.Group()
        # 创建一个用于存储外星人的精灵组
        self.aliens = pygame.sprite.Group()
        self.create_fleet()

    def create_fleet(self):
        """创建外星人群"""
        # 创建一个外星人，并计算一行可容纳多少个外星人
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        screen_width, screen_height = self.screen.get_rect().size  # 获取屏幕的宽高
        available_space_x = screen_width - 4 * alien_width
        number_aliens_x = available_space_x // (4 * alien_width)

        # 计算可容纳多少行
        available_space_y = screen_height - 6 * alien_height
        number_rows = available_space_y // (2 * alien_height)

        # 创建外星人群
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self.create_alien(alien_number, row_number)

    def create_alien(self,alien_number, row_number):
        """创建一个外星人并将其放在当前行"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 4 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def check_events(self):
        """响应按键和鼠标事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:  # 按下键盘
                self.check_keydown_events(event)
            elif event.type == pygame.KEYUP:  # 松开键盘
                self.check_keyup_events(event)

    def check_keydown_events(self, event):
        """键盘按下事件处理"""
        if event.key == pygame.K_ESCAPE:  # 按下esc键退出
            sys.exit()
        if event.key == pygame.K_RIGHT:  # 右移
            self.ship.move_right = True
        if event.key == pygame.K_LEFT:  # 左移
            self.ship.move_left = True
        if event.key == pygame.K_SPACE:  # 发射子弹
            self.fire_bullet()

    def fire_bullet(self):
        """发射子弹"""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)  # 将子弹添加到精灵组中

    def check_keyup_events(self, event):
        """键盘松开处理"""
        if event.key == pygame.K_RIGHT:
            self.ship.move_right = False
        if event.key == pygame.K_LEFT:
            self.ship.move_left = False

    def update_bullets(self):
        """更新子弹的位置"""
        self.bullets.update()
        # 删除已消失的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def update_aliens(self):
        """更新外星人的位置"""
        self.check_feet_edges()
        self.aliens.update()

    def check_feet_edges(self):
        """外星人到达边缘时，改变方向"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self.change_fleet_direction()
                break

    def change_fleet_direction(self):
        """改变外星人群的方向"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.alien_y_speed
        self.settings.fleet_direction *= -1

    def update_screen(self):
        """更新屏幕上的图像，并切换到新屏幕"""

        # 每次循环时都重绘屏幕
        self.screen.fill(self.bg_color)
        self.ship.blit_ship()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        # 更新屏幕
        pygame.display.flip()

    def run_game(self):
        """开始游戏"""
        # 主循环
        while True:
            self.check_events()
            self.ship.move()
            self.update_bullets()
            self.update_aliens()
            self.update_screen()


if __name__ == '__main__':
    # 创建游戏对象
    alien_main = AlienMain()
    # 启动游戏
    alien_main.run_game()
