import random

class Cell:
    def __init__(self, around_mines = 0, mine = False):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = False


class GamePole:
    
    def __init__(self, N, M):
        self.N = N
        self.M = M
        self.pole = [[0]*self.N for i in range(self.N)]
        self.create_mine_field()

    def show(self):
        
        for i in self.pole:
            for j in i:
                if j.fl_open == False:
                    print('#', end=' ')
                else:
                    print(j.mine, end = ' ')
            print()

    def mine_generator(self):

        self.mines = [True for i in range(self.M)]
        self.empty_cell = [False for i in range(self.N * self.N - self.M)]
        self.mines.extend(self.empty_cell)
        random.shuffle(self.mines)        
        return (i for i in self.mines)


    def create_mine_field(self):

        self.gen_mines = self.mine_generator()

        for i in range(self.N):
            for j in range(self.N):
                self.pole[i][j] = Cell(mine=next(self.gen_mines))

        self.count_mines_around()

    def count_mines_around(self):

        self.biger_field = [[0]*(self.N+2) for i in range(self.N+2)]

        for i in range(self.N):
            for j in range(self.N):
                self.biger_field[i+1][j+1] = int(self.pole[i][j].mine)

        for i in range(1, self.N+1):
            for j in range(1, self.N+1):
                self.pole[i-1][j-1].around_mines = sum([self.biger_field[i][j], self.biger_field[i][j+1], self.biger_field[i][j-1],
                                                        self.biger_field[i+1][j], self.biger_field[i+1][j+1], self.biger_field[i+1][j-1],
                                                        self.biger_field[i-1][j], self.biger_field[i-1][j+1], self.biger_field[i-1][j-1]])




pole_game = GamePole(10, 12)
pole_game.show()


