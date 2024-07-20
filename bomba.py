import pygame
from pygame.sprite import Sprite

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
        self.tempo_animacao = 0.3
        self.contador_tempo = 0
    
    def criar_explosao(self):
        raio_explosao = pygame.Rect(self.rect.centerx - self.__raiodeexplosao,
                                    self.rect.centery - self.__raiodeexplosao,
                                    self.__raiodeexplosao * 2,
                                    self.__raiodeexplosao * 2)
        pygame.draw.rect(self.mapa.tela, (240, 0, 0), raio_explosao, 2)
        return raio_explosao


    def causar_dano(self, raio_explosao):
        for bloco in self.mapa.blocos:
            if raio_explosao.colliderect(bloco.rect) and bloco.destrutivel:
                print(f"Colisão detectada com bloco destrutível: {bloco.rect}") #Testando a colisão
                bloco.kill()
                self.mapa.blocos.remove(bloco)
                
        for jogador in self.mapa.jogadores:
            if raio_explosao.colliderect(jogador.rect):
                print("Colisão com jogador detectada")
                jogador.morrer()
    
    def explodir(self):
        raio_explosao = self.criar_explosao()
        self.causar_dano(raio_explosao)
        self.kill()


    def update(self, dt):
        self.tempo_decorrido +=  dt
        self.contador_tempo += dt
        if self.contador_tempo >= self.tempo_animacao:
            self.contador_tempo = 0
            self.image_index = (self.image_index + 1) % len(self.images)
            self.image = self.images[self.image_index]
        if self.tempo_decorrido >= self.__tempo:
            self.explodir()

   
    @property
    def posicaoBomba(self):
        return self.__posicaobomba
    @property
    def tempo(self):
        return self.__tempo
    @property
    def raio(self):
        return self.__raiodeexplosao
    


