#!coding:utf-8
#test_move_v1.py

import random
import math
import pygame
from pygame.math import Vector2

pygame.init()

width = 600
height = 600
clock = pygame.time.Clock()
fps = 30
running = True

screen = pygame.display.set_mode((width, height), pygame.DOUBLEBUF)

class Particle:

    def __init__(self):
        self.x, self.y = Vector2(0,0)
        self.x = random.randint(0, width)
        self.y = random.randint(0, height)
        self.size = random.randint(10, 30)
        self.color = (255,255,255)
        self.tickness = 3
        self.speed = 0
        self.angle = 0

    def display(self):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)),
                           self.size, self.tickness)

    def update(self):
        self.speed = random.randint(-5, 5)
        self.angle = random.randint(0, 360)
        self.x += math.sin(self.angle) * self.speed
        self.y += math.cos(self.angle) * self.speed

all_particles = []
for x in range(10):
    particle = Particle()
    all_particles.append(particle)

while(running):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((51,51,51))
    for particles in all_particles:
        particles.display()
        particles.update()
    pygame.display.flip()
    clock.tick(fps)
    print(clock.get_fps())

pygame.quit()

