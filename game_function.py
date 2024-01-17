import pygame
import sys

def check(ship):
    for event in pygame.event.get():
        #обработчик нажатия крестика для выхода из игры
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(ship,event)
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
def check_keyup_events(ship, event):
        if event.key == pygame.K_LEFT:
            ship.moving_left = False
        if event.key == pygame.K_RIGHT:
            ship.moving_right = False
        if event.key == pygame.K_UP:
            ship.moving_up = False
        if event.key == pygame.K_DOWN:
            ship.moving_down = False
def update_screen(ai_settings, screen, ship):
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    pygame.display.flip()