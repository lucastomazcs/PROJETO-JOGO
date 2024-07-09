import pygame

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

    
    def desenhar(self, tela):
        for y, linha in enumerate(self.mapa):
            for x, bloco in enumerate(linha):
                x_pos = x * self.tamanho_bloco
                y_pos = y * self.tamanho_bloco
                if bloco == 'W':
                    pygame.draw.rect(tela, self.cinza, pygame.Rect(x_pos, y_pos, self.tamanho_bloco, self.tamanho_bloco))
                elif bloco == 'B':
                    pygame.draw.rect(tela, self.azul, pygame.Rect(x_pos, y_pos, self.tamanho_bloco, self.tamanho_bloco))
                elif bloco == 'E':
                   pygame.draw.rect(tela, self.branco, pygame.Rect(x_pos, y_pos, self.tamanho_bloco, self.tamanho_bloco))