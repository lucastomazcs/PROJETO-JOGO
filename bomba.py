import pygame
from pygame.sprite import Sprite, Group

class Explosão(Sprite):
    def __init__(self, posicao, tamanho, tempo_animacao, mapa) -> None:
        super().__init__()

        self.images = [
            pygame.transform.scale(pygame.image.load('Explosão/explosao.png').convert_alpha(), tamanho),
            pygame.transform.scale(pygame.image.load('Explosão/explosao2.png').convert_alpha(), tamanho),
            pygame.transform.scale(pygame.image.load('Explosão/explosao3.png').convert_alpha(), tamanho)
        ]

        self.image_index = 0
        self.image = self.images[self.image_index]
        self.rect = self.image.get_rect(center=posicao)
        self.tempo_animacao = tempo_animacao
        self.contador_tempo = 0
        self.mapa = mapa

    def update(self, dt):
        self.contador_tempo += dt
        if self.contador_tempo >= self.tempo_animacao:
            self.contador_tempo = 0
            self.image_index += 1
            if self.image_index < len(self.images):
                self.image = self.images[self.image_index]
            else:
                self.kill()

class Bomba(Sprite):
    def __init__(self, posicaobomba, tempo, raiodeexplosao, tamanho, direcao, mapa):
        pygame.sprite.Sprite.__init__(self)

        self.__posicaobomba = posicaobomba
        self.__tempo = tempo
        self.__raiodeexplosao = raiodeexplosao
        self.direcao = direcao  # Adiciona a direção como atributo
        self.tempo_decorrido = 0
        self.mapa = mapa

        self.image_index = 0
        self.images = [
            pygame.transform.scale(pygame.image.load('Bombas/bombinha1.png').convert_alpha(), tamanho),
            pygame.transform.scale(pygame.image.load('Bombas/bombinha02.png').convert_alpha(), tamanho),
            pygame.transform.scale(pygame.image.load('Bombas/bombinha03.png').convert_alpha(), tamanho),
            pygame.transform.scale(pygame.image.load('Bombas/bombinha04.png').convert_alpha(), tamanho)
        ]

        self.image = self.images[self.image_index]
        self.rect = self.image.get_rect(topleft=posicaobomba)
        self.tempo_animacao = 0.3
        self.contador_tempo = 0

    def criar_explosao(self): 
        explosao = Explosão(self.posicaoBomba, (self.__raiodeexplosao * 5, self.__raiodeexplosao * 5), 0.3, self.mapa)
        self.mapa.explosoes.add(explosao)
        return explosao

    def calcular_bloco_mirado(self):
        # Calcule a posição do bloco com base na direção
        x, y = self.posicaoBomba
        if self.direcao == 'up':
            y -= self.__raiodeexplosao
        elif self.direcao == 'down':
            y += self.__raiodeexplosao
        elif self.direcao == 'left':
            x -= self.__raiodeexplosao
        elif self.direcao == 'right':
            x += self.__raiodeexplosao
        return x, y

    def causar_dano(self, explosao):
        bloco_mirado_pos = self.calcular_bloco_mirado()
        bloco_destruido = False

        for bloco in self.mapa.blocos:
            if bloco.rect.collidepoint(bloco_mirado_pos) and bloco.destrutivel:
                print(f"Colisão detectada com bloco destrutível: {bloco.rect}")
                bloco.kill()
                self.mapa.blocos.remove(bloco)
                bloco_destruido = True
                break

        # Checa se jogadores estão dentro do raio de explosão
        raio_explosao = explosao.rect
        for jogador in self.mapa.jogadores:
            if raio_explosao.colliderect(jogador.rect):
                print("Colisão com jogador detectada")
                jogador.morrer()

        # Checa se inimigos estão dentro do raio de explosão
        for inimigo in self.mapa.inimigos:
            if raio_explosao.colliderect(inimigo.rect):
                print("Colisão com inimigo detectada")
                inimigo.sofrer_dano()

    def explodir(self):
        explosao = self.criar_explosao()
        self.causar_dano(explosao)
        self.kill()

    def update(self, dt):
        dt = dt / 10
        self.tempo_decorrido += dt
        self.contador_tempo += dt
        if self.contador_tempo >= self.tempo_animacao:
            self.contador_tempo = 0
            self.image_index = (self.image_index + 1) % len(self.images)
            self.image = self.images[self.image_index]
        if self.tempo_decorrido >= self.__tempo:
            self.explodir()

    @property
    def posicaoBomba(self):
        return self.__posicaobomba
    @property
    def tempo(self):
        return self.__tempo
    @property
    def raio(self):
        return self.__raiodeexplosao
