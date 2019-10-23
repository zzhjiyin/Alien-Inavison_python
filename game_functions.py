
import sys
import pygame
from bullet import Bullet
from alien import Alien

def check_keydown_events(event,ai_settings,screen,ship,bullets):
    """响应键盘"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings,screen,ship,bullets)
    elif event.key == pygame.K_q:
        sys.exit()
def fire_bullet(ai_settings,screen,ship,bullets):
    """未达到上限，创建1个新的子弹"""
    # 创建一个子弹，加入编组bullets中
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
def check_keyup_events(event,ship):
    """松开键盘"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False



def check_events(ai_settings,screen,ship,bullets):
    """响应键盘和鼠标"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)

def update_screen(ai_settings,screen,ship,aliens,bullets):
    """更新屏幕新的图像，并切换新的屏幕"""
    # 每次循环重绘屏幕
    screen.fill(ai_settings.bg_color)
    # 在飞船和外星人后面绘制所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)
    # 绘制屏幕最近可见
    pygame.display.flip()

def update_bullets(bullets):
    bullets.update()
    # 删除子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def creat_fleet(ai_settings,screen,aliens):
    """创建外星人群"""
    #创建一个外星人，并计算一行容纳多少个外星人
    #外星人间距等于外星人宽度
    alien = Alien(ai_settings,screen)
    alien_width = alien.rect.width
    available_space_x = ai_settings.screen_width - 2*alien_width
    number_aliens_x = int(available_space_x/(2*alien_width))

    #创建第一行外星人
    for alien_number in range(number_aliens_x):
        #创建一个外星人并使其加入行
        alien = Alien(ai_settings,screen)
        alien.x = alien_width +2*alien_width*alien_number
        alien.rect.x = alien.x
        aliens.add(alien)