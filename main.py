import pygame
import sys
from mapa import Mapa


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
 

    while rodando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               rodando = False
               
          
        tela.fill(preto)
        mapa.desenhar(tela)
        

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()