import pickle

class GameStats():
    """跟踪游戏的统计信息"""
    def __init__(self,ai_settings):
        """初始化统计信息"""
        self.ai_settings = ai_settings
        self.reset_stats()
        # 游戏刚启动时处于活动状态
        self.game_active = False
        # 在任何情况下都不应重置最高得分
        self.high_score = 0

    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
        self.load_high_score()
    def save_high_score(self):
        f=open("high_score.pkl",'wb')
        pickle.dump(str(self.high_score),f,0)
        f.close()

    def load_high_score(self):
        f = open("high_score.pkl", 'rb')
        try:
            str_high_score = pickle.load(f)
            self.high_score=int(str_high_score)
        except EOFError:
            str_high_score = 0
        finally:
            f.close()
