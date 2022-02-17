# 4. Itérations

## 4.1 La punition de Bart
<img href="https://psicoedublog.files.wordpress.com/2013/05/board.jpg">
Bart a de nouveau été punie : il doit recopier 2000 fois "I WILL NOT DO ANYTHING BAD EVER AGAIN".
Cela l’empêche de participer au tournoi de foot ce week-end, et sans lui vous risquez de perdre :/

Peut-être que tu pourrais l'aider avec tes connaissances d'informatique...

## 4.2 C'est carré
Afficher le carré de tout les nombres entre 0 et 20 : 0 1 4 9 16 25 .... 400


## 4.3 Valeur entre 50 et 100
Afficher toutes les valeurs entre 50 et 100 : 50 51 52 53 54 55 ... 98 99 100

## 4.4 Tester le code suivant
```python
for i in range(10,15):
  print(i)
```
Que-ce-qui s'affiche ?
Afficher toutes les valeurs entre 50 et 100 : 50 51 52 53 54 55 ... 98 99 100

## 4.3  Bonjour la classe
Peux-tu compléter le code suivant pour dire bonjour à la classe ?
```python
classe = ["Alain", "François", "Karima", "Enzo"]
for i in range(?):
  print("Bonjour" + ?)
```



## 4.3 Moyenne de classe
Dumbledore sohaite calculer la moyenne de sa classe : il se souvient que la moyenne est le total des notes diviser par le nombre d'éléments de la liste (en python `len(liste_notes)`) mais ne parvient pas à calculer le total:
```python
liste_notes = [12, 15, 11, 16]
total = 0
TODO
```
## 4.4 Présentiel
Écris un programme qui :
1. Demande le nom de l'élève en entrée
2. Vérifie si l'élève appartient à la classe
```Python
classe = ["Karim", "George", "Sandy", "Nicolas", "Elise"]
```

## 4.5 Compte des occurrences
Karim se demande combien de lettre 'i' contient son livre.
Complète le programme pour compter le nombre d'occurrences (apparitions) de la lettre 'i'.
```python
livre = "Le jour de ses onze ans, Harry Potter, un orphelin élevé par un oncle et une tante qui le détestent, voit son existence bouleversée. Un géant vient le chercher pour l'emmener au collège Poudlard, école de sorcellerie, où une place l'attend depuis toujours. Qui est donc Harry Potter ? Et qui est l'effroyable V..., le mage dont personne n'ose prononcer le nom ?"
occurrences_i = 0
for lettre in livre:
  if TODO:
    TODO
```

### 4.6 Comparaison des occurrences
Il se demande maintenant si le texte contient plus de lettre 'e' ou de lettre 'a'.
Serais-tu lui dire ?

## 4.7 (optionnel) Une formule équilibrée
Une formule mathématique peut contenir des parenthèses :
```python
(3+5) - x = (y + 1) / 2
```

Pour être équilibrée une formule doit contenir autant de parenthèses ouvrantes que de parenthèses fermantes.

Serais-tu écrire un programme qui affiche "correcte" si la formule est équilibrée, et "incorrecte" sinon.

Exemple :
```python
f0 = "89 * 7" # f0 est correcte car aucune parenthèse
f1 = "(3+5) - x = (y + 1) / 2" # f1 est correcte : deux ouvrantes et deux fermantes
f2 = "((3+5) - x = (y + 1) / 2" # f2 est incorrecte
f3 = "(3+5) - x = (y + 1)) / 2" # f3 est incorrecte
```
