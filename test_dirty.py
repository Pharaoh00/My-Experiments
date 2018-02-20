#-*- coding:utf-8 -*-
#test_dirty.py
# Teste usando Dirty_Rects Pygame.
# O objetivo do Dirty_Rect é não atualizar toda a screen,
# Como é feito com display.flip() ou display.update() [sem argumentos].

import pygame
from pygame.locals import *

pygame.init()
#pygame.key.set_repeat(500, 50)

s_width = 500
s_height = 500
clock = pygame.time.Clock()
fps = 60
running = True

game_screen = pygame.display.set_mode((s_width, s_height), pygame.DOUBLEBUF)
background = pygame.Surface(game_screen.get_size()) # Criando uma nova Surface
background = background.convert() # Conversando os pixels para "pygame"
background.fill((255,0,0)) # Cor do Background

class Player(pygame.sprite.DirtySprite): # Herdando Dirty_Sprites

    def __init__(self):
        
        pygame.sprite.DirtySprite.__init__(self) # Inicializando a Herança
        #self.image = pygame.image.load("poo1.png") # Imagem aleatoria
        self.image = pygame.Surface((50,50)) # Criando uma nova Surface
        self.rect = self.image.get_rect() # Criando um rect do tamanho da Surface
        self.rect = pygame.draw.rect(self.image, (0,255,0), self.rect)
        # Desenhando um quadrado na tela.

    def update(self, x=0, y=0):
        # Update o Objeto para se mover na tela.
        self.x = x
        self.y = y

        self.rect.x += self.x
        self.rect.y += self.y
        
        if self.rect.left < 0:
            self.rect.x -= self.x
        elif self.rect.right > s_width:
            self.rect.x -= self.x

        if self.rect.top < 0:
            self.rect.y -= self.y
        elif self.rect.bottom > s_height:
            self.rect.y -= self.y
            
        self.dirty = 1 # Atualiza Sprite

player = Player()

allsprites = pygame.sprite.LayeredDirty(player) # Adicionando o Objeto ao "grupo"
allsprites.clear(game_screen, background) # Limpando a tela

while(running):

    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        player.update(x=-10)
    if key[pygame.K_RIGHT]:
        player.update(x=10)
    if key[pygame.K_UP]:
        player.update(y=-10)
    if key[pygame.K_DOWN]:
        player.update(y=10)

    allsprites.update()

    rects = allsprites.draw(game_screen) # Desenhando os objetos do grupo na tela
    pygame.display.update(rects) # Atualizando os objetos do grupo
    print(clock.get_fps())

pygame.quit()
