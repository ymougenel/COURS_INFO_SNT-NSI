import sys, pygame

import GestionEvenements
from Balle import Balle
from Brique import Brique
from Raquette import Raquette
from constants import *

pygame.init()

ecran = pygame.display.set_mode((ECRAN_LARGEUR, ECRAN_HAUTEUR))

raquette = Raquette()
balle = Balle()
horloge = pygame.time.Clock()

toutes_briques = pygame.sprite.Group()

for i in range(8):
    brique = Brique(i * BRIQUE_LARGEUR + i * 3, 0)
    toutes_briques.add(brique)

while True:

    # Evenements
    GestionEvenements.gerer_evenements()

    # Déplacements
    touches_clavier = pygame.key.get_pressed()
    raquette.deplacer(touches_clavier)
    balle.deplacer()

    # Collisions
    collision_balle_raquette = pygame.sprite.spritecollideany(balle, [raquette])
    if collision_balle_raquette:
        print("Collision balle raquette")
        balle.vy = balle.vy * -1
        balle.remettre_vitesse()

    # Collisions brique -ball
    collision_balle_brique = pygame.sprite.spritecollideany(balle, toutes_briques)
    if collision_balle_brique:
        print("Collision balle brique")
        balle.vy = balle.vy * -1
        toutes_briques.remove(collision_balle_brique)
        balle.remettre_vitesse()

    ecran.fill(COULEUR_ECRAN)
    for brick in toutes_briques:
        brick.display(ecran)
    raquette.display(ecran)
    balle.display(ecran)
    pygame.display.flip()
    horloge.tick(30)
