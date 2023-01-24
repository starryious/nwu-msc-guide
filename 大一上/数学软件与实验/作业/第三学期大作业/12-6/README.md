## 练习12-6:

> 姓名:
> 学号:
> 年级:2021级
> 专业:应用统计学
> 课程:数学软件与实验

### 一.题目   :

**侧面射击**  编写一个游戏，将一艘飞船放在屏幕左边，并允许玩家上下移动 飞船。在玩家按空格键时，让飞船发射一颗在屏幕中向右穿行的子弹，并在子弹离开屏 幕而消失后将其删除.

### 二.代码以及相关解释 :

首先根据教材中的外星人设置,相似的方法设置游戏参数,该段代码在项目的`settings.py`下

```Python
class Settings():
    """存储所有的类 """
    def __init__(self):
        """初始化游戏 """
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船的设置
        self.ship_speed_factor = 1.5

        # 子弹设置
        self.bullet_speed_factor = 1
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
```

接着创建飞船的类,该段代码在项目的`ship.py` 下,根据教材所给源代码进行更改,主要更改位置为`self.rect.x = 0` , `self.rect.bottom = self.screen_rect.centery` ,`if self.moving_up and self.rect.top > 0:` ,` if self.moving_down and self.rect.bottom < self.screen_rect.bottom:` 将源代码飞船在底部移动更改为了将飞船在侧面移动

```python
import pygame

class Ship():
    def __init__(self, ai_settings,screen):
        """初始化飞船并设置其初始位置"""
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/rocket.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕左侧中央
        self.rect.x = 0
        self.rect.bottom = self.screen_rect.centery

        #在飞船的属性center中存储小数值
        self.center = float(self.rect.centerx)
        self.centery = float(self.rect.centery)


        # 移动标志
        self.moving_up = False
        self.moving_down = False
    def update(self):
        """"根据移动标志调整飞船的位置"""
        # 更新飞船的center值，而不是rect
        if self.moving_up and self.rect.top > 0:
            self.centery -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.ai_settings.ship_speed_factor
         # 根据self.center更新rect对象
        self.rect.centery = self.centery

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

```

创建子弹的类,该段代码在项目的`bullet.py` 下, 根据教材源代码主要将子弹从下到上更改为了从左到右,具体更改方法就是将代码中y的变化量改为x的变化量即可

```python
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """一个对飞船发射的子弹进行管理的类"""

    def __init__(self, ai_settings, screen, ship):
        """在飞船所处的位置创建一个子弹对象"""
        super(Bullet, self).__init__()
        self.screen = screen

        # 在(0,0)处创建一个表示子弹的矩形，再设置正确的位置
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centery = ship.rect.centery
        self.rect.right = ship.rect.right

        # 存储用小数表示的子弹位置
        self.x = float(self.rect.x)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """向右移动子弹"""
        # 更新表示子弹位置的小数值
        self.x += self.speed_factor
        # 更新表示子弹的rect的位置
        self.rect.x = self.x

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)
```



游戏设置,该段代码在项目的`game_function.py` 下,由于是根据教材源代码进行更改,保留了只能在屏幕中射出三颗子弹的限制

```python
import sys

import pygame

from bullet import Bullet

def check_keydown_events(event, ai_settings,screen,ship,bullets):
    """响应按键"""
    if event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
       fire_bullet(ai_settings,screen,ship,bullets)
def fire_bullet(ai_settings,screen,ship,bullets):
    """若还没有达到限制,就发射一颗子弹"""
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
def check_keyup_events(event, ship):
    """响应松开"""
    if event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False

def check_events(ai_settings, screen, ship, bullets):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship, bullets):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)
    # 在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    # 让最近绘制的屏幕可见
    pygame.display.flip()

def update_bullets(bullets):
        """更新子弹的位置，并删除已消失的子弹"""
        # 更新子弹的位置
        bullets.update()

        # 删除已消失的子弹
        for bullet in bullets.copy():
            if bullet.rect.right >= 1200 :
                bullets.remove(bullet)


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

由于markdown的图片只能贴本地图片和网上图片,这里把图片上传图床.

![43ueC.png](https://i.328888.xyz/2022/12/17/43ueC.png)



### 四.遇到的问题以及解决方法

**Error1** 子弹发出位置的更改.

**Solution** 子弹发出位置为飞船的右侧中部,更改为以下代码解决:

```python
  self.rect.centery = ship.rect.centery
        self.rect.right = ship.rect.right
```

这里注意是`self.rect.centery` 而不是源代码中的 `self.rect.center`

