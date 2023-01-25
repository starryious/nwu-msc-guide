import sys

import pygame
from bullet import Bullets


def check_keydown_events(event, ai_setting, screen, rocket, bullets):
    if event.key == pygame.K_UP:
        rocket.moving_up = True
    elif event.key == pygame.K_DOWN:
        rocket.moving_down = True
    elif event.key == pygame.K_SPACE:
        new_bullet = Bullets(ai_setting, screen, rocket)
        bullets.add(new_bullet)


def check_keyup_events(event, rocket):
    if event.key == pygame.K_UP:
        rocket.moving_up = False
    elif event.key == pygame.K_DOWN:
        rocket.moving_down = False


def check_events(ai_settings, screen, rocket, bullets):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Quit")
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, rocket, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, rocket)


def update_bullet(bullets):
    for bullet in bullets:
        if bullet.rect_left <= 0:
            bullets.remove(bullet)


def update_screen(ai_settings, screen, rocket, bullets):
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    rocket.blitme()
    pygame.display.flip()