import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, ai_settings, ship, screen):
        super(Bullet,self).__init__()
        self.screen = screen
        # создание пули в позиции (0,0)
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y)
        self.color_bullet = ai_settings.bullet_color
        self.speed_bullet = ai_settings.bullet_speed

    def update(self):
        self.y -= self.speed_bullet
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color_bullet, self.rect)