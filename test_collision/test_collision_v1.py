#!coding:utf-8
#test_collision_v1.py

import pygame
import random
from pygame.math import Vector2

pygame.init()

width = 600
height = 600
clock = pygame.time.Clock()
fps = 60
running = True

screen = pygame.display.set_mode((width, height), pygame.DOUBLEBUF)

class Obstacles(pygame.sprite.Sprite):

    def __init__(self):

        pygame.sprite.Sprite.__init__(self) # inheritance from the pygame sprite
        self.size = 50 # size of the square
        self.x = random.randint(0, (width - self.size+10)) # Some offset
        self.y = random.randint(0, (height - self.size+10))
        self.image = pygame.Surface((self.size, self.size), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        pygame.draw.rect(self.image, (255,255,255), self.rect)
        self.rect.x = self.x # Putting the rect on a random location
        self.rect.y = self.y 

class Player(pygame.sprite.Sprite):

    def __init__(self, position):

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((70, 50), pygame.SRCALPHA)
        self.image.fill((0,0,0))
        self.original_image = self.image
        self.rect = self.image.get_rect(center=position)
        self.pos = Vector2(position)
        self.direction = Vector2(1,0)
        self.speed = 0
        self.angle_speed = 0
        self.angle, self.radius = self.direction.as_polar()

        
    # Moving the rect on the screen
    def start_move_left(self):
        self.angle_speed = -10
    def stop_move_left(self):
        self.angle_speed = 0

    def start_move_right(self):
        self.angle_speed = 5
    def stop_move_right(self):
        self.angle_speed = 0

    def start_move_up(self):
        self.speed = -5
    def stop_move_up(self):
        self.speed = 0

    def start_move_down(self):
        self.speed = 10
    def stop_move_down(self):
        self.speed = 0

    def update(self):
        self.angle = self.angle % 360 # keeping on 360 degrees

        if self.angle_speed:
            self.angle += self.angle_speed # add the angle to the "Vector"
            # Putting the angle on the direction Vector
            self.direction.rotate_ip(self.angle_speed)
            # Rotate the Object
            self.image = pygame.transform.rotate(self.original_image,
                                                 -self.angle)
            # Keep the object centered
            self.rect = self.image.get_rect(center=self.rect.center)
        # Add the position to the velocity
        self.pos += self.direction * self.speed
        # Keep the object centered
        self.rect.center = self.pos


allsprites = pygame.sprite.Group()
walls = pygame.sprite.Group()
character = pygame.sprite.Group()
player = Player((width/2, height/2))
character.add(player)

for x in range(10): # Add walls
    x = Obstacles()
    x.add(walls)

allsprites.add(walls)
allsprites.add(character)

def check_if_hits():

    # Checking the Colision
    collision = pygame.sprite.groupcollide(character, walls, False, False)
    stop_loop = True
    
    if collision:
        while stop_loop:
            # Only when are collision, the number is generate
            num = random.randint(0, 100)
            print("You number is: {}".format(num))

            if num >= 30:
                print("You hit!")
                stop_loop = False
                #break
            else:
                print("You miss")
                stop_loop = False
                #break

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

    check_if_hits() # Calling the Function

    allsprites.update()
    screen.fill((51,51,51))
    allsprites.draw(screen)
    pygame.display.flip()
    clock.tick(fps)
    #print(clock.get_fps())

pygame.quit()


