#-*- coding:utf-8 -*-
#test_00.py

import pygame

pygame.init()
pygame.key.set_repeat(500, 50)

s_width = 1200
s_height = 600
clock = pygame.time.Clock()
fps = 60
running = True
tile_size = 15*4
w_offset = 0
h_offset = 0

game_screen = pygame.display.set_mode((s_width, s_height), pygame.DOUBLEBUF)
def player():
    player = pygame.Rect(w_offset*tile_size,
                         h_offset*tile_size,
                         tile_size, tile_size)
    pygame.draw.rect(game_screen, (255,255,0), player)
    pygame.display.update(player)


def screen_grid():
    for x in range(0, s_width, tile_size):
        x_line = pygame.draw.line(game_screen,(255,255,255), (x,0),(x,s_height))
        pygame.display.update(x_line)
    for y in range(0, s_height, tile_size):
        y_line = pygame.draw.line(game_screen,(255,255,255), (0,y),(s_width,y))
        pygame.display.update(y_line)
    #pygame.display.update()

while(running):
    clock.tick(fps)
    #print(clock.get_fps())
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                h_offset -= 1
            if event.key == pygame.K_DOWN:
                h_offset += 1
            if event.key == pygame.K_LEFT:
                w_offset -= 1
            if event.key == pygame.K_RIGHT:
                w_offset += 1

    if h_offset > (s_height/tile_size)-1:
        h_offset -= 1
    elif h_offset < 0:
        h_offset += 1
    elif w_offset > (s_width/tile_size)-1:
        w_offset -= 1
    elif w_offset < 0:
        w_offset += 1
    game_screen.fill((0,0,0))
    #screen_grid()
    player()
    #print(h_offset)
    #print(w_offset)
    #print(clock.get_fps())
    #pygame.display.flip()

"""
A fazer:
O problema está em que o offset é uma variavel global, não pode ser alterada,
por uma função.
Então, draw e "show", o player devem estar dentro de uma classe, que terá as
posições x, y do player, o tamanho e a onde vai ser o respawn.
Os eventos, podem ser colocados novamente dentro da classe, sendo assim a classe
sozinha irá cuidar dos eventos de teclado ou mouse (o que for necessario) dentro
da classe, podendo assim ser utilizada dentro dela mesma.
"""
