import sys, pygame

from Balle import Balle
from Brique import Brique
from Raquette import Raquette
from constants import *

pygame.init()

ecran = pygame.display.set_mode((ECRAN_LARGEUR, ECRAN_HAUTEUR))
brique = Brique()
raquette = Raquette()
balle = Balle()
horloge = pygame.time.Clock()
while True:

    # Gestion des evenements
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    # Déplacements
    touches_clavier = pygame.key.get_pressed()
    raquette.deplacer(touches_clavier)
    balle.deplacer()

    ecran.fill(COULEUR_ECRAN)
    brique.display(ecran)
    raquette.display(ecran)
    balle.display(ecran)
    pygame.display.flip()
    horloge.tick(30)
