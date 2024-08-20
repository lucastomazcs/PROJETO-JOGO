import pygame
from pygame.sprite import Sprite
from bloco import Bloco

class Mapa:
    def __init__(self, num_blocos_x, num_blocos_y, tamanho_bloco, tela):
        self.tela = tela
        self.num_blocos_x = num_blocos_x
        self.num_blocos_y = num_blocos_y
        self.tamanho_bloco = tamanho_bloco

        # Definindo mapa
        self.mapa = [
            "WWWWWWWWWWWWWWW",
            "WEEEDDDDDDDEEEW",
            "WEBEBEBEBEBDBEW",
            "WEDDDDDDEEEDDEW",
            "WDBEBEBEBEBDBDW",
            "WDDEDDDDDDEDDDW",
            "WDBEBEBDBEBDBDW",
            "WDDDDEEDEDDDDDW",
            "WDBEBEBDBEBDBDW",
            "WDDEDDDDDDDDDDW",
            "WDBEBEBDBEBDBDW",
            "WDDDEEEEDDDDDDW",
            "WEBEBEBEBEBEBEW",
            "WEEEDDDDDDDEEEW",
            "WWWWWWWWWWWWWWW"
        ]

        self.blocos = pygame.sprite.Group()
        self.bombas = pygame.sprite.Group()
        self.explosoes = pygame.sprite.Group()
        self.criar_mapa()

    def criar_mapa(self):
        for y, linha in enumerate(self.mapa):
            for x, bloco in enumerate(linha):
                x_pos = x * self.tamanho_bloco
                y_pos = y * self.tamanho_bloco
                if bloco == 'W':
                    bloco_lateral = Bloco('Blocos/bloco_lateral4.png', x_pos, y_pos, self.tamanho_bloco)
                    self.blocos.add(bloco_lateral)
                elif bloco == 'B':
                    bloco_fixo = Bloco('Blocos/blocoEstrelas.png', x_pos, y_pos, self.tamanho_bloco)
                    self.blocos.add(bloco_fixo)
                elif bloco == 'E':
                    Bloco('Fundo/fundo.png', x_pos, y_pos, self.tamanho_bloco)  # Apenas um fundo vazio
                elif bloco == 'D':
                    bloco_destrutivel = Bloco('Blocos/bloco_destrutivel.png', x_pos, y_pos, self.tamanho_bloco, destrutivel=True)
                    self.blocos.add(bloco_destrutivel)

    def desenhar(self, tela):
        self.blocos.draw(tela)
        self.bombas.draw(tela)

    def update(self, dt):
        self.bombas.update(dt)
        self.explosoes.update(dt)

    def aumentar_tamanho_bloco(self, novo_tamanho):
        for bloco in self.blocos:
            bloco.aumentar_tamanho(novo_tamanho)

    def obter_blocos_destrutiveis(self):
        for bloco in self.blocos:
            if bloco.destrutivel:
                print(f"Bloco destrutível encontrado: {bloco.rect}")
