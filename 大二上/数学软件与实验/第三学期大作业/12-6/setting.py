class Setting():

    def __init__(self):
        """关于游戏的全局设置"""
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (255, 255, 255)
        self.ship_speed_factor = 1.5

        self.bullet_speed_factor = 1
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60)