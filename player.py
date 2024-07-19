import pygame
from mapa import Mapa
from pygame.sprite import Sprite
from bomba import Bomba

class Player(Sprite):
   def __init__(self, posicao, vida, velocidade, range_bomba, mapa, tamanho):
      super().__init__() #Inicialização da Super classe: Sprite através de um metodo construtor
    
      self.__posicao = posicao
      self.__vida = vida
      self.__velocidade = velocidade
      self.__range_bomba = range_bomba
      self.mapa = mapa

      #Carregando imagens de animação do jogador:
      #Falta o sprite virando para a esquerda
      self.images = [

          pygame.transform.scale(pygame.image.load('Bomberman/bomberman01.png').convert_alpha(), tamanho),
          pygame.transform.scale(pygame.image.load('Bomberman/bomberman02.png').convert_alpha(), tamanho),
          pygame.transform.scale(pygame.image.load('Bomberman/bomberman03.png').convert_alpha(), tamanho)
      ]
      self.image_index = 0
      self.image = self.images[self.image_index]
      self.rect = self.image.get_rect()

      #Definindo posição inicial do jogador:
      self.rect.topleft = posicao

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
   def raio(self):
        return self.__range_bomba

   def movimento(self):
     keys = pygame.key.get_pressed()
     movimento_x = 0
     movimento_y = 0
     if keys[pygame.K_w]:
         movimento_y -= self.__velocidade
         self.image = self.images[2]
     if keys[pygame.K_s]:
         movimento_y += self.__velocidade
         self.image = self.images[0]
     if keys[pygame.K_d]:
         movimento_x += self.__velocidade
         self.image = self.images[1]
     if keys[pygame.K_a]:
         movimento_x -= self.__velocidade
         self.image = self.images[0]
    
     self.rect.x += movimento_x
     if pygame.sprite.spritecollideany(self, self.mapa.blocos) or pygame.sprite.spritecollideany(self, self.mapa.bombas):
         self.rect.x -= movimento_x
    
     self.rect.y += movimento_y
     if pygame.sprite.spritecollideany(self, self.mapa.blocos) or pygame.sprite.spritecollideany(self, self.mapa.bombas):
            self.rect.y -= movimento_y
     
     self.__posicao = self.rect.topleft
   
    #Metodo para Jogador plantar a bomba, ajuste de tamanho, tempo e raio da bomba:
   def plantar_bomba(self):
      
       if self.image == self.images[0]:
           bomba_pos = (self.rect.centerx, self.rect.bottom + 5)
       elif self.image == self.images[1]:  # Imagem apontando para direita
            bomba_pos = (self.rect.right + 5, self.rect.centery)
       elif self.image == self.images[2]:  # Imagem apontando para cima
            bomba_pos = (self.rect.centerx, self.rect.top - 5)
       else:  # Imagem apontando para esquerda
            bomba_pos = (self.rect.left - 5, self.rect.centery)
        
       bomba = Bomba(bomba_pos, 0.4, 25, (40, 40), self.mapa)
       self.mapa.bombas.add(bomba)
      

    #teste de colisão com a bomba:
   def colisao_bomba(self):
       for bomba in self.mapa.bombas:
           if pygame.sprite.collide_rect(self, bomba):
               print("Colisão com bomba detectada")
                              
       
     

   def update(self, dt):
     self.movimento() 
     #self.animacao(dt)
     keys = pygame.key.get_pressed()
     if keys[pygame.K_SPACE]:
         self.plantar_bomba()
     self.colisao_bomba()