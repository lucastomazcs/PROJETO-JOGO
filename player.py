import pygame
from bomba import Bomba

class Player(Bomba, pygame.sprite.Sprite):
   def __init__(self, posicaobomba, tempo, raiodeexplosao, posicao, vida, velocidade, range_bomba):
      super().__init__(posicaobomba, tempo, raiodeexplosao)
      pygame.sprite.Sprite.__init__(self) #Inicializa uma superclasse do pygame

      self.__posicao = posicao
      self.__vida = vida
      self.__velocidade = velocidade
      self.__range_bomba = range_bomba

      self.image = pygame.Surface((40,50))
      self.image.fill((255,0,0))

      self.rect = self.image.get_rect(topleft=posicao)


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
     if keys[pygame.K_w]:
         self.rect.y -= self.__velocidade
     if keys[pygame.K_s]:
         self.rect.y += self.__velocidade
     if keys[pygame.K_d]:
         self.rect.x += self.__velocidade
     if keys[pygame.K_a]:
         self.rect.x -= self.__velocidade

     self.__posicao = self.rect.topleft

   def update(self):
     self.movimento() 