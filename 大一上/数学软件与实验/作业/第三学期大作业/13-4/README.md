## 练习13-4:

> 姓名:
> 学号:
> 年级:2021级
> 专业:应用统计学
> 课程:数学软件与实验

### 一.题目   :

**连绵细雨**  修改为完成练习 13-3 而编写的代码，使得一行雨滴消失在屏幕底 端后，屏幕顶端又出现一行新雨滴，并开始往下落。

### 二.代码以及相关解释 :

`settings.py` 与 `alien.py` 都不变

```Python
class Settings():
    """存储所有的类 """
    def __init__(self):
        """初始化游戏 """
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 水滴低落的速度设置
        self.alien_speed_factor = 1
```



```python
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

```

`game_function` 中在最后增加`  if alien.rect.bottom >= ai_settings.screen_height:
        for alien_number in range(get_number_aliens_x(ai_settings, alien.rect.width)):
            create_alien(ai_settings, screen, aliens, alien_number, 1)` 表示若最后一行消失,重新生成一行雨滴

```python
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
```

最后是游戏的主函数,该段代码在项目的`alien_invasion.py` 下,根据教材的主函数设定稍修改即可

```python
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
        gf.update_aliens(ai_settings, aliens,screen)
        gf.update_screen(ai_settings, screen, aliens)

run_game()

```

### 三.运行游戏截图

由于markdown的图片只能贴本地图片和网上图片,这里把图片上传图床.

![43Kky.png](https://i.328888.xyz/2022/12/17/43Kky.png)





