class TicTacToe:
    board = []
    player = None
    x = None
    y = None
    state = 'start'

    def __init__(self):
        self.board = [['.' for _ in range(3)] for _ in range(3)]
        self.player = 1

    def display(self):
        for row in self.board:
            print(''.join(row))

    def check(self):
        sign = 'x' if self.player == 1 else 'o'
        count = 0
        for i in range(3):
            if self.board[self.x][i] == sign:
                count += 1
        if count == 3:
            print(sign + ' win the game')
            self.state = 'end'
            return
        count = 0
        for j in range(3):
            if self.board[j][self.y] == sign:
                count += 1
        if count == 3:
            print(sign + ' win the game')
            self.state = 'end'
            return
        count = 0
        for k in range(3):
            if self.board[k][k] == sign:
                count += 1
        if count == 3:
            print(sign + ' win the game')
            self.state = 'end'
            return
        count = 0
        for k in range(3):
            if self.board[k][3 - k - 1] == sign:
                count += 1
        if count == 3:
            print(sign + ' win the game')
            self.state = 'end'
            return
        if not any('.' in rows for rows in self.board):
            print('it\'s a draw')
            self.state = 'draw'
            return

    def empty_case(self):
        if self.board[self.x][self.y] == '.':
            return True
        return False

    def move(self):
        self.x = int(input('Choose a column : ')) - 1
        self.y = int(input('Choose a row : ')) - 1
        while not self.empty_case():
            print('Invalid column !')
            self.x = int(input('Choose a column : ')) - 1
            self.y = int(input('Choose a row : ')) - 1

        if self.player == 1:
            self.board[self.x][self.y] = 'x'
        else:
            self.board[self.x][self.y] = 'o'

        self.display()
        self.check()
        self.player = (self.player + 1) % 2


game = TicTacToe()
game.display()
while game.state == 'start':
    game.move()
print('end')
