import pygame
from settings import Settings
from ship import Ship
import game_function as fn
from pygame.sprite import Group
from fon import Fon
from button import Button



def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(screen, ai_settings)
    fon = Fon(ai_settings,screen)
    play_button = Button(screen, "Играть")
    aliens_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(aliens_timer, ai_settings.aliens_timer)
    bullets = Group()
    aliens = Group()


    while True:
        fn.collision_tracking(aliens, ship, ai_settings)
        ship.update()

        fn.check(ship, ai_settings, bullets, screen,aliens,aliens_timer)

        fn.update_alien(aliens,ai_settings)

        fn.update_bullets(bullets,aliens)
        fn.update_screen(ship, ai_settings, bullets, screen, aliens, fon, play_button)







run_game()
