import pygame
import sys
from player import Player


pygame.init()

largura = 1024
altura = 800

tela = pygame.display.set_mode((largura, altura))

pygame.display.set_caption("Bomberman")

branco = (255,255,255)

def main():

    clock = pygame.time.Clock()
    rodando = True

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
        todos_os_sprites.draw(tela)
        

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()