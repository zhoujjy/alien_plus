# -*- coding = utf-8 -*-
# @Time: 2022/4/21 11:43
# @Author : zj
# @File : settings.py
# @Software: PyCharm

class Settings:
    """设置类"""
    def __init__(self):

        '颜色设置'
        self.bg_color = (230,230,230)
        self.bg_color3 = (230,230,230)
        self.bg_color4 = (0, 255, 0)

        '飞船设置'
        self.life_num = 3 # 定义生命数量
        self.ship_speed = 1 # 定义飞船移动速度

        '子弹设置'
        self.bullet_speed = 1 # 定义子弹的速度
        self.bullet_allowed = 10 # 定义允许发射的子弹数量
        self.bullet_width = 3 # 子弹宽
        self.bullet_height = 15 # 子弹高
        self.bullet_color = (60,60,60) # 子弹颜色

        '外星人设置'
        self.alien_x_speed = 1 # 定义外星人移动速度
        self.alien_y_speed = 30 # 定义外星人移动速度

        '游戏节奏'
        self.speedup_scale = 1.1 # 定义游戏速度提升的比例
        # self.speedlist = (ship_speed,bullet_speed,alien_y_speed)
