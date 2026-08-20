import pygame
from pygame.locals import *


class Elétron(pygame.sprite.Sprite):
    image = None
    x = None
    Y = None
    aceleration_y = None
    Inversor = None
    shoot_goup = None

    def __init__(self, x, y, shoot_group):

        super().__init__()
        eletron_img = pygame.image.load('Image/elétron.png')
        eletron_img.convert()
        eletron_img = pygame.transform.scale(eletron_img, (16, 16))
        self.image = eletron_img

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.aceleration_y = 10
        self.inversor = False
        self.shoot_goup = shoot_group
    # __init__()

    def draw(self, screen, x, y):
        screen.blit(self.image, (x, y))
    # draw()

    def update(self):
        if not self.inversor:
            self.rect.y -= self.aceleration_y
            if self.rect.bottom < 0:
                self.kill()
        if self.inversor:
            self.aceleration_y = 5
            self.rect.y += self.aceleration_y
            if self.rect.top > 480:
                self.kill()
    # update()
# Elétron:
