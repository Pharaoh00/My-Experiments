#-*- coding:utf-8 -*-
#test_trigger_v7.py

import pygame
from pygame.math import Vector2

pygame.init()

s_width = 600
s_height = 600
clock = pygame.time.Clock()
fps = 30
running = True

game_screen = pygame.display.set_mode((s_width, s_height), pygame.DOUBLEBUF)

class Player(pygame.sprite.Sprite):
    
    def __init__(self):
        
        pygame.sprite.Sprite.__init__(self) # Inicializando a Herança
        self.image = pygame.Surface((50,50)) # Criando uma nova Surface
        self.original_image = self.image
        self.rect = self.image.get_rect() # Criando um rect do tamanho da Surface
        self.pos = Vector2(0,0)
        self.vel = Vector2(0,0)
        self.speed = 10
        

    def start_move_left(self):
        self.vel.x = -self.speed
    def stop_move_left(self):
        self.vel.x = 0

    def start_move_right(self):
        self.vel.x = self.speed
    def stop_move_right(self):
        self.vel.x = 0

    def start_move_up(self):
        self.vel.y = -self.speed
    def stop_move_up(self):
        self.vel.y = 0

    def start_move_down(self):
        self.vel.y = self.speed
    def stop_move_down(self):
        self.vel.y = 0

    def start_rotate_left(self):
        self.angle = -10
    def stop_rotate_left(self):
        self.angle = 0
    def start_rotate_right(self):
        self.angle = 10
    def stop_rotate_right(self):
        self.angle = 0

    def update(self):
        if self.vel:
            self.pos += self.vel
            self.rect.x, self.rect.y = self.pos
        
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
            if event.key == pygame.K_q:
                player.start_rotate_left()
            if event.key == pygame.K_e:
                player.start_rotate_right()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.stop_move_left()
            if event.key == pygame.K_RIGHT:
                player.stop_move_right()
            if event.key == pygame.K_UP:
                player.stop_move_up()
            if event.key == pygame.K_DOWN:
                player.stop_move_down()
            if event.key == pygame.K_q:
                player.stop_rotate_left()
            if event.key == pygame.K_e:
                player.stop_rotate_right()

    allsprites.update() # Update o grupo das sprites
    game_screen.fill((255,0,0)) # fill screen com a cor vermelha
    allsprites.draw(game_screen) # desenha os sprites na tela
    pygame.display.update() # update a tela toda
    clock.tick(fps)
    #print(clock.get_fps())

pygame.quit()
