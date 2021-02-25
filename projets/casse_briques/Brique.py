import pygame
from constants import *


class Brique(pygame.sprite.Sprite):
    def __init__(self):
        super(Brique, self).__init__()
        self.surf = pygame.Surface((BRIQUE_LARGEUR, BRIQUE_HAUTEUR))
        self.surf.fill(COULEUR_BRIQUE)
        self.rect = self.surf.get_rect()

        self.rect.move_ip(ECRAN_LARGEUR / 2, 0)

    def display(self, screen: pygame.Surface):
        screen.blit(self.surf, self.rect)
