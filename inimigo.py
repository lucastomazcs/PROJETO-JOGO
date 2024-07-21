from pygame.sprite import Sprite
import pygame
import math
import random
from mapa import Mapa
from bomba import Bomba
from player import Player


class Inimigo(Sprite):

    def __init__(self, posicao, vida, velocidade, direcao, mapa, tamanho):
        super().__init__()
        self.__posicao = posicao
        self.__vida = vida
        self.__velocidade = velocidade
        self.__direcao = direcao

        self.mapa = mapa

        # Carregando imagens inimigo
        self.images = [
            pygame.transform.scale(pygame.image.load(
                'Inimigo/inimigo_andando01.png').convert_alpha(), tamanho),
            pygame.transform.scale(pygame.image.load(
                'Inimigo/inimigo_andando02.png').convert_alpha(), tamanho),
            pygame.transform.scale(pygame.image.load(
                'Inimigo/inimigo_andando03.png').convert_alpha(), tamanho),
            pygame.transform.scale(pygame.image.load(
                'Inimigo/inimigo_andando_lado01.png').convert_alpha(), tamanho),
            pygame.transform.scale(pygame.image.load(
                'Inimigo/inimigo_andando_lado02.png').convert_alpha(), tamanho),
            pygame.transform.scale(pygame.image.load(
                'Inimigo/inimigo_andando_lado03.png').convert_alpha(), tamanho),
            pygame.transform.scale(pygame.image.load(
                'Inimigo/inimigo_andando_tras01.png').convert_alpha(), tamanho),
            pygame.transform.scale(pygame.image.load(
                'Inimigo/inimigo_andando_tras02.png').convert_alpha(), tamanho),
            pygame.transform.scale(pygame.image.load(
                'Inimigo/inimigo_andando_tras03.png').convert_alpha(), tamanho)

        ]

        self.image_index = 0
        self.image = self.images[self.image_index]
        self.rect = self.image.get_rect()

        # Definindo posição inicial do inimigo:
        self.rect.bottomright = posicao

        # Tempo de troca de animação:
        self.tempo_animacao = 1
        self.contador_tempo = 0

    @property
    def posicao(self):
        return self.__posicao

    @property
    def vida(self):
        return self.__vida

    @property
    def velocidade(self):
        return self.__velocidade

    @property
    def direcao(self):
        return self.__direcao

    def movimento(self, posicao_player, dt: float):
        # Calcula a direção para o jogador
        direcao_x, direcao_y = 0, 0
        if self.rect.x < posicao_player[0]:
            direcao_x = 1
        elif self.rect.x > posicao_player[0]:
            direcao_x = -1
        if self.rect.y < posicao_player[1]:
            direcao_y = 1
        elif self.rect.y > posicao_player[1]:
            direcao_y = -1

        # Movimenta o inimigo no eixo x
        self.rect.x += direcao_x * self.velocidade * dt

        # Checa colisões com blocos e bombas no eixo X
        if pygame.sprite.spritecollideany(self, self.mapa.blocos) or pygame.sprite.spritecollideany(self, self.mapa.bombas):
            # Reverte movimento no eixo X
            self.rect.x -= direcao_x * self.velocidade * dt

        # Movimenta o inimigo no eixo Y
        self.rect.y += direcao_y * self.velocidade * dt
        
        # Checa colisões com blocos e bombas no eixo Y
        if pygame.sprite.spritecollideany(self, self.mapa.blocos) or pygame.sprite.spritecollideany(self, self.mapa.bombas):
            # Reverte movimento no eixo Y
            self.rect.y -= direcao_y * self.velocidade * dt

        # Atualiza a posição interna do inimigo
        self.__posicao = self.rect.topleft


        # Adicionar colisão com obstaculos:
    def plantar_bomba(self):
        #Fazer o inimigo plantar bombas
        pass
    
    '''def sofrer_dano(self):
       self.vidas -= 1
       if self.vidas <=0:
          self.morrer()'''

    def morrer(self):
       print("O Inimigo morreu!!")
       self.kill()

    def update(self, posicao_jogador,  dt: float):
       posicao_antiga = self.rect.bottomright
       
       #Perseguir Jogador:
       self.movimento(posicao_jogador, dt)

        #Checar colisão com bombas:
       self.checar_colisão_bombas()
    
    def checar_colisão_bombas(self):
       for bomba in self.mapa.bombas:
          if pygame.sprite.collide_rect(self, bomba):
             print("Inimigo atingido!")
             self.sofrer_dano()
             break

    def colisao(self, sprite, eixo):
        if eixo == 'x':
            if self.rect.x < sprite.rect.x:
                self.rect.right = sprite.rect.left
            else:
                self.rect.left = sprite.rect.right
        elif eixo == 'y':
            if self.rect.y < sprite.rect.y:
                self.rect.bottom = sprite.rect.top
            else:
                self.rect.top = sprite.rect.bottom

    def animacao(self, dt: float):
        self.contador_tempo += dt
        if self.contador_tempo >= self.tempo_animacao:
            self.contador_tempo = 0
            self.image_index = (self.image_index + 1) % len(self.images)
            self.image = self.images[self.image_index]


    def update(self, posicao_player, dt: float):
        #print(f"Update chamado com posicao_player: {posicao_player}, dt: {dt}") #Debug
        #Atualiza a posição do inimigo
        self.movimento(posicao_player, dt)
        #Atualiza animação quando inimigo se move:
        self.animacao(dt)
        print(self.velocidade) #Debug