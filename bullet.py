import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """一个对飞船发射的子弹进行管理的类"""
    def  __init__(self,ai_settings,screen,ship):
        """在飞船位置创建一个子弹的对象"""
        super(Bullet,self).__init__()
        self.screen = screen
    #在（0,0）处创建一个表示子弹的矩形，再设置正确位置
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
    #存储浮点型子弹位置
        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """子弹向上移动"""
        self.y -= self.speed_factor
        #更新子弹的位置
        self.rect.y = self.y

    def draw_bullet(self):
        """屏幕绘制子弹"""
        pygame.draw.rect(self.screen,self.color,self.rect)