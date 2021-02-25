from enum import Enum
import pygame


class Events(Enum):
    BALLE_PERDUE = pygame.USEREVENT + 1
    RETRECIR_RAQUETTE = pygame.USEREVENT + 2