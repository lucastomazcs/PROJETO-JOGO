from typing import Any
import pygame


class Bomba(pygame.sprite.Sprite):
    
    def __init__(self, posicaobomba, tempo, raiodeexplosao, imagem_Bombas):
        pygame.sprite.Sprite.__init__(self)

        self.__posicaobomba = posicaobomba
        self.__tempo = tempo
        self.__raiodeexplosao = raiodeexplosao

        #Carregamento das sprites plantar bomba
        self.sprites_plantar = []
        for Bombas in imagem_Bombas:
            imagem = pygame.image.load(Bombas).convert_alpha()
            self.sprites_plantar.append(imagem)

        #Indice atual da sprite
        self.contagem_sprite_plantar = 0
        self.image = self.sprites_plantar[self.contagem_sprite_plantar]
        self.rect = self.image.get_rect()
        self.rect.center = self.__posicaobomba

        #Controle de animação:
        self.timer_animacao = pygame.time.get_ticks()
        self.delay = 100 #Tempo entre cada frame de animação(milissegundos)

    def animacao_plantar(self):
        self.timer_animacao = pygame.time.get_ticks()
        self.contagem_sprite_plantar = 0
        self.image = self.sprites_plantar[self.contagem_sprite_plantar]

    def atualizar_plante(self):
        agora = pygame.time.get_ticks()
        if agora - self.timer_animacao > self.delay:
            self.timer_animacao = agora
            self.contagem_sprite_plantar += 1
            if self.contagem_sprite_plantar >= len(self.sprites_plantar):
                #Finalizando a animação quando chega ao ultimo frame
                self.contagem_sprite_plantar = 0
                return True #Retorno pra avisar que a animação acabou
            self.image = self.sprites_plantar[self.contagem_sprite_plantar]
    
    def update(self):
        pass

    
    @property
    def posicaoBomba(self):
        return self.__posicaobomba
    @property
    def tempo(self):
        return self.__tempo
    @property
    def raio(self):
        return self.__raiodeexplosao
    

