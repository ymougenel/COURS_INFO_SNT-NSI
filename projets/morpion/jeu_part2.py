# Noms des joueurs
nom_joueur1 = ""
nom_joueur2 = ""
joueur_courant = ""

# Symboles des joueurs
symbole_joueur1 = "X"
symbole_joueur2 = "O"
symbole_courant = ""

# Les 3 lignes du plateau de morpion
# BONUS 1ere: transformer les 3 lignes en matrice (aide : https://cahier-de-prepa.fr/psi-pv/download?id=300)
ligne1 = ["", "", ""]
ligne2 = ["", "", ""]
ligne3 = ["", "", ""]

# Initialise la partie
# Place le premier joueur comme joueur_courant
def init_partie():
    global joueur_courant, symbole_courant
    joueur_courant = nom_joueur1
    symbole_courant = symbole_joueur1


# Lecture du plateau de jeu
# Retourne la valeur à la ligne i, colonne j
def lire_plateau(i, j):
    # TODO: eleve excercice


# Ecriture sur plateau de jeu
# Place la valeur à la ligne i, colonne j
def ecrire_plateau(i, j, valeur):
    # TODO: eleve excercice

# Demande aux joueurs d'entrer leurs noms
def demander_noms_joueurs():
    global nom_joueur1, nom_joueur2
    # TODO eleve: demander les noms des joueurs en entrée
    nom_joueur1 = "John"
    nom_joueur2 = "Marc"

# Demande une entrée clavier comprise entre val_min et val_max
def demander_entier(val_min, val_max):
    # TODO eleve: exercice demander le coup à l'utilisateur
    valeur =
    return valeur


def demander_ligne():
    print("Choix de la ligne...")
    return demander_entier(0, 3)


def demander_colonne():
    print("Choix de la colonne...")
    return demander_entier(0, 3)




def changer_joueur():
    global joueur_courant, symbole_courant
    # TODO eleve: changer le joueur courant ainsi que le symbole courant


# TODO teacher: pretty display
def afficher_plateau():
    print(ligne1)
    print(ligne2)
    print(ligne3)



def plateau_remplie():
    # NE pas toucher (partie3)
    return False


def coup_gagnant(symbole_courant):
    # NE pas toucher (partie3)
    return False


if __name__ == '__main__':
    print("Début de partie")
    demander_noms_joueurs()
    init_partie()

    partie_terminee = False
    gagnant = ""
    while partie_terminee == False:
        print("C'est à " + joueur_courant + " de jouer")
        afficher_plateau()
        ligne_jouee = demander_ligne()
        colonne_jouee = demander_colonne()

        ecrire_plateau(ligne_jouee, colonne_jouee, symbole_courant)
        changer_joueur()
