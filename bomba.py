import pygame
from pygame.sprite import Sprite, Group
import math
from explosao import Explosao

class Bomba(Sprite): #herança da classe Sprite
    def __init__(self, posicaobomba, tempo, raiodeexplosao, tamanho, mapa, dono = None):
        pygame.sprite.Sprite.__init__(self)

        self.__posicaobomba = posicaobomba
        self.__tempo = tempo
        self.__raiodeexplosao = raiodeexplosao
        self.tempo_decorrido = 0
        self.mapa = mapa
        self.dono = dono

        self.image_index = 0
        self.images = [
            pygame.transform.scale(pygame.image.load('Bombas/bombinha1.png').convert_alpha(), tamanho),
            pygame.transform.scale(pygame.image.load('Bombas/bombinha02.png').convert_alpha(), tamanho),
            pygame.transform.scale(pygame.image.load('Bombas/bombinha03.png').convert_alpha(), tamanho),
            pygame.transform.scale(pygame.image.load('Bombas/bombinha04.png').convert_alpha(), tamanho) 
        ]

        self.image = self.images[self.image_index]
        self.rect = self.image.get_rect(topleft = posicaobomba)
        self.tempo_animacao = 0.05
        self.contador_tempo = 0
    
    def criar_explosao(self): 
        centro_explosao = (self.rect.centerx, self.rect.centery)
        explosao = Explosao(centro_explosao, (self.__raiodeexplosao * 2, self.__raiodeexplosao * 2),0.05, self.mapa, dono= self.dono)

        self.mapa.explosoes.add(explosao)

        return explosao
    
    def causar_dano(self, explosao):
        raio_explosao = explosao.rect
        bloco_destruido = False

        centro_explosao = raio_explosao.center

        #Identificando o bloco mais proximo do centro da explosão:
        bloco_mais_proximo = None
        menor_distancia = float('inf')

        for bloco in self.mapa.blocos:
            if bloco.destrutivel:
                bloco_centro = bloco.rect.center
                distancia = math.hypot(bloco_centro[0] - centro_explosao[0], bloco_centro[1] - centro_explosao[1])

                if distancia <= self.__raiodeexplosao + bloco.rect.width / 2:
                    if raio_explosao.colliderect(bloco.rect):
                        if distancia < menor_distancia:
                            menor_distancia = distancia
                            bloco_mais_proximo = bloco
                            
        if bloco_mais_proximo:
            print(f"Colisão detectada com bloco destrutível: {bloco.rect}") #Testando a colisão
            bloco_mais_proximo.kill()
            self.mapa.blocos.remove(bloco_mais_proximo)
            bloco_destruido = True
                
        for jogador in self.mapa.jogadores:
            if raio_explosao.colliderect(jogador.rect):
                print("Colisão com jogador detectada")
                jogador.morrer()

        for inimigo in self.mapa.inimigos:
            if raio_explosao.colliderect(inimigo.rect):
                if inimigo != self.dono:
                    print("Colisão com jogador detectada")
                    inimigo.sofrer_dano(self)
                
    
    def explodir(self):
        explosao= self.criar_explosao()
        self.causar_dano(explosao)
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
    

