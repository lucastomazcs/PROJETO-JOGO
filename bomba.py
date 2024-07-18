import pygame
from pygame.sprite import Sprite
from mapa import Mapa

class Bomba(Sprite):
    
    def __init__(self, posicaobomba, tempo, raiodeexplosao, tamanho, mapa):
        pygame.sprite.Sprite.__init__(self)

        self.__posicaobomba = posicaobomba
        self.__tempo = tempo
        self.__raiodeexplosao = raiodeexplosao
        self.tempo_decorrido = 0
        self.mapa = mapa

        self.image_index = 0
        self.images = [
            pygame.transform.scale(pygame.image.load('Bombas/bombinha1.png').convert_alpha(), tamanho),
            pygame.transform.scale(pygame.image.load('Bombas/bombinha02.png').convert_alpha(), tamanho),
            pygame.transform.scale(pygame.image.load('Bombas/bombinha03.png').convert_alpha(), tamanho),
            pygame.transform.scale(pygame.image.load('Bombas/bombinha04.png').convert_alpha(), tamanho)
        ]

        self.image = self.images[self.image_index]
        self.rect = self.image.get_rect(topleft = posicaobomba)
        self.tempo_animacao = 0.02
        self.contador_tempo = 0
    
    def update(self, dt):
        self.tempo_decorrido +=  dt
        self.contador_tempo += dt
        if self.contador_tempo >= self.tempo_animacao:
            self.contador_tempo = 0
            self.image_index = (self.image_index + 1) % len(self.images)
            self.image = self.images[self.image_index]
        if self.tempo_decorrido >= self.__tempo:
            self.explodir()

    def explodir(self):
        self.criar_explosao()
        self.causar_dano()
        self.kill() #remover bomba da tela

    def criar_explosao(self):
        raio_explosao = pygame.Rect(self.rect.centerx - self.__raiodeexplosao,
                                    self.rect.centery - self.__raiodeexplosao,
                                    self.__raiodeexplosao *2,
                                    self.__raiodeexplosao *2)
        pygame.draw.rect(self.mapa.tela, (220, 0, 0), raio_explosao, 2) #Desenha o raio de exploão na tela (Teste)
    def causar_dano(self):
        raio_explosao = pygame.Rect(self.rect.centerx - self.__raiodeexplosao,
                                    self.rect.centery - self.__raiodeexplosao,
                                    self.__raiodeexplosao *2,
                                    self.__raiodeexplosao *2)
        for bloco in self.mapa.blocos:
            if raio_explosao.colliderect(bloco.rect) and bloco.destrutivel:
                bloco.kill()
                self.mapa.blocos.remove(bloco)
    @property
    def posicaoBomba(self):
        return self.__posicaobomba
    @property
    def tempo(self):
        return self.__tempo
    @property
    def raio(self):
        return self.__raiodeexplosao
    

