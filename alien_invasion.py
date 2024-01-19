import pygame
from settings import Settings
from ship import Ship
import game_function as fn
from pygame.sprite import Group


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(screen, ai_settings)
    bullets = Group()


    while True:
        fn.check(ship, ai_settings, bullets, screen)
        ship.update()
        bullets.update()
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        fn.update_screen(ship, ai_settings,bullets, screen)




run_game()
