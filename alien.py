import pygame
from pygame.sprite import Group
import random

class Alien:
    def __init__(self,screen,ai_settings):
        super(Alien,self).__init__()
        self.coordinate_x = random.randint(0,ai_settings.screen_width - 100)
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load("images/alien.bmp")
        self.image = pygame.transform.scale(self.image,(50,50))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.x = self.screen_rect.left + self.coordinate_x
        self.rect.y = self.screen_rect.top - 200
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)


    def update(self):
        self.y += self.ai_settings.alien_speed
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)