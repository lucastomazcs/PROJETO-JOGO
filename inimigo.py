import pygame
from pygame.sprite import Sprite
import math
from mapa import Mapa
from bomba import Bomba
from personagens import Personagem

class Inimigo(Personagem, Sprite):  # Inimigo herda de Personagem e Sprite
    def __init__(self, posicao, vida, velocidade, direcao, mapa, tamanho):
        # Inicialização da classe base (Personagem)
        Personagem.__init__(self, vida, posicao, velocidade, range_bomba=2)

        # Inicialização da classe Sprite
        Sprite.__init__(self)
        
        self.mapa = mapa
        self.__direcao = direcao

        # Carregando imagens inimigo
        self.images = [
            pygame.transform.scale(pygame.image.load('Inimigo/inimigo_andando01.png').convert_alpha(), tamanho),
            pygame.transform.scale(pygame.image.load('Inimigo/inimigo_andando02.png').convert_alpha(), tamanho),
            pygame.transform.scale(pygame.image.load('Inimigo/inimigo_andando03.png').convert_alpha(), tamanho),
            pygame.transform.scale(pygame.image.load('Inimigo/inimigo_andando_lado01.png').convert_alpha(), tamanho),
            pygame.transform.scale(pygame.image.load('Inimigo/inimigo_andando_lado02.png').convert_alpha(), tamanho),
            pygame.transform.scale(pygame.image.load('Inimigo/inimigo_andando_lado03.png').convert_alpha(), tamanho),
            pygame.transform.scale(pygame.image.load('Inimigo/inimigo_andando_tras01.png').convert_alpha(), tamanho),
            pygame.transform.scale(pygame.image.load('Inimigo/inimigo_andando_tras02.png').convert_alpha(), tamanho),
            pygame.transform.scale(pygame.image.load('Inimigo/inimigo_andando_tras03.png').convert_alpha(), tamanho)
        ]

        self.image_index = 0
        self.image = self.images[self.image_index]
        self.rect = self.image.get_rect()

        # Definindo posição inicial do inimigo
        self.rect.bottomright = posicao

        # Tempo de troca de animação
        self.tempo_animacao = 1
        self.contador_tempo = 0
        self.tempo_ultimo_plante = 0
        self.intervalo_bomba = 3
        self.minhas_bombas = []

    @property
    def direcao(self):
        return self.__direcao

    def movimento(self, posicao_player, dt: float):
        posicao_original = self.rect.topleft
    
        # Calcula a direção para o jogador:
        delta_x = posicao_player[0] - self.rect.centerx
        delta_y = posicao_player[1] - self.rect.centery
        distancia = math.hypot(delta_x, delta_y)

        if distancia != 0:
            direcao_x = (delta_x / distancia) * self.velocidade * dt
            direcao_y = (delta_y / distancia) * self.velocidade * dt
        else:
            direcao_x = 0
            direcao_y = 0

        #Tentativa de movimento no eixo X
        self.rect.x += direcao_x

        #Checa colisões com blocos e bombas no eixo X
        if pygame.sprite.spritecollideany(self, self.mapa.blocos) or pygame.sprite.spritecollideany(self, self.mapa.bombas):
            self.rect.x = posicao_original[0]

        #Tentativa de movimento no eixo Y
        self.rect.y += direcao_y

        #Checa colisões com blocos e bombas no eixo Y
        if pygame.sprite.spritecollideany(self, self.mapa.blocos) or pygame.sprite.spritecollideany(self, self.mapa.bombas):
            self.rect.y = posicao_original[1]

        self._Personagem__posicao = self.rect.topleft  # Atualiza a posição herdada de Personagem

        if self.caminho_bloqueado():
            self.plantar_bomba()

    def caminho_bloqueado(self):
        for bloco in self.mapa.blocos:
            if bloco.destrutivel and self.rect.colliderect(bloco.rect.inflate(20, 20)):
                return True
        return False

    def plantar_bomba(self):
        current_time = pygame.time.get_ticks() / 1000
        if current_time - self.tempo_ultimo_plante >= self.intervalo_bomba:
            bomba = Bomba(self.rect.topleft, self.range_bomba, 30, (40, 40), self.mapa, dono=self)
            self.minhas_bombas.append(bomba)
            self.mapa.bombas.add(bomba)
            self.tempo_ultimo_plante = current_time

    def sofrer_dano(self, fonte):
        # Evita dano de suas próprias bombas
        if fonte in self.minhas_bombas:
            return
        super().sofrer_dano(fonte)  # Usa o método herdado de Personagem

    def matar_jogador(self):
        for jogador in self.mapa.jogadores:
            if pygame.sprite.collide_rect(self, jogador):
                jogador.morrer()

    def animacao(self, dt: float):
        self.contador_tempo += dt
        if self.contador_tempo >= self.tempo_animacao:
            self.contador_tempo = 0
            self.image_index = (self.image_index + 1) % len(self.images)
            self.image = self.images[self.image_index]

    def update(self, posicao_player, dt: float):
        self.movimento(posicao_player, dt)
        self.animacao(dt)
        if abs(posicao_player[0] - self.rect.centerx) <= 40 and abs(posicao_player[1] - self.rect.centery) <= 40:
            self.matar_jogador()
