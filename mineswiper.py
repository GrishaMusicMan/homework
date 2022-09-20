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
        print(self.pole)

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

    def count_mines_around(self):

        self.pole


#c1 = Cell(around_mines, mine)
pole_game = GamePole(5, 10)

for i in pole_game.pole:
    for j in i:
        print(j.mine, end=' ')
    print() 

# print(*pole_game.gen_mines)
