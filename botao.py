import pygame

class Botao:
    
    def __init__(self, x, y, largura, altura, texto, cor_fundo, cor_texto, acao = None) -> None:
        self.rect = pygame.Rect(x, y, largura, altura)
        self.texto = texto
        self.cor_fundo = cor_fundo
        self.cor_texto = cor_texto
        self.acao = acao
    
    def desenhar(self, tela):
        pygame.draw.rect(tela, self.cor_fundo, self.rect)
        font = pygame.font.Font(None, 36)
        texto_surface = font.render(self.texto, True, self.cor_texto)
        texto_rect = texto_surface.get_rect(center = self.rect.center)
        tela.blit(texto_surface, texto_rect)

    def checar_clique(self, posicao_mouse):
        if self.rect.collidepoint(posicao_mouse):
            if self.acao:
                self.acao()