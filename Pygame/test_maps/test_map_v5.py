#-*- coding:utf-8 -*-
#test_map_v5.py

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

class Maps:

    def __init__(self, objects, m):
        self.maps = m
        self.current_map = self.maps[1][1]
        self.objects = objects
        self.image = pygame.Surface(game_screen.get_size())
        self.rect = self.image.get_rect()

    def update(self):
        #print("current map: ",self.current_map)
        game_screen.blit(self.image, (0,0))
        self.objects.update()
        """
        self.object.update(), objects sendo o grupo com todas as sprites,
        funciona da seguinte forma:
        Tudo na tela será "autalizado", posição dos objetos do grupo.
        """
        self.image.fill(self.current_map)
        self.objects.draw(self.image)
        """
        self.objects.draw(self.image), objects sendo o grupo com todas as sprites
        self.image, sendo a onde os objetos serão desenhados, no caso, no mapa
        atual. Funciona da seguinte forma:
        Todos os objetos do grupo serão desenhados na tela, mas não diz respeito,
        aos calculos como posição por exemplos.
        So diz respeito a desenha os objetos na tela.
        """
        self.next_map(player)
        """
        A FAZER:
        Adicionar mais "mapas" na lista.
        Usar as index´s da lista da coordenadas, (0,0) para andar pelos mapas.
        (0,0) sendo (x,y), x cima/baixo, y(esquerda/direita)
        Se o player for para cima, (-1,0), se o player for para baixo, (0,0)
        Se o player for para esquerda, (0, -1), se o player for
        para direita (0,0).
        self.current_map = self.map[1]
        
        Observações:
        Se self.object.update() estiver "ativo", e self.objects.draw(), estiver
        "desligado", os objetos na tela não seram mostrados, mas a posição será
        atualizada.
        Se self.object.draw() estiver "ativo", e self.objects.update(), estiver
        "desligado", os objetos na tela serão desenhados, mas ficaram estaticos
        na tela. Não iram ser atualizados.

        Meus pensamentos sobre isso:
        No conceito dos mapas, se REALMENTE o player estiver no mapa, os objetos
        (do mapa), serão desenhados. Mas, pode ter outra boolean que irá manter
        track dos outros mapas, os mapas em volta do player por exemplo, podem
        continuar sendo atualizados (suas posições/mecanicas), em um framerate
        menor, e quando o player for nesses mapas, é como se o "mundo" estivesse
        ativo em sua ausencia, dando a iluzação que o "mundo está vivo". 
        Com update() eu posso monter track desses mapas, e continuar os
        atualizando, e com draw(), eu posso manter track a onde o player
        realmente está e desenhar os objetos do mapa.
        Talvez a melhor forma de se atingir esse objetivo é usar os
        sprite.Group() de forma inteligente.
        Ter sprite.Group() para os mapas, para os objetos animados, e assim 
        atualizando e denhando de forma eficiente.
        
        Problemas futuros:
        Como os objetos estarão sendo atualizados na mesma surface, eles vão 
        estar se "esbarrando", se ouver alguma mecanica de colisão, ela será
        aplicada da mesma forma sem os objetos estarem sendo mostrados na tela.
        Talvez colocar os objetos de mapas diferentes em grupos diferentes, 
        sendo assim cada mapa terá o seu proprio grupo? 
        Cabe so testar para saber.
        """
        self.test_current_map = 1
        self.test = self.maps[self.test_current_map][0]
        self.test_map_x = 0
        self.test_map_y = 0
        if self.test[0] == self.test_map_x and self.test[1] == self.test_map_y:
            print(self.test)
        

    def next_map(self, p):
        self.p = p
        if self.p.pos[0] < 0:
            self.current_map = self.maps[0][1]
            self.p.pos[0] = s_width
            self.image.fill(self.current_map)
        if self.p.pos[0] > s_width:
            self.current_map = self.maps[1][1]
            self.p.pos[0] = 0
            self.image.fill(self.current_map)

class Player(pygame.sprite.Sprite):
    
    def __init__(self):
        
        pygame.sprite.Sprite.__init__(self) # Inicializando a Herança
        #self.image = pygame.image.load("poo1.png") # Imagem aleatoria
        self.image = pygame.Surface((50,50)) # Criando uma nova Surface
        self.rect = self.image.get_rect()
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
        #print(self.moving)

player = Player()
maps = (
((-1,-1), (255,255,0)),
((0,0), (255,0,0))
)
allsprites = pygame.sprite.Group()
allsprites.add(player)
m1 = Maps(allsprites, maps)

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
