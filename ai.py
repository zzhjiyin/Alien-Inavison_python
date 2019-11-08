
import pygame

from settings import  Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import  Button
from scoreboard import  Scoreboard

def run_game():
    pygame.init() #初始化pygame
    ai_settings = Settings() #初始化设置参数
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height)) #屏幕尺寸
    pygame.display.set_caption('Alian Invasion')
    #创建play按钮
    play_button = Button(ai_settings,screen,"Start")
    ship = Ship(ai_settings,screen) #初始化飞船,参数顺序不能反
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings,screen,stats)
    bullets = Group() #初始化子弹编组
    aliens = Group()#初始化外星人编组
    gf.create_fleet(ai_settings,screen,ship,aliens)
    while True:
        #监视鼠标和键盘事件
        gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
            gf.update_aliens(ai_settings,screen,stats,sb,ship,aliens,bullets)
        gf.update_screen(ai_settings, screen,stats,sb,ship,aliens,bullets,play_button)

run_game()