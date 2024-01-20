import pygame
import sys
from bullet import Bullet
from alien import Alien
from ship import Ship

def check(ship, ai_settings, bullets,screen,aliens,aliens_timer):
    for event in pygame.event.get():
        #обработчик нажатия крестика для выхода из игры
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(ship, event,ai_settings,screen,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(ship, event)
        if event.type == aliens_timer:
            call_aliens(ai_settings,screen,aliens)
        #обработчик нажатия стрелки


def update_alien(aliens,ai_settings):
    aliens.update()
    for alien in aliens.copy():
        if alien.rect.top >= ai_settings.screen_height:
            aliens.remove(alien)
def call_aliens(ai_settings,screen,aliens):
    new_alien = Alien(screen, ai_settings)
    aliens.add(new_alien)
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



def update_screen(ship, ai_settings, bullets, screen,aliens):
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    for alien in aliens.sprites():
        alien.blitmes()
    ship.blitme()
    pygame.display.flip()
    screen.fill(ai_settings.bg_color)

def collision_tracking(aliens, ship,ai_settings):
    for alien in aliens:
        if ship.rect.colliderect(alien.rect):
            ai_settings.gameplay = False


def gameplay_false(screen,lose_label,restart_label,restart_label_rect,ai_settings,ship,aliens):
    for event in pygame.event.get():
        #обработчик нажатия крестика для выхода из игры
        if event.type == pygame.QUIT:
            sys.exit()
    mouse = pygame.mouse.get_pos()
    screen.fill((176, 181, 181))
    screen.blit(lose_label, (425,200))
    screen.blit(restart_label,restart_label_rect)
    if restart_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[1]:
        ai_settings.gameplay = True
        ship.rect.y = ship.screen_rect.centery
        ship.rect.centerx = ship.screen_rect.centerx
        aliens.remove()
    pygame.display.flip()



