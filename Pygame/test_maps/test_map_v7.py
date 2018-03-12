#!coding:utf-8
#test_map_v7.py
import pygame
from pygame.math import Vector2

pygame.init()

s_width = 600
s_height = 600
clock = pygame.time.Clock()
fps = 30
running = True

game_screen = pygame.display.set_mode((s_width, s_height), pygame.DOUBLEBUF)

class Maps:

    def __init__(self, objects):
        self.objects = objects
        self.image = pygame.Surface(game_screen.get_size())
        self.rect = self.image.get_rect()
        self.map_x = 0
        self.map_y = 0
        self.current_map = (self.map_x, self.map_y)
        self.current_color = self.current_map[1]
        self.current_index = None
        self.steps = 1

    def update(self):
        self.current_map = (self.map_x, self.map_y)
        self.next_map(maps, player)
        game_screen.blit(self.image, (0,0))
        self.image.fill(self.current_color)
        self.objects.update()
        self.objects.draw(self.image)
        print(self.current_map)

    def next_map(self, map_list, p):
        self.p = p
        self.map_list = map_list
        self.current_index = [i for i, j in enumerate(self.map_list) if j[0] == self.current_map]

        for pos, color in self.map_list:
            if pos == self.current_map:
                self.current_map = pos
                self.current_color = color
                
        if self.p.pos[0] < 0:
            self.p.pos[0] = s_width
            self.map_x -= self.steps
        if self.p.pos[0] > s_width:
            self.p.pos[0] = 0
            self.map_x += self.steps

        if self.p.pos[1] < 0:
            self.p.pos[1] = s_height
            self.map_y -= self.steps
        if self.p.pos[1] > s_height:
            self.p.pos[1] = 0
            self.map_y += self.steps

class Player(pygame.sprite.Sprite):
    
    def __init__(self):
        
        pygame.sprite.Sprite.__init__(self) # Inicializando a Herança
        #self.image = pygame.image.load("poo1.png") # Imagem aleatoria
        self.image = pygame.Surface((50,50)) # Criando uma nova Surface
        self.rect = self.image.get_rect()
        self.rect = pygame.draw.rect(self.image, (0,0,0), self.rect)
        self.pos = Vector2(0,0)
        self.vel = Vector2(0,0)
        self.speed = 10
        
    def start_move_left(self):
        self.vel[0] = -self.speed
    def stop_move_left(self):
        self.vel[0] = 0

    def start_move_right(self):
        self.vel[0] = self.speed
    def stop_move_right(self):
        self.vel[0] = 0

    def start_move_up(self):
        self.vel[1] = -self.speed
    def stop_move_up(self):
        self.vel[1] = 0

    def start_move_down(self):
        self.vel[1] = self.speed
    def stop_move_down(self):
        self.vel[1] = 0
        
    def update(self):
        if self.vel:
            self.pos += self.vel
            self.rect.x, self.rect.y = self.pos
        #print(self.pos)
        #print(self.moving)

player = Player()
maps = (((-1,-1),(255,0,0)), ((0,-1),(0,255,0)), ((1,-1), (0,0,255)),
        ((-1,0), (155,0,0)), ((0,0), (0,155,0)), ((1,0), (0,0,155)),
        ((-1,1), (55,0,0)),  ((0,1), (0,55,0)),  ((1,1), (0,0,55)))
allsprites = pygame.sprite.Group()
allsprites.add(player)
m1 = Maps(allsprites)

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

    m1.update()
    pygame.display.update()
    clock.tick(fps)
    #print(clock.get_fps())

pygame.quit()
