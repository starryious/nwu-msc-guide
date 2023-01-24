import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """表示单个水滴的类"""

    def __init__(self, ai_settings, screen):
        """初始化水滴并设置其起始位置"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载水滴图像，并设置其rect属性
        self.image = pygame.image.load('images/raindrop.png')
        self.rect = self.image.get_rect()

        # 每个水滴最初都在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储水滴的准确位置
        self.x = float(self.rect.x)

    def blitme(self):
        """在指定位置绘制水滴"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """移动水滴"""
        self.rect.y += self.ai_settings.alien_speed_factor
