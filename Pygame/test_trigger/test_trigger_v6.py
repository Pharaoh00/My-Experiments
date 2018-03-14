#-*- coding:utf-8 -*-
#test_trigger_v6.py

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
    
    def __init__(self, position):
        
        pygame.sprite.Sprite.__init__(self) # Inicializando a Herança
        self.image = pygame.Surface((70,50), pygame.SRCALPHA)
        self.image.fill((0,0,0))
        self.original_image = self.image
        self.rect = self.image.get_rect(center=position)
        self.pos = Vector2(position)
        #self.vel = Vector2(0,0)
        self.direction = Vector2(1,0)
        self.speed = 0
        self.angle_speed = 0
        #self.angle = 0
        self.angle, self.radius = self.direction.as_polar()

    def start_move_left(self):
        self.angle_speed = -10
    def stop_move_left(self):
        self.angle_speed = 0

    def start_move_right(self):
        self.angle_speed = 10
    def stop_move_right(self):
        self.angle_speed = 0

    def start_move_up(self):
        self.speed = -10
    def stop_move_up(self):
        self.speed = 0

    def start_move_down(self):
        self.speed = 10
    def stop_move_down(self):
        self.speed = 0

    def update(self):
        self.angle = self.angle % 360

        if self.angle_speed:
            self.angle += self.angle_speed
            self.direction.rotate_ip(self.angle_speed)
            self.image = pygame.transform.rotate(self.original_image,
                                                 -self.angle)
            self.rect = self.image.get_rect(center=self.rect.center)
        self.pos += self.direction * self.speed
        self.rect.center = self.pos
        #print(self.angle)
        #print(self.radius)
        #print(self.direction)
        
player = Player((s_width/2, s_height/2))

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
    pygame.draw.line(game_screen, (255,255,255), player.pos,
                     player.direction, 2)
    pygame.display.update() # update a tela toda
    clock.tick(fps)
    #print(clock.get_fps())

pygame.quit()
