nom_joueur1 = ""
nom_joueur2 = ""
symbole_joueur1 = "X"
symbole_joueur2 = "O"

joueur_courant = ""
symbole_courant = ""

# Les 3 lignes du plateau de morpion
# BONUS 1ere: transformer les 3 lignes en matrice
# TODO: me lien matrice
ligne1 = ["", "", ""]
ligne2 = ["", "", ""]
ligne3 = ["", "", ""]


def init_partie():
    global joueur_courant
    joueur_courant = nom_joueur1
    global symbole_courant
    symbole_courant = symbole_joueur1


# TODO: eleve excercice
def lire_plateau(i, j):
    if i == 0:
        return ligne1[j]
    if i == 1:
        return ligne2[j]
    if i == 2:
        return ligne3[j]


# TODO: eleve excercice
def ecrire_plateau(i, j, valeur):
    if i == 0:
        ligne1[j] = valeur
    if i == 1:
        ligne2[j] = valeur
    if i == 2:
        ligne3[j] = valeur


def demander_noms_joueurs():
    global nom_joueur1
    global nom_joueur2
    # TODO: demander les noms des joueurs en entrée
    nom_joueur1 = "John"
    nom_joueur2 = "Marc"


def demander_ligne():
    print("Choix de la ligne...")
    return demander_entier(0, 3)


def demander_colonne():
    print("Choix de la colonne...")
    return demander_entier(0, 3)


# TODO: exercice eleve
def demander_entier(val_min, val_max):
    # Bonus terminal: tester le type avant de convertir en entier (exemple: si l'utilisateur tape "azerty")
    valeur = int(input("Ou voulez vous jouer ?"))
    while val_min > valeur >= val_max:
        valeur = int(input("Ou voulez vous jouer ?"))
    return valeur


def changer_joueur():
    global joueur_courant
    global symbole_courant
    if joueur_courant == nom_joueur1:
        joueur_courant = nom_joueur2
        symbole_courant = symbole_joueur2
    else:
        joueur_courant = nom_joueur1
        symbole_courant = symbole_joueur1


# TODO: me pretty display
def afficher_plateau():
    print(ligne1)
    print(ligne2)
    print(ligne3)


# TODO: exercice eleve
def plateau_remplie():
    return not "" in ligne1 + ligne2 + ligne3


def coup_gagnant(symbole_courant):
    return \
        ligne_complete(ligne1, symbole_courant) \
        or ligne_complete(ligne2, symbole_courant) \
        or ligne_complete(ligne3, symbole_courant) \
        or ligne_complete(ligne1[0] + ligne2[0] + ligne3[0], symbole_courant) \
        or ligne_complete(ligne1[1] + ligne2[1] + ligne3[1], symbole_courant) \
        or ligne_complete(ligne1[2] + ligne2[2] + ligne3[2], symbole_courant) \
        or ligne_complete(ligne1[0] + ligne2[1] + ligne3[2], symbole_courant) \
        or ligne_complete(ligne1[2] + ligne2[1] + ligne3[0], symbole_courant)


def ligne_complete(ligne, symbole):
    return ligne.count(symbole) == 3


if __name__ == '__main__':
    print("Début de partie")
    demander_noms_joueurs()
    init_partie()

    partie_terminee = False
    gagnant = ""
    # TODO: changer avec une porte logique
    while partie_terminee == False:
        print("C'est à " + joueur_courant + " de jouer")
        afficher_plateau()
        ligne_jouee = demander_ligne()
        colonne_jouee = demander_colonne()

        ecrire_plateau(ligne_jouee, colonne_jouee, symbole_courant)

        if coup_gagnant(symbole_courant):
            print("Vistoire de " + joueur_courant)
            partie_terminee = True
        else:
            partie_terminee = plateau_remplie()
        changer_joueur()
