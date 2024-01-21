import pygame

class Settings:
    def __init__(self):
        self.gameplay = True
        self.ship_speed_factor = 0.5
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0,0,0)
        #настройки пуль
        self.bullet_speed = 0.5
        self.bullet_width = 5
        self.bullet_height = 20
        self.bullet_color = 60,60,60
        self.bullet_allowed = 3
        #настройка пришельцев
        self.alien_speed = 0.1
        self.aliens_timer = 3000


