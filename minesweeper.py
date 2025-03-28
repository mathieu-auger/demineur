import pygame

ROWS, COLS = 10, 10
CELL_SIZE = 40
HEADER_HEIGHT = 60
WIDTH, HEIGHT = COLS * CELL_SIZE, ROWS * CELL_SIZE + HEADER_HEIGHT

WHITE = (255, 255, 255)
LIGHT_GRAY = (180, 180, 180)
DARK_GRAY = (150, 150, 150)
BLACK = (0, 0, 0)

class Cell:
    def __init__(self, x, y, size):
        self.rect = pygame.Rect(x, y, size, size)
        self.is_revealed = False

    def draw(self, screen):
        pygame.draw.rect(screen, LIGHT_GRAY, self.rect)
        pygame.draw.rect(screen, BLACK, self.rect, 2)

class Grid:
    def __init__(self, rows, cols, cell_size, header_height):
        self.rows = rows
        self.cols = cols
        self.cell_size = cell_size
        self.header_height = header_height
        self.cells = [[Cell(col * cell_size, row * cell_size + header_height, cell_size)
                       for col in range(cols)] for row in range(rows)]
    
    def draw(self, screen):
        for row in self.cells:
            for cell in row:
                cell.draw(screen)

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Minesweeper")
        self.grid = Grid(ROWS, COLS, CELL_SIZE, HEADER_HEIGHT)
        self.running = True
    
    def run(self):
        while self.running:
            self.screen.fill(WHITE)
            pygame.draw.rect(self.screen, DARK_GRAY, (0, 0, WIDTH, HEADER_HEIGHT))  
            self.grid.draw(self.screen)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            pygame.display.flip()
        
        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()