import pygame
import sys

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1600,800))
    pygame.display.set_caption("Alien Invasion")
    while True:

        for event in pygame.event.get():
            screen.fill((0,0,255))
            if event.type == pygame.QUIT:
                sys.exit()
    pygame.display.flip()
run_game()