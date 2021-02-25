import sys, pygame

import gestionEvenements
from balle import Balle
from brique import Brique
from projets.casse_briques.item import Item
from raquette import Raquette
from constants import *
from events import Events

pygame.init()

ecran = pygame.display.set_mode((ECRAN_LARGEUR, ECRAN_HAUTEUR))

raquette = Raquette()
balle = Balle()
horloge = pygame.time.Clock()

toutes_briques = pygame.sprite.Group()
toutes_items = pygame.sprite.Group()

for i in range(8):
    brique = Brique(i * BRIQUE_LARGEUR + i * 3, 0)
    toutes_briques.add(brique)

timer = 0


while True:

    # Evenements
    gestionEvenements.gerer_evenements(raquette)

    # Déplacements
    touches_clavier = pygame.key.get_pressed()
    raquette.deplacer(touches_clavier)
    balle.deplacer()

    # Collisions
    collision_balle_raquette = pygame.sprite.spritecollideany(balle, [raquette])
    if collision_balle_raquette:
        balle.vy = balle.vy * -1
        balle.remettre_vitesse()

    # Collisions brique -ball
    collision_balle_brique = pygame.sprite.spritecollideany(balle, toutes_briques)
    if collision_balle_brique:
        balle.vy = balle.vy * -1
        if collision_balle_brique.item:
            item = Item(collision_balle_brique.rect.x, collision_balle_brique.rect.y)
            toutes_items.add(item)
        toutes_briques.remove(collision_balle_brique)
        balle.remettre_vitesse()

    ecran.fill(COULEUR_ECRAN)
    for brick in toutes_briques:
        brick.display(ecran)
    raquette.display(ecran)
    balle.display(ecran)
    for item in toutes_items:
        item.display(ecran)
        item.move()

    collision_item_raquette = pygame.sprite.spritecollideany(raquette, toutes_items)
    if collision_item_raquette:
        raquette.surf = pygame.transform.scale( raquette.surf, (RAQUETTE_LARGEUR_MAX, RAQUETTE_HAUTEUR))
        pygame.time.set_timer(Events.RETRECIR_RAQUETTE.value, TIMER_ITEM)

    pygame.display.flip()
    horloge.tick(30)
