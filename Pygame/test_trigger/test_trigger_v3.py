#-*- coding:utf-8 -*-
#test_trigger_v3.py

import pygame
from pygame.locals import *
from pygame.math import Vector2

pygame.init()
#pygame.key.set_repeat(250, 25)

s_width = 600
s_height = 600
clock = pygame.time.Clock()
fps = 30
running = True

game_screen = pygame.display.set_mode((s_width, s_height), pygame.DOUBLEBUF)

class Player(pygame.sprite.Sprite):
    
    def __init__(self):
        
        pygame.sprite.Sprite.__init__(self) # Inicializando a Herança
        #self.image = pygame.image.load("poo1.png") # Imagem aleatoria
        self.image = pygame.Surface((50,50)) # Criando uma nova Surface
        self.rect = self.image.get_rect() # Criando um rect do tamanho da Surface
        self.rect = pygame.draw.rect(self.image, (0,255,0), self.rect)
        self.pos = Vector2(0,0)
        self.speed_x = 0
        self.speed_y = 0
        

    def start_move_left(self):
        self.speed_x = -10
    def stop_move_left(self):
        self.speed_x = 0

    def start_move_right(self):
        self.speed_x = 10
    def stop_move_right(self):
        self.speed_x = 0

    def start_move_up(self):
        self.speed_y = -10
    def stop_move_up(self):
        self.speed_y = 0

    def start_move_down(self):
        self.speed_y = 10
    def stop_move_down(self):
        self.speed_y = 0

    def update(self):
        self.moving = Vector2(self.speed_x, self.speed_y) #Mistake? 
        #print(self.rect)
        #print(self.speed_x)
        #print(self.speed_y)
        if self.moving:
            self.pos += self.moving
            self.rect.x, self.rect.y = self.pos
        #print(self.pos)
        print(self.moving)
        
player = Player()

allsprites = pygame.sprite.Group() # Adicionando o Objeto ao "grupo"
allsprites.add(player)

while(running):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.start_move_left()
            if event.key == pygame.K_RIGHT:
                player.start_move_right()
            if event.key == pygame.K_UP:
                player.start_move_up()
            if event.key == pygame.K_DOWN:
                player.start_move_down()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.stop_move_left()
            if event.key == pygame.K_RIGHT:
                player.stop_move_right()
            if event.key == pygame.K_UP:
                player.stop_move_up()
            if event.key == pygame.K_DOWN:
                player.stop_move_down()

    allsprites.update() # Update o grupo das sprites
    game_screen.fill((255,0,0)) # fill screen com a cor vermelha
    allsprites.draw(game_screen) # desenha os sprites na tela
    pygame.display.update() # update a tela toda
    clock.tick(fps)
    #print(clock.get_fps())

pygame.quit()
