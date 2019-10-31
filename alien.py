import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """表示单个外星人的类"""
    def __init__(self,ai_settings,screen):
        """初始化外星人参数，注意参数签名顺序！！！"""
        super(Alien,self).__init__()
        self.ai_settings = ai_settings
        self.screen = screen

        #加载外星人图像
        self.image = pygame.image.load('alien.bmp')
        self.rect = self.image.get_rect()

        #每个外星人从屏幕左上方附近
        self.rect.x =  self.rect.width
        self.rect.y = self.rect. height

        #储存每个外星人的准确位置
        self.x = float(self.rect.x)
    def blitme(self):
        """指定位置绘制外星人"""
        self.screen.blit(self.image,self.rect)
    def update(self):
        """外星人群移动"""
        self.x += ( self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction )
        self.rect.x = self.x

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True