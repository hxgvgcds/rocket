import pygame
from pygame.locals import *
import time

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((600, 600))

player_x = 250
player_y = 250
player = pygame.image.load("images/rocket.png")
background = pygame.image.load("images/nightsky.png")
font = pygame.font.SysFont("Comfortaa", 160)
keys = [False, False, False, False]

while player_y < 600:
    screen.blit(background, (0, 0))
    screen.blit(player, (player_x, player_y))
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == K_w:
                keys[0] = True
            elif event.key == K_a:
                keys[1] = True
            elif event.key == K_s:
                keys[2] = True
            elif event.key == K_d:
                keys[3] = True
        if event.type == pygame.KEYUP:
            if event.key == K_w:
                keys[0] = False
            elif event.key == K_a:
                keys[1] = False
            elif event.key == K_s:
                keys[2] = False
            elif event.key == K_d:
                keys[3] = False
