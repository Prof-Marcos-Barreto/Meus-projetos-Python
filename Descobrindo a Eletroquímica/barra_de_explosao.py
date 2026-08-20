import pygame

barra_explosao = [pygame.image.load("Image/barra_de_explosão_00.png"),
                  pygame.image.load("Image/barra_de_explosão_01.png"),
                  pygame.image.load("Image/barra_de_explosão_02.png"),
                  pygame.image.load("Image/barra_de_explosão_03.png"),
                  pygame.image.load("Image/barra_de_explosão_04.png"),
                  pygame.image.load("Image/barra_de_explosão_05.png"),
                  pygame.image.load("Image/barra_de_explosão_06.png"),
                  pygame.image.load("Image/barra_de_explosão_07.png"),
                  pygame.image.load("Image/barra_de_explosão_08.png"),
                  pygame.image.load("Image/barra_de_explosão_09.png"),
                  pygame.image.load("Image/barra_de_explosão_10.png")]


class Barra_de_Explosao(pygame.sprite.Sprite):
    image = None
    img_barra_explosao = []
    index = 0

    def __init__(self, x, y):
        super().__init__()

        # carregar a lista de imagens para dentro da classe
        self.img_barra_explosao = barra_explosao
        self.image = self.img_barra_explosao[self.index]

        # Convertendo as imagens em retângulos
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    # __init__()

    def proxima_imagem(self):
        if self.index < len(self.img_barra_explosao) - 1: # Verifica se a imagem atual é menor que a última imagem
            self.index += 1
            self.image = self.img_barra_explosao[self.index] # Atualiza a imagem
    # proxima_imagem()

    def imagem_anterior(self):
        if self.index > 0:
            self.index -= 1
            self.image = self.img_barra_explosao[self.index]  # Atualiza a imagem
    # imagem_anterior()

    def reset_image(self):
        if self.index >= 0:
            self.index = 0
    # reset_image()
