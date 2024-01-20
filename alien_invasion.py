import pygame
from settings import Settings
from ship import Ship
import game_function as fn
from pygame.sprite import Group
from alien import Alien


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(screen, ai_settings)
    bullets = Group()
    alien = Alien(screen, ai_settings)


    while True:
        fn.check(ship, ai_settings, bullets, screen)
        ship.update()
        alien.update()
        fn.update_bullets(bullets)
        fn.update_screen(ship, ai_settings,bullets, screen,alien)




run_game()
