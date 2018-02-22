#-*- coding:utf-8 -*-
#test_dirty_v4.py

import pygame
from pygame.locals import *

pygame.init()
#pygame.key.set_repeat(250, 25)

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
        self.speed_x = 0
        self.speed_y = 0
        # Desenhando um quadrado na tela.
        self.check_press_x = False
        self.check_press_y = False
        
    def move_right(self, x):
        self.speed_x = x
        self.check_press_x = True
    def move_left(self, x):
        self.speed_x = x
        self.check_press_x = True
    def stop_move_x(self):
        self.check_press_x = False

    def move_up(self, y):
        self.speed_y = y
        self.check_press_y = True
    def move_down(self, y):
        self.speed_y = y
        self.check_press_y = True
    def stop_move_y(self):
        self.check_press_y = False

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

        print(self.check_press_y)
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
                player.move_left(-speed)
            if event.key == pygame.K_RIGHT:
                player.move_right(speed)
            if event.key == pygame.K_UP:
                player.move_up(-speed)
            if event.key == pygame.K_DOWN:
                player.move_down(speed)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.stop_move_x()
            if event.key == pygame.K_RIGHT:
                player.stop_move_x()
            if event.key == pygame.K_UP:
                player.stop_move_y()
            if event.key == pygame.K_DOWN:
                player.stop_move_y()

    allsprites.update()

    rects = allsprites.draw(game_screen) # Desenhando os objetos do grupo na tela
    pygame.display.update(rects) # Atualizando os objetos do grupo
    clock.tick(fps)
    #print(clock.get_fps())

pygame.quit()
