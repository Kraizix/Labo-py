player=1
board=[[".", ".", "."], [".", ".", "."], [".", ".", "."]]

def printBoard(board):
    for x in range(len(board)):
        for y in range(len(board[x])):
            print(board[x][y], end="")
        print()

def who(player):
    if player==1:
        player+=1
    else:
        player= 1
    return player
    
def checkWin(player,x):
    a=""
    if player==1:
        a="X"
    else :
        a="O"
    
    print(board[x])
    print(board[x].count(a))
    if board[x].count(a)==3:
        print("Player 1 Win !")
        return True



def localisation(player):
    x=input("Choisissez une case :")
    x=int(x)
    y=input(int)
    y=int(y)
    if player==1:
        board[x-1][y-1]="X"
    else:
        board[x-1][y-1]="O"
    return x-1,y-1



def main():
    global player
    while True:
        printBoard(board)
        if player==1:
            print("player1")
        else:
            print("player2")
        x,y=localisation(player)
        player = who(player)
        if checkWin(player,x,)==True:
            break

main()