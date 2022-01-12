# Manipulation de nombre entier

## Sommaire
- [Manipulation de nombre entier](#manipulation-de-nombre-entier)
  - [Sommaire](#sommaire)
  - [Intro](#intro)
  - [**I. Table de multiplications**](#i-table-de-multiplications)
  - [**II. Suite logique**](#ii-suite-logique)
  - [**III. Nombre manquant \***](#iii-nombre-manquant-)

## Intro

Dans ce document nous allons avoir plusieurs exercices afin de manipuler des integer. 

Les exos marqué avec des astérix vont être corrigé devant vous, les autres ne vont pas l'être et seront seulement là si vous désirez vous entraîner. Mais des test (3 généralement) seront là pour vous aiguiller.

PS: Si la gestion d'erreur n'est pas précisé dans l'énoncé c'est qu'elle n'est pas obligatoire. On imagine que l'utilisateur à un minimum de QI et sait quoi renter XD. Indiquez lui juste ce qu'il doit rentrer dans la fonction avec un commentaire. Pour les plus avancés vous pouvez chercher à automatiser ça en demandant un input pour savoir quel function (parmis les parties ci-dessous) il souhaite exécuter et les paramètres.
<br>

## **I. Table de multiplications**

Vous devez réaliser l'affichage de la table de multiplication du nombre *n* rentré en paramètre quelque soit le valeur de *n*.

<u><b>Entrée :</b></u>

Un nombre *n* quelconque.

<u><b>Sortie :</b></u>

Une belle table de multiplicatioon tel que:

```
1 x 1 = 1
1 x 2 = 2
1 x 3 = 3
1 x 4 = 4
1 x 5 = 5
1 x 6 = 6
1 x 7 = 7
1 x 8 = 8
1 x 9 = 9
1 x 10 = 10
```
Vous personnaliser la sortie du moment que le résultat est là.

<u><b>Test :</b></u>

```
Input:

2

Output:

2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8
2 x 5 = 10
2 x 6 = 12
2 x 7 = 14
2 x 8 = 16
2 x 9 = 18
2 x 10 = 20
```

```
Input:

52

Output:

52 x 1 = 52
52 x 2 = 104
52 x 3 = 156
52 x 4 = 208
52 x 5 = 260
52 x 6 = 312
52 x 7 = 364
52 x 8 = 416
52 x 9 = 418
52 x 10 = 520
```

```
Input:

-7

Output:

-7 x 1 = -7
-7 x 2 = -14
-7 x 3 = -21
-7 x 4 = -28
-7 x 5 = -35
-7 x 6 = -42
-7 x 7 = -49
-7 x 8 = -56
-7 x 9 = -63
-7 x 10 = -70
```

## **II. Suite logique**

Considérons un algorithme qui prend en entrée un entier positif *n* tel que 1 ≤*n*≤ 106 :

Si *n* est pair, l'algorithme le divise par deux.

Si *n* est impair, l'algorithme le multiplie par trois et ajoute un. 

L'algorithme répète cela jusqu'à ce que *n* soit égal à un. 

Par exemple, la séquence pour n=3 est la suivante : 
3→10→5→16→8→4→2→1

Votre tâche consiste à simuler l'exécution de l'algorithme pour une valeur donnée de *n*. 

<br>
<u><b>Entrée :</b></u>

La seule ligne d'entrée contient un entier *n*. 

<br>
<u><b>Sortie :</b></u>

 Imprime une ligne qui contient toutes les valeurs de *n* pendant l'algorithme. 


<u><b>Gestion d'erreur :</b></u>
Si le nombre n'est pas compris entre 1 et 106 compris vous devez lui demdander de selectionner un nombre compris entre ces bornes.


<u><b>Test :</b></u>

```
Input:

5

Output:

5->16->8->4->2->1
```

```
Input:

108

Output:

Error, n isn't between 1 and 106
```

```
Input:

65

Output:

65->196->98->49->148->74->37->112->56->28->14->7->22->11->34->17->52->26->13->40->20->10->5->16->8->4->2->1
```

## **III. Nombre manquant \***

On vous donne des nombres entre 1,2,…,*n* . Votre tâche est de trouver les numéros manquants à la liste de 1 à *n*. *n* étant le plus grand nombre de la série rentrée.

<u><b>Entrée :</b></u>

Les nombres compris entre 1 et *n* (inclus). Chaque nombre est distinct. Vous devez vérifier que le nombre n'est pas répétés 2 fois ou plus. 


<u><b>Sortie :</b></u>

Imprimer les nombres manquants.

Si le nombre est répétés 2 fois (ou plus), vous devez indiquer à l'utilisateur qu'il a rentrée plusieurs fois le nombres .

Si il n'y a aucun nombre manquant vous pouvez féliciter l'utilisateur de n'avoir raté aucun nombre.

<u><b>Test :</b></u>

```
Entrée :

exo3(1,2,3,4)

Sortie : 

Congratulation you forgot nothing !!
```

```
Entrée :

exo3(-19, 1,2,3,5,6,8,9,10,11,23)

Sortie : 

Error, please enter numbers better than 0
```

```
Entrée :

exo3(1,2,3,5,6,8,9,1, 10,11,23, 3, 6, 5)

Sortie : 

1  was enter more than 1 time :  2  exactly!
3  was enter more than 1 time :  2  exactly!
5  was enter more than 1 time :  2  exactly!
6  was enter more than 1 time :  2  exactly!
13  numbers were forget
```