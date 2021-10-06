# import du module mysql
import mysql.connector

connector = None
cursor = None

def connexion_base():
    """Connexion à la base de donnée

    Arguments: Aucun
    """
    global connector
    global cursor
    print()
    print("*** Connexion avec la base de donnée ***")
    print("Prise de la pilule rouge, synchronization avec la Matrix")
    # A FAIRE (0.1) connection avec la base de donnée
    # A FAIRE (0.3): message disant que la connexion est établie


    # A FAIRE (0.2) : création du cursor permettant de faire des requetes

def inserer_eleve(eleve):
    # A FAIRE (1.3): COMMENTER FONCTION
    global connector
    global cursor

    # A FAIRE (1.1): executer la commande d'ajout (comme pour exemple.py)

def selectionner_eleves():
    # A FAIRE 3.2 : COMMENTER FONCTION
    global cursor
    # A FAIRE 3.1 afficher les eleves de la base

def modification_eleve(eleve):
    global connector
    global cursor
    # A FAIRE 4

def suppression_eleve(id):
    global cursor
    global connector
    #  A FAIRE 2.2


def deconnexion_base():
    """Fermeture de la connexion avec la base à la fin du programme

    Arguments: Aucun
    """
    global connector
    connector.close()
