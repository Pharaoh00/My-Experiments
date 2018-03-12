#!coding:utf-8
#test_collision_v2_PT.py

import random
import math
import pygame
import random
from pygame.math import Vector2

"""
Simples exemplo usango pygame collision.
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

        pygame.sprite.Sprite.__init__(self) # Herança da Classe Sprite
        self.size = 50 # Tamanho do quadrado
        self.x = random.randint(0, (width - self.size+10))
        self.y = random.randint(0, (height - self.size+10))
        self.image = pygame.Surface((self.size, self.size), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        pygame.draw.rect(self.image, (255,255,255), self.rect)
        self.rect.x = self.x # Colocando os quadrados em posições aleatorias
        self.rect.y = self.y 

class Player(pygame.sprite.Sprite):

    """
    Pygame sprite class need a:
    self.image = "something" (a pygame.Surface, or a real load image)
    self.rect = self.image.get_rect()
    get_rect() function, grab the size of the surface/image. If is a real image,
    the pygame make some calculation for try to make the best rectangle for the
    image.

    Pygame sprite Class precisa de:
    self.image = "alguma coisa" (pode ser, pygame.Surface ou alguma imagem)
    # Se for alguma imagem, precisa de carregar ela antes.
    self.rect = self.image.get_rect()
    get_rect() é uma função que pega o tamanho da surface/image. Se é uma imagem,
    pygame vai tentar calcular o melhor quadrado para o tamanho da imagem.
    """

    def __init__(self):

        pygame.sprite.Sprite.__init__(self) # Herança da classe sprite
        self.image = pygame.Surface((50, 50)) # Superficie/Surface
        self.rect = self.image.get_rect()
        self.color = (0, 255, 0) # A cor para o objeto

        """
        self.pos e self.vel são Vetores, em metamatica vetores são objectos que
        tem uma magnitude e uma direção. No caso de self.pos e self.vel os dois
        coordenadas x e y. 
        x = esqueda/direita
        y = cima/baixo
        """
        self.pos = Vector2(0, 0)
        self.vel = Vector2(0, 0)
        self.speed = 10

    def display(self):
        """
        Desenhando um quadrado na superficie que criamos, com a cor que criamos
        e com o quadrado que tem o mesmo tamanho da superficie.
        """
        pygame.draw.rect(self.image, self.color, self.rect)

    # As funções a seguir são para o movimento do objeto
    """
    Os valores são separados por x e y, assim você pode manipular os eixos sepa_
    radamente e assim você pode aperdetar esqueda e cima para andar na diagonal
    ou baixo e direita... e assim vai.
    """
    def start_move_left(self):
        self.vel.x = -self.speed # Para a esquerda
    def stop_move_left(self):
        self.vel.x = 0 # Para de mover
    def start_move_right(self):
        self.vel.x = self.speed # Para a direita
    def stop_move_right(self):
        self.vel.x = 0 # Para de mover
    def start_move_up(self):
        self.vel.y = -self.speed # Para cima
    def stop_move_up(self):
        self.vel.y = 0 # Para de mover
    def start_move_down(self):
        self.vel.y = self.speed # Para baixo
    def stop_move_down(self):
        self.vel.y = 0 # Para de mover

    def update(self):
        self.display() # Mostrando o retangulo

        if self.vel: # Se a velocidade não for 0
            self.pos += self.vel # Adiciona o Vetor da velocidade ao da Posição
            self.rect.x, self.rect.y = self.pos
            # Faz com que o centro do quadrado seja a posição atual

allsprites = pygame.sprite.Group() # Cria o grupo principal para os sprites
walls = pygame.sprite.Group() # Cria o grupo para as paredes
character = pygame.sprite.Group() # Cria um grupo separado para o personagel

player = Player() # Chama a Classe do Player
character.add(player) # Adiciona o grupo separado do Player ao grupo principal

for x in range(10): # Cria 10 obstaculos
    x = Obstacles() # Chama a Classe do Obstacles
    x.add(walls) # Adiciona os obstaculos ao grupo das paredes.

allsprites.add(walls) # Adiciona o grupo das paredes ao grupo principal
allsprites.add(character) # Adiciona o grupo do personagem ao grupo principal

def check_if_hits():

    # Checa por colisão
    collision = pygame.sprite.groupcollide(character, walls, False, False)
    stop_loop = False
    
    if collision:
        while not stop_loop:
            # Somente se há colisão um numero será gerado
            num = random.randint(0, 100)
            print("You number is: {}".format(num))

            if num < 30:
                print("You miss!")
                stop_loop = True
                #break
            if num >= 30: # Tem 70% de chance de acerto
                print("You hit!")
                stop_loop = True
                #break

while(running):

    # Loop principal

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Checa se clicou para sair
            running = False # Se clicou o programa irá parar, saindo do loop

        """
        Se uma das teclas está pressionada, começa a mexer o objeto, quando a 
        tecla é solta o objeto é parado
        """
        
        # Pega os eventos das teclas pressionadas
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.start_move_left()
            if event.key == pygame.K_RIGHT:
                player.start_move_right()
            if event.key == pygame.K_UP:
                player.start_move_up()
            if event.key == pygame.K_DOWN:
                player.start_move_down()

        # Pega os eventos das telcas soltas
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.stop_move_left()
            if event.key == pygame.K_RIGHT:
                player.stop_move_right()
            if event.key == pygame.K_UP:
                player.stop_move_up()
            if event.key == pygame.K_DOWN:
                player.stop_move_down()

    check_if_hits() # Chama a função de colisão

    allsprites.update() # Update o grupo principal das sprites
    screen.fill((51,51,51)) # Cria um fundo cinza claro
    allsprites.draw(screen) # Desenha todos os objetos do grupo principal
    pygame.display.flip() # Update a tela toda
    clock.tick(fps) # Coloca um limite de fps no programa.

pygame.quit() # Limpa todos os recursos do pygame


