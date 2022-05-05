# -*- coding = utf-8 -*-
# @Time: 2022/5/5 8:36
# @Author : zj
# @File : game_stats.py
# @Software: PyCharm
class GameStats:
    """游戏统计信息"""
    def __init__(self,ai_game):
        """初始化统计信息"""
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = True

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit