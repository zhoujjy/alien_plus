# -*- coding = utf-8 -*-
# @Time: 2022/5/22 21:59
# @Author : zj
# @File : test_ship.py
# @Software: PyCharm

import unittest
from ship import Ship
from alien_main import AlienMain


class TestMove(unittest.TestCase):
    """测试飞船的移动"""

    def test_left_move(self):
        # 飞船左移测试
        ship = Ship(AlienMain())
        ship.move_left = True
        ship.move()
        # 飞船坐标小于屏幕底部中心坐标
        self.assertLess(ship.rect.midbottom, ship.screen_rect.midbottom)

    def test_right_move(self):
        # 飞船右移测试
        ship = Ship(AlienMain())
        ship.move_right = True
        ship.move()
        # 飞船坐标大于屏幕底部中心坐标
        self.assertGreater(ship.rect.midbottom, ship.screen_rect.midbottom)
