import pygame
from constants import *


class Balle(pygame.sprite.Sprite):
    def __init__(self):
        super(Balle, self).__init__()
        self.surf = pygame.image.load("images/balle.png")
        self.surf = pygame.transform.scale(self.surf, (BALLE_TAILLE, BALLE_TAILLE))
        self.rect = self.surf.get_rect()

        self.rect.move_ip(ECRAN_LARGEUR / 2, ECRAN_HAUTEUR / 2)

    def display(self, screen: pygame.Surface):
        screen.blit(self.surf, self.rect)
