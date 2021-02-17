# Noms des joueurs
nom_joueur1 = ""
nom_joueur2 = ""

# Symboles des joueurs
symbole_joueur1 = "X"
symbole_joueur2 = "O"

joueur_courant = ""
symbole_courant = ""

# Les 3 lignes du plateau de morpion
# BONUS 1ere: transformer les 3 lignes en matrice (aide : https://cahier-de-prepa.fr/psi-pv/download?id=300)
ligne1 = [" ", " ", " "]
ligne2 = [" ", " ", " "]
ligne3 = [" ", " ", " "]


# Initialise la partie
# Place le premier joueur comme joueur_courant
def init_partie():
    global joueur_courant, symbole_courant
    joueur_courant = nom_joueur1
    symbole_courant = symbole_joueur1


# Lecture du plateau de jeu
# Retourne la valeur à la ligne i, colonne j
def lire_plateau(i, j):
    valeur = 42
    # TODO A faire élève : Compléter la fonction pour retourner la valeur du plateau à la ligne i, colonne j
    return valeur


# Ecriture sur plateau de jeu
# Place la valeur à la ligne i, colonne j
def ecrire_plateau(i, j, valeur):
    print("")
    # TODO A faire élève : Compléter la fonction pour écrire la valeur sur le plateau à la ligne i, colonne j


# Demande aux joueurs d'entrer leurs noms
def demander_noms_joueurs():
    global nom_joueur1, nom_joueur2
    # TODO A faire élève demander les noms des joueurs en entrée
    nom_joueur1 = "John"
    nom_joueur2 = "Marc"


# Demande une entrée clavier comprise entre val_min et val_max ( val_min <= entrée < val_max)
def demander_entier(val_min, val_max):
    # TODO A faire élève : Demander un entier supérieur ou égale à val_min ET strictement inférieur à val_max
    valeur = 42
    # Bonus terminal: tester le type avant de convertir en entier (exemple: si l'utilisateur tape "azerty")

# Affiche le plateau de jeu
def afficher_plateau():
    entre_ligne = "---------"
    print(entre_ligne)
    print(*ligne1, sep=' |')
    print(entre_ligne)
    print(*ligne2, sep=' |')
    print(entre_ligne)
    print(*ligne3, sep=' |')
    print(entre_ligne)


# ------------------------------------Début de la partie ------------------------------------

# Initialisation
init_partie()
afficher_plateau()
demander_noms_joueurs()
print("Les joueurs : " + nom_joueur1 + " et " + nom_joueur2 + "s'affrontent !")

# le joueur1 joue au centre
ecrire_plateau(1, 1, "X")
afficher_plateau()
print(lire_plateau(1, 1))

# le joueur2 joue en haut à gauche
ecrire_plateau(0, 0, "O")
afficher_plateau()
print(lire_plateau(0, 0))