## 练习12-4:

> 姓名:
> 学号:
> 年级:2021级
> 专业:应用统计学
> 课程:数学软件与实验

### 一.题目   :

**火箭**  编写一个游戏，它在屏幕中央显示一个火箭,而玩家可使用四个方向键上下左右移动火箭.请务必确保火箭不会移到屏幕外面.

### 二.代码以及相关解释 :

首先根据教材中的外星人设置,相似的方法设置游戏参数,该段代码在项目的`settings.py`下

```Python
class Settings():
    """存储《外星人入侵》的所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        self.ship_speed_factor = 1.5
```

接着创建飞船的类,该段代码在项目的`ship.py` 下,在教材提供的源代码下,加入上下移动即可

```python
import pygame
class Ship():
    def __init__(self, ai_settings, screen):
        """初始化飞船并设置其初始位置"""
        self.screen = screen
        self.ai_settings = ai_settings
        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery


        # 在飞船的属性center中存储小数值
        self.center = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        # 移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """根据移动标志调整飞船的位置"""
        # 更新飞船的center值，而不是rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top > 0:
            self.centery -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.ai_settings.ship_speed_factor

        # 根据self.center更新rect对象
        self.rect.centerx = self.center
        self.rect.centery = self.centery

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
```

`game_function.py` 同样的在源代码的基础上加上键盘的上下方向键

```python
import sys
import pygame


def check_events(ship):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True
            elif event.key == pygame.K_UP:
                ship.moving_up = True
            elif event.key == pygame.K_DOWN:
                ship.moving_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False
            elif event.key == pygame.K_UP:
                ship.moving_up = False
            elif event.key == pygame.K_DOWN:
                ship.moving_down = False


def update_screen(ai_settings, screen, ship):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # 让最近绘制的屏幕可见
    pygame.display.flip()

```



`alien_invasion.py` 根据源代码即可

```python
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)

    # 开始游戏的主循环
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)


run_game()

```

最后是游戏的主函数,该段代码在项目的`alien_invasion.py` 下,根据教材的主函数设定稍修改即可

```python
import pygame

from settings import Settings

from ship import Ship

import game_function as gf

from pygame.sprite import Group

def run_game():
    # 初始化游戏,设置,屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建飞船
    ship=Ship(ai_settings,screen)

    #创建一个用于存储子弹的编组
    bullets = Group()

    # 开始游戏主循环
    while True:
        gf.check_events(ai_settings, screen,ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, bullets)

run_game()

```

### 三.运行游戏截图

由于markdown的图片只能贴本地图片和网上图片,这里把图片上传图床.(图一,生成在中央,图二无法向上移出)

![4m2Ix.png](https://i.328888.xyz/2022/12/17/4m2Ix.png)

![4mHdk.png](https://i.328888.xyz/2022/12/17/4mHdk.png)



### 四.遇到的问题以及解决方法

**Error1** y方向上的定位问题.

**Solution** 添加以下代码解决:

```python
 # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        
  # 在飞船的属性center中存储小数值
        self.center = float(self.rect.centerx)
        self.centery = float(self.rect.centery)
```



