class TicTacToe:
    board = []
    player = None
    x = None
    y = None
    count={'x':0,'o':0}
    state = "start"
    def __init__(self):
        self.board = [['.' for _ in range(3)]for _ in range(3)]
        self.player = 1
    
    def display(self):
        for row in self.board:
            print(''.join(row))

    def check(self):
        for i in range(3):
            if(self.board[self.x][i] != '.'):
                self.count[self.board[self.x][i]] += 1
        if 3 in self.count.values():
            print(list(self.count.keys())[list(self.count.values()).index(3)]+' win the game')
            self.state = "end"
            return
        self.resetCount()
        for j in range(3):
            if(self.board[j][self.y] != '.'):
               self.count[self.board[j][self.y]] += 1
        if 3 in self.count.values():
            print(list(self.count.keys())[list(self.count.values()).index(3)]+' win the game')
            self.state = "end"
            return
        self.resetCount()
        for k in range(3):
            if (self.board[k][k] != '.'):
                self.count[self.board[k][k]] += 1
        if 3 in self.count.values():
            print(list(self.count.keys())[list(self.count.values()).index(3)]+' win the game')
            self.state = "end"
            return
        self.resetCount()
        for k in range(3):
            if (self.board[k][3-k-1] != '.'):
                self.count[self.board[k][3-k-1]] += 1
        if 3 in self.count.values():
            print(list(self.count.keys())[list(self.count.values()).index(3)]+' win the game')
            self.state = "end"
            return


    def move(self):
        self.x = int(input("Choose a column : "))-1
        self.y = int (input("Choose a row : "))-1
        if self.player == 1:
            self.board[self.x][self.y]='x'
        else :
            self.board[self.x][self.y]='o'
        self.player = (self.player + 1)%2
        self.display()
        self.check()

    def resetCount(self):
        self.count['x']=0
        self.count['o']=0

game = TicTacToe()
game.display()
while game.state == "start":
    game.move()
print("end")
