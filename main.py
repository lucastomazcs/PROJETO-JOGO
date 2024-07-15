import pygame
import sys
from mapa import Mapa
from player import Player
from inimigo import Inimigo

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
    tamanho_imagem = (55,50)
    tamanho_imagem_inimigo = (45, 45)
    jogador = Player((50, 50), 100, 12, 3, mapa, tamanho= tamanho_imagem)
    inimigo = Inimigo((850, 800), 100, 10, 'direcao', mapa, tamanho= tamanho_imagem_inimigo)

    sprites = pygame.sprite.Group()
    sprites.add(jogador)
    sprites.add(inimigo)

    while rodando:
        dt = clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               rodando = False
               
        jogador.update(dt)
        inimigo.update(jogador.posicao, dt)
        tela.fill(preto)
        mapa.desenhar(tela)
        
        sprites.draw(tela)

        mapa.update(dt)
        
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()