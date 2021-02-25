import sys
import pygame
from events import *
def gerer_evenements():
    # Gestion des evenements
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == Events.BALLE_PERDUE:
            print("Reception evenement fin de partie")
            sys.exit()
