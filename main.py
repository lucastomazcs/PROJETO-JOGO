import pygame
import sys
from player import Player
from mapa import Mapa

pygame.init()

num_blocos_x = 12
num_blocos_y = 11
tamanho_bloco = 64

largura = num_blocos_x * tamanho_bloco
altura =  num_blocos_y * tamanho_bloco

tela = pygame.display.set_mode((largura, altura))

pygame.display.set_caption("Bomberman")

branco = (255,255,255)

def main():

    clock = pygame.time.Clock()
    rodando = True

    mapa = Mapa(num_blocos_x, num_blocos_y, tamanho_bloco)

    #Criando o objeto jogador:
    jogador = Player(posicaobomba=(0,0), tempo=(0), raiodeexplosao=(2), posicao=(90,100), vida= (100), velocidade=(5), range_bomba=(10))
    todos_os_sprites = pygame.sprite.Group()
    todos_os_sprites.add(jogador)


    while rodando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               rodando = False

        todos_os_sprites.update()

        tela.fill(branco)
        mapa.desenhar(tela)
        todos_os_sprites.draw(tela)
        

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()