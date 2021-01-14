# Entraînement Python
<img src="https://i.imgur.com/7jFH0SD.jpg?fb">

# 1. Input/Output et conversions
## Ex 1.1: Hello World!
Tout les informaticiens ont écris une fois dans leur vie l'incontournable "Hello World", c'est maintenant ton tour :
Ecrire un programme qui affiche "Hello World"

_*Note :*_ Commencer par un simple Hello World quand on utilise un nouveau langage ou un nouveau PC permet de s'assurer que l'environnement est opérationnel. Ici par exemple on vérifie que Python est bien installé.

## Ex 1.2: Hello You!
Compléter le programme pour :
1. Demander le prénom en entrée (input)
2. Demander le nom en entrée (input)
2. Dire bonjour à la personne (ex: "Bienvenue Alan Turing")

## Ex 1.3: Date de naissance de Lucie
### Partie 1:
Lucie a 24 ans, complète le code pour trouver son année de naissance :
```python
age = 24
date_naissance = TODO
print(date_naissance)
```
### Partie 2:
Je ne suis plus certain de l'age de Lucie, peux-tu lui demander (en entrée) avant de calculer sa date de naissance ?
<details>
  <summary>TypeError</summary>
  Quelle est le type renvoyé par la fonction input ? Probablement pas un entier... il va falloir convertir...
</details>


# 2. Un peu de calcul

## 2.1 Air du triangle aux dimensions données
Soit un triangle rectangle de côté a, b et c.

On sait que les plus petits côtés a et b sont égales à 2 et 5.

Pourrais un programme qui calcul l'aire du triangle ?

<details>
  <summary>Aide trigonométrie</summary>
  L'aire d'un triangle rectangle est égale à: **a * b / 2**
</details>

## 2.2 Aire pour tous les triangles
Compléter le programme de périmètre pour prendre les deux valeurs des côtés en entrée.

## 2.3 (optionnel) Périmètre pour tous les triangles
Tant qu'à y être, calculons également son périmètre !
<details>
  <summary>Aide Pythagore</summary>
  c<sub>2 = a<sub>2 + b<sub>2
</details>
<details>
  <summary>Aide racine carré</summary>
  Un module (on verra la puissance des modules dans un prochain chapitre ;) ) de math permet de calculer la racine carré d'un nombre :
  ```
  import Math
  x = 3
  x = x * x # x est maintenant égale à 9
  racine_carre = math.sqrt(x)
  ```
</details>

# 3. Conditionnel et boucles

## 3.1 Pegi 18
Samy veut acheter le dernier jeu GTA, mais ce dernier est interdit aux moins de 18 ans (Pegi18).
Peux-tu nous aider à vérifier l'age de Samy ?
```python
age = int(input("Quel age as-tu ?"))
if TODO:
  print("Ok...Achat en cours")
else:
  print("Accès interdit, va jouer à Candy Crush !")
```

## 3.2 La punition de Bart
<img href="https://psicoedublog.files.wordpress.com/2013/05/board.jpg">
Bart a de nouveau été punie : il doit recopier 2000 fois "I WILL NOT DO ANYTHING BAD EVER AGAIN".
Cela l'empeche de participer au tournoi de foot ce week-end, et sans lui vous risquez de perdre :/

Peut-être que tu pourrais l'aider avec tes connaissances d'informatique...

## 3.3 Compte des occurrences (occurrence = nombre d'apparitions)
Karim se demande combien de lettre 'i' contient son livre.
Compléte le programme pour compter le nombre d'occurrences (apparitions) de la lettre 'i'.
```python
livre = "Le jour de ses onze ans, Harry Potter, un orphelin élevé par un oncle et une tante qui le détestent, voit son existence bouleversée. Un géant vient le chercher pour l'emmener au collège Poudlard, école de sorcellerie, où une place l'attent depuis toujours. Qui est donc Harry Potter ? Et qui est l'effroyable V..., le mage dont personne n'ose prononcer le nom ?"
occurrences_i = 0
for lettre in livre:
  if TODO:
    TODO
```

### 3.4 Comparaison des occurrences
Il se demande maintenant si le texte contient plus de lettre 'e' ou de lettre 'a'.
Peux-tu l'aider ?


## 3.5 (optionnel) Une formule équilibrée
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

# 4. Tableaux
TODO
