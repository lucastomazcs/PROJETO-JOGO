import pygame
from pygame.sprite import Sprite


class Bloco(Sprite):
    def __init__(self, imagem, x, y, tamanho_bloco, destrutivel = False):
        super().__init__() #Inicializando a sprite
        self.image = pygame.image.load(imagem).convert_alpha()
        self.image = pygame.transform.scale(self.image,(tamanho_bloco, tamanho_bloco))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x , y) # para definir a posição do retângulo (Bloco destrutivel) na tela
        self.destrutivel = destrutivel

    def aumentar_tamanho(self,tamanho_novo):
        center = self.rect.center
        self.image = pygame.transform.scale(self.image,(tamanho_novo, tamanho_novo))
        self.rect = self.image.get_rect()
        self.rect.center = center


    def redimensionar_imagem(self, novo_tamanho):
        self.image = pygame.transform.scale(self.image, (novo_tamanho, novo_tamanho))
        self.rect = self.image.get_rect(topleft = self.rect.topleft)

class Mapa:
    
    def __init__(self, num_blocos_x, num_blocos_y, tamanho_bloco, tela):
        self.branco = (255,255,255)
        self.preto = (0,0,0)
        self.cinza = (128,128,128)
        self.azul = (0,0,120)
        self.tela = tela

        self.num_blocos_x = num_blocos_x
        self.num_blocos_y = num_blocos_y
        self.tamanho_bloco = tamanho_bloco

        
        #definindo mapa
        self.mapa = [
            # 'W' = paredes, 'E' = espaços vazios e 'B' = bloco indestrutível e 'D' = bloco destrutível
            "WWWWWWWWWWWWWWW",
            "WEEDDDEDDDDDEEW",
            "WEBDBEBEBEBDBEW",
            "WEDDDDDDEEEDDEW",
            "WDBEBEBEBEBDBDW",
            "WDDEDDDDDDEDDDW",
            "WDBEBEBDBEBDBDW",
            "WDDDDEEDEDDDDDW",
            "WDBEBEBDBEBDBDW",
            "WDDDDDDDDDDDDDW",
            "WDBEBEBDBEBDBDW",
            "WDDDDDDDDDDDDDW",
            "WEBEBEBEBEBEBEW",
            "WEEEDDDDDDDEEEW",
            "WWWWWWWWWWWWWWW"
            

        ]
        

        self.blocos = pygame.sprite.Group()
        self.bombas = pygame.sprite.Group()
    
    def desenhar(self, tela):
        #Limpa os blocos antes de redesenhá-los:
        self.blocos.empty() 

        #Desenha os blocos:
        for y, linha in enumerate(self.mapa):
            for x, bloco in enumerate(linha):
                x_pos = x * self.tamanho_bloco
                y_pos = y * self.tamanho_bloco
                if bloco == 'W':
                    #Adicionar Sprites que faltam 
                    pygame.draw.rect(tela, self.branco, pygame.Rect(x_pos, y_pos, self.tamanho_bloco, self.tamanho_bloco))
                    self.blocos.add(Bloco('Blocos/bloco_lateral.png', x_pos, y_pos, self.tamanho_bloco))
                elif bloco == 'B':
                    bloco_fixo = Bloco('Blocos/bloco_fixo.png', x_pos, y_pos, self.tamanho_bloco)
                    self.blocos.add(bloco_fixo)
                elif bloco == 'E':
                    bloco_sprite = Bloco('Fundo/fundo.png', x_pos, y_pos, self.tamanho_bloco)                  
                elif bloco == 'D':
                    bloco_destrutivel = Bloco('Blocos/bloco_destrutivel.png', x_pos, y_pos, self.tamanho_bloco, destrutivel= True)
                    self.blocos.add(bloco_destrutivel)
        self.blocos.draw(tela)
        self.bombas.draw(tela)

    def update(self, dt):
        self.bombas.update(dt)
        
        
    def aumentar_tamanho_bloco(self, novo_tamanho):
        for bloco in self.blocos:
            bloco.aumentar_tamanho(novo_tamanho)

    def obter_blocos_destrutiveis(self):
        for bloco in self.mapa.blocos:
            if bloco.destrutivel:
                print(f"Bloco destrutível encontrado: {bloco.rect}")
            
    