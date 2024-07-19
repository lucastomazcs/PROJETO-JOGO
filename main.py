import pygame
import sys
from mapa import Mapa
from player import Player
from inimigo import Inimigo
from tkinter import *


pygame.init()
#Temos que ajustar a tela:
root = Tk()
monitor_height = root.winfo_screenheight()
monitor_width = root.winfo_screenwidth()

num_blocos_x = 15
num_blocos_y = 15
tamanho_bloco = (monitor_height // num_blocos_y) - 5

largura = num_blocos_x * tamanho_bloco
altura =  num_blocos_y * tamanho_bloco

tela = pygame.display.set_mode((largura, altura), pygame.RESIZABLE)

pygame.display.set_caption("Bomberman")

preto = (0,0,0)

def main():

    clock = pygame.time.Clock()
    rodando = True

    mapa = Mapa(num_blocos_x, num_blocos_y, tamanho_bloco, tela)
    tamanho_imagem = (tamanho_bloco - 9, tamanho_bloco - 9)
    tamanho_imagem_inimigo = (tamanho_bloco - 9, tamanho_bloco - 9)
    jogador = Player((60, 60), 100, 12, 3, mapa, tamanho= tamanho_imagem)
    inimigo = Inimigo((tamanho_bloco * 13, tamanho_bloco * 13), 100, 10, 'direcao', mapa, tamanho= tamanho_imagem_inimigo)
    

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
        mapa.bombas.update(dt)
        mapa.bombas.draw(tela)
        sprites.draw(tela)
    
        mapa.update(dt)
        
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()