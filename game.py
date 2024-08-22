import pygame
import sys
from mapa import Mapa
from player import Player
from inimigo import Inimigo
from tkinter import Tk
from save import Salvar
from config import Configurações

class Jogo:
    def __init__(self, dificuldade = 'Médio', numero_jogadores = 1):
        pygame.init()

        root = Tk()
        altura_monitor = root.winfo_screenheight()
        largura_monitor = root.winfo_screenwidth()

        self.num_blocos_x = 15
        self.num_blocos_y = 15
        self.tamanho_bloco = (altura_monitor // self.num_blocos_y) - 5

        self.largura = self.num_blocos_x * self.tamanho_bloco
        self.altura = self.num_blocos_y * self.tamanho_bloco

        self.tela = pygame.display.set_mode((self.largura, self.altura), pygame.RESIZABLE)
        pygame.display.set_caption("Bomberman")

        self.cor_preta = (0, 0, 0)
        self.clock = pygame.time.Clock()
        self.game_over = False
        self.vitoria = False
        self.rodando = True

        self.dificuldade = dificuldade
        self.numero_jogadores = numero_jogadores

        if self.dificuldade == 'Fácil':
            self.velocidade_jogador = 3
            self.velocidade_inimigo = 50
            self.vida_inimigo = 1
        elif self.dificuldade == 'Médio':
            self.velocidade_jogador = 2
            self.velocidade_inimigo = 100
            self.vida_inimigo = 2
        elif self.dificuldade == 'Difícil':
            self.velocidade_jogador = 1
            self.velocidade_inimigo = 150
            self.vida_inimigo = 4


        # Inicializa o mapa, jogador e inimigo
        self.mapa = Mapa(self.num_blocos_x, self.num_blocos_y, self.tamanho_bloco, self.tela)
        tamanho_imagem = (self.tamanho_bloco - 9, self.tamanho_bloco - 9)
        tamanho_imagem_inimigo = (self.tamanho_bloco - 9, self.tamanho_bloco - 9)


        self.jogador = Player((60, 60), 100, self.velocidade_jogador, 3, self.mapa, tamanho=tamanho_imagem)
        self.inimigo = Inimigo((self.tamanho_bloco * 14, self.tamanho_bloco * 14), self.vida_inimigo, self.velocidade_inimigo, 'direcao', self.mapa, tamanho=tamanho_imagem_inimigo)

        self.mapa.jogadores = [self.jogador]
        self.mapa.inimigos = [self.inimigo]

        self.sprites = pygame.sprite.Group()
        self.sprites.add(self.jogador)
        self.sprites.add(self.inimigo)

        #Verifica se o numero de jogadores é igual a 2 para adicionar o segundo:
        if numero_jogadores == 2:
            controles_player2 ={
            'cima': pygame.K_UP,
            'baixo': pygame.K_DOWN,
            'esquerda': pygame.K_LEFT,
            'direita': pygame.K_RIGHT,
            'bomba': pygame.K_KP_ENTER
        }
            self.jogador2 = Player((700, 60), 100, self.velocidade_jogador, 3, self.mapa, tamanho=tamanho_imagem, controles=controles_player2 )
            self.mapa.jogadores.append(self.jogador2)
            self.sprites.add(self.jogador2)

        #Criando botões:
        self.botao_start = pygame.Rect(300, 455, 150, 50)
        self.botao_sair = pygame.Rect(300, 530, 150, 50)

        self.salvar = Salvar()

        self.estado = "Inicial" #Define Estado inicial do Jogo

    
    def tela_inicial(self):
        imagem_inicio = pygame.image.load("telas/tela_inicial.png")
        imagem_inicio = pygame.transform.scale(imagem_inicio, (self.largura, self.altura))
        self.tela.blit(imagem_inicio, (0,0))

       # pygame.draw.rect(self.tela, (0,0,0), self.botao_start, 2)
       # pygame.draw.rect(self.tela, (0,0,0), self.botao_sair, 2)

        pygame.display.flip()

    def tela_game_over(self):
        imagem_game_over = pygame.image.load("telas/Tela_Game_Overr.png")
        imagem_game_over = pygame.transform.scale(imagem_game_over, (self.largura, self.altura))
        self.tela.blit(imagem_game_over, (0, 0))
        pygame.display.flip()

    def tela_vitoria(self):
        imagem_vitoria = pygame.image.load("telas/tela_Vitoriaa.png")
        imagem_vitoria = pygame.transform.scale(imagem_vitoria, (self.largura, self.altura))
        self.tela.blit(imagem_vitoria, (0, 0))
        pygame.display.flip()

    def tratar_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.rodando = False
            elif evento.type == pygame.KEYDOWN:
                if self.estado == "Inicial" and evento.key == pygame.K_SPACE:  # Pressione espaço para iniciar
                    self.estado = "Jogando"
                elif self.game_over and evento.key == pygame.K_r:
                    self.reiniciar_jogo()
                elif self.game_over and evento.key == pygame.K_q:
                    self.rodando = False
                elif self.vitoria and evento.key == pygame.K_r:
                    self.reiniciar_jogo()
                elif self.vitoria and evento.key == pygame.K_q:
                    self.rodando = False
                elif evento.key == pygame.K_t:
                    self.salvar.salvar_jogo(self.jogador, self.inimigo, self.mapa)
                elif evento.key == pygame.K_l:
                    self.salvar.carregar_jogo(self.jogador, self.inimigo, self.mapa)
                    self.estado = "Jogando"
            elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:  # Clique com o botão esquerdo do mouse
                if self.estado == "Inicial":
                    if self.botao_start.collidepoint(evento.pos):  # Se clicar no botão Start invisível
                        self.estado = "Jogando"
                    elif self.botao_sair.collidepoint(evento.pos):  # Se clicar no botão Sair invisível
                        self.rodando = False

    def reiniciar_jogo(self):
        self.__init__(dificuldade=self.dificuldade, numero_jogadores=self.numero_jogadores)

    def update(self, dt):
        if self.estado == "Jogando":
            if not self.game_over and not self.vitoria:
                self.jogador.update(dt)
                if len(self.mapa.jogadores) > 1:
                    self.jogador2.update(dt)

                self.inimigo.update(self.jogador.rect.topleft, dt)

                self.tela.fill(self.cor_preta)
                self.mapa.desenhar(self.tela)
                self.mapa.bombas.draw(self.tela)
                self.sprites.draw(self.tela)

                # Atualiza e desenha as explosões
                self.mapa.explosoes.update(dt)
                self.mapa.explosoes.draw(self.tela)

                self.mapa.update(dt)

                pygame.display.flip()

                if len(self.mapa.jogadores) == 1:
                    if not self.jogador.alive():
                        self.game_over = True
                elif len(self.mapa.jogadores) == 2:
                    if not self.jogador.alive() and not self.jogador2.alive():
                        self.game_over = True

                if not self.inimigo.alive():
                    self.vitoria = True

            elif self.game_over:
                self.tela_game_over()
                self.clock.tick(60)
            elif self.vitoria:
                self.tela_vitoria()
                self.clock.tick(60)
        
        elif self.estado == "Inicial":
            self.tela_inicial()    

    def run(self):
        while self.rodando:
            dt = self.clock.tick(60) / 1000
            self.tratar_eventos()
            self.update(dt)

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    configuracoes = Configurações()
    configuracoes.escolher_dificuldade('Difícil')
    configuracoes.escolher_numero_jogadores(2)
    game = Jogo(dificuldade=configuracoes.dificuldade_atual, numero_jogadores= configuracoes.numero_jogadores)
    game.run()
