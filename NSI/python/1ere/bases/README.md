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
<details>
  <summary>Demander une entrée</summary>
La fonction `input` permet de demander à l'utilisateur d'entrer une valeur (cf: fiche récapitulative)
</details>
## Ex 1.3: Date de naissance de Lucie
Lucie a 24 ans, complète le code en remplaçant le TODO pour trouver son année de naissance :
```python
age = 24
date_naissance = TODO
print(date_naissance)
```

## Ex 1.4: Vraie date de naissance de Lucie
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
  L'aire d'un triangle rectangle est égale à: a * b / 2
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
<img src="https://github.com/ymougenel/COURS_INFO_SNT-NSI/blob/main/.README/math_sqrt.png">
</details>
