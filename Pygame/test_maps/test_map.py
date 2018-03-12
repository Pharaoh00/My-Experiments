#-*- coding:utf-8 -*-
#test_map.py

import pygame
from pygame.locals import *

pygame.init()

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

    def update(self):
        #self.p_move() #Chamando p_move(), para atualizar o objeto
        #print(self.rect)
        self.dirty = 1 # Atualiza Sprite

    def p_move(self):
        #Atualizado:
        #Ao invez de usar update() com argumentos,
        #p_move pega o rect.x, rect.y e o movimenta

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if key[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if key[pygame.K_UP]:
            self.rect.y -= self.speed
        if key[pygame.K_DOWN]:
            self.rect.y += self.speed

        #Limitando o Objeto dentro da tela
        if self.rect.left < 0:
            self.rect.x += self.speed
        elif self.rect.right > s_width:
            self.rect.x -= self.speed

        if self.rect.top < 0:
            self.rect.y += self.speed
        elif self.rect.bottom > s_height:
            self.rect.y -= self.speed

player = Player()

allsprites = pygame.sprite.LayeredDirty(player) # Adicionando o Objeto ao "grupo"
allsprites.clear(game_screen, background) # Limpando a tela

while(running):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    allsprites.update()
    player.p_move()

    rects = allsprites.draw(game_screen) # Desenhando os objetos do grupo na tela
    pygame.display.update(rects) # Atualizando os objetos do grupo
    clock.tick(fps)
    #print(clock.get_fps())

pygame.quit()
