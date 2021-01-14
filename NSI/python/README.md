# Entraînement Python
<img src="https://i.imgur.com/7jFH0SD.jpg?fb">

## Hello!
Ecrire un programme qui affiche "Hello World"

_*Note :*_ Commencer par un simple Hello World quand on utilise un nouveau langage ou un nouveau PC permet de s'assurer que l'environnement est opérationnel. Ici par exemple on vérifie que Python est bien installé.

## Hello You!
Compléter le programme pour :
1. Demander le prénom en entrée
2. Demander le nom en entrée
2. Dire bonjour à la personne (ex: "Bienvenue Alan Turing")

# Un peu de trigonométrie

## Périmètre pour un triangle spécifique
Soit un triangle rectangle de côté a, b et c.

On sait que les plus petits côtés a et b sont égales à 2 et 5.

Pourrais un programme qui calcul le périmètre du triangle ?

## Air du triangle
Tant qu'à y être, calculons également son aire !

## Périmètre pour tous les triangles
Compléter le programme de périmètre pour prendre les deux valeurs des côtés en entrée.
<details>
  <summary>Aide</summary>
  La fonction `input` renvoie une chaîne de caractère, il va falloir convertir pour faire des calculs
</details>

## Compte des occurrences
### iiiiiiiiiiiiiiiiii
Karim se demande combien de lettre 'i' contient un livre.
Compléte le programme pour compter le nombre d'occurrences (apparitions) de la lettre 'i'.
```python
livre = "Le jour de ses onze ans, Harry Potter, un orphelin élevé par un oncle et une tante qui le détestent, voit son existence bouleversée. Un géant vient le chercher pour l'emmener au collège Poudlard, école de sorcellerie, où une place l'attent depuis toujours. Qui est donc Harry Potter ? Et qui est l'effroyable V..., le mage dont personne n'ose prononcer le nom ?"
occurrences_i = 0
for lettre in livre:
  if ...:
    ...
```

### aeaeaeaeaeaeaeaeaea
Il se demande maintenant si le texte contient plus de lettre 'e' ou de lettre 'a'.
Peux-tu l'aider ?


### Toutes les lettres ?
Le livre contient-il toutes les lettres de l'alphabet ?
```python
import string
livre = "Le jour de ses onze ans, Harry Potter, un orphelin élevé par un oncle et une tante qui le détestent, voit son existence bouleversée. Un géant vient le chercher pour l'emmener au collège Poudlard, école de sorcellerie, où une place l'attent depuis toujours. Qui est donc Harry Potter ? Et qui est l'effroyable V..., le mage dont personne n'ose prononcer le nom ?"
liste_alphabet = list(string.ascii_lowercase)
print(liste_alphabet)
```
<details>
  <summary>Aide</summary>
  Tu peux supprimer chaque lettre trouver de la liste, les lettres restantes à la fin sont celles absentes du texte.
</details>

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

## (Difficile) Une formule équilibrée et juste !
Tu réalises qu'une formule équilibrée n'est pas forcément juste :
```python
# Contient autant de parenthèse ouvrantes que fermantes
f4 = "(1+9)) + x ("
```
Pourrais-tu corriger la vérification ?

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
