#!coding:utf-8
#test_move_v9.py

import random
import math
import pygame
from pygame.math import Vector2

pygame.init()

width = 600
height = 600
clock = pygame.time.Clock()
fps = 60
running = True

screen = pygame.display.set_mode((width, height), pygame.DOUBLEBUF)

class Particle(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.size = random.randint(30, 50)
        self.x = random.randint(0, (width - self.size))
        self.y = random.randint(0, (height - self.size))
        self.image = pygame.Surface((self.size, self.size), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.angle = 0
        self.pos = Vector2(self.x, self.y)
        
        self.color = (255,255,255)
        self.tick_size = 3

        #pygame.draw.ellipse(self.image, self.color, self.rect, self.tick_size)
        pygame.draw.circle(self.image, self.color, (self.size//2, self.size//2),
                           self.size//2, self.tick_size)

    def update(self):
        self.speed = random.uniform(2, 5)
        self.angle = math.radians(random.gauss(0, 1) * 360)
        self.speedx = math.sin(self.angle)
        self.speedy = math.cos(self.angle)

        self.pos.x += self.speedx * self.speed
        self.pos.y += self.speedy * self.speed
        self.rect.x, self.rect.y = self.pos

        if self.rect.left < 0:
            self.angle -= self.angle
            self.speed -= self.speed
            self.rect.left = 0
            
        if self.rect.right > width:
            self.angle -= self.angle
            self.speed -= self.speed
            self.rect.right = width
            
        if self.rect.top < 0:
            self.angle -= self.angle
            self.speed -= self.speed
            self.rect.top = 0
            
        if self.rect.bottom > height:
            self.angle -= self.angle
            self.speed -= self.speed
            self.rect.bottom = height
            

        #print(self.pos)

allsprites = pygame.sprite.Group()

for x in range(10):
    particles = Particle()
    allsprites.add(particles)

while(running):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    allsprites.update()
    screen.fill((51,51,51))
    allsprites.draw(screen)
    pygame.display.flip()
    clock.tick(fps)
    #print(clock.get_fps())

pygame.quit()

