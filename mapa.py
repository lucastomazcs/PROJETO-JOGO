import pygame
from pygame.sprite import Sprite

class Bloco(Sprite):
    def __init__(self, imagem, x, y, tamanho_bloco):
        super().__init__() #Inicializando a sprite
        self.image = pygame.image.load(imagem).convert_alpha()
        self.image = pygame.transform.scale(self.image,(tamanho_bloco, tamanho_bloco))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x , y) # para definir a posição do retângulo (Bloco destrutivel) na tela

class Mapa:
    
    def __init__(self, num_blocos_x, num_blocos_y, tamanho_bloco):
        self.branco = (255,255,255)
        self.preto = (0,0,0)
        self.cinza = (128,128,128)
        self.azul = (0,0,120)

        self.num_blocos_x = num_blocos_x
        self.num_blocos_y = num_blocos_y
        self.tamanho_bloco = tamanho_bloco

        
        #definindo mapa
        self.mapa = [
            # 'W' = Paredes, 'E' = espaços vazios e 'B' = Blocos
            "WWWWWWWWWWWWWWW",
            "WEEEEEEEEEEEEEW",
            "WEBEBEBEBEBEBEW",
            "WEEEEEEEEEEEEEW",
            "WEBEBEBEBEBEBEW",
            "WEEEEEEEEEEEEEW",
            "WEBEBEBEBEBEBEW",
            "WEEEEEEEEEEEEEW",
            "WEBEBEBEBEBEBEW",
            "WEEEEEEEEEEEEEW",
            "WWWWWWWWWWWWWWW"
        ]

        self.blocos = pygame.sprite.Group()
    
    def desenhar(self, tela):

        self.blocos.empty() #Limpa os blocos antes de redesenhá-los

        for y, linha in enumerate(self.mapa):
            for x, bloco in enumerate(linha):
                x_pos = x * self.tamanho_bloco
                y_pos = y * self.tamanho_bloco
                if bloco == 'W':
                    pygame.draw.rect(tela, self.cinza, pygame.Rect(x_pos, y_pos, self.tamanho_bloco, self.tamanho_bloco))
                elif bloco == 'B':
                    bloco_sprite = Bloco('bloco_fixo.png', x_pos, y_pos, self.tamanho_bloco)
                    self.blocos.add(bloco_sprite)
                elif bloco == 'E':
                   pygame.draw.rect(tela, self.preto, pygame.Rect(x_pos, y_pos, self.tamanho_bloco, self.tamanho_bloco))
        
        self.blocos.draw(tela)
               