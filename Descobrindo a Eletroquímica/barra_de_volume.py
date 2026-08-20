import pygame
from pygame.locals import *

# Carregando imagens - barra de volume
barra_volume = [pygame.image.load("Image/barra_de_volume_00.png"),
                pygame.image.load("Image/barra_de_volume_01.png"),
                pygame.image.load("Image/barra_de_volume_02.png"),
                pygame.image.load("Image/barra_de_volume_03.png"),
                pygame.image.load("Image/barra_de_volume_04.png"),
                pygame.image.load("Image/barra_de_volume_05.png"),
                pygame.image.load("Image/barra_de_volume_06.png"),
                pygame.image.load("Image/barra_de_volume_07.png"),
                pygame.image.load("Image/barra_de_volume_08.png"),
                pygame.image.load("Image/barra_de_volume_09.png"),
                pygame.image.load("Image/barra_de_volume_10.png"),
                ]


class Barra_de_volume(pygame.sprite.Sprite):
    image = None
    img_barra_volume = []
    index = 5

    def __init__(self, x, y):
        super().__init__()

        self.img_barra_volume = barra_volume
        self.image = self.img_barra_volume[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    # __init__()

    def aumentar_volume(self):
        if self.index < len(self.img_barra_volume) - 1: # verifica de está no fim da lista
            self.index += 1 # muda para a próxima imagem
            self.image = self.img_barra_volume[self.index] # Atualiza a imagem que está sendo formada
    # aumentar_volume()

    def diminuir_volume(self):
        if self.index > 0:
            self.index -= 1 # passa para a imagem anterior
            self.image = self.img_barra_volume[self.index]
    # diminuir_volume()

