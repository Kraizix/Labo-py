# Manipulation de listes, tuples et dictionnaires

## Sommaire
- [Manipulation de listes, tuples et dictionnaires](#manipulation-de-listes-tuples-et-dictionnaires)
  - [Sommaire](#sommaire)
  - [Intro](#intro)
  - [**I. Base \***](#i-base-)
  - [**II. Note une personne**](#ii-note-une-personne)
  - [**III. Note classe**](#iii-note-classe)
  - [**IV. Fibonacci**](#iv-fibonacci)
  - [**V. Répétitions 2.0**](#v-répétitions-20)

## Intro

Dans ce document nous allons avoir plusieurs exercices afin de manipuler des listes, dictionnaires et tuples. 

Les exos marqué avec des astérix vont être corrigé devant vous, les autres ne vont pas l'être et seront seulement là si vous désirez vous entraîner. Mais des test (3 généralement) seront là pour vous aiguiller.


PS: Si la gestion d'erreur n'est pas précisé dans l'énoncé c'est qu'elle n'est pas obligatoire. On imagine que l'utilisateur à un minimum de QI et sait quoi renter XD. Indiquez lui juste ce qu'il doit rentrer dans la fonction avec un commentaire. Pour les plus avancés vous pouvez chercher à automatiser ça en demandant un input pour savoir quel function (parmis les parties ci-dessous) il souhaite exécuter et les paramètres
<br>

## **I. Base \***

Vous devez réaliser une fonction dans laquelle vous allez utiliser plusieurs methodes de base des Listes:
- count()
- len()
- append()
- remove()

<u><b>Entrée :</b></u>

La liste fournis (ou la votre si vous voulez tester votre programme perso)

Une chaîne de caractères représentant un flag. (Dans le cas de count vous devez recenser tout les occurrence de tout les éléments)

<u><b>Sortie :</b></u>

Tout ce qui a était demandé dans la fonction.

<u><b>Liste fournis </b></u>

```py
list = [
  22, 
  "bleu",
  True,
  "Hello",
  156,
  -2,
  "Str",
  "Hello",
  22,
  25,
  55
]

```

<u><b>Test :</b></u>

```py
Entrée : 

flag(list, "count")

Sortie :

{22: 2, 'bleu': 1, True: 1, 'Hello': 2, 156: 1, -2: 1, 'Str': 1, 25: 1, 55: 1}

```

```py
Entrée : 

flag(list, "len")

Sortie :

11

```

```py
Entrée : 

flag(list, "append", "TEST")

Sortie :

append  TEST  in list
[22, 'bleu', True, 'Hello', 156, -2, 'Str', 'Hello', 22, 25, 55, 'TEST']
```

```py
Entrée : 

flag(list, "remove", 22)

Sortie :

remove  22  from list
['bleu', True, 'Hello', 156, -2, 'Str', 'Hello', 22, 25, 55]

```

## **II. Note une personne**

Vous devez réaliser 3 fonctions permettant de gérer les notes d'une personne:

- max -> renvoi la note maximum d'un personne
- min -> renvoi la note minimum d'une personne
- moy -> renvoi la moyenne de la personne

<u><b>Entrée :</b></u>

Une liste de integer non négatif compris en 0 et 20

<u><b>Sortie :</b></u>

Ce qui est demandé suivant la fonction

<u><b>Gestion d'erreur :</b></u>

Si la liste ne contient pas que des integers ressortir l'erreur: "Impossible d'exécuter la fonction, toute la liste ne contient pas que des integer"

<u><b>Test :</b></u>

```python

Entrée :
notes1 = [12,15,18,20,8,10]
notes2=[0, 19, 11, 18, 4]

maximum(notes1)
minimum(notes1)
moy(notes1)

maximum(notes2)
minimum(notes2)
moy(notes2)

Sortie: 

The maximum is  20
The minimum is  8
The average is  13.83
The maximum is  19
The minimum is  0
The average is  10.4
```

## **III. Note classe**

Vous devez réaliser une fonction permettant de gérer les notes d'une classes (vous pouvez vous aider de l'exo ci-dessus). A partir de cette fonction vous devez réaliser une action demandé rentrée en tant que flag dans l'appel de la fonction.

- best -> renvoi l'élève avec la meilleur note sur l'eval donné
- worst -> renvoi l'élève avec la pire note sur l'eval donné
- moySomeone -> renvoi la moyenne de l'élève rentré en paramètre
- moy -> renvoi la moyenne de la classe sur un Contrôle
- moyTotal -> renvoi la moyenne de classe

<u><b>Entrée :</b></u>

Une liste de integer non négatif compris en 0 et 20 et un flag (une chaîne de caractères)

<u><b>Sortie :</b></u>

Ce qui est demandé suivant la fonction

<u><b>Gestion d'erreur :</b></u>

Si la liste ne contient pas que des integers ressortir l'erreur: "Impossible d'exécuter la fonction, toute la liste ne contient pas que des integer"

<u><b>Test :</b></u>

```python

Entrée :

Programmateam = {
    "Costa" : [18,15,17,20,8],
    "Kevin" : [20,19,16,20,19],
    "Valentin" : [18,19,17,18,15],
    "Benji" : [17, 14, 15, 17, 15],
    "Arthur" : [17, 15, 13, 19, 13]
    }

print(classe(Programmateam, "best", 1))
print(classe(Programmateam, "worst", 1))
print(classe(Programmateam, "moy", 1))
print(classe(Programmateam, "moySomeone", "Kevin"))
print(classe(Programmateam, "moyTotal",1 ))

Sortie :

The best note of the test n°  0
It's Kevin with 20
The worst note of the test n°  0
It's Arthur with 17
The average of the calss on the test n° 1
[18, 20, 18, 17, 17]
18.0
Kevin has 18.8
The class has an average of 16.56
```

## **IV. Fibonacci**

Considérons une liste remplie que de nombre entier. Vous devez vérifier si cette liste correspond à une liste simillaire à une suite de Fibonacci.

Qu'est ce qu'une suite de Fibonacci? C'est quand, chaque nombre est égale à la somme des 2 précèdents. S'il n'en a pas il n'est pas concerné par cette condition.

Exemple: 

0-1-1-2-3-5-8-13 est une suite de Fibonacci

1-8-9-13 n'en n'est pas une.

<u><b>Entrée :</b></u>

Une liste de integer non négatif

<u><b>Sortie :</b></u>

Savoir si le suite respecte la suite de Fibonacci ou non. (Vous pouvez sortir un Booléan si vous le souhaitez)

<u><b>Gestion d'erreur :</b></u>

Si la liste ne contient pas que des integers ressortir l'erreur: "Impossible d'exécuter la fonction, toute la liste ne contient pas que des integer"

<u><b>Test :</b></u>

```python
Entrée :
print(febonacci([1,1,2,3,5,8,13,21,34]))
print(febonacci([0,1,1,2,3,5,8,13]))
print(febonacci([1,8,9,13]))
print(febonacci([1,2,3,5,8,"13",21]))
print(febonacci(12))

Sortie : 
This list respect the Febonacci's suite !!! 
True
This list respect the Febonacci's suite !!! 
True
It's not a Febonacci's suite  13  !=  9  +  8 !
False
The function can't be execute because all elements of the list aren't integers
None
Please enter a list or a tuple
None

```

## **V. Répétitions 2.0**

<u>Pré-requis :</u>
Je vous conseil fortement d'avoir fait **Répétition 1.0** avant celui-ci.


Comme dans sa version antérieur, vous devez compter le *n* de répétition d'un caractère dans une chaîne de caractère. Sauf qu'ici, je vous demande de compter tout les caractères et de stocker le résultat dans un dictionnaire.

<u><b>Entrée :</b></u>

Une phrase/mot *str* quelconque.

<u><b>Sortie :</b></u>

Un dictionnaire dénombrant les caractères et leur nombres *n* répétition. 

<u><b>Test :</b></u>

```py
Entrée :

print(repetitions("Hello World"))
print()
print(repetitions("His palm are sweaty,  knees weak, arms are heavy"))
print()
print(repetitions("One thing, I don't know why. It doesn't even matter how hard you try. Keep that in mind. I designed this rhyme. To explain in due time"))

Sortie :
{'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}

{'h': 2, 'i': 1, 's': 4, ' ': 9, 'p': 1, 'a': 7, 'l': 1, 'm': 2, 'r': 3, 'e': 7, 'w': 2, 't': 1, 'y': 2, ',': 2, 'k': 2, 'n': 1, 'v': 1}

{'o': 7, 'n': 11, 'e': 13, ' ': 26, 't': 12, 'h': 7, 'i': 11, 'g': 2, ',': 1, 'd': 7, "'": 2, 'k': 2, 'w': 3, 'y': 4, '.': 4, 's': 3, 'v': 1, 'm': 4, 'a': 4, 'r': 4, 'u': 2, 'p': 2, 'x': 1, 'l': 1}

```