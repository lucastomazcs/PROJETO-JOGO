import pygame
import sys
from mapa import Mapa
from player import Player

pygame.init()
num_blocos_x = 15
num_blocos_y = 15
tamanho_bloco = 64

largura = num_blocos_x * tamanho_bloco
altura =  num_blocos_y * tamanho_bloco

tela = pygame.display.set_mode((largura, altura))

pygame.display.set_caption("Bomberman")

preto = (0,0,0)

def main():

    clock = pygame.time.Clock()
    rodando = True

    mapa = Mapa(num_blocos_x, num_blocos_y, tamanho_bloco)
    tamanho_imagem = (60,60)
    jogador = Player((50, 50), 100, 10, 3, mapa, tamanho= tamanho_imagem)
 

    while rodando:
        dt = clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               rodando = False
               
        jogador.update(dt)
        tela.fill(preto)
        mapa.desenhar(tela)
        tela.blit(jogador.image, jogador.rect.topleft)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()