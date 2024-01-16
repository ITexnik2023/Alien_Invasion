import pygame
import sys

def check(ship):
    for event in pygame.event.get():
        #обработчик нажатия крестика для выхода из игры
        if event.type == pygame.QUIT:
            sys.exit()
        #обработчик нажатия стрелки
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            if event.key == pygame.K_LEFT:
                ship.moving_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                ship.moving_left = False
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
def update_screen(ai_settings, screen, ship):
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    pygame.display.flip()