import pygame
from pygame.sprite import Sprite
class Ship(Sprite):
    def __init__(self,ai_settings,screen):
        """初始化飞船设置和初始化位置"""
        self.screen =screen
        self.ai_settings = ai_settings
        super(Ship, self).__init__()
        #加载飞船图形并获取外接矩阵
        self.image = pygame.image.load('ship.bmp') #返回一个图形surface属性
        self.rect =self.image.get_rect()  #获取surface的rect属性
        self.screen_rect = screen.get_rect()
        #将飞船放置屏幕底部中间
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # 初始化飞船移动值属性为浮点型
        self.center = float(self.rect.centerx)

        #初始化移动标志、
        self.moving_right = False
        self.moving_left = False


    def update(self):
        """根据移动标志调整位置"""
        #更新飞船位置值center，不是rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor

        if self.moving_left and self.rect.left >0 :
            self.center -= self.ai_settings.ship_speed_factor


        #更新飞船的位置
        self.rect.centerx = self.center

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        """让飞船居中"""
        self.center = self.screen_rect.centerx