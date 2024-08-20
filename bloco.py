import pygame
from pygame.sprite import Sprite

class Bloco(Sprite):  # Herança da classe Sprite
    def __init__(self, imagem, x, y, tamanho_bloco, destrutivel=False):
        super().__init__()  # Inicializa a sprite
        self.image_path = imagem  # Salva o caminho da imagem
        self.image = pygame.image.load(imagem).convert_alpha()
        self.image = pygame.transform.scale(self.image, (tamanho_bloco, tamanho_bloco))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)  # Define a posição do retângulo (Bloco destrutível) na tela
        self.destrutivel = destrutivel

    def aumentar_tamanho(self, tamanho_novo):
        center = self.rect.center
        self.image = pygame.transform.scale(self.image, (tamanho_novo, tamanho_novo))
        self.rect = self.image.get_rect()
        self.rect.center = center

    def redimensionar_imagem(self, novo_tamanho):
        self.image = pygame.transform.scale(self.image, (novo_tamanho, novo_tamanho))
        self.rect = self.image.get_rect(topleft=self.rect.topleft)