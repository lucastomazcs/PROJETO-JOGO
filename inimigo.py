import pygame

class Inimigo(pygame.sprite.Sprite):
    
    def __init__(self, posicao, vida, velocidade, direcao):
        super().__init__()
        self.__posicao = posicao
        self.__vida = vida
        self.__velocidade = velocidade
        self.__direcao = direcao
    
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
