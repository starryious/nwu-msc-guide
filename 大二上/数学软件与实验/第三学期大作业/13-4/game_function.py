import sys
import pygame
from alien import Alien

def check_events():
    """响应按键和鼠标事件"""#(若不添加,点击后游戏可能会未响应)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def get_number_rows(ai_settings, alien_height):
    """计算屏幕可容纳多少行水滴"""
    available_space_y = (ai_settings.screen_height - (2 * alien_height))
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def get_number_aliens_x(ai_settings, alien_width):
    """计算每行可容纳多少个水滴"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """创建一个水滴并将其放在当前行"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(ai_settings, screen, aliens):
    """创建水滴群"""
    # 创建一个水滴，并计算一行可容纳多少个水滴
    # 水滴间距为水滴宽度
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, alien.rect.height)

    # 创建第一行水滴
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def update_screen(ai_settings, screen, aliens):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)
    aliens.draw(screen)

    # 让最近绘制的屏幕可见
    pygame.display.flip()


def update_aliens(ai_settings, aliens,screen):
    """更新整群水滴的位置"""
    aliens.update()

    # 删除已消失的水滴
    for alien in aliens.copy():
        if alien.rect.bottom >= ai_settings.screen_height:
            aliens.remove(alien)

    if alien.rect.bottom >= ai_settings.screen_height:
        for alien_number in range(get_number_aliens_x(ai_settings, alien.rect.width)):
            create_alien(ai_settings, screen, aliens, alien_number, 1)