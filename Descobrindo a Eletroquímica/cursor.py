import pygame

# Carregando as Imagens do Sprite do Cursor
sprite_cursor = []
sprite_cursor.append(pygame.image.load('Image/atom_cursor_0.png'))
sprite_cursor.append(pygame.image.load('Image/atom_cursor_1.png'))
sprite_cursor.append(pygame.image.load('Image/atom_cursor_2.png'))
sprite_cursor.append(pygame.image.load('Image/atom_cursor_3.png'))
sprite_cursor.append(pygame.image.load('Image/atom_cursor_4.png'))


class ImgCursor(pygame.sprite.Sprite):
    image = None
    image_cursor = []
    index = 0
    cursor_rect = None

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image_cursor = sprite_cursor # Trazendo a lista de imagens para o classe
        self.image = self.image_cursor[self.index]

        # Transformando a imagem em um retângulo
        self.rect = self.image.get_rect()
        self.rect.center = [100, 100]
    # __init__()

    def update(self):
        self.index += 0.3
        if self.index >= len(self.image_cursor):
            self.index = 0
        self.image = self.image_cursor[int(self.index)]


        # Movimento
        self.rect.center = pygame.mouse.get_pos()
    # update()
# ImgCursor:
