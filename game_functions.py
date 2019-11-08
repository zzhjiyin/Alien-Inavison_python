import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import  sleep


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

def check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets):
    """响应键盘和鼠标"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets,mouse_x,mouse_y)

def check_play_button(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets,mouse_x,mouse_y):
    """玩家单击开始按钮开始新游戏"""
    button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
    if button_clicked and not stats.game_active:
        #重置游戏设置
        ai_settings.initialize_dynamic_settings()
        pygame.mouse.set_visible(False)
        stats.reset_stats()
        stats.game_active = True

        #重置分数牌和剩下的飞船
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

        #清空外星人列表和子弹
        aliens.empty()
        bullets.empty()

        #创建新的外星人和飞船居中
        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()

def update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button):
    """更新屏幕新的图像，并切换新的屏幕"""
    # 每次循环重绘屏幕
    screen.fill(ai_settings.bg_color)
    # 在飞船和外星人后面绘制所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    sb.show_score()
    ship.blitme()
    aliens.draw(screen)
    if not stats.game_active:
        play_button.draw_button()
    # 绘制屏幕最近可见
    pygame.display.flip()

def update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets):
    """更新子弹位置，删除消失的子弹"""
    bullets.update()
    # 删除子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # 检查子弹是否击中外星人
    # 如果是这样，删除对应子弹和外星人
    check_bullet_alien_collisions(ai_settings,screen,stats,sb,ship,aliens,bullets)

def create_fleet(ai_settings,screen,ship,aliens):
    #创建一个外星人，并计算一行容纳多少个外星人
    alien =Alien(ai_settings,screen)
    number_alien_x = get_number_alien_x(ai_settings,alien.rect.width)
    number_rows = get_number_rows(ai_settings,ship.rect.height,alien.rect.height)
    #创建外星人群
    for row_number in range(number_rows):
        for alien_number in range( number_alien_x):
            create_alien(ai_settings,screen,aliens,alien_number,row_number)

def get_number_alien_x(ai_settings,alien_width):
    """计算一行可以容纳多少外星人"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return   number_aliens_x

def get_number_rows(ai_settings,ship_height,alien_height):
    """计算屏幕可以容纳多少行外星人"""
    available_space_y = (ai_settings.screen_height -
                         ( 3 *alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(ai_settings,screen,aliens,alien_number,row_number):
    """创建一个外星人并放入其行"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def check_fleet_edges(ai_settings,aliens):
    """检测外星人达到边缘时的动作"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings,aliens):
    """降外星人群下移，并改变方向"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def update_aliens(ai_settings,screen,stats,sb,ship,aliens,bullets):
   """更新外星人群中所有外星人的位置"""
   check_fleet_edges(ai_settings, aliens)
   aliens.update()
    #检测外星人和飞船碰撞
   if pygame.sprite.spritecollideany(ship,aliens):
       ship_hit(ai_settings,stats,sb,screen,ship,aliens,bullets)
   check_aliens_bottom(ai_settings,screen,stats,sb,ship,aliens,bullets)
def ship_hit(ai_settings,screen,stats,sb,ship,aliens,bullets):
    """响应被外星人撞的飞船"""
    if stats.ship_left > 0:
        stats.ship_left -=  1
        #更新记分牌
        sb.prep_ships()

    else:
       stats.game_active = False
       pygame.mouse.set_visible(True)
    #清空外星人和子弹
    aliens.empty()
    bullets.empty()

    #创建新的外星人，并重置新飞船
    create_fleet(ai_settings, screen, ship, aliens)
    ship.center_ship()

    sleep(0.5)

def check_aliens_bottom(ai_settings,screen,stats,sb,ship,aliens,bullets):
    """检测是否有外星人到达屏幕底部"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            #像飞船撞到一样处理
            ship_hit(ai_settings,screen,stats,sb,ship,aliens,bullets)
            break

def check_bullet_alien_collisions(ai_settings,screen,stats,sb,ship,aliens,bullets):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    # 删除子弹以及发生碰撞的子弹和外星人
    if collisions :
        for aliens in collisions.values():
             stats.score += ai_settings.alien_points
             sb.prep_score()
        check_high_score(stats,sb)

    if len(aliens) == 0 :
        #删除现在所有的子弹，加快游戏节奏，刷新外星人
        bullets.empty()
        ai_settings.increase_speed()
        stats.level += 1
        sb.prep_level()
        create_fleet(ai_settings,screen,ship,aliens)

def check_high_score(stats,sb):
    """检查是否新的最高分诞生"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()