#-*- coding:utf-8 -*-
#test_dirty_v3.py

import pygame
from pygame.locals import *

pygame.init()
pygame.key.set_repeat(250, 25)

s_width = 600
s_height = 600
clock = pygame.time.Clock()
fps = 30
running = True

game_screen = pygame.display.set_mode((s_width, s_height), pygame.DOUBLEBUF)
background = pygame.Surface(game_screen.get_size()) # Criando uma nova Surface
#background = background.convert() # Convertendo os pixels para "pygame"
background.fill((255,0,0)) # Cor do Background

class Player(pygame.sprite.DirtySprite): # Herdando Dirty_Sprites

    def __init__(self):
        
        pygame.sprite.DirtySprite.__init__(self) # Inicializando a Herança
        #self.image = pygame.image.load("poo1.png") # Imagem aleatoria
        self.image = pygame.Surface((50,50)) # Criando uma nova Surface
        self.rect = self.image.get_rect() # Criando um rect do tamanho da Surface
        self.rect = pygame.draw.rect(self.image, (0,255,0), self.rect)
        self.speed = 10
        # Desenhando um quadrado na tela.
        self.change_x = 0
        self.change_y = 0

    def update(self):
        print(self.rect)
        self.dirty = 1 # Atualiza Sprite        

    def p_move_x(self, x):
        self.rect.x += x
    def p_move_y(self, y):
        self.rect.y += y
        
player = Player()

allsprites = pygame.sprite.LayeredDirty(player) # Adicionando o Objeto ao "grupo"
allsprites.clear(game_screen, background) # Limpando a tela
p_speed = 10

while(running):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.p_move_x(-p_speed)
            if event.key == pygame.K_RIGHT:
                player.p_move_x(p_speed)
            if event.key == pygame.K_UP:
                player.p_move_y(-p_speed)
            if event.key == pygame.K_DOWN:
                player.p_move_y(p_speed)

    allsprites.update()

    rects = allsprites.draw(game_screen) # Desenhando os objetos do grupo na tela
    pygame.display.update(rects) # Atualizando os objetos do grupo
    clock.tick(fps)
    #print(clock.get_fps())

pygame.quit()
