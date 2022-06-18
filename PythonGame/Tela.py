import pygame
from pygame.constants import *
from sys import exit

pygame.init()

larguraTela = 640
alturaTela = 480

largRect = 50
altRect = 60

xQuad = (larguraTela / 2) - (largRect / 2)
yQuad = (alturaTela / 2) - (altRect / 2)


tela = pygame.display.set_mode((larguraTela, alturaTela))
pygame.display.set_caption('PokeCloud')
relogio = pygame.time.Clock()

while True:
    relogio.tick(10)
    tela.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYUP:
            yQuad = yQuad + 1

        if event.type == KEYDOWN:
            yQuad = yQuad - 1

        pygame.draw.rect(tela, (255,0,0), (xQuad, yQuad, largRect, altRect))




        pygame.display.update()
