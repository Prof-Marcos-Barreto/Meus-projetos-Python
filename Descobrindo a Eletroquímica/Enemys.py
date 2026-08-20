import pygame
from random import randint, choice

# Criando Grupo para os tiros de elétrons
eletronGroup = pygame.sprite.Group()

# Lista de inimigos
atomos = {}
atomos['oxidados'] = [pygame.image.load('Image/litio.png'),
                      pygame.image.load('Image/potássio.png'),
                      pygame.image.load('Image/sódio.png')]

atomos['reduzidos'] = [pygame.image.load('Image/fluor.png'),
                       pygame.image.load('Image/Oxigênio.png'),
                       pygame.image.load('Image/nitrogênio.png')]


class Inimigos(pygame.sprite.Sprite):
    image = None
    x = None
    y = None

    aceleration_x = 0.0
    aceleration_y_oxidados = 0.0
    aceleration_y_reduzidos = 0.0

    grupo = None
    elemento = None
    is_oxidado = None
    is_reduzido = None

    atingido = None

    def __init__(self, x, y):
        super().__init__()

        # Sorteando os inimigos
        self.grupo = choice(['oxidados', 'reduzidos'])
        self.elemento = randint(0, 2)
        self.image = atomos[self.grupo][self.elemento]
        self.image = pygame.transform.scale(self.image, (randint(45, 55), randint(45, 55)))

        # Criando retangulo da imagem dos inimigos para as colisões
        self.x = x
        self.y = y

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.aceleration_x = randint(2, 4)# velocidade do inimigo
        self.aceleration_y_oxidados = 6
        self.aceleration_y_reduzidos = 2
        self.atingido = False # detecta se o inimigo foi atingido

        # Separando os grupos de inimigos para as futuras colisões
        self.is_oxidado = (self.grupo == 'oxidados')
        self.is_reduzido = (self.grupo == 'reduzidos')
    # __init__()

    def draw(self, screen, x, y):
        screen.blit(self.image, x, y)
    # draw()

    def update(self):
        if not self.atingido:
            self.rect.x += self.aceleration_x # movimenta os inimigos
        else:
            if self.is_oxidado:
                self.rect.y += self.aceleration_y_oxidados
            elif self.is_reduzido:
                self.rect.y -= self.aceleration_y_reduzidos
        if self.rect.x > 640 or -50 > self.rect.y > 530:
            self.kill() # elimina os inimigos após saírem da tela
    # update()
# Inimigos:
