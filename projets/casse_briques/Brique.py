import pygame
from constants import *
import random


class Brique(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Brique, self).__init__()
        self.surf = pygame.Surface((BRIQUE_LARGEUR, BRIQUE_HAUTEUR))

        nombre_aleatoire = random.randint(0, len(COULEURS_BRIQUE) - 1)
        couleur = COULEURS_BRIQUE[nombre_aleatoire]
        self.surf.fill(couleur)
        self.rect = self.surf.get_rect()

        self.rect.move_ip(x, y)

    def display(self, screen: pygame.Surface):
        screen.blit(self.surf, self.rect)
