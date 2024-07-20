import pygame
import sys
from mapa import Mapa
from player import Player
from inimigo import Inimigo
from tkinter import *


pygame.init()
#ajusta o tamanho da tela de acordo com o monitor do usuário
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

def game_over_d(tela):
    game_over_imagem = pygame.image.load("telas/tela_game_over.png")
    game_over_imagem = pygame.transform.scale(game_over_imagem,(largura, altura))
    tela.blit(game_over_imagem, (0,0))
    pygame.display.flip()

def main():

    clock = pygame.time.Clock()
    rodando = True
    game_over = False

    mapa = Mapa(num_blocos_x, num_blocos_y, tamanho_bloco, tela)
    tamanho_imagem = (tamanho_bloco - 9, tamanho_bloco - 9)
    tamanho_imagem_inimigo = (tamanho_bloco - 9, tamanho_bloco - 9)
    jogador = Player((60, 60), 100, 2, 3, mapa, tamanho= tamanho_imagem)
    inimigo = Inimigo((tamanho_bloco * 14, tamanho_bloco * 14), 100, 10, 'direcao', mapa, tamanho= tamanho_imagem_inimigo)
    

    mapa.jogadores = [jogador]

    sprites = pygame.sprite.Group()
    sprites.add(jogador)
    sprites.add(inimigo)

    while rodando:
        dt = clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               rodando = False
            elif event.type == pygame.KEYDOWN:
                if game_over and event.key == pygame.K_r:
                    main() #Reinicia o jogo
                elif game_over and event.key == pygame.K_q:
                    rodando = False
        if not game_over:           
            jogador.update(dt)
            inimigo.update(jogador.posicao, dt)

            tela.fill(preto)
            mapa.desenhar(tela)
            mapa.bombas.update(dt)
            mapa.bombas.draw(tela)
            sprites.draw(tela)
    
            mapa.update(dt)
        
            pygame.display.flip()
            if not jogador.alive():
                game_over = True
        else:
            game_over_d(tela)
            clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()