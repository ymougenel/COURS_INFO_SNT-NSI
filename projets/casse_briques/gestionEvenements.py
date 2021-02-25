import sys
import pygame
from events import *
from constants import *


def gerer_evenements(raquette):
    # Gestion des evenements
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == Events.RETRECIR_RAQUETTE:
            raquette.surf = pygame.transform.scale(raquette.surf, (RAQUETTE_LARGEUR, RAQUETTE_HAUTEUR))
            print('gerer_enevements')
        if event.type == Events.BALLE_PERDUE:
            print("Reception evenement fin de partie")
            sys.exit()
