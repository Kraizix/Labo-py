# Manipulation de chaîne de caractères

## Sommaire
- [Manipulation de chaîne de caractères](#manipulation-de-chaîne-de-caractères)
  - [Sommaire](#sommaire)
  - [Intro](#intro)
  - [**I. Inversion**](#i-inversion)
  - [**II. Separation d'une chaîne de caractère \***](#ii-separation-dune-chaîne-de-caractère-)
  - [**III. Répétition 1.0**](#iii-répétition-10)
  - [**IV. Majuscule ou minuscule**](#iv-majuscule-ou-minuscule)

## Intro

Dans ce document nous allons avoir plusieurs exercices afin de manipuler des Strings. 

Les exos marqué avec des astérix vont être corrigé devant vous, les autres ne vont pas l'être et seront seulement là si vous désirez vous entraîner. Mais des test (3 généralement) seront là pour vous aiguiller.

PS: Si la gestion d'erreur n'est pas précisé dans l'énoncé c'est qu'elle n'est pas obligatoire. On imagine que l'utilisateur à un minimum de QI et sait quoi renter XD. Indiquez lui juste ce qu'il doit rentrer dans la fonction avec un commentaire. Pour les plus avancés vous pouvez chercher à automatiser ça en demandant un input pour savoir quel function (parmis les parties ci-dessous) il souhaite exécuter et les paramètres
<br>

## **I. Inversion**

Vous devez réaliser un fonction permettant d'inverser une chaîne de caractère *str*.  

<u><b>Entrée :</b></u>

Une phrase/mot *str* quelconque.

<u><b>Sortie :</b></u>

*str* dans l'autre sens

<u><b>Exemple :</b></u>

```
Entrée : 
Jingle bell, jingle bell, jingle bell rock

Sortie :
kcor lleb elgnij ,lleb elgnij ,lleb elgnij
```

<u><b>Test :</b></u>

```python
Entrée :
print(inversion("Bleu"))
print(inversion("DX essap ed tom"))
print(inversion("EngagLeJeuQueJeLeGagne"))

Sortie :
kcor lleb elgnij ,lleb elgnij ,lleb elgniJ
uelB
mot de passe XD
engaGeLeJeuQueJeLgagnE
```


## **II. Separation d'une chaîne de caractère \***

Le but ici est de séparer un chaîne de caractère *str* a niveau de la séparation qui est rentré. 

<u><b>Conditions :</b></u>

La séparation *sep* doit contenir 1 seul caractère.

<u><b>Entrée :</b></u>

Une chaîne de caractère *str*
Un séparateur *sep* d'un seul caractère.

<u><b>Sortie :</b></u>

Une liste (ou un tuple) contenant chaque partie du String sans le séparateur.

<u><b>Exemple :</b></u>

```
Entrée :
Jingle bell, jingle bell, jingle bell rock
,

Sortie : 

['Jingle bell', ' jingle bell', ' jingle bell rock']
```

<u><b>Test :</b></u>

```python
Entrée :
print(seperate("Jingle bell, jingle bell, jingle bell rock", ","))
print(seperate("Mzezszszazgzez zCzazczhzéz", "z"))

Sortie :
['Jingle bell', ' jingle bell', ' jingle bell rock']
['M', 'e', 's', 's', 'a', 'g', 'e', ' ', 'C', 'a', 'c', 'h', 'é', '']
```

## **III. Répétition 1.0**

Vous devez réaliser un fonction permettant de compter le nombre de fois *n* que le carctère *char* apparaît.  

<u><b>Entrée :</b></u>

Une phrase/mot *str* quelconque.
Une lettre/caractère *char*.

<u><b>Sortie :</b></u>

Le nombre *n* de répétition. 

Si le caractère n'apparaît aucune fois, à vous d'annoncer l'abscence de ce caractère dans *str*.

<u><b>Test :</b></u>

```py
Entrée :

print(counterChar("Hello World", "l"))
print(counterChar("His palm are sweaty,  knees weak, arms are heavy", "z"))
print(counterChar("One thing, I don't know why. It doesn't even matter how hard you try. Keep that in mind. I designed this rhyme. To explain in due time", "i"))

Sortie :
The char l is in the str 3 times
The char z is not in the str His palm are sweaty,  knees weak, arms are heavy
The char i is in the str 8 times
```

## **IV. Majuscule ou minuscule**

Considérons une chaîne de caractères *str*. Vous devez mettre en majuscule ou en minuscule suivant une distance *n* entrée dans la console. 

<u><b>Entrée :</b></u>

Une phrase/mot *str* quelconque.
Un nombre représentant le saut de lettre avat de remettre uen majuscule.

<u><b>Sortie :</b></u>

La chaîne de caractères modifiée.

<u><b>Exemple :</b></u>

```
Entrée:
Vive le vent d'hiver
2

Sortie:
ViVe le VeNt d'hiVer
```

<u><b>Gestion d'erreur :</b></u>

Si le nombre rentré est plus grand que la longueur de la chaîne de caractères vous devez redemander un nombre à l'utilisateur. 

Si le nombre rentré est négatif, lui dire que cela est impossible. 

Si c'est 0 tout est en majuscule (comme 1).

<u><b>Test :</b></u>

```python
Entrée :

print(MajMin("Vive le vent d'hiver", 2))
print(MajMin("hello World", 0))
print(MajMin("Blue", 10))
print(MajMin("If you're not the most gifted, be the one who works the most ", 10))

Sortie :

ViVe lE VeNt d'hIvEr
HELLO WORLD
The number is over than the length of the string
If you're Not the moSt gifted, be the onE who workS the most
```
