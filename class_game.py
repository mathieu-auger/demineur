class Game:
    def __init__(self, size, num_mines):
        self.grid = Grid(size, num_mines)
        self.game_lost = False

    def play_turn(self, x, y):
        if self.grid.matrix[x][y].mine:
            self.game_lost = True
            print("You clicked on a mine! Game over.")
        else:
            self.grid.reveal_cell(x, y)

    def first_click(self, x, y):
        if self.grid.matrix[x][y].mine:
            self.grid.matrix[x][y].mine = False
            self.grid.place_mines()
