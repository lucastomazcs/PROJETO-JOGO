import pygame
from pygame.sprite import Sprite, Group

class Explosao(Sprite):
    
    def __init__(self, posicao, tamanho, tempo_animacao, mapa, dono = None):
        super().__init__()

        self.images = [
            pygame.transform.scale(pygame.image.load('Explosão/explosao.png').convert_alpha(), tamanho),
            pygame.transform.scale(pygame.image.load('Explosão/explosao2.png').convert_alpha(), tamanho),
            pygame.transform.scale(pygame.image.load('Explosão/explosao3.png').convert_alpha(), tamanho)

        ]

        self.image_index = 0
        self.image = self.images[self.image_index]
        self.rect = self.image.get_rect(center = posicao)
        self.tempo_animacao = tempo_animacao
        self.contador_tempo = 0
        self.mapa = mapa
        self.dono = dono

    def update(self, dt):
        self.contador_tempo += dt
        if self.contador_tempo >= self.tempo_animacao:
            self.contador_tempo = 0
            self.image_index += 1
            if self.image_index < len(self.images):
                self.image = self.images[self.image_index]
            else:
                self.causar_dano()
                self.kill()
            
    def causar_dano(self):
        for sprite in pygame.sprite.spritecollide(self, self.mapa.jogadores, False):
            sprite.sofrer_dano(self)
        for sprite in pygame.sprite.spritecollide(self, self.mapa.inimigos, False):
            if sprite != self.dono:
                sprite.sofrer_dano(self)


class Bomba(Sprite):
    
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
            pygame.transform.scale(pygame.image.load('Bombas/bombinha04.png').convert_alpha(), tamanho) #Provisorio, porra
        ]

        self.image = self.images[self.image_index]
        self.rect = self.image.get_rect(topleft = posicaobomba)
        self.tempo_animacao = 0.3
        self.contador_tempo = 0
    
    def criar_explosao(self): 
        explosao = Explosao(self.posicaoBomba, (self.__raiodeexplosao * 5, self.__raiodeexplosao * 5), 0.3, self.mapa, dono= self.dono)

        self.mapa.explosoes.add(explosao)

        return explosao
    
    def causar_dano(self, explosao):
        raio_explosao = explosao.rect
        bloco_destruido = False

        for bloco in self.mapa.blocos:
            if raio_explosao.colliderect(bloco.rect) and bloco.destrutivel:
                print(f"Colisão detectada com bloco destrutível: {bloco.rect}") #Testando a colisão
                bloco.kill()
                self.mapa.blocos.remove(bloco)
                bloco_destruido = True
                break
                
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
        dt = dt / 10
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
    


