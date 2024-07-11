import pygame

class Bomba(pygame.sprite.Sprite):
    
    def __init__(self, posicaobomba, tempo, raiodeexplosao, imagem_Bombas):
        pygame.sprite.Sprite.__init__(self)

        self.__posicaobomba = posicaobomba
        self.__tempo = tempo
        self.__raiodeexplosao = raiodeexplosao
        self.sprites = []
        self.sprites.append(pygame.image.load('Bombas/bombinha1.png'))


    @property
    def posicaoBomba(self):
        return self.__posicaobomba
    @property
    def tempo(self):
        return self.__tempo
    @property
    def raio(self):
        return self.__raiodeexplosao
    

