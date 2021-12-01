import random

# déclaration de la grille de jeu
grid=[]
for i in range(1,10):
    grid.append(i)

#random
startPlayer=random.randint(1,2)

Player=startPlayer

# affichage déconseillé, mais utile pour comprendre l'autre technique
def affBrut():
    print(grid[0], end="")
    print(grid[1], end="")
    print(grid[2], end="")
    print()
    print(grid[3], end="")
    print(grid[4], end="")
    print(grid[5], end="")
    print()
    print(grid[6], end="")
    print(grid[7], end="")
    print(grid[8], end="")
    print()

def affFor():
    iList = [0,3,6]
    for i in iList:
        for j in range(3):
            print(grid[i+j], end="")
        print()

# Gère un tour de jeu
def play():
    # global permet de récupérer une variable déclarée hors fonction et de pouvoir la modifier
    global Player
    # Player%2+1 permet d'avoir le joueur actuel. Ex: si player =6: 6%2+1=1 -> donc au joueur 1 de jouer
    print("Joueur " + str(Player%2+1) + " à toi de jouer")
    signe=""
    #Determiner le signe X O
    if Player%2==0:
        signe="X"
    else : 
        signe = "O"
    
    #récupérer la grille
    global grid

    # déclaration d'une liste pour accéder au chiffre sous des chaînes de caractère:
    # ainsi on peut vérifier si l'input correspond à un chiffre pour pouvoir le transformer
    answer=[]
    for i in range(9):
        answer.append(str(i+1))
    
    # si l'input est pas bon
    while True:
        # recup input
        case=input("Quelle case voulez vous? 1-9 \n")
        if case not in answer:
            # errors
            print("Entre 1 et 9 stp!")
            continue
        # str -> int
        case=int(case)   
        if type(grid[case-1])!=int:
            print("Cette case est occupée")
            continue
        break
    # modification de la valeur de grid à la position case-1
    grid[case-1]=signe

    #Change de joueur
    Player=Player+1

# vérifie si la partie doit se finir
def verif():
    # Win?
    #horizontal
    # nous donne les index de début de ligne
    iList = [0,3,6]
    for i in iList:
        # verifie si la ligne n'a que le même signe
        if grid[i]==grid[i+1]==grid[i+2]:
            print("Joueur " + str(Player%2+1) + "a gagné!")
            return True
    # Vertical
    # nous donne les index de début de colonne
    iList = [0,1,2]
    for i in iList:
        # verifie si la colonne n'a que le même symbole
        if grid[i]==grid[i+3]==grid[i+6]:
            print("Joueur " + str(Player%2+1) + "a gagné!")
            return True
    # Diago
    # on vérifie les seuls diagonales possibles
    # A noter que le "or" correspond un "ou" logique (soit une condition soit l'autre)
    if grid[2]==grid[4]==grid[6] or grid[0]==grid[4]==grid[8]:
        print("Joueur " + str(Player%2+1) + " a gagné!")
        return True
    # Rempli?
    # si les vérifications du dessus n'ont rien données, on vérifie si la grille est pleine
    if Player==startPlayer+10:
        print("Egalité!")
        return True

    # si aucune des conditions n'est valide, on return false
    # cela signifie que le jeu n'est pas finit.
    return False

# boucle dite "main" qui va exécuter les autres fonctions tant que le jeu n'est pas finit (tant que verif() retourne un false)

affBrut()
while verif()==False:
    play()
    affFor()
