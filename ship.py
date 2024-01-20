import pygame


class Ship:
    def __init__(self, screen, ai_settings):
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load("images/ship.bmp")
        self.image = pygame.transform.scale(self.image,(50,50))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.y = self.screen_rect.centery
        self.rect.centerx = self.screen_rect.centerx
        self.centerx = float(self.rect.centerx)
        self.y = float(self.rect.y)
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.centerx -= self.ai_settings.ship_speed_factor
        if self.moving_up:
            self.y -= self.ai_settings.ship_speed_factor
        if self.moving_down:
            self.y += self.ai_settings.ship_speed_factor

        self.rect.centerx = self.centerx
        self.rect.y = self.y


    def blitme(self):
        self.screen.blit(self.image, self.rect)