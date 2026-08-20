import pygame

# Imagem do player
player = [pygame.image.load("Image/hydrogen_player_0.png"),
          pygame.image.load("Image/hydrogen_player_1.png"),
          pygame.image.load("Image/hydrogen_player_2.png"),
          pygame.image.load("Image/hydrogen_player_3.png"),
          pygame.image.load("Image/hydrogen_player_4.png"),
          pygame.image.load("Image/hydrogen_player_5.png"),
          pygame.image.load("Image/hydrogen_player_6.png"),
          ]

class Jogador(pygame.sprite.Sprite):
    image = None
    x = None
    y = None
    index = 0

    def __init__(self, x, y):
        super().__init__()
        # Carregando a imagem
        #player_img = pygame.image.load('Image/hidrogênio.png')
        self.player_img = player
        #self.player_img.convert_alpha()
        self.image = self.player_img[self.index]
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y
    # __init__()

    def draw_image(self, screen):
        screen.blit(self.image, self.rect)
    # draw_image()

    def move(self, aceleration_x):
        self.rect.x += aceleration_x
    # move()

    def update(self):
        self.index += 0.3
        if self.index >= len(self.player_img):
            self.index = 0
        self.image = self.player_img[int(self.index)]
    # upadate()
# Jogador:
