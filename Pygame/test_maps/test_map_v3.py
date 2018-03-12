#-*- coding:utf-8 -*-
#test_map_v3.py

import pygame

pygame.init()

s_width = 640
s_height = 360
clock = pygame.time.Clock()
fps = 60
running = True

game_screen = pygame.display.set_mode((s_width, s_height), pygame.DOUBLEBUF)

class Maps:

    def __init__(self, color):

        self.surface = pygame.Surface(game_screen.get_size())
        self.rect = self.surface.get_rect()
        self.surface.fill(color) # Facilitar a visualização

class Player(pygame.sprite.Sprite):
    
    def __init__(self):
        
        pygame.sprite.Sprite.__init__(self) # Inicializando a Herança
        #self.image = pygame.image.load("poo1.png") # Imagem aleatoria
        self.image = pygame.Surface((50,50)) # Criando uma nova Surface
        self.rect = self.image.get_rect() # Criando um rect do tamanho da Surface
        self.rect = pygame.draw.rect(self.image, (0,0,0), self.rect)
        self.speed_x = 0
        self.speed_y = 0
        self.moving = 0

    def start_move_left(self):
        self.moving = 1
        self.speed_x = -10
    def stop_move_left(self):
        self.moving = 0
        self.speed_x = 0

    def start_move_right(self):
        self.moving = 1
        self.speed_x = 10
    def stop_move_right(self):
        self.moving = 0
        self.speed_x = 0

    def start_move_up(self):
        self.moving = 1
        self.speed_y = -10
    def stop_move_up(self):
        self.moving = 0
        self.speed_y = 0

    def start_move_down(self):
        self.moving = 1
        self.speed_y = 10
    def stop_move_down(self):
        self.moving = 0
        self.speed_y = 0

    def update(self):
        #print(self.rect)
        print(self.speed_x)
        print(self.speed_y)
        if self.moving:
            self.rect.x += self.speed_x
            self.rect.y += self.speed_y
            self.dirty = 1

        if self.rect.left < 0:
            m1 = Maps((0,255,0))
            game_screen.blit(m1.surface, (0,0))
        
player = Player()
allsprites = pygame.sprite.Group()
allsprites.add(player)

#m1 = Maps((0,255,0))
#m2 = Maps((255,255,0))
#m3 = Maps((255,0,255))

#current_map = m1.surface
#reset = m1.surface
        
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

    allsprites.update()
    game_screen.fill((100,0,0))
    player.update()
    allsprites.draw(game_screen)
    #game_screen.blit(current_map, (0,0))
    pygame.display.update()
    clock.tick(fps)
    
pygame.quit()
