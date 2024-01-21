import pygame

class Fon:
    def __init__(self,ai_settings,screen):
        self.screen = screen
        self.ai_settings = ai_settings
        self.fon = pygame.image.load("images/cosmoc.bmp")
        self.fon = pygame.transform.scale(self.fon,(ai_settings.screen_width,ai_settings.screen_height))
        self.rect = self.fon.get_rect()

    def blitme(self):
        self.screen.blit(self.fon, self.rect)