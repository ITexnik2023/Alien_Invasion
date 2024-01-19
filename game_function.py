import pygame
import sys
from bullet import Bullet

def check(ship, ai_settings, bullets,screen):
    for event in pygame.event.get():
        #обработчик нажатия крестика для выхода из игры
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(ship, event,ai_settings,screen,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(ship, event)

        #обработчик нажатия стрелки

def check_keydown_events(ship, event,ai_settings,screen,bullets):
        if event.key == pygame.K_RIGHT:
            ship.moving_right = True
        if event.key == pygame.K_LEFT:
            ship.moving_left = True
        if event.key == pygame.K_UP:
            ship.moving_up = True
        if event.key == pygame.K_DOWN:
            ship.moving_down = True
        if event.key == pygame.K_SPACE:
            fire_bullet(bullets,ai_settings,ship,screen)




def fire_bullet(bullets,ai_settings,ship,screen):
    if len(bullets) <= ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings, ship, screen)
        bullets.add(new_bullet)
def update_bullets(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
def check_keyup_events(ship, event):
        if event.key == pygame.K_LEFT:
            ship.moving_left = False
        if event.key == pygame.K_RIGHT:
            ship.moving_right = False
        if event.key == pygame.K_UP:
            ship.moving_up = False
        if event.key == pygame.K_DOWN:
            ship.moving_down = False



def update_screen(ship, ai_settings, bullets, screen,alien):
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    alien.blitme()
    pygame.display.flip()
    screen.fill(ai_settings.bg_color)