import pygame, sys

from events import *
from constants import *
import random


class Balle(pygame.sprite.Sprite):
    def __init__(self):
        super(Balle, self).__init__()
        self.surf = pygame.image.load("images/balle.png")
        self.surf = pygame.transform.scale(self.surf, (BALLE_TAILLE, BALLE_TAILLE))
        self.rect = self.surf.get_rect()

        position_x = random.randint(0, ECRAN_LARGEUR)
        self.rect.move_ip(position_x, ECRAN_HAUTEUR / 4)
        self.vx = 1
        self.vy = 1
        self.vitesse = VITESSE_BALLE

    def deplacer(self):
        vitesse = max(self.vitesse, VITESSE_BALLE_MINIMUM)
        self.rect.move_ip(self.vx * vitesse, self.vy * vitesse)
        self.vitesse = self.vitesse - VITESSE_BALLE_REDUCTION
        if self.rect.left < 0 or self.rect.right > ECRAN_LARGEUR:
            self.vx *= -1
            print("Balle touche gauche/droite")
            self.remettre_vitesse()
        if self.rect.top < 0:
            self.vy = self.vy * -1
            print("Balle touche haut")
            self.remettre_vitesse()
        if self.rect.bottom - self.surf.get_height() > RAQUETTE_LIGNE:
            print("Lancement evenement fin de partie")
            pygame.event.post(pygame.event.Event(Events.BALLE_PERDUE.value, {}))

            print("Partie perdue")

    def remettre_vitesse(self):
        self.vitesse = VITESSE_BALLE

    def display(self, screen: pygame.Surface):
        screen.blit(self.surf, self.rect)
