import pygame

class Mapa:
    
    def __init__(self):
        self.branco = (255,255,255)
        self.preto = (0,0,0)
        self.cinza = (128,128,128)
        self.azul = (0,0,120)

        self.largura_tela = 1024
        self.altura_tela = 800

        self.largura_mapa = self.largura_tela
        self.altura_mapa = self.altura_tela

        self.num_blocos_x = 12
        self.num_blocos_y = 10


        self.tamanho_bloco_x = self.largura_tela // self.num_blocos_x
        self.tamanho_bloco_y = self.altura_tela // self.num_blocos_y

        #definindo mapa
        self.mapa = [
            # 'W' = Paredes, 'E' = espaços vazios e 'B' = Blocos
            "WWWWWWWWWWWW",
            "WEEEEEEEEEEW",
            "WEBEBEBEBEBW",
            "WEEEEEEEEEEW",
            "WEBEBEBEBEBW",
            "WEEEEEEEEEEW",
            "WEBEBEBEBEBW",
            "WEEEEEEEEEEW",
            "WEBEBEBEBEBW",
            "WEEEEEEEEEEW",
            "WWWWWWWWWWWW"
        ]

        #Ajuste de escala do mapa:
        self.largura_mapa = self.num_blocos_x * self.tamanho_bloco_x
        self.altura_mapa = self.num_blocos_y * self.tamanho_bloco_y


    def desenhar(self, tela):
        for y, linha in enumerate(self.mapa):
            for x, bloco in enumerate(linha):
                x_pos = x * self.tamanho_bloco_x
                y_pos = y * self.tamanho_bloco_y
                if bloco == 'W':
                    pygame.draw.rect(tela, self.cinza, pygame.Rect(x_pos, y_pos, self.tamanho_bloco_x, self.tamanho_bloco_y))
                elif bloco == 'B':
                    pygame.draw.rect(tela, self.azul, pygame.Rect(x_pos, y_pos, self.tamanho_bloco_x, self.tamanho_bloco_y))
                elif bloco == 'E':
                   pygame.draw.rect(tela, self.branco, pygame.Rect(x_pos, y_pos, self.tamanho_bloco_x, self.tamanho_bloco_y))