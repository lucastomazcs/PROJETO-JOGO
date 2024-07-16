import pygame
from mapa import Mapa
from pygame.sprite import Sprite
from bomba import Bomba

class Player(Sprite):
   def __init__(self, posicao, vida, velocidade, range_bomba, mapa, tamanho):
      super().__init__()
    
      self.__posicao = posicao
      self.__vida = vida
      self.__velocidade = velocidade
      self.__range_bomba = range_bomba

      self.mapa = mapa

      #Carregando imagens de animação do jogador:
      self.images = [
          pygame.transform.scale(pygame.image.load('bomberman01.png').convert_alpha(),tamanho),
          pygame.transform.scale(pygame.image.load('bomberman02.png').convert_alpha(),tamanho),
          pygame.transform.scale(pygame.image.load('bomberman03.png').convert_alpha(), tamanho)
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
     if keys[pygame.K_s]:
         movimento_y += self.__velocidade
     if keys[pygame.K_d]:
         movimento_x += self.__velocidade
     if keys[pygame.K_a]:
         movimento_x -= self.__velocidade
    
     self.rect.x += movimento_x
     if pygame.sprite.spritecollideany(self, self.mapa.blocos):
         self.rect.x -= movimento_x
    
     self.rect.y += movimento_y
     if pygame.sprite.spritecollideany(self, self.mapa.blocos):
         self.rect.y -= movimento_y
     
     self.__posicao = self.rect.topleft
   
   def animacao(self, dt):
     self.contador_tempo += dt
     if self.contador_tempo >= self.tempo_animacao:
         self.contador_tempo = 0
         self.image_index = (self.image_index + 1) % len(self.images)
         self.image = self.images[self.image_index]

   def plantar_bomba(self):
       bomba_pos = self.rect.topleft
       bomba = Bomba(bomba_pos, 3, self.__range_bomba, (40,40))
       self.mapa.bombas.add(bomba)
       
     

   def update(self, dt):
     self.movimento() 
     self.animacao(dt)
     keys = pygame.key.get_pressed()
     if keys[pygame.K_SPACE]:
         self.plantar_bomba()