import pygame


class Alien:
    def __init__(self,screen,ai_settings):
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load("images/alien.bmp")
        self.image = pygame.transform.scale(self.image,(100,100))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.centerx = float(self.rect.centerx)

    def update(self):
        self.rect.centerx = self.centerx

    def blitme(self):
        self.screen.blit(self.image, self.rect)