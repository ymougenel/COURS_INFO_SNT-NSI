import pygame
from constants import *
import random


class Item(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Item, self).__init__()
        self.surf = pygame.Surface((TAILLE_ITEM, TAILLE_ITEM))
        self.surf.fill(COULEUR_ITEM)
        self.rect = self.surf.get_rect()
        self.rect.move_ip(x, y)

    def display(self, screen: pygame.Surface):
        screen.blit(self.surf, self.rect)

    def move(self):
        self.rect.move_ip(0, 7)

