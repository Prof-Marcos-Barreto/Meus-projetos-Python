import pygame
from pygame.locals import *


def surfaces(dimension):
    return pygame.Surface(dimension)
# surfaces()

pygame.init()

width = 640
height = 480

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Shoot End Time')

# Criando a Superfície da Fase 1
dimFase1 = [width, height]
surf_Fase1 = surfaces(dimFase1)


def write_message(screen, fonte, size, negrito, message, R, G, B, x, y):
    font = pygame.font.SysFont(fonte, size)
    text = font.render(message, negrito, (R, G, B))
    screen.blit(text, (x, y))
# write_message()


def menu():
    FPS = pygame.time.Clock()
    dt = 16
    run = True

    # loop principal
    while run:
        # Fazendo o preenchimento da tela
        screen.fill((100, 200, 100))

        # Pegando a posição do mouse
        mouse_pos = pygame.mouse.get_pos()

        FPS.tick(1000 / dt)

        # Responsável pelos inputs do jogador
        for event in pygame.event.get():
            if event.type == QUIT:
                quit()
                exit()
            if event.type == MOUSEBUTTONDOWN:
                if 100 < mouse_pos[0] < 270 and 76 < mouse_pos[1] < 116:
                    fase_1()

        # Menssagens para a ação do jogador
        write_message(screen, "daunpenh", 80, True, "START", 255, 255, 255, 100, 60)

        if 100 < mouse_pos[0] < 270 and 76 < mouse_pos[1] < 116:
            write_message(screen, "daunpenh", 80, True, "START", 0, 100, 0, 100, 60)

        pygame.display.update()
        FPS.tick(2000)
# menu()


def fase_1():
    FPS = pygame.time.Clock()
    dt = 16
    run = True

    # Variável do tempo da fase
    timer = timer_fase = 0

    # loop principal
    while run:
        # Pegando a posição do mouse
        mouse_pos = pygame.mouse.get_pos()

        # Fazendo o preenchimento da tela
        # self.screen.fill((150, 200, 50))
        FPS.tick(1000 / dt)

        # Responsável pelos inputs do jogador
        for event in pygame.event.get():
            if event.type == QUIT:
                quit()
                exit()


        screen.blit(surf_Fase1, (0, 0))

        # Fazendo o preenchimento da Surf_Fase1
        surf_Fase1.fill((150, 200, 50))

        # Determinando o tempo da fase
        timer += 1
        if timer == 60:
            timer_fase += 1
            timer = 0

        # Desenhando o timer na tela
        write_message(surf_Fase1, "daunpenh", 40, True, 'Timer', 255, 255, 255, 560, 10)
        write_message(surf_Fase1, "daunpenh", 40, True, str(timer_fase), 255, 255, 255, 590, 50)

        # Determinando o Fim da Fase
        if timer_fase >= 5:
            write_message(surf_Fase1, "daunpenh", 50, True, 'Reiniciar', 255, 255, 255, 270, 80)
            write_message(surf_Fase1, "daunpenh", 50, True, 'Menu', 255, 255, 255, 270, 120)
            write_message(surf_Fase1, "daunpenh", 50, True, 'Próxima Fase', 255, 255, 255, 270, 160)
            # pygame.display.update()
            # self.fase_1()
            # self.run = False

        pygame.display.update()
        FPS.tick(2000)
# fase_1()

# Iniciando o Jogo
menu()