# import du module mysql
import mysql.connector

# command SQL permettant d'inserer des eleves
COMMAND_INSERT_ELEVE = """INSERT INTO eleves VALUES (%s, %s, %s, %s, %s)"""

# connection avec la base de donnée
connector = mysql.connector.connect(host="ymougenel.com", user="...", password="...", database="...", port="...")
# création du cursos permettant de faire des requetes
cursor = connector.cursor()

eleve=(43, 'Anakin','Skylwalker','2004-02-24','M')

# Ajout de l'eleve Anakin, /!\ penser au commit après chaque requete
cursor.execute(COMMAND_INSERT_ELEVE,eleve)
connector.commit()

# Fermeture de la connexion avec la base à la fin du programme
connector.close()
