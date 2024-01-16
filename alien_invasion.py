import pygame
from settings import Settings
from ship import Ship
import game_function as fn


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(screen)


    while True:
        fn.check(ship)
        ship.update()
        fn.update_screen(ai_settings, screen, ship)




run_game()
