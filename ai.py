
import pygame

from settings import  Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group

def run_game():
    pygame.init() #初始化pygame
    ai_settings = Settings() #初始化设置参数
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height)) #屏幕尺寸
    pygame.display.set_caption('Alian Invasion')
    bg_color = (230,230,230)  # 背景颜色
    ship = Ship(screen,ai_settings) #初始化飞船,参数顺序不能反

    bullets = Group() #初始化子弹编组
    aliens = Group()#初始化外星人编组
    gf.creat_fleet(ai_settings,screen,aliens)
    while True:
        #监视鼠标和键盘事件
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, aliens,bullets)


run_game()