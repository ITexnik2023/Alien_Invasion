import pygame
import sys
from bullet import Bullet

def check(ship, ai_settings, bullets,screen):
    for event in pygame.event.get():
        #обработчик нажатия крестика для выхода из игры
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(ship, event)
            bullet_strike(event, ai_settings, bullets, ship, screen)
        elif event.type == pygame.KEYUP:
            check_keyup_events(ship, event)

        #обработчик нажатия стрелки

def check_keydown_events(ship, event):
        if event.key == pygame.K_RIGHT:
            ship.moving_right = True
        if event.key == pygame.K_LEFT:
            ship.moving_left = True
        if event.key == pygame.K_UP:
            ship.moving_up = True
        if event.key == pygame.K_DOWN:
            ship.moving_down = True
def bullet_strike(event,ai_settings,bullets,ship,screen):
        if len(bullets) != ai_settings.bullet_count:
            if event.key == pygame.K_SPACE:
                new_bullet = Bullet(ai_settings,ship, screen)
                bullets.add(new_bullet)
        else:
            pygame.time.wait(ai_settings.bullet_recharge)



def check_keyup_events(ship, event):
        if event.key == pygame.K_LEFT:
            ship.moving_left = False
        if event.key == pygame.K_RIGHT:
            ship.moving_right = False
        if event.key == pygame.K_UP:
            ship.moving_up = False
        if event.key == pygame.K_DOWN:
            ship.moving_down = False



def update_screen(ship, ai_settings, bullets, screen):
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    pygame.display.flip()
    screen.fill(ai_settings.bg_color)