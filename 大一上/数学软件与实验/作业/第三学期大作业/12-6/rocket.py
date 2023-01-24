import pygame
class Rocket():
    """docstring for Rocket"""
    def __init__(self,ai_setting, screen):
        self.screen = screen
        self.image = pygame.image.load('image/plane.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.ai_setting = ai_setting
        self.rect.x = 0
        self.rect.centery = self.screen_rect.centery
        self.center = float(self.rect.centerx)
        self.centery = float(self.rect.centery)
        self.moving_up = False
        self.moving_down = False
    def update(self):
        if self.moving_up and self.rect.top > 0:
            self.centery -= self.ai_setting.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery +=self.ai_setting.ship_speed_factor
        self.rect.centery = self.centery
    def blitme(self):
        self.screen.blit(self.image,self.rect)