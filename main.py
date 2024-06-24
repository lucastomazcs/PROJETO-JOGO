import pygame
import sys

pygame.init()

largura = 1024
altura = 800

tela = pygame.display.set_mode((largura, altura))

pygame.display.set_caption("Bomberman")

branco = (255,255,255)

def main():

    clock = pygame.time.Clock()
    rodando = True

    while rodando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               rodando = False

        tela.fill(branco)
        
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()