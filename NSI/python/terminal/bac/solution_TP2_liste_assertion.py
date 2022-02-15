def total_hors_reduction(tableau):
    total = 0
    for element in tableau:
        total = total + element
    return total


def total_hors_reduction(tableau):
    total = 0
    assert tableau != [], "Le tableau est vide"
    taille = len(tab)
    for i in range(taille):
        assert tableau[i] >=0, "Prix négatif"
        total = total + tableau[i]
    return total

tab=[30.5,15.0,6.0,20.0,5.0,35.0,10.5]
total_hors_reduction([])

def offre_bienvenue(tab):
    """tableau->float"""
    somme=0
    longueur=len(tab)
    if longueur>0:
        somme=tab[0]*0.8
    if longueur>1:
        somme=somme+tab[1]*0.7
    if longueur>2:
        for i in range (2,longueur):
            somme=somme+tab[i]
    return somme

def prix_solde(tab):
    total = total_hors_reduction(tab)
    if len(tab) == 1:
        total_solde=0.9*solde
    if len(tab) == 2:
        total_solde=0.8*solde
    if len(tab) == 3:
        total_solde=0.7*solde
    if len(tab) == 4:
        total_solde=0.6*solde
    if len(tab) >= 5:
        total_solde=0.5*solde
    return total_solde

def minimum(tab):
    mini = tab[0]
    taille = len(tab)
    for i in range(taille):
        if tab[i] < mini:
            mini = tab[i]
    return mini

def offre_bon_client(tab):
    if len(tab) == 0:
        total = 0
    elif len(tab) == 1:
        total = tab[0]
    else:
        moins_cher = minimum(tab)
        tab.remove(moins_cher)
        total = total_hors_reduction(tab)
    return total
