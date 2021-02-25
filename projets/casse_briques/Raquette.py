import pygame
from constants import *


class Raquette(pygame.sprite.Sprite):
    def __init__(self):
        super(Raquette, self).__init__()
        self.surf = pygame.Surface((RAQUETTE_LARGEUR, RAQUETTE_HAUTEUR))
        self.surf.fill(COULEUR_RAQUETTE)
        self.rect = self.surf.get_rect()

        self.rect.move_ip(ECRAN_LARGEUR / 2, RAQUETTE_LIGNE)

    def display(self, screen: pygame.Surface):
        screen.blit(self.surf, self.rect)
