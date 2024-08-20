import pygame
from pygame.sprite import Sprite
from mapa import Mapa
from bomba import Bomba
from personagens import Personagem

class Player(Personagem, Sprite):  # Player herda de Personagem e Sprite
    def __init__(self, posicao, vida, velocidade, range_bomba, mapa, tamanho):
        # Inicialização da classe base (Personagem)
        Personagem.__init__(self, vida, posicao, velocidade, range_bomba)
        
        # Inicialização da classe Sprite
        Sprite.__init__(self)
        
        self.mapa = mapa

        # Carregando imagens de animação do jogador:
        self.images = [
            pygame.transform.scale(pygame.image.load('Bomberman/bomberman01.png').convert_alpha(), tamanho),
            pygame.transform.scale(pygame.image.load('Bomberman/bomberman02.png').convert_alpha(), tamanho),
            pygame.transform.scale(pygame.image.load('Bomberman/bomberman03.png').convert_alpha(), tamanho),
            pygame.transform.scale(pygame.image.load('Bomberman/bomberman04.png').convert_alpha(), tamanho)
        ]
        
        self.image_index = 0
        self.image = self.images[self.image_index]
        self.rect = self.image.get_rect()

        # Definindo posição inicial do jogador:
        self.rect.topleft = posicao

        # Tempo de troca de animação:
        self.tempo_animacao = 0.01
        self.contador_tempo = 0

        # Variáveis de controle do tempo de plantar a bomba:
        self.tempo_ultimo_plante = 0
        self.intervalo_bomba = 3

    def movimento(self):
        keys = pygame.key.get_pressed()
        movimento_x = 0
        movimento_y = 0

        # Movimentação do jogador
        if keys[pygame.K_w]:
            movimento_y -= self.velocidade  # Usando o atributo herdado de Personagem
            self.image = self.images[2]
        if keys[pygame.K_s]:
            movimento_y += self.velocidade
            self.image = self.images[0]
        if keys[pygame.K_d]:
            movimento_x += self.velocidade
            self.image = self.images[1]
        if keys[pygame.K_a]:
            movimento_x -= self.velocidade
            self.image = self.images[3]

        # Movimenta o jogador no eixo X e checa colisões
        self.rect.x += movimento_x
        bloco_colidido = pygame.sprite.spritecollideany(self, self.mapa.blocos)
        bomba_colidida = pygame.sprite.spritecollideany(self, self.mapa.bombas)

        if bloco_colidido or bomba_colidida:
            if bloco_colidido:
                self.colisao(bloco_colidido, eixo='x')
            if bomba_colidida:
                self.colisao(bomba_colidida, eixo='x')

        # Movimenta o jogador no eixo Y e checa colisões
        self.rect.y += movimento_y
        bloco_colidido = pygame.sprite.spritecollideany(self, self.mapa.blocos)
        bomba_colidida = pygame.sprite.spritecollideany(self, self.mapa.bombas)

        if bloco_colidido or bomba_colidida:
            if bloco_colidido:
                self.colisao(bloco_colidido, eixo='y')
            if bomba_colidida:
                self.colisao(bomba_colidida, eixo='y')

        self._Personagem__posicao = self.rect.topleft  # Atualiza a posição herdada de Personagem

    def update(self, dt):
        self.movimento()
        # self.animacao(dt)  # Caso precise de animação
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.plantar_bomba(dt)
