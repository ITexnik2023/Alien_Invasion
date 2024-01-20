import pygame
import sys

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1600,800))
    pygame.display.set_caption("Alien Invasion")
    image = pygame.image.load("images/alien.bmp")
    rect = image.get_rect()
    image = pygame.transform.scale(image,(100,100))
    screen_rect = screen.get_rect()
    rect.x = screen_rect.left + 1500

    while True:

        for event in pygame.event.get():
            screen.fill((0,0,255))
            if event.type == pygame.QUIT:
                sys.exit()
        screen.blit(image, rect)
        pygame.display.flip()
run_game()