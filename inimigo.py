from pygame.sprite import Sprite
import pygame
import math
from mapa import Mapa

class Inimigo(Sprite):
    
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
            pygame.transform.scale(pygame.image.load('Inimigo/inimigo_andando_lado03.png').convert_alpha(), tamanho),
            pygame.transform.scale(pygame.image.load('Inimigo/inimigo_andando_tras01.png').convert_alpha(), tamanho),
            pygame.transform.scale(pygame.image.load('Inimigo/inimigo_andando_tras02.png').convert_alpha(), tamanho),
            pygame.transform.scale(pygame.image.load('Inimigo/inimigo_andando_tras03.png').convert_alpha(), tamanho)
           
        ]

        self.image_index = 0
        self.image = self.images[self.image_index]
        self.rect = self.image.get_rect()

        #Definindo posição inicial do inimigo:
        self.rect.bottomright = posicao

        #Tempo de troca de animação:
        self.tempo_animacao = 0.1
        self.contador_tempo = 0

        #Inicializar vidas:
        self.vidas = 3


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

    def movimento(self, posicao_jogador, dt: float):
        #Calcula a direção para o jogador:
        jogador_x, jogador_y = posicao_jogador
        inimigo_x, inimigo_y = self.rect.bottomright
        direcao_x = jogador_x - inimigo_x
        direcao_y = jogador_y - inimigo_y
        distancia = math.hypot(direcao_x, direcao_y)   

        if distancia > 0:
            direcao_x /= distancia
            direcao_y /= distancia 
        
        #Atualizando posição inimigo:
        self.rect.x += direcao_x * self.velocidade * dt
        self.rect.y += direcao_y * self.velocidade * dt

        #Atualiza posição interna:
        self.__posicao = (self.rect.x, self.rect.y)

        #Adicionar colisão com obstaculos:


    def animacao(self, dt: float):
     self.contador_tempo += dt
     if self.contador_tempo >= self.tempo_animacao:
         self.contador_tempo = 0
         self.image_index = (self.image_index + 1) % len(self.images)
         self.image = self.images[self.image_index]

    def plantar_bomba(self):
        #Fazer o inimigo plantar bombas
        pass
    
    def sofrer_dano(self):
       self.vidas -= 1
       if self.vidas <=0:
          self.morrer()

    def morrer(self):
       print("O Inimigo morreu!!")
       self.kill()

    def update(self, posicao_jogador,  dt: float):
       posicao_antiga = self.rect.bottomright
       
       #Perseguir Jogador:
       self.movimento(posicao_jogador, dt)

       #Atualiza animação quando inimigo se move:
       if self.rect.topleft!= posicao_antiga:
        self.animacao(dt)

        #Checar colisão com bombas:
       self.checar_colisão_bombas()
    
    def checar_colisão_bombas(self):
       for bomba in self.mapa.bombas:
          if pygame.sprite.collide_rect(self, bomba):
             print("Inimigo atingido!")
             self.sofrer_dano()
             break