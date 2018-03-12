#!coding:utf-8
#test_collision_v2_EN.py

import random
import math
import pygame
import random
from pygame.math import Vector2

"""
A simple axample of collision.
"""

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

    """
    Pygame sprite class need a:
    self.image = "something" (a pygame.Surface, or a real load image)
    self.rect = self.image.get_rect()
    get_rect() function, grab the size of the surface/image. If is a real image,
    the pygame make some calculation for try to make the best rectangle for the
    image.
    """

    def __init__(self):

        pygame.sprite.Sprite.__init__(self) # inheritance of sprite Class
        self.image = pygame.Surface((50, 50))
        self.rect = self.image.get_rect()
        self.color = (0, 255, 0) # A color for the object draw

        """
        self.pos and self.vel, are Vectors, in math vectors are a object
        which have a magnitude and direction.
        self.pos, self.vel both have a x and y coordinates.
        """
        self.pos = Vector2(0, 0)
        self.vel = Vector2(0, 0)
        self.speed = 10

    def display(self):
        pygame.draw.rect(self.image, self.color, self.rect)

    # This functions are the moviment of the object
    """
    Separate the values you can manipulate the axis separately, so, you can
    press both up and left to move diagonal, down and right... and so on.
    """
    def start_move_left(self):
        self.vel.x = -self.speed # Moving Left
    def stop_move_left(self):
        self.vel.x = 0 # Stop moving
    def start_move_right(self):
        self.vel.x = self.speed # Moving Right
    def stop_move_right(self):
        self.vel.x = 0 # Stop moving
    def start_move_up(self):
        self.vel.y = -self.speed # Moving Up
    def stop_move_up(self):
        self.vel.y = 0 # Stop moving
    def start_move_down(self):
        self.vel.y = self.speed # Moving Down
    def stop_move_down(self):
        self.vel.y = 0 # Stop moving

    def update(self):
        self.display() # Drawing the rectangle

        if self.vel: # If has velocity
            self.pos += self.vel # Add the Velocity Vector to the Position Vector
            self.rect.center = self.pos
            # Made the center of the object the Current Position

allsprites = pygame.sprite.Group() # Creating a Main sprites group
walls = pygame.sprite.Group() # Creating the obstacles grup
character = pygame.sprite.Group() # Creatin/Separating the player for the rest

player = Player() # Calling the Player Class
character.add(player) # Add the Player Class to the separate group

for x in range(10): # Making 10 walls
    x = Obstacles() # Calling the Obstacles Class
    x.add(walls) # Add the walls to the Group

allsprites.add(walls) # Add the walls to the Main Group
allsprites.add(character) # Add the character to the Main Group

def check_if_hits():

    # Checking the Colision
    collision = pygame.sprite.groupcollide(character, walls, False, False)
    stop_loop = False
    
    if collision:
        while not stop_loop:
            # Only when are collision, the number is generate
            num = random.randint(0, 100)
            print("You number is: {}".format(num))

            if num < 30:
                print("You miss!")
                stop_loop = True
                #break
            if num >= 30: # You have 70% of change to hit
                print("You hit!")
                stop_loop = True
                #break

while(running):

    # The main Loop

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Checking of quit's
            running = False # if quit's, exit to the programing by stop the loop

        """
        If the key are down, start move the object, when the key are up, stop
        the object from moving.
        """
        
        # Grabing the key events from pygame.KEYDOWN, if the key's are down
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.start_move_left()
            if event.key == pygame.K_RIGHT:
                player.start_move_right()
            if event.key == pygame.K_UP:
                player.start_move_up()
            if event.key == pygame.K_DOWN:
                player.start_move_down()

        # Grabing the key events from pygame.UP, if the key's are up
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

    allsprites.update() # Update the Main Group of the sprites
    screen.fill((51,51,51)) # Make the backgroup a light gray
    allsprites.draw(screen) # Showing/Drawing all the objects from Main group
    pygame.display.flip() # Update/fliping the screen
    clock.tick(fps) # Setting the fps

pygame.quit() # Cleaning all pygame resources


