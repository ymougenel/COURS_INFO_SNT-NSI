import persistence
import random

choix = 0
persistence.connexion_base()

# eleve anakin avec un ID aléatoire
ANAKIN = (random.randint(100,2000),'Anakin','Skylwalker', '2004-05-03', 'M')

while 0 <= choix < 9:
    # A FAIRE (1.2): demande du choix à l'utilisateur
    choix = -1
    print("Vous avez tapez...")
    print(choix)

    # AJOUT
    if choix == 1:
        print("... bien reçu, insertion de l'élève %s %s %s %s %s", str(ANAKIN))
        persistence.inserer_eleve(ANAKIN)


    # SUPPRESSION
    # A FAIRE (2.1): Demander l’id de l’élève à supprimer
    # A FAIRE (2.2): Supprimer l'eleve


    # LECTURE
    # A FAIRE (3): Afficher

    # MODIFICATION
    # A FAIRE (4) modification_eleve


    # QUITTER
    if choix == 9:
        persistence.deconnexion_base()
        exit()
