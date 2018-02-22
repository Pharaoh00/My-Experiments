#-*- coding:utf-8 -*-
#test_dirty_v5.py

import pygame
from pygame.locals import *

pygame.init()
#pygame.key.set_repeat(250, 25)

s_width = 500
s_height = 500
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
        self.speed_x = 0
        self.speed_y = 0
        # Desenhando um quadrado na tela.
        self.check_press_x = False
        self.check_press_y = False

    def move_player(self, x=0, y=0, bool_x=False, bool_y=False):
        self.speed_x = x
        self.speed_y = y
        self.check_press_x = bool_x
        self.check_press_y = bool_y

    def update(self):
        #print(self.rect)
        if self.check_press_x == True:
            self.rect.x += self.speed_x
        if self.check_press_x == False:
            self.rect.x += 0

        if self.check_press_y == True:
            self.rect.y += self.speed_y
        if self.check_press_y == False:
            self.rect.y += 0

        print(self.check_press_x)
        self.dirty = 1 # Atualiza Sprite        
        
player = Player()

allsprites = pygame.sprite.LayeredDirty(player) # Adicionando o Objeto ao "grupo"
allsprites.clear(game_screen, background) # Limpando a tela
speed = 10

while(running):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.move_player(x=-speed, bool_x=True)
            if event.key == pygame.K_RIGHT:
                player.move_player(x=speed, bool_x=True)
            if event.key == pygame.K_UP:
                player.move_player(y=-speed, bool_y=True)
            if event.key == pygame.K_DOWN:
                player.move_player(y=speed, bool_y=True)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.move_player(bool_x=False)
            if event.key == pygame.K_RIGHT:
                player.move_player(bool_x=False)
            if event.key == pygame.K_UP:
                player.move_player(bool_y=False)
            if event.key == pygame.K_DOWN:
                player.move_player(bool_y=False)

    allsprites.update()

    rects = allsprites.draw(game_screen) # Desenhando os objetos do grupo na tela
    pygame.display.update(rects) # Atualizando os objetos do grupo
    clock.tick(fps)
    #print(clock.get_fps())

pygame.quit()
