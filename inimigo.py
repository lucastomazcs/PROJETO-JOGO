from typing import Any
import pygame

class Inimigo(pygame.sprite.Sprite):
    
    def __init__(self, posicao, vida, velocidade, direcao, mapa, tamanho):
        super().__init__()
        self.__posicao = posicao
        self.__vida = vida
        self.__velocidade = velocidade
        self.__direcao = direcao

        self.mapa = mapa

        #Carregando imagens inimigo
        self.images = [
            pygame.transform.scale(pygame.image.load('Inimigo/inimigo_andando01.png').convert_alpha(), tamanho),
            pygame.transform.scale(pygame.image.load('Inimigo/inimigo_andando02.png').convert_alpha(), tamanho),
            pygame.transform.scale(pygame.image.load('Inimigo/inimigo_andando03.png').convert_alpha(), tamanho),
            pygame.transform.scale(pygame.image.load('Inimigo/inimigo_andando_lado01.png').convert_alpha(), tamanho),
            pygame.transform.scale(pygame.image.load('Inimigo/inimigo_andando_lado02.png').convert_alpha(), tamanho),
            pygame.transform.scale(pygame.image.load('Inimigo/inimigo_jogando_bomba01.png').convert_alpha(), tamanho)
        ]

        self.image_index = 0
        self.image = self.images[self.image_index]
        self.rect = self.image.get_rect()

        #Definindo posição inicial do inimigo:
        self.rect.bottomright = posicao

        #Tempo de troca de animação:
        self.tempo_animacao = 0.1
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

    def movimento(self):
        pass
    

    def animacao(self, dt: float):
     self.contador_tempo += dt
     if self.contador_tempo >= self.tempo_animacao:
         self.contador_tempo = 0
         self.image_index = (self.image_index + 1) % len(self.images)
         self.image = self.images[self.image_index]

    def update(self, dt: float):
       self.animacao(dt)