import pygame
from pygame.sprite import Sprite, Group
from bomba import Bomba

class Personagem:
    def __init__(self, vida, posicao, velocidade, range_bomba):
        self.__vida = vida
        self.__posicao = posicao
        self.__velocidade = velocidade
        self.__range_bomba = range_bomba    
    
    @property
    def vida(self):
        return self.__vida
    
    @property
    def posicao(self):
        return self.__posicao
    
    @property
    def velocidade(self):
        return self.__velocidade
    
    @property
    def range_bomba(self):
        return self.__range_bomba

    @vida.setter
    def vida(self, nova_vida):
        self._vida = nova_vida
    
    def colisao(self, sprite, eixo):
        for bomba in self.mapa.bombas:
            if pygame.sprite.collide_rect(self, bomba):
               print("Colisão com bomba detectada")
        if eixo == 'x':
            if self.rect.right > sprite.rect.left and self.rect.left < sprite.rect.right:
                if self.rect.centerx < sprite.rect.centerx:
                   self.rect.right = sprite.rect.left
                else:
                   self.rect.left = sprite.rect.right
        if eixo == 'y':
            if self.rect.bottom > sprite.rect.top and self.rect.top < sprite.rect.bottom:
                if self.rect.centery < sprite.rect.centery:
                   self.rect.bottom = sprite.rect.top
                else:
                   self.rect.top = sprite.rect.bottom

    def plantar_bomba(self, dt):
        current_time = pygame.time.get_ticks() / 1000 #Obtem o tempo atual em segundos
        if current_time - self.tempo_ultimo_plante >= self.intervalo_bomba:
            if self.image == self.images[0]:
                bomba_pos = (self.rect.centerx - 25, (self.rect.bottom + self.rect.height // 2) - 10)
            elif self.image == self.images[1]:  #Imagem apontando para direita
                bomba_pos = ((self.rect.right + self.rect.width // 2) - 20, self.rect.centery - 19)
            elif self.image == self.images[2]:  #Imagem apontando para cima
                bomba_pos = (self.rect.centerx - 20, (self.rect.top - self.rect.height // 2) - 20)
            elif self.image == self.images[3]:  #Imagem apontando para esquerda
                bomba_pos = (self.rect.left - 40, self.rect.centery - 20)
                        
            bomba = Bomba(bomba_pos, 4.0, 50, (40, 40), self.mapa)

            self.mapa.bombas.add(bomba)
            self.tempo_ultimo_plante = current_time 
    
    def sofrer_dano(self, fonte):
        self.__vida -= 1
        print(f'Perdeu vida, vidas {self.__vida}')
        if self.__vida <= 0:
            self.morrer()
    
    def morrer(self):
        print("O jogador morreu!!")
        self.kill()
    

