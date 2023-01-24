import pygame
from pygame.sprite import Sprite
class Bullets(Sprite):
    """docstring for Bullets"""
    def __init__(self, ai_settings, screen, rocket):
        super(Bullets, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centery = rocket.rect.centery
        self.rect.right = rocket.rect.right
        # 存储小数表示的子弹位置
        self.x = float(self.rect.x)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
    def update(self):
        self.x += self.speed_factor
        self.rect.x = self.x
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)