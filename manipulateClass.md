# **Manipulation de classe**

## **Sommaire**
- [**Manipulation de classe**](#manipulation-de-classe)
  - [**Sommaire**](#sommaire)
  - [**Intro**](#intro)
  - [**I. Iniatiliser une Classe**](#i-iniatiliser-une-classe)
  - [**II. Premières méthodes**](#ii-premières-méthodes)
  - [**III. Attribut protégés**](#iii-attribut-protégés)
  - [**IV. Héritage**](#iv-héritage)

## **Intro**

Dans ce document nous allons avoir plusieurs exercices afin de manipuler les classes. 


PS: Si la gestion d'erreur n'est pas précisé dans l'énoncé c'est qu'elle n'est pas obligatoire. On imagine que l'utilisateur à un minimum de QI et sait quoi renter XD. Indiquez lui juste ce qu'il doit rentrer dans la fonction avec un commentaire. Pour les plus avancés vous pouvez chercher à automatiser ça en demandant un input pour savoir quelle fonction (parmis les parties ci-dessous) il souhaite exécuter et les paramètres.
<br>

Tout au long des exos je vais prendre en exemple un mmorpg (avec player, classes ...)

## **I. Iniatiliser une Classe**

Pour commencer **Rappelez vous!!** dans une methode (une fonction dans une classe) il y a toujours en paramètre au moins **```self```**.


Dans une classe la première fonction exécutée est: ```__init__```. C'est pour quoi on la nomme constructeur: c'est elle qui va permetrre à la class de bien s'**initialiser**.

<u><b>Exemple :</b></u>

```py
class Player:
    def __init__(self):
        self.name = "Shiroe"
        self.level = 2
```

De plus, lors de l'instanciation d'une classe, vous pouvez demander des variables à rentrer en paramètre pour enrichir la classe et la personnaliser.

<u><b>Exemple :</b></u>

```python
class Player:
    def __init__(self, name , level):
        self.name = name
        self.level = level
```

<u><b>A vous de jouer</b></u>

Pratiquer les bases en créant une classe *Drink* dans laquelle vous allez créer une fonction ```__init__``` qui va prendre 2 paramètres  *name* et *quantity*.

Une fois cela fait vous devriez pouvoir instancier votre classe. C'est à dire que vous pouvez donner ce type à une variable. Vous allez donc créer une variable et lui donner pour valeur le constructeur de votre classe. C'est à dire:


<u><b>Exemple :</b></u>

```python
moi=Player("Yami", 3)
print(type(moi))

```

Ce qui vous donnera : ```<class '__main__.Player'>``` (où à la place de Player ça sera Drink)



## **II. Premières méthodes**

Nous allons maintenant créer des méthodes dans notre classe et les utiliser. Commençons par les *getters*. Ces méthodes permettent de récupérer la valeur d'un attribut de notre variable. 

<u><b>Exemple :</b></u>

```python
moi=Player("Yami", 3)
print(moi.get_name())
print(moi.get_level())
```


<u><b>Output :</b></u>

```
Yami
3
```

Comme vous pouvez le voir, nous arrivons à récupérer les attributs de notre classe assez aisément. Mais cela va être embêtant si on cherche à faire une phrase avec. On serait sinon obligé de faire un:

```python
print("Player ", moi.get_name()), " is level ", moi.get_level())
```

Cela est bien long. Nous allons alors créer une méthode ```ToString()``` dans laquelle on va pouvoir créer une sortie des infomations de manière claire et propre.

<u><b>Exmple :</b></u>

```python
def ToString(self):
    return "Player {0} is Level {1}".format(self.name, self.level)
```

Ce qui me donne : 
<u><b>Output :</b></u>

```
Player Yami is Level 3
```

<u><b>A vous de jouer</b></u>

Vous l'aurez compris, c'est à vous de créer vos méthodes dans votre cas. Je vous demande donc de réaliser un ```getName()``` et un ```getQuantity()``` pour les getters. Et de faire un ```ToString()``` qui renvoi une phrase dans le style de celle ci-dessus.


___
A ce niveau vous avez réalisé les bases d'une classe. Nous allons maintenant compléxifier les choses.

## **III. Attribut protégés**

Un attribut d'une classe peut être protégé (privé). C'est à dire que nous n'avons pas accès à ce dernier hors de la classe.
Dans l'exemple ci-dessous j'ai un attribut *PV* que je déclare en tant que privé grâce au "```__```" devant un attribut. 

<u><b>Exemple :</b></u>

```python
class Player:
  def __init__(self, name , level):
      self.name = name
      self.level = level
      self.__life = self.level*30

moi = Player("Tamashi", 3)
print(moi.__life)

```

<u><b>Output :</b></u>
```powershell
Traceback (most recent call last):
  File "c:\Users\reype\Documents\YNOV\B2\LABO_PY\Labo-py\manipulateClass.py", line 18, in <module>
    print(moi.__life)
AttributeError: 'Player' object has no attribute '__life'
```

Comme vous pouvez l'observer, nous ne pouvons pas accéder à cet attribut  *__life*  le code me pète une erreur. Nous allons donc créer un *getter* permettant de récupérer cet attribut. 

```python
lass Player:
  def __init__(self, name , level):
      self.name = name
      self.level = level
      self.__life = self.level*30

  def get_life(self):
      return self.__life


moi = Player("Tamashi", 3)
print(moi.get_life())

```

<u><b>Output :</b></u>

```
90
```

Comme vous vous en doutez, puisqu'on peut utiliser l'attribut seulement dans la classe nous allons faire une méthode qui va nous permettre de perdre des points de vie (et donc t'intérargir avec cet attribut privé).

<u><b>Exemple :</b></u>

```python
class Player:
    def __init__(self, name , level):
        self.name = name
        self.level = level
        self.__life = self.level*30

    def get_life(self):
        return self.__life
    
    def ToString(self):
        return "Player {0} is Level {1} and I've {2} pv".format(self.name, self.level, self.__life)

    def getDamage(self, damage):
        self.__life -= damage
        if self.__life < 0:
            print("You are dead")

moi = Player("Yami", 3)
print(moi.get_life())
print("20 damage to player --->")
moi.getDamage(20)
print(moi.ToString())
```

<u><b>Output :</b></u>
```
90
20 damage to player --->
Player Yami is Level 3 and I've 70 pv
```

<u><b>A vous de jouer</b></u>*

Vous devez maintenant passer *Quantity* en attribut privé et vous allez créer une méthode ```shot()``` qui va prendre en paramètre un integer représentant la grandeur du verre. Et ainsi vous allez enlever cette quantité à celle de votre boisson.

## **IV. Héritage**

Le dernier point que je vais aborder sur les classes est l'héritage. Il permet de partir d'une  classe en la personnalisant un peu plus afin de ne pas partir de 0.

Ici je vias créer une classe *Bard* qui va hériter de *Player* mais où je vais changer 2-3 attribut ou méthodes:

- Réduire ```__life```de trois-quart
- Créer une méthode ```HealingSong``` .
- Ajouter *"Bard - "* devant le ```name```

<b>Créer l'héritage</b>

Pour créer un héritage, il faut préciser entre parenthèse la class mère dont hérite notre nouvelle classe (voir ci-dessous). Puis lors de l'initialisation, il suffit d'exécuter l'initialisation de la classe mère avant celle de la classe fille. Pour se faire, si nous possédons une seule classe mère (car oui on peut hériter de plusieurs) il suffit de faire un ```super().__init__()``` et rentrer les paramètre de la classe mère comme si vous instanciez votre classe.

```python
class Bard(Player):
    def __init__(self, name, level, PM):
        super().__init__(name, level)
        self.PM = PM
```

On peut maintenant instancier notre classe *Bard* et voir si nous avons accès aux méthodes de notre classe *Player*

```python
other = Bard("Tamashi", 5, 100)
print(other.get_life())
print("2 damage to player --->")
other.getDamage(20)
print(other.ToString())
print(type(other))
print(other.get_name())
print(other.get_level())
print(other.ToString())
```

<u><b>Output :</b></u>

```powershell
150
20 damage to player --->
Player Tamashi is Level 5 and I've 130 pv
<class '__main__.Bard'>
Tamashi
5
Player Tamashi is Level 5 and I've 130 pv
```

Comme on peut le voir, on a bien tout nos attributs et nos méthode. Donc *Bard* à tout ce que notre class *Player* a.

Nous allons donc passer au changement:

<b>Réduire ```__life``` de trois-quart</b>

Pour se faire il nous faut juste modifier sa valeur dans notre ```__init__()```.

```Python
class Bard(Player):
    def __init__(self, name, level, PM):
        super().__init__(name, level)
        self.PM = PM

        self.__life -= self.get_life()/4
```

<u><b>Output: </b></u>

```
Traceback (most recent call last):
  File "c:\Users\reype\Documents\YNOV\B2\LABO_PY\Labo-py\manipulateClass.py", line 43, in <module>
    other = Bard("Tamashi", 5, 100)
  File "c:\Users\reype\Documents\YNOV\B2\LABO_PY\Labo-py\manipulateClass.py", line 29, in __init__
    self.__life -= self.get_life()/4
AttributeError: 'Bard' object has no attribute '_Bard__life'
```

Ah, probème: notre ```__life``` n'est pas reconnu de notre classe *Bard*. Cela est normale, ```__life``` est un attribut privé. Donc la privatisation d'un attribut se fait **même pour une classe fille**. Nous allons donc être plus malin, 2 options: 
- rendre public norte ```__life```
- créer un setter ```set__life()``` qui permet de modifier la valeur de l'attribut ```life```. 

Je vais opter pour la deuxième par choix personnel mais aussi par respect de la consigne (suite des questions précèdentes). 

Dans *Player*
```python
class Player:
    def __init__(self, name , level):
        self.name = name
        self.level = level
        self.__life = self.level*30

    def set_life(self, nb):
        self.__life = nb
```

Dans *Bard*
```python
class Bard(Player):
    def __init__(self, name, level, PM):
        super().__init__(name, level)
        self.PM = PM
        self.set_life(self.get_life() - self.get_life()//4)
```

Vérifions ce changement:

```Python
other = Bard("Tamashi", 4, 100)
print(other.get_life())
print("2 damage to player --->")
other.getDamage(20)
print(other.ToString())
print(type(other))
print(other.get_name())
print(other.get_level())
print(other.ToString())
```

<u><b>Output :</b></u>
```powershell
90
20 damage to player --->
Player Tamashi is Level 4 and I've 70 pv
<class '__main__.Bard'>
Tamashi
4
Player Tamashi is Level 4 and I've 70 pv
```

<b> Créer une méthode ```HealingSong()``` .</b>

Cette méthode va rajouter 2*level de point de vie au joueur et va lui enlever 40 PM.


```python
class Bard(Player):
    def __init__(self, name, level, PM):
        super().__init__(name, level)
        self.PM = PM
        self.set_life(self.get_life() - self.get_life()//4)

    def HealingSong(self):
        self.set_life(self.get_life() + 2*self.level)
        self.PM -=40


other = Bard("Tamashi", 4, 100)
print(other.ToString())
print("HealingSong used--->")
other.HealingSong()
print(other.ToString())
```

<u><b>Output :</b></u>

```powershell
Player Tamashi is Level 4 and I've 70 pv
HealingSong used--->
Player Tamashi is Level 4 and I've 82 pv
```

On peut donc bien rajouter une méthode à notre classe fille. Mais peut on modifier une méthode noter class mère et la réécrire dans notre classe fille? Testons cela.

```python
class Bard(Player):
    def __init__(self, name, level, PM):
        super().__init__(name, level)
        self.PM = PM
        self.set_life(self.get_life() - self.get_life()//4)

    def HealingSong(self):
        self.set_life(self.get_life() + 3*self.level)
        self.PM -=40

    def ToString(self):
        return "Player {0} is Level {1} and I've {2} pv. Rest {3} PM".format(self.name, self.level, self.get_life(), self.PM)


other = Bard("Tamashi", 4, 100)
print(other.ToString())
```

<u><b>Output :</b></u>

```
Player Tamashi is Level 4 and I've 90 pv. Rest 100 PM
```

Donc notre ToString  de la classe fille passe avant le ToString de notre classe mère.

Dernière étape:

<b>Ajouter *"Bard - "* devant le ```name```</b>

Il suffit juste de modifier notre attribut. Celui-ci n'étant pas privé, on peut faire cela simplement tel que:

```python
class Bard(Player):
    def __init__(self, name, level, PM):
        super().__init__(name, level)
        self.PM = PM
        self.name = "Bard - "+name
        self.set_life(self.get_life() - self.get_life()//4)
    
    ...

other = Bard("Tamashi", 4, 100)
print(other.ToString())
```

<u><b>Output :</b></u>

```
Player Bard - Tamashi is Level 4 and I've 70 pv. Rest 100 PM
```

Voilà cela est fait aussi simplement que ça. 

<u><b>A vous de jouer</b></u>
Vous allez devoir réaliser plusieurs choses:
- Créer une classe *Bottle* qui hérite de *Drink*.
- Y ajouter l'attribut *price*. Ainsi que l'attribut privé *quantityOfOne* qui s'initialise à la valeur 1,5
- Y ajouter les méthodes ```howMany()``` qui va calculer le nombre de bouteille nécessaire pour contenir la quantité de notre boissons, et ```howMuch()``` permettant de calculer le prix totale pour ces bouteilles. 
- Redéfinir ```ToString()``` avec une phrase tel que: "For 2L of Fanta, we need 2 bottles. It will cost x" (ou x sera le prix total)
___

Vous voici à la fin de ce document. J'espère que les classes vous paraissent plus claire et plus accessibles.

