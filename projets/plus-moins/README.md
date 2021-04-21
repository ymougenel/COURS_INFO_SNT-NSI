# Le Jeu du plus ou moins

## Regles
Le jeu se joue a 1 joueur : Un nombre caché est générer aléatoirement entre 1 et 100. Le joueur va tenter à chaque tour de deviner sa valeur.
Il gagne s'il devine juste, sinon le programme lui indique si c'est plus ou moins.

Exemple :
1. Le nombre caché est 87.
2. Le joueur devine 55 -> Le programme lui dit "C'est plus !"
3. Le joueur devine 75 -> Le programme lui dit "C'est plus !"
4. Le joueur devine 90 -> Le programme lui dit "C'est moins !"
5. Le joueur devine 87 -> Le programme lui dit "Gagné !"


## Exercice
### Conception
Préparer un diagramme d'action

### Code
Ecrire le programme permettant de joueur

```python
# Le module random permet de générer un nombre aléatoire :
import random
nombre = random.randint(1,101)
```

### Bonus
Afficher en combien de coups l'utilisateur a déviné
