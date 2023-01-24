import sys
import pygame
from rocket import Rocket
from setting import Setting
from pygame.sprite import Group
import game_functions as gf
def run():
    pygame.init()
    ai_setting = Setting()
    screen =pygame.display.set_mode((ai_setting.screen_width,ai_setting.screen_height))
    pygame.display.set_caption("Rocket")
    r = Rocket(ai_setting,screen)
    bullets = Group()
    while True:
        gf.check_events(ai_setting,screen,r,bullets)
        r.update()
        bullets.update()
        gf.update_screen(ai_setting,screen,r,bullets)
run()