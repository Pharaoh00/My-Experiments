#-*- coding:utf-8 -*-
#test_map_v2.py

import pygame
from pygame.locals import *

pygame.init()

s_width = 640
s_height = 360
clock = pygame.time.Clock()
fps = 30
running = True

game_screen = pygame.display.set_mode((s_width, s_height), pygame.DOUBLEBUF)
game_surface = pygame.Surface(game_screen.get_size())

class Maps(pygame.sprite.Sprite):

    def __init__(self, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(game_screen.get_size())
        self.rect = self.image.get_rect()
        self.image.fill(color)

m1 = Maps((0,255,0))
m2 = Maps((255,255,0))
all_maps = pygame.sprite.Group()
        
while(running):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                m2.add(all_maps)                
            if event.key == pygame.K_RIGHT:
                all_maps.remove(m2)
                all_maps.clear(game_screen, game_surface)
                game_screen.fill((255,255,0))

    all_maps.update()
    all_maps.draw(game_screen)
    pygame.display.flip()
    print(all_maps)

pygame.quit()
