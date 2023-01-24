class Settings():
    """存储所有的类 """
    def __init__(self):
        """初始化游戏 """
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 水滴低落的速度设置
        self.alien_speed_factor = 1