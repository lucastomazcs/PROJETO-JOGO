import pygame
from pygame.sprite import Sprite, Group
import math

class Explosao(Sprite): #herança da classe Sprite
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

