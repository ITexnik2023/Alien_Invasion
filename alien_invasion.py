import pygame
from settings import Settings
from ship import Ship
import game_function as fn
from pygame.sprite import Group
from fon import Fon



def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    #label = pygame.font.Font("fonts/Roboto-Medium.ttf",60)
    #lose_label = label.render("Вы проиграли", False,(84, 56, 56))
    #restart_label = label.render("RESTART", False,(84, 56, 56))
    #restart_label_rect = restart_label.get_rect(topleft = (510,300))
    ship = Ship(screen, ai_settings)
    fon = Fon(ai_settings,screen)
    aliens_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(aliens_timer, ai_settings.aliens_timer)
    bullets = Group()
    aliens = Group()


    while True:
        #if ai_settings.gameplay:
        fn.check(ship, ai_settings, bullets, screen,aliens,aliens_timer)
        ship.update()
        fn.update_alien(aliens,ai_settings)
        fn.collision_tracking(aliens,ship,ai_settings)
        fn.update_bullets(bullets,aliens)
        fn.update_screen(ship, ai_settings, bullets, screen, aliens, fon)
        #else:
            #fn.gameplay_false(screen,lose_label,restart_label, restart_label_rect, ai_settings,ship)





run_game()
