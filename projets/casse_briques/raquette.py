import pygame
from constants import *


class Raquette(pygame.sprite.Sprite):
    def __init__(self):
        super(Raquette, self).__init__()
        self.surf = pygame.Surface((RAQUETTE_LARGEUR, RAQUETTE_HAUTEUR))
        self.surf.fill(COULEUR_RAQUETTE)
        self.rect = self.surf.get_rect()

        self.rect.move_ip(ECRAN_LARGEUR / 2, RAQUETTE_LIGNE)

    def deplacer(self, touches_clavier):
        if touches_clavier[pygame.K_LEFT]:
            self.rect.move_ip(-VITESSE_RAQUETTE, 0)
        if touches_clavier[pygame.K_RIGHT]:
            self.rect.move_ip(+VITESSE_RAQUETTE, 0)
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > ECRAN_LARGEUR:
            self.rect.right = ECRAN_LARGEUR

    def display(self, screen: pygame.Surface):
        screen.blit(self.surf, self.rect)
