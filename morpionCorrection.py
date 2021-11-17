import random

grid=[]
for i in range(9):
    grid.append(i)

#random
startPlayer=random.randint(1,2)

Player=startPlayer


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

def play():
    global Player
    print("Joueur " + str(Player%2+1) + " à toi de jouer")
    signe=""
    #Determiner le signe X O
    if Player%2==0:
        signe="X"
    else : 
        signe = "O"

    global grid
    answer=[]
    for i in range(9):
        answer.append(str(i+1))
    print(answer, end="")
    
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
    
    grid[case-1]=signe

    #Change de joueur
    Player=Player+1

def verif():
    # Win?
    #horizontal
    iList = [0,3,6]
    for i in iList:
        if grid[i]==grid[i+1]==grid[i+2]:
            print("Joueur " + str(Player%2+1) + "a gagné!")
            return True
    # Vertical
    iList = [0,1,2]
    for i in iList:
        if grid[i]==grid[i+3]==grid[i+6]:
            
            print("Joueur " + str(Player%2+1) + "a gagné!")
            return True
    # Diago
    if grid[2]==grid[4]==grid[6] or grid[0]==grid[4]==grid[8]:
        
        print("Joueur " + str(Player%2+1) + " a gagné!")
        return True
    # Rempli?
    if Player==startPlayer+10:
        print("Egalité!")
        return True

    return False

while verif()==False:
    play()
    affBrut()
