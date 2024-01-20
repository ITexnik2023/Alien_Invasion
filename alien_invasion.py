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
    aliens_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(aliens_timer, ai_settings.aliens_timer)
    bullets = Group()
    aliens = Group()


    while True:
        fn.check(ship, ai_settings, bullets, screen,aliens,aliens_timer)
        ship.update()
        fn.update_alien(aliens,ai_settings)
        print(len(aliens))
        fn.update_bullets(bullets)
        fn.update_screen(ship, ai_settings,bullets, screen,aliens)




run_game()
