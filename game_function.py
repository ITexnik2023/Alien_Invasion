import pygame
import sys
from bullet import Bullet
from alien import Alien


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
def update_bullets(bullets,aliens):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    pygame.sprite.groupcollide(bullets,aliens,True,True)
def check_keyup_events(ship, event):
        if event.key == pygame.K_LEFT:
            ship.moving_left = False
        if event.key == pygame.K_RIGHT:
            ship.moving_right = False
        if event.key == pygame.K_UP:
            ship.moving_up = False
        if event.key == pygame.K_DOWN:
            ship.moving_down = False



def update_screen(ship, ai_settings, bullets, screen,aliens,fon, play_button):

    fon.blitme()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    for alien in aliens.sprites():
        alien.blitmes()

    ship.blitme()

    pygame.display.flip()

    screen.fill(ai_settings.bg_color)

def collision_tracking(aliens, ship,ai_settings):
    if pygame.sprite.spritecollideany(ship,aliens):
        ai_settings.gameplay = False



def gameplay_false(play_button,ai_settings):
    play_button.draw_button()
    for event in pygame.event.get():
        #обработчик нажатия крестика для выхода из игры
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            if play_button.rect.collidepoint(mouse_x,mouse_y):
                ai_settings.gameplay = True

    pygame.display.flip()


