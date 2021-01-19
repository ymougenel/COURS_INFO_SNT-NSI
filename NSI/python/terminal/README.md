# Entraînement Python
<img src="https://i.imgur.com/7jFH0SD.jpg?fb">

## Une formule équilibrée
Une formule mathématique peut contenir des parenthèses :
```python
(3+5) - x = (y + 1) / 2
```

Pour être correcte une formule doit contenir autant de parenthèses ouvrantes que de parenthèses fermantes.

Serais-tu écrire un programme qui affiche "correcte" si la formule est bonne, et "incorrecte" sinon.

Exemple:
```python
f0 = "89 * 7" # f0 est correcte aucune parenthèse
f1 = "(3+5) - x = (y + 1) / 2" # f1 est correcte : deux ouvrantes et deux fermantes
f2 = "((3+5) - x = (y + 1) / 2" # f2 est incorrecte
f3 = "(3+5) - x = (y + 1)) / 2" # f3 est incorrecte
```
<details>
  <summary>Aide</summary>
  Nous avions vu dans les exercices de premières comment compter les occurences.
</details>

## Une formule équilibrée et juste !
Tu réalises qu'une formule équilibrée n'est pas forcément juste :
```python
# Contient autant de parenthèse ouvrantes que fermantes
f4 = "(1+9)) + x ("
```
Pourrais-tu corriger la vérification ?

## Jeu "Plus ou moins"
Le jeu est tiré du très bon site d'apprentissage : [openclassroom](https://openclassrooms.com/fr/courses/19980-apprenez-a-programmer-en-c/14828-tp-plus-ou-moins-votre-premier-jeu#/id/r-14773)

Voici la consigne :

<im src="https://github.com/ymougenel/COURS_INFO_SNT-NSI/blob/main/.README/jeu_plus_moins.png">
<details>
  <summary>Aide nombre aléatoire</summary>
  ```python
from random import randrange
print(randrange(100))
  ```
</details>
## (Difficile) occurrences le retour
Calculer toutes les occurrences du précédents livre.
<details>
  <summary>Aide</summary>
  Une liste de tuple peut contenir les occurrences :
  ```python
  # Par exemple pour le mot elephant
  [ ("a", 1), ("b", 0), ...., (e, 2),...,(z,0)]
  ```
  [Quesqu'un tuple ?](https://courspython.com/tuple.html)
</details>

## (Difficile) Avec un dictionnaire
Génère un dictionnaire contenant les occurrences.
