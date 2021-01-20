# 4. Itérations

## 4.0  Bonjour la classe
Peux-tu dire bonjour à la classe ?
```python
classe = ["Alain", "François", "Karima", "Enzo"]
for TODO in TODO:
  TODO
```

## 4.1 C'est carré
Affiche le carré de tout les nombres entre 1 et 20

## 4.2 La punition de Bart
<img href="https://psicoedublog.files.wordpress.com/2013/05/board.jpg">
Bart a de nouveau été punie : il doit recopier 2000 fois "I WILL NOT DO ANYTHING BAD EVER AGAIN".
Cela l’empêche de participer au tournoi de foot ce week-end, et sans lui vous risquez de perdre :/

Peut-être que tu pourrais l'aider avec tes connaissances d'informatique...

## 4.3 Compte des occurrences
Karim se demande combien de lettre 'i' contient son livre.
Complète le programme pour compter le nombre d'occurrences (apparitions) de la lettre 'i'.
```python
livre = "Le jour de ses onze ans, Harry Potter, un orphelin élevé par un oncle et une tante qui le détestent, voit son existence bouleversée. Un géant vient le chercher pour l'emmener au collège Poudlard, école de sorcellerie, où une place l'attend depuis toujours. Qui est donc Harry Potter ? Et qui est l'effroyable V..., le mage dont personne n'ose prononcer le nom ?"
occurrences_i = 0
for lettre in livre:
  if TODO:
    TODO
```

### 4.4 Comparaison des occurrences
Il se demande maintenant si le texte contient plus de lettre 'e' ou de lettre 'a'.
Serais-tu lui dire ?

## 4.5 (optionnel) Une formule équilibrée
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
