# Imporatnado Bibliotecas
import pygame
from pygame.locals import *
from cursor import ImgCursor
from Player import Jogador
from eletron import Elétron
from Enemys import Inimigos
from random import randint, choice
from soundtrack import SoundTrack
from barra_de_volume import Barra_de_volume
from barra_de_explosao import Barra_de_Explosao

# Criando um grupo
cursorGroup = pygame.sprite.Group()
eletronGroup = pygame.sprite.Group()
enemyGroup = pygame.sprite.Group()
volumeGroup = pygame.sprite.Group()
b_explosaoGroup = pygame.sprite.Group()

# Instanciando a Classes
    # Imagem do Cursor
imgcursor = ImgCursor()
cursorGroup.add(imgcursor)

    # As SoundTracks
soundtracks = SoundTrack()

    # A barra de volume
b_volume = Barra_de_volume(-50, 120)
b_1_volume = Barra_de_volume(-50, 200)
volumeGroup.add(b_volume, b_1_volume)

    # A barra de explosão
b_explosao = Barra_de_Explosao(500, 20)
b_explosaoGroup.add(b_explosao)

# carregando a imagem de explosão
img_explotion = pygame.image.load("Image/explosion.png")
pygame.transform.scale(img_explotion, (64, 64))


class Gerenciador:
    WIDTH = 640
    HEIGHT = 480
    SCREEN = None
    CLICK_MOUSE = False
    CLICK_SPACE = False
    CLICK_ESCAPE = False
    FPS = pygame.time.Clock()
    RUN = True

    cursor_img = None
    mouse_pos = None

    check_Menu = False
    check_gamemode = False
    check_oxidacao = False
    check_reducao = False
    check_pause_menu = False
    check_opcao = False
    check_instrucao = False
    check_game_over = False

    player = None
    shoot = None
    musicas = soundtracks
    inimigos = {}
    imgvolume = [b_volume, b_1_volume]
    imgexplosao = b_explosao

    aceleration_x = 0.0
    aceleration_y = 0.0
    count_hits = 0

    def __init__(self):
        # Iniciando o pygame
        pygame.init()

        # Criando a tela principal e lhe nomeando
        self.SCREEN = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption('Ainda Não Sei!!!')
        self.SCREEN.fill((5, 5, 5))
        self.SCREEN.set_alpha(400)

        # Sumindo com o cursor do Mouse
        pygame.mouse.set_visible(0)
    # __init__()

    def surfaces(self, width, height):
        dimention = [width, height]
        return pygame.Surface(dimention)
    # surfaces()

    def handle_events(self):
        for event in pygame.event.get(): # Coletando os eventos/mudançãs na tela
            if event.type == QUIT: # Quando clicar no "X" da tela
                quit() # Feche a Tela

            if event.type == MOUSEBUTTONDOWN: # quando eu clico com o botão esquerdo do mouse

                if self.check_Menu: # Ações da Tele Menu
                    # Indicação da colisão do cursor com a palavra START
                    if 211 <= self.mouse_pos[0] <= 444 and 190 <= self.mouse_pos[1] <= 276:
                        self.CLICK_MOUSE = True # Indica que o obotão esquerdo do mouse foi usado

                    # Indicação da colisão do cursor com a palavra INSTRUÇÃO
                    if self.mouse_pos[0] >= 411 and self.mouse_pos[1] >= 417:
                        self.CLICK_MOUSE = True

                    # Indicação da colisão do cursor com a palavra OPÇÃO
                    if self.mouse_pos[0] <= 152 and self.mouse_pos[1] >= 417:
                        self.CLICK_MOUSE = True

                if self.check_gamemode: # ações na tela do Modo de Jogo
                    # Clicou no botão Menu
                    if 466 <= self.mouse_pos[0] <= 619 and 390 <= self.mouse_pos[1] <= 462:
                        self.CLICK_MOUSE =True
                    # Clicou no Botão Oxidação
                    if 379 <= self.mouse_pos[0] <= 624 and 171 <= self.mouse_pos[1] <= 246:
                        self.CLICK_MOUSE = True
                    # Clicou no Botão Redução
                    if 28 <= self.mouse_pos[0] <= 257 and 171 <= self.mouse_pos[1] <= 246:
                        self.CLICK_MOUSE = True

                if self.check_oxidacao:
                    if not self.check_pause_menu:
                        # Criando o tiro de eletron
                        novo_eletron = Elétron(self.player.rect.centerx, self.player.rect.top,
                                               self.inimigos.grupo)
                        eletronGroup.add(novo_eletron)
                        self.musicas.load_sound("tiro", 'Sons/disparo_elétron.wav')
                        self.musicas.play_sound('tiro')

                if self.check_pause_menu:
                    if 14 <= self.mouse_pos[0] <= 168 and 393 <= self.mouse_pos[1] <= 458:
                        self.CLICK_MOUSE = True

                    if 466 <= self.mouse_pos[0] <= 619 and 390 <= self.mouse_pos[1] <= 462:
                        self.CLICK_MOUSE = True

                if self.check_opcao:
                    # Fecha a superfíci  do menu de opções
                    if 237 <= self.mouse_pos[0] <= 409 and 392 <= self.mouse_pos[1] <= 465:
                        self.CLICK_MOUSE = True

                    # Diminue o volume da música de fundo
                    if 2 <= self.mouse_pos[0] <= 50 and 112 <= self.mouse_pos[1] <= 160:
                        self.CLICK_MOUSE = True

                    # Aumenta o volume da música de fundo
                    if 362 <= self.mouse_pos[0] <= 410 and 112 <= self.mouse_pos[1] <= 160:
                        self.CLICK_MOUSE = True

                    # Diminuir o volume dos efeitos sonoros
                    if 2 <= self.mouse_pos[0] <= 50 and 192 <= self.mouse_pos[1] <= 240:
                        self.CLICK_MOUSE = True

                    # Aumentar o volume dos efeitos sonoros
                    if 362 <= self.mouse_pos[0] <= 410 and 192 <= self.mouse_pos[1] <= 240:
                        self.CLICK_MOUSE = True

                if self.check_game_over:
                    if 92 <= self.mouse_pos[0] <= 308 and 272 <= self.mouse_pos[1] <= 338:
                        self.CLICK_MOUSE = True

                    if 392 <= self.mouse_pos[0] <= 538 and 272 <= self.mouse_pos[1] <= 338:
                        self.CLICK_MOUSE = True

            if event.type == MOUSEBUTTONUP:
                self.CLICK_MOUSE = False

            if event.type == KEYDOWN:
                # Aumenta o som do background
                if event.key == K_KP_PLUS:
                    self.imgvolume[0].aumentar_volume()
                    self.musicas.adjust_volume('music', 0.1)

                # Diminuindo o som do background
                if event.key == K_KP_MINUS:
                    self.imgvolume[0].diminuir_volume()
                    self.musicas.adjust_volume('music', -0.1)

                if self.check_reducao or self.check_oxidacao:
                    if event.key == K_LEFT or event.key == K_a: # movimenta o player para a esquerda
                        self.aceleration_x = -5

                    if event.key == K_RIGHT or event.key == K_d: # movimenta o player para a direita
                        self.aceleration_x = 5

                    if event.key == K_ESCAPE:
                        self.check_pause_menu = not self.check_pause_menu

                if self.check_oxidacao:
                    if event.key == K_SPACE:
                        # Criando o tiro de eletron / instanciando a classe Elétron
                        new_eletron = self.shoot = Elétron(self.player.rect.centerx, self.player.rect.top,
                                                           self.inimigos.grupo)
                        eletronGroup.add(new_eletron)
                        self.musicas.load_sound("tiro", 'Sons/disparo_elétron.wav')
                        self.musicas.play_sound('tiro')

            if event.type == KEYUP: # Quando a tecla for solta o player não se movimenta
                if self.check_reducao or self.check_oxidacao:
                    self.aceleration_x = 0
    # handle_events()

    def draw_message(self, screen, fonte, size, negrito, message, R, G, B, x, y):
        font = pygame.font.SysFont(fonte, size) # Definindo a Fonte e seu Tamanho
        text = font.render(message, negrito, (R, G, B)) # Renderizando o Texto e colorindo ele
        screen.blit(text, (x, y)) # Desenhando o texto na tela na posição desejada
    # draw_message()

    def draw_botao_de_acao(self, screen, size_str, msg, x_msg, y_msg,R, G, B, x_rect, y_rect, dimX_rect, dimY_rect, negativo=False):
        if not negativo:
            pygame.draw.rect(screen, (30, 30, 30), (x_rect + 10, y_rect + 10, dimX_rect, dimY_rect), 0, 10, 10, 10, 10, 10)
            pygame.draw.rect(screen, (0, 0, 0), (x_rect, y_rect, dimX_rect, dimY_rect), 0, 10, 10, 10, 10, 10)
            self.draw_message(screen, "microsofthimalaya", size_str, True, msg, R, G, B, x_msg, y_msg)
        if negativo:
            pygame.draw.rect(screen, (0, 0, 0), (x_rect + 10, y_rect + 10, dimX_rect, dimY_rect), 0, 10, 10, 10, 10, 10)
            pygame.draw.rect(screen, (30, 30, 30), (x_rect, y_rect, dimX_rect, dimY_rect), 0, 10, 10, 10, 10, 10)
            self.draw_message(screen, "microsofthimalaya", size_str, True, msg, R, G, B, x_msg, y_msg)
    # draw_botao_de_acao()

    def menu(self):
        # Criando a superfície do Menu
        surf_Menu = self.surfaces(self.WIDTH, self.HEIGHT)

        # Carregando a música de Fundo
        self.musicas.load_music('Sons/background_Menu.mp3')
        self.musicas.play_music()

        # Variável de controle dos objetos de fundo
        nascidos = 0
        print(pygame.font.get_fonts())

        while self.RUN:
            # Verificando se esta na superfície do menu
            self.check_Menu = True
            self.check_gamemode = False
            self.check_reducao = False
            self.check_oxidacao = False
            self.check_pause_menu = False
            self.check_opcao = False
            self.check_instrucao = False
            self.check_game_over = False

            # Posicionando a Superfície do Menu
            self.SCREEN.blit(surf_Menu, (0, 0))

            # Gravando a posição do curso do mouse
            self.mouse_pos = pygame.mouse.get_pos()

            # Preenchendo a a superfície do Menu
            surf_Menu.fill((233, 150, 122))

            # Controla as ações de entrada do jogador
            self.handle_events()

            # Desenhando objetos de fundo
            enemyGroup.draw(surf_Menu)

            # Desenhando o Botão START
            self.draw_botao_de_acao(surf_Menu, 100, "START", (self.WIDTH /2) - 100, (self.HEIGHT / 2) - 50,
                                    255, 255, 255, 218, 198, 208, 60)

                # Indicação da colisão do cursor com a palavra START
            if 211 <= self.mouse_pos[0] <= 444 and 190 <= self.mouse_pos[1] <= 276:
                self.draw_botao_de_acao(surf_Menu, 100, "START", (self.WIDTH / 2) - 100, (self.HEIGHT / 2) - 50,
                                        50, 205, 50, 218, 198, 208, 60, True)

                if self.CLICK_MOUSE: # Mudando para a tela de Modo de Jogo
                    enemyGroup.empty()
                    self.modo_de_jogo()

            # Desenhando o Botão de Instruções
            self.draw_botao_de_acao(surf_Menu, 50, "INSTRUÇÕES", 420, 425, 255, 255, 255, 418, 425, 208, 40)

            # Indicação da colisão do cursor com a palavra instruções
            if self.mouse_pos[0] >= 411 and self.mouse_pos[1] >= 417:
                self.draw_botao_de_acao(surf_Menu, 50, "INSTRUÇÕES", 420, 425, 50, 205, 50, 418, 425, 208, 40, True)

                if self.CLICK_MOUSE: # Muda para a tela de Instruções
                    self.menu_informacao()

            # Desenhando o Botão de Opções
            self.draw_botao_de_acao(surf_Menu, 50, "OPÇÕES", 7, 425, 255, 255, 255, 5, 425, 130, 40)
            #print(f' Posição X: {self.mouse_pos[0]}\nPosição Y: {self.mouse_pos[1]}')

            # Indicação da colisão do cursor com a palavra opções
            if self.mouse_pos[0] <= 152 and self.mouse_pos[1] >= 417:
                self.draw_botao_de_acao(surf_Menu, 50, "OPÇÕES", 7, 425, 50, 205, 50, 5, 425, 130, 40, True)

                if self.CLICK_MOUSE: # Muda para a tela de Opições
                    self.menu_opcao()

            # Desenhando um novo elemento do plano de fundo
            if nascidos <= 0:
                new_enemy = self.inimigos = Inimigos(-50, randint(-30, 460))
                enemyGroup.add(new_enemy)
            nascidos+=1
            if nascidos >= 80:
                nascidos = 0

            self.FPS.tick(60)
            pygame.display.update()
            cursorGroup.draw(surf_Menu)
            cursorGroup.update()
            enemyGroup.update()
    # menu()

    def pause_menu(self):
        # Pausando o efeito sonoro dos tiros
        self.musicas.stop_sound('tiro')

        # Criando a superfície do Pause Menu
        surf_pause_menu = self.surfaces(self.WIDTH, self.HEIGHT)
        surf_pause_menu.set_alpha(200) # deixa a tela semi-transparente

        # Preenchendo a a superfície do Menu
        surf_pause_menu.fill((10, 10, 10))

        # Desenhando o título do menu de pause
        self.draw_message(surf_pause_menu, "microsofthimalaya", 70, True,
                          'JOGO PAUSADO', 255, 255, 255,
                          (self.WIDTH / 2) - 150, (self.HEIGHT / 2) - 70)

        # Desenhando os Botões de Ação
            # Botão de retorno ao Menu
        self.draw_botao_de_acao(surf_pause_menu, 50, "MENU", 490, 400, 255, 255, 255, 474, 398, 128, 46)

            # Colissão botão de ação e cursor
        if 466 <= self.mouse_pos[0] <= 619 and 390 <= self.mouse_pos[1] <= 462:
            self.draw_botao_de_acao(surf_pause_menu, 50, "MENU", 490, 400, 50, 205, 50, 474, 398, 128, 46, True)

            if self.CLICK_MOUSE:
                self.menu()

        # Desenhando o Botão de Opções
        self.draw_botao_de_acao(surf_pause_menu, 50, "OPÇÕES", 24, 405, 255, 255, 255, 21, 400, 135, 46)
        #print(f' Posição X: {self.mouse_pos[0]}\nPosição Y: {self.mouse_pos[1]}')

        # Indicação da colisão do cursor com a palavra opções
        if 14 <= self.mouse_pos[0] <= 168 and 393 <= self.mouse_pos[1] <= 458:
            self.draw_botao_de_acao(surf_pause_menu, 50, "OPÇÕES", 24, 405, 50, 205, 50, 21, 400, 135, 46, True)

            if self.CLICK_MOUSE:  # Muda para a tela de Opições
                self.menu_opcao()

        # Posicionando a superfície do Pause Menu
        self.SCREEN.blit(surf_pause_menu, (0, 0))

        # Gravando a posição do curso do mouse
        self.mouse_pos = pygame.mouse.get_pos()

        # Controla as ações de entrada do jogador
        self.handle_events()

        cursorGroup.draw(self.SCREEN)
        cursorGroup.update()
        pygame.display.update()
    # pause_menu()

    def menu_opcao(self):
        # criando a superfície
        surf_menu_opcao = self.surfaces(self.WIDTH, self.HEIGHT)

        # carregando imagens de aumentar e diminuir o volume
        aumentar_volume = [pygame.image.load("Image/aumentar_abaixa_0.png"),
                           pygame.image.load("Image/aumentar_abaixa_1.png")]
        diminuir_volume = [pygame.image.load("Image/aumentar_abaixa_2.png"),
                           pygame.image.load("Image/aumentar_abaixa_3.png")]

        while self.RUN:
            # verificando se está na superfície menu_opcao
            self.check_oxidacao = False
            self.check_reducao = False
            self.check_gamemode = False
            self.check_Menu = False
            self.check_opcao = True
            self.check_instrucao = False
            self.check_game_over = False

            # Posicionando a superfície do menu_opcao
            self.SCREEN.blit(surf_menu_opcao, (0, 0))

            # Preenchendo o background da superfície do menu_opcao
            surf_menu_opcao.fill((200, 50, 200))

            # Gravando a posição do curso do mouse
            self.mouse_pos = pygame.mouse.get_pos()

            # Controla as ações de entrada do jogador
            self.handle_events()

            # Desenhando o Título da superfície
            self.draw_botao_de_acao(surf_menu_opcao, 70, "Menu de Opções", 162, 10, 255, 255, 255, 145, 15, 350, 50)

            # Desenhando título da barra de volume da música de fundo
            self.draw_message(surf_menu_opcao, "microsofthimalaya", 30, True, "Volume da Música de Fundo",
                              0, 0, 0, 10, 90)

            # Desenhando imagem de diminuir volume da música de fundo
            if 2 <= self.mouse_pos[0] <= 50 and 112 <= self.mouse_pos[1] <= 160:
                surf_menu_opcao.blit(diminuir_volume[1], (10, 120))

                # Diminuindo o volume da música de fundo
                if self.CLICK_MOUSE:
                    self.imgvolume[0].diminuir_volume()
                    self.musicas.adjust_volume("music", -0.1)
            else:
                surf_menu_opcao.blit(diminuir_volume[0], (10, 120))

            # Desenhando imagem de aumentar volume da música de fundo
            if 362 <= self.mouse_pos[0] <= 410 and 112 <= self.mouse_pos[1] <= 160:
                surf_menu_opcao.blit(aumentar_volume[1], (370, 120))

                # Aumenta o volume da música de fundo
                if self.CLICK_MOUSE:
                    self.imgvolume[0].aumentar_volume()
                    self.musicas.adjust_volume("music", 0.1)
            else:
                surf_menu_opcao.blit(aumentar_volume[0], (370, 120))

            # Desenhando título da barra de volume dos efeitos sonoros
            self.draw_message(surf_menu_opcao, "microsofthimalaya", 30, True, "Volume dos Efeitos Sonoros",
                              0, 0, 0, 10, 170)

            # Desenhando imagem de diminuir volume dos efeitos sonoros
            if 2 <= self.mouse_pos[0] <= 50 and 192 <= self.mouse_pos[1] <= 240:
                surf_menu_opcao.blit(diminuir_volume[1], (10, 200))

                # Diminuindo o volume dos efeitos sonoros
                if self.CLICK_MOUSE:
                    self.imgvolume[1].diminuir_volume()
                    self.musicas.adjust_volume("sfx", -0.1)
            else:
                surf_menu_opcao.blit(diminuir_volume[0], (10, 200))

            # Desenhando imagem de aumentar volume dos efeitos sonoros
            if 362 <= self.mouse_pos[0] <= 410 and 192 <= self.mouse_pos[1] <= 240:
                surf_menu_opcao.blit(aumentar_volume[1], (370, 200))

                # Aumenta o volume dos efeitos sonoros
                if self.CLICK_MOUSE:
                    self.imgvolume[1].aumentar_volume()
                    self.musicas.adjust_volume("sfx", 0.1)
            else:
                surf_menu_opcao.blit(aumentar_volume[0], (370, 200))

            # Desenhando as Barras de volume
            volumeGroup.draw(surf_menu_opcao)

            # Desenhando os botões de ação
            self.draw_botao_de_acao(surf_menu_opcao, 50, "VOLTAR", 255, 405, 255, 255, 255, 245, 400, 150, 50)
            #print(f'mouseX = {self.mouse_pos[0]}\n\nmouseY = {self.mouse_pos[1]}')

            # verificando a colilisão do nome voltar e o cursor
            if 237 <= self.mouse_pos[0] <= 409 and 392 <= self.mouse_pos[1] <= 465:
                self.draw_botao_de_acao(surf_menu_opcao, 50, "VOLTAR", 255, 405, 50, 205, 50, 245, 400, 150, 50, True)

                if self.CLICK_MOUSE:
                    break

            # Atualizando a tela
            self.FPS.tick(60)
            cursorGroup.draw(surf_menu_opcao)
            cursorGroup.update()
            pygame.display.update()
    # menu_opcao()

    def menu_informacao(self):
        surf_menu_informacao = self.surfaces(self.WIDTH, self.HEIGHT)

        while self.RUN:
            # verificando se está na superfície menu_informação
            self.check_oxidacao = False
            self.check_reducao = False
            self.check_gamemode = False
            self.check_Menu = False
            self.check_opcao = False
            self.check_instrucao = True
            self.check_game_over = False

            # Posicionando a superfície do menu_opcao
            self.SCREEN.blit(surf_menu_informacao, (0, 0))

            # Preenchendo o background da superfície do menu_opcao
            surf_menu_informacao.fill((100, 50, 250))

            # Gravando a posição do curso do mouse
            self.mouse_pos = pygame.mouse.get_pos()

            # Controla as ações de entrada do jogador
            self.handle_events()

            # Desenhando um botão de voltar
            #self.draw_botao_de_acao(surf_menu_informacao)

            # Atualizando a tela
            self.FPS.tick(60)
            cursorGroup.draw(surf_menu_informacao)
            cursorGroup.update()
            pygame.display.update()
    # menu_informacao()

    def game_over(self):
        surf_game_over = self.surfaces(self.WIDTH, self.HEIGHT)
        surf_game_over.set_alpha(200)  # deixa a tela semi-transparente

        # Preenchendo o background da superfície do menu_opcao
        surf_game_over.fill((10, 10, 10))

        # Gravando a posição do curso do mouse
        self.mouse_pos = pygame.mouse.get_pos()

        # Desenhando a mensagem de game Over na tela
        self.draw_message(surf_game_over, "vani", 100, True, "Game Over", 175, 32, 68, 80, 160)

        # Desenhando botões de ação
        self.draw_botao_de_acao(surf_game_over, 50, "REINICIAR", 110, 280, 255, 255, 255, 100, 280, 190, 40)

        if 92 <= self.mouse_pos[0] <= 308 and 272 <= self.mouse_pos[1] <= 338:
            # colisão do cursor na região do botão reiniciar
            self.draw_botao_de_acao(surf_game_over, 50, "REINICIAR", 110, 280, 50, 205, 50, 100, 280, 190,
                                    40, True)
            if self.CLICK_MOUSE:
                self.reset_game()
                return "reiniciar"

        self.draw_botao_de_acao(surf_game_over, 50, "MENU", 410, 280, 255, 255, 255, 400, 280, 120, 40)

        if 392 <= self.mouse_pos[0] <= 538 and 272 <= self.mouse_pos[1] <= 338:
            # colisão do cursor na região do botão menu
            self.draw_botao_de_acao(surf_game_over, 50, "MENU", 410, 280, 50, 205, 50, 400, 280, 120, 40,
                                    True)

            if self.CLICK_MOUSE:
                return "menu"

        # Posicionando a superfície do menu_opcao
        self.SCREEN.blit(surf_game_over, (0, 0))

        # Trabalha com a entrada do jogador
        self.handle_events()

        # Atualizando a tela
        self.FPS.tick(60)
        cursorGroup.draw(self.SCREEN)
        cursorGroup.update()
        pygame.display.update()
    # game_over()

    def reset_game(self):
        # Limpa todos os grupos
        enemyGroup.empty()
        eletronGroup.empty()

        # Reseta variáveis de estado
        self.count_hits = 0
        self.aceleration_x = 0
        self.imgexplosao.reset_image()

        # Para e Reinicia as músicas
        self.musicas.stop_music()
        self.musicas.stop_sound("tiro")

        # Parando o movimento do player e dos inimigos
        self.check_oxidacao = False
        self.check_reducao = False
        self.check_pause_menu = False  # Impedide que menu de pause do jogo seja aberto
    # reset_game()

    def modo_de_jogo(self):
        # Criando a superfície do modo de jogo
        surf_gamemode = self.surfaces(self.WIDTH, self.HEIGHT)

        while self.RUN: #loop da tela
            # verificando se está na superfície modo de jogo
            self.check_Menu = False
            self.check_oxidacao = False
            self.check_reducao = False
            self.check_gamemode = True
            self.check_pause_menu = False
            self.check_opcao = False
            self.check_instrucao = False
            self.check_game_over = False

            # Posicionando a tela do modo de jogo
            self.SCREEN.blit(surf_gamemode, (0, 0))

            # Gravando a posição do curso do mouse
            self.mouse_pos = pygame.mouse.get_pos()

            # Preenchendo a superfície da tela
            surf_gamemode.fill((233, 150, 122))

            # Controla as ações dos jogadores
            self.handle_events()

            # Posicionando os Botões de ação

                # Título da Tela
            self.draw_botao_de_acao(surf_gamemode, 70, "Selecione o Modo de Jogo", 70, 10, 255, 255, 255, 70, 10, 496, 60)

                # Botões de escolha de modo
            self.draw_botao_de_acao(surf_gamemode, 60, "REDUÇÃO", 40, 180, 255, 255, 255, 36, 178, 204, 50)

            self.draw_botao_de_acao(surf_gamemode, 60, "OXIDAÇÃO", 390, 180, 255, 255, 255, 387, 178, 220, 50)

                # Botão de retorno ao Menu
            self.draw_botao_de_acao(surf_gamemode, 60, "MENU", 480, 400, 255, 255, 255, 474, 398, 128, 46)

            # Indicação de colisão do cursor com os botões de ação
            if 28 <= self.mouse_pos[0] <= 257 and 171 <= self.mouse_pos[1] <= 246:
                self.draw_botao_de_acao(surf_gamemode, 60, "REDUÇÃO", 40, 180, 50, 205, 50, 36, 178, 204, 50, True)

                # Quadrado de informações do modo
                texto = 'Modo para reforçar os conceitos de redução'
                pygame.draw.rect(surf_gamemode, (0, 0, 0), (40, 250, 570, 40), 3, -1, 20, 20, 20, 20)
                self.draw_message(surf_gamemode, "microsofthimalaya", 35, True, texto, 0, 0, 0, 50, 255)

                if self.CLICK_MOUSE:
                    self.modo_redução()

            if 379 <= self.mouse_pos[0] <= 624 and 171 <= self.mouse_pos[1] <= 246:
                self.draw_botao_de_acao(surf_gamemode, 60, "OXIDAÇÃO", 390, 180, 50, 205, 50, 387, 178, 220, 50, True)

                # Quadrado de informações do modo
                texto = 'Modo para reforçar os conceitos de oxidação'
                pygame.draw.rect(surf_gamemode, (0, 0, 0), (40, 250, 570, 40), 3, -1, 20, 20, 20, 20)
                self.draw_message(surf_gamemode, "microsofthimalaya", 35, False, texto, 0, 0, 0, 50, 255)

                if self.CLICK_MOUSE:
                    self.modo_oxidação()

            if 466 <= self.mouse_pos[0] <= 619 and 390 <= self.mouse_pos[1] <= 462:
                self.draw_botao_de_acao(surf_gamemode, 60, "MENU", 480, 400, 50, 205, 50, 474, 398, 128, 46, True)

                if self.CLICK_MOUSE:
                    self.menu()

            # Atualizando a Tela
            self.FPS.tick(60)
            pygame.display.update()
            cursorGroup.draw(surf_gamemode)
            cursorGroup.update()
    # modo_de_jogo()

    def modo_oxidação(self):
        surf_oxidação = self.surfaces(self.WIDTH, self.HEIGHT) # Criando a superfício para o modo oxidação

        # Posição do Player
        x = (self.WIDTH / 2) - 32
        y = self.HEIGHT - 64

        # Instanciando classe Jogador
        self.player = Jogador(x, y)

        # Limitando a quantidade de inimigos
        nascido = 0

        # Carregando a música de Fundo
        self.musicas.load_music('Sons/background_Oxidação.mp3')
        self.musicas.play_music()

        while self.RUN:
            # verificando se está na superfície oxidação
            self.check_oxidacao = True
            self.check_reducao = False
            self.check_gamemode = False
            self.check_Menu = False
            self.check_opcao = False
            self.check_instrucao = False
            self.check_game_over = False

            # Se o jogo estiver pausado, mostra o menu de pause e continua o loop
            if self.check_pause_menu:
                self.pause_menu()
                continue  # Pula o resto do loop enquanto estiver pausado

            # Posicionando a superfície do modo
            self.SCREEN.blit(surf_oxidação, (0, 0))

            surf_oxidação.fill((30, 30, 30)) # preenchendo o fundo da superfície

            self.handle_events() # controlando as ações do jogador

            # Desenhando o player na tela
            self.player.draw_image(surf_oxidação)

            # Desenhando o eletron na tela [o tiro]
            eletronGroup.draw(surf_oxidação)

            # Desenhando os Inimigos na tela
            enemyGroup.draw(surf_oxidação)

            # Desenhando a barra de explosão
            b_explosaoGroup.draw(surf_oxidação)

            # Limitando a movimentação do player - não utrapassar as bordas da tela
            if self.player.rect.x <= 0:
                self.player.rect.x = 0
            elif self.player.rect.x >= 578:
                self.player.rect.x = 578

            # Criando novos inimigos
            if nascido <= 0:
                new_enemy = self.inimigos = Inimigos(-60, randint(60, 128))
                enemyGroup.add(new_enemy)

            nascido += 1
            if nascido >= 70: # limita a quantidade de inimigos que são gerados
                nascido = 0

            # Definindo o sistema de colisões
            hits = pygame.sprite.groupcollide(eletronGroup, enemyGroup, True, False)

            for eletron, inimigos in hits.items():
                for inimigo in inimigos:
                    inimigo.atingido = True
                    inimigo.aceleration_x = 0

                    if inimigo.grupo == "oxidados":
                        self.imgexplosao.proxima_imagem()
                        self.count_hits += 1

                    if inimigo.grupo == "reduzidos":
                        self.imgexplosao.imagem_anterior()
                        if self.count_hits > 0:
                            self.count_hits -= 1

            if self.count_hits >= 1:
                # criar imagem de explosão quando chegar na última img
                surf_oxidação.blit(img_explotion, (self.player.rect.x - 32, self.player.rect.y - 32))
                self.check_game_over = True
                self.game_over()

            if not self.check_game_over:
                # movimentando o Player
                self.player.move(self.aceleration_x)
                # movimentando o eletron
                eletronGroup.update()

                # movimentando os inimigos
                enemyGroup.update()

            # Atualizando a tela
            self.player.update()
            self.FPS.tick(60)
            pygame.display.update()
    # modo_oxidação()

    def modo_redução(self):
        surf_redução = self.surfaces(self.WIDTH, self.HEIGHT)  # Criando a superfício para o modo oxidação

        # Posição do Player
        x = (self.WIDTH / 2) - 32
        y = self.HEIGHT - 64

        # Instanciando classe Jogador
        self.player = Jogador(x, y)

        # Limitando a quantidade de inimigos
        nascido = 0

        # Definindo variáveis de atraso dos tiros
        last_shot_time = 0  # Armazena o momento do último tiro
        shot_delay = 500  # Delay entre tiros em milissegundos (500ms = 0.5s)

        # Carregando a música de Fundo
        self.musicas.load_music('Sons/background_Redução.mp3')
        self.musicas.play_music()

        while self.RUN:
            # verificando se está na superfície reduçãoção
            self.check_oxidacao = False
            self.check_reducao = True
            self.check_gamemode = False
            self.check_Menu = False
            self.check_opcao = False
            self.check_instrucao = False
            self.check_game_over = False

            # Se o jogo estiver pausado, mostra o menu de pause e continua o loop
            if self.check_pause_menu:
                self.pause_menu()
                continue  # Pula o resto do loop enquanto estiver pausado

            # Posicionando a superfície do modo
            self.SCREEN.blit(surf_redução, (0, 0))

            surf_redução.fill((90, 60, 30))  # preenchendo o fundo da superfície

            self.handle_events()  # controlando as ações do jogador

            # Desenhando o player na tela
            self.player.draw_image(surf_redução)

            # Desenhando os inimigos
            enemyGroup.draw(surf_redução)

            # Desenhando a barra de explosão
            b_explosaoGroup.draw(surf_redução)

            # Limitando a movimentação do player - não utrapassar as bordas da tela
            if self.player.rect.x <= 0:
                self.player.rect.x = 0
            if self.player.rect.x >= 578:
                self.player.rect.x = 578

            # Criando novos inimigos
            if nascido <= 0:

                new_enemy = self.inimigos = Inimigos(-60, randint(60, 128))
                enemyGroup.add(new_enemy)

            nascido += 1
            if nascido >= 70:
                nascido = 0

            # Tiro de elétrons dos inimigos
            current_time = pygame.time.get_ticks()  # Obtém o tempo atual em milissegundos

            # Verifica se passou tempo suficiente desde o último tiro
            if current_time - last_shot_time > shot_delay and len(enemyGroup):

                # Sorteia um inimigo aleatório do grupo
                inimigo = choice(list(enemyGroup))

                # Cria um novo tiro para cada inimigo na tela
                tiro = Elétron(inimigo.rect.centerx, inimigo.rect.bottom, inimigo.grupo)
                tiro.inversor = True
                eletronGroup.add(tiro)
                self.musicas.load_sound("tiro", 'Sons/disparo_elétron.wav')
                self.musicas.play_sound('tiro')

                last_shot_time = current_time  # Atualiza o tempo do último tiro

            eletronGroup.draw(surf_redução) # Desenhando o tira na tela

            # Definindo o sistema de colisões
            hits = pygame.sprite.spritecollide(self.player, eletronGroup, True)

            for tiro in hits:
                print(f'Player atingido pelo grupo de inimigos: {tiro.shoot_goup}')

                if tiro.shoot_goup == 'reduzidos':
                    self.player.rect.y -= 30
                    self.imgexplosao.imagem_anterior()
                    if self.count_hits > 0:
                        self.count_hits -= 1

                elif tiro.shoot_goup == 'oxidados':
                    self.player.rect.y += 30
                    self.imgexplosao.proxima_imagem()
                    self.count_hits += 1
                    if self.player.rect.bottom >= 480:
                        self.player.rect.bottom = 480

            if self.count_hits >= 1:
                # criar imagem de explosão quando chegar na última img
                surf_redução.blit(img_explotion, (self.player.rect.x - 32, self.player.rect.y - 32))
                self.check_game_over = True
                self.game_over()

            if not self.check_game_over:
                # movimentando o Player
                self.player.move(self.aceleration_x)

                eletronGroup.update() # Movimentando o tiro

                #movimentando os inimigos
                enemyGroup.update()

            # Atualizando a tela
            self.FPS.tick(60)
            pygame.display.update()
    # modo_redução()
# Gerenciador:
