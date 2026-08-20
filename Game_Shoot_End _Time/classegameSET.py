"""
    Shoot End Time:
        Jogo onde o objetivo é eleminar todos os alvos na tela antes que o tempo acabe.
            - Eleminando os alvos antes da finalização do tempo próxima fase, onde o tempo será reduzido
            - Ou mais alvos e mais tempo
"""
import pygame
from pygame.locals import *
from random import randrange, randint
from time import sleep
import os, sys


class Background:
    pass
# Background


class SoundTrack:
    soundtrack = None
    sound = None

    def __init__(self, soundtrack):
        if os.path.isfile(soundtrack):
            self.soundtrack = soundtrack
        else:
            print(soundtrack + " not foud... ignoring", file=sys.stderr)
    # init()

    def play(self): # Define a música de background do jogo
        # Incluir trilha sonora
        pygame.mixer.music.load(self.soundtrack)
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(loops=-1)  # Nº negativos faz a musica tocar infinitamente
    # play()

    def set(self, soundtrack):
        if os.path.isfile(soundtrack):
            self.soundtrack = soundtrack
        else:
            print(soundtrack + " not foud... ignoring", file=sys.stderr)
    # set()

    def play_sound(self, sound):# Definine sons curto, associados a condições
        # Som de colisão
        if os.path.isfile(sound):  # verifica se a música existe
            self.sound = sound
            pygame.mixer.music.load(sound)
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play()
        else:
            print(sound + " not foud... ignoring", file=sys.stderr)
    # play_sounds()
# SoundTrack


class Inimigos:
    image = None
    x = None
    y = None

    def __init__(self, img, x, y):
        inimigos_fig = pygame.image.load(img)
        inimigos_fig.convert()
        inimigos_fig = pygame.transform.scale(inimigos_fig, (60, 60))
        self.image = inimigos_fig
        self.x = x
        self.y = y
    # __initi__()

    def draw(self, screen, x, y):
        screen.blit(self.image, (x, y))
    # draw()
# Inimigos


class Player:
    image = None
    x = None
    y = None

    def __init__(self, img,  x, y):
        player_img = pygame.image.load(img)
        player_img.convert()
        player_img = pygame.transform.scale(player_img, (40, 40))
        self.image = player_img
        self.x = x
        self.y = y
    # __init__()

    def draw(self, screen, x, y):
        screen.blit(self.image, (x, y))
    # draw()
# Player


class Jogo:
    screen = None
    size_screen = None
    width = 640
    height = 480
    run = True

    background = None
    soundtrack = None

    player = []
    player_rect = None
    # movimentação do player
    mouse_pos = None

    inimigos = []
    inimigos_rect = None
    # Variaveis de posição e escolha dos inimigos
    i_x = randrange(60, 580)
    i_y = randrange(147, 333)
    # Variaveis de posição e escolha dos inimigos
    id_inimigos = randint(0, 6)

    aliado = []
    aliado_rect = None

    surf_Fase1 = None

    # Variável para contar os acertos/colisões
    colidiu = 0
    click = False  # verifica se foi clicado com o mouse

    def __init__(self):
        pygame.init() # Iniciando o pygame

        # Criando, nomeando e dimensionando a tela do jogo
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.size_screen = self.screen.get_size()

        # Nomeando a janela do jogo
        pygame.display.set_caption("Shoot End Time")

        # Criando as superfícies das Fases
        dimFase1 = [200, 393]
        self.surf_Fase1 = self.surfaces(dimFase1)
    # __init__()

    def handle_events(self, tela):
        if tela == "menu":
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.run = False
                    exit()
                if event.type == MOUSEBUTTONDOWN:
                    if 100 < self.mouse_pos[0] < 270 and 76 < self.mouse_pos[1] < 116:
                        self.fase_1()
        if tela == "fases":
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.run = False
                    exit()
                if event.type == MOUSEBUTTONDOWN:
                    self.click = True

                if event.type == MOUSEBUTTONUP:
                    self.click = False
    # handle_events

    def surfaces(self, dimension):
        return pygame.Surface(dimension)
    # surfaces()

    def write_message(self, screen, fonte, size, negrito, message, R, G, B, x, y):
        font = pygame.font.SysFont(fonte, size)
        text = font.render(message, negrito, (R, G, B))
        screen.blit(text, (x, y))
    # write_message()

    def draw_explotion(self, screen, x, y):
        explotion_fig = pygame.image.load('Image/explosion.png')
        explotion_fig.convert()
        explotion_fig = pygame.transform.scale(explotion_fig, (120, 120))
        screen.blit(explotion_fig, (x, y))
    # draw_explotion()

    def menu(self):
        FPS = pygame.time.Clock()
        dt = 16

        # loop principal
        while self.run:
            # Fazendo o preenchimento da tela
            self.screen.fill((100, 200, 100))

            # Pegando a posição do mouse
            self.mouse_pos = pygame.mouse.get_pos()

            FPS.tick(1000 / dt)

            # Responsável pelos inputs do jogador
            self.handle_events("menu")

            # Menssagens para a ação do jogador
            self.write_message(self.screen, "daunpenh", 80, True, "START", 255, 255, 255, 100, 60)

            if 100 < self.mouse_pos[0] < 270 and 76 < self.mouse_pos[1] < 116:
                self.write_message(self.screen, "daunpenh", 80, True, "START", 0, 100, 0, 100, 60)

            pygame.display.update()
            FPS.tick(2000)
    # menu()

    def fase_1(self):
        FPS = pygame.time.Clock()
        dt = 16

        # Background
        background_img = pygame.image.load('Image/backgroud.jpg')
        background_img.convert()
        background_img = pygame.transform.scale(background_img, (640, 393))
        self.background = background_img

        # Variável do tempo e controle da fase
        timer = 0
        timer_fase = 10
        contar = True
        iniciar = True
        score = 0

        # Instanciando a classe SoundsTrack e tocando o background
        self.soundtrack = SoundTrack('Sounds/background.wav')
        background_song = pygame.mixer.Sound('Sounds/background.wav')
        pygame.mixer.Channel(0).play(background_song, loops=-1)

        som_tocando = False
        vitoria = False
        game_over = False

        # Definido a posição do personagem
        x = self.mouse_pos[0]
        y = self.mouse_pos[1]

        # Instanciando a classe Player e criando ele
        self.player.append(Player('Image/Mira_0.png', x, y))
        self.player.append(Player('Image/Mira_1.png', x, y))

        # Instaciando os Inimigos
        self.inimigos.append(Inimigos('Image/alien_1.png', self.i_x, self.i_y))
        self.inimigos.append(Inimigos('Image/alien_2.png', self.i_x, self.i_y))
        self.inimigos.append(Inimigos('Image/alien_5.png', self.i_x, self.i_y))
        self.inimigos.append(Inimigos('Image/nave.png', self.i_x, self.i_y))
        self.inimigos.append(Inimigos('Image/alien_6.png', self.i_x, self.i_y))
        self.inimigos.append(Inimigos('Image/alien_7.png', self.i_x, self.i_y))
        self.inimigos.append(Inimigos('Image/alien_8.png', self.i_x, self.i_y))

        # loop principal
        while self.run:
            # Pegando a posição do mouse
            self.mouse_pos = pygame.mouse.get_pos()

            # tocando background music
            #self.soundtrack.play()

            # Atualizando a posição do personagem
            x = self.mouse_pos[0] - 20
            y = self.mouse_pos[1] - 20

            # Fazendo o preenchimento da tela
            self.screen.fill((100, 100, 100))
            FPS.tick(1000 / dt)

            # Responsável pelos inputs do jogador
            self.handle_events("fases")

            # Desenando retângulo da area do jogo e o background
            pygame.draw.rect(self.screen, (0, 0, 0), (0, 87, 640, 393))
            self.screen.blit(self.background, (0, 87))

            # Determinando o tempo da fase
            if contar:
                timer += 1
                if timer == 60:
                    timer_fase -= 1
                    timer = 0

            # Criando Retângulos para as colisões
            self.player_rect = self.player[0].image.get_rect()
            self.player_rect.topleft = (self.mouse_pos[0], self.mouse_pos[1])
            self.inimigos_rect = self.inimigos[self.id_inimigos].image.get_rect()
            self.inimigos_rect.topleft = (self.inimigos[self.id_inimigos].x, self.inimigos[self.id_inimigos].y)

            # Atualizando a posição do inimigo e contando as colisões
            if iniciar:
                if self.player_rect.colliderect(self.inimigos_rect) and self.click:

                    # desenhando imagem de explosão
                    self.draw_explotion(self.screen, self.inimigos[self.id_inimigos].x - 30,
                                        self.inimigos[self.id_inimigos].y - 30)

                    # Som de Explosão
                    self.soundtrack.play_sound('Sounds/explosion.wav')

                    self.id_inimigos = randint(0, 6)
                    self.inimigos[self.id_inimigos].x = self.i_x = randrange(60, 580)
                    self.inimigos[self.id_inimigos].y = self.i_y = randrange(147, 333)

                    self.inimigos_rect.topleft = (self.inimigos[self.id_inimigos].x, self.inimigos[self.id_inimigos].y)

                    self.colidiu += 1
                    score += 10
                    pygame.display.update()

            ############## Inicio dos desenhos dos elementos na superfície 1 ##############
            # Desenhando os inimigos
            self.inimigos[self.id_inimigos].draw(self.screen, self.i_x, self.i_y)

            # Desenhando o timer na tela
            self.write_message(self.screen, "daunpenh", 40, True, 'Timer', 255, 255, 255, 560, 10)
            self.write_message(self.screen, "daunpenh", 40, True, str(timer_fase), 255, 255, 255, 590, 35)

            # Desenhando o Contador de Acertos
            self.write_message(self.screen, "daunpenh", 40, True, 'Acertos', 255, 255, 255, 10, 10)
            self.write_message(self.screen, "daunpenh", 40, True, str(self.colidiu), 255, 255, 255, 45, 35)

            # Desenhando o scorre na tela
            self.write_message(self.screen, "daunpenh", 40, True, 'Pontuação', 255, 255, 255, 280, 10)
            self.write_message(self.screen, "daunpenh", 40, True, str(score), 255, 255, 255, 320, 35)

            # Desenhando a linha que separa a area do jogo
            pygame.draw.line(self.screen, (255, 255, 255), (0, 80), (640, 80), 10)

            # Determinando o Fim da Fase
            if timer_fase > 0 and self.colidiu >= 30:
                background_song.stop()

                self.write_message(self.screen, None, 80, True, 'VENCEDOR', 0, 70, 0, 170, 240)
                self.write_message(self.screen, "daunpenh", 50, True, 'MENU', 255, 255, 255, 5, 440)
                self.write_message(self.screen, "daunpenh", 50, True, 'PRÓXIMA FASE', 255, 255, 255, 384, 440)
                contar = False
                iniciar = False
                vitoria = True

                # Controle dos botões de ação
                if self.click and 5 < self.mouse_pos[0] < 110 and 450 < self.mouse_pos[1] < 478:
                    self.write_message(self.screen, "daunpenh", 50, True, 'MENU', 0, 200, 200, 5, 440)
                    self.colidiu = 0
                    self.menu()

                if 5 < self.mouse_pos[0] < 110 and 450 < self.mouse_pos[1] < 478:
                    self.write_message(self.screen, "daunpenh", 50, True, 'MENU', 0, 200, 200, 5, 440)

                if self.click and 384 < self.mouse_pos[0] < 638 and 450 < self.mouse_pos[1] < 478:
                    self.write_message(self.screen, "daunpenh", 50, True, 'PRÓXIMA FASE', 0, 200, 200, 384, 440)
                    self.colidiu = 0
                    self.fase_2()

                if 384 < self.mouse_pos[0] < 638 and 450 < self.mouse_pos[1] < 478:
                    self.write_message(self.screen, "daunpenh", 50, True, 'PRÓXIMA FASE', 0, 200, 200, 384, 440)

                # tocar musica da vitória da fase
                if not som_tocando and vitoria:
                    self.soundtrack.play_sound('Sounds/vitoria_2.wav')
                    som_tocando = True

            # Determinando o game over
            if timer_fase <= 0 and self.colidiu < 30:
                background_song.stop()

                self.write_message(self.screen, None, 100, True, 'GAME OVER', 70, 0, 0, 130, 240)
                self.write_message(self.screen, "daunpenh", 50, True, 'MENU', 255, 255, 255, 5, 440)
                self.write_message(self.screen, "daunpenh", 50, True, 'REINICIAR', 255, 255, 255, 460, 440)
                contar = False
                iniciar = False
                game_over = True

                # Controle dos botões de ação
                if self.click and 5 < self.mouse_pos[0] < 110 and 450 < self.mouse_pos[1] < 478:
                    self.write_message(self.screen, "daunpenh", 50, True, 'MENU', 0, 200, 200, 5, 440)
                    self.colidiu = 0
                    self.menu()
                if 5 < self.mouse_pos[0] < 110 and 450 < self.mouse_pos[1] < 478:
                    self.write_message(self.screen, "daunpenh", 50, True, 'MENU', 0, 200, 200, 5, 440)

                if self.click and 460 < self.mouse_pos[0] < 638 and 450 < self.mouse_pos[1] < 478:
                    self.write_message(self.screen, "daunpenh", 50, True, 'REINICIAR', 0, 200, 200, 460, 440)
                    self.colidiu = 0
                    self.fase_1()

                if 460 < self.mouse_pos[0] < 638 and 450 < self.mouse_pos[1] < 478:
                    self.write_message(self.screen, "daunpenh", 50, True, 'REINICIAR', 0, 200, 200, 460, 440)

                # tocar musica do game over
                if not som_tocando and game_over:
                    self.soundtrack.play_sound('Sounds/gameover_1.wav')
                    som_tocando = True

            # Desenhando o Player
            if self.inimigos_rect.colliderect(self.player_rect):
                # Desenhando o Player
                self.player[1].draw(self.screen, x, y)
            else:
                # Desenhando o Player
                self.player[0].draw(self.screen, x, y)
            ############## Fim dos desennhos dos elementos na superfície 1 ##############

            pygame.display.update()
            FPS.tick(2000)
    # fase_1()

    def fase_2(self):
        pass
    # fase_2()
# Jogo

print(pygame.font.get_fonts())

# Rodando o Jogo
jogo = Jogo()
jogo.menu()
