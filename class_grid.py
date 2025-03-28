import random

class Grid:
    def __init__(self, size, num_mines):
        self.size = size
        self.num_mines = num_mines
        self.matrix = [[Cell() for _ in range(size)] for _ in range(size)]
        self.place_mines()

    def place_mines(self):
        placed_mines = 0
        while placed_mines < self.num_mines:
            x = random.randint(0, self.size - 1)
            y = random.randint(0, self.size - 1)
            if not self.matrix[x][y].mine:
                self.matrix[x][y].mine = True
                placed_mines += 1
                self.update_neighbors(x, y)

    def update_neighbors(self, x, y):
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.size and 0 <= ny < self.size:
                self.matrix[nx][ny].adjacent_mines += 1

    def reveal_cell(self, x, y):
        if self.matrix[x][y].revealed or self.matrix[x][y].mine:
            return
        
        self.matrix[x][y].reveal()
        
        if self.matrix[x][y].adjacent_mines == 0:  # Recursive propagation
            directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.size and 0 <= ny < self.size:
                    self.reveal_cell(nx, ny)
