import pygame, sys
from pygame.locals import *

largura = 900
altura = 400


class Tiro(pygame.sprite.Sprite):
    def __init__(self, posx, posy):
        pygame.sprite.Sprite.__init__(self)
        self.imagemTiro = pygame.image.load('imagens/tiro.png')


        self.rect = self.imagemTiro.get_rect()
        self.velocidadeTiro = 5
        self.rect.top = posy
        self.rect.left = posx

    def trajetoria(self):
        self.rect.top = self.rect.top - self.velocidadeTiro

    def colocar(self, superfice):
        superfice.blit(self.imagemTiro, self.rect)


class NaveEspacial(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.ImagemNave = pygame.image.load('imagens/nave.png')

        self.rect = self.ImagemNave.get_rect()
        self.rect.centerx = largura / 2
        self.rect.centery = altura - 30

        self.listaDisparo = []
        self.vida = True
        self.velocidade = 20

    def movimento(self):
        if self.vida == True:
            if self.rect.left <= 0:
                self.rect.left = 0

            elif self.rect.right > 900:
                self.rect.right = 900

    def disparar(self):
        print('Disparou')

    def colocar(self, superfice):
        superfice.blit(self.ImagemNave, self.rect)
        pass


def invasaoEspacao():
    pygame.init()
    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption('Invasão do Espaço')

    jogador = NaveEspacial()
    imagemFundo = pygame.image.load('imagens/background.jpg')

    jogando = True

    tiro = Tiro(largura / 2, altura - 30)

    while True:
        jogador.movimento()
        tiro.trajetoria()
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    jogador.rect.left -= jogador.velocidade
                elif evento.key == pygame.K_RIGHT:
                    jogador.rect.right += jogador.velocidade
                elif evento.key == pygame.K_SPACE:
                    jogador.disparar()

        tela.blit(imagemFundo, (0, 0))
        jogador.colocar(tela)
        tiro.colocar(tela)
        pygame.display.update()


invasaoEspacao()
