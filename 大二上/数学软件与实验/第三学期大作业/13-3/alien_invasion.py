import pygame
from settings import Settings
import game_function as gf
from pygame.sprite import Group

def run_game():
    # 初始化游戏,设置,屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))

    # 创建水滴编组
    aliens = Group()

    # 创建水滴群
    gf.create_fleet(ai_settings, screen, aliens)

    # 开始游戏主循环
    while True:
        gf.check_events()
        gf.update_aliens(ai_settings, aliens)
        gf.update_screen(ai_settings, screen, aliens)

run_game()
