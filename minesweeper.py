import pygame

ROWS, COLS = 10, 10 
CELL_SIZE = 40  
HEADER_HEIGHT = 60
WIDTH, HEIGHT = COLS * CELL_SIZE, ROWS * CELL_SIZE + HEADER_HEIGHT

WHITE = (255, 255, 255)
LIGHT_GRAY = (180, 180, 180)  
DARK_GRAY = (150, 150, 150)  
BLACK = (0, 0, 0)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Minesweeper")

# Main loop
running = True
while running:
    screen.fill(WHITE)

    #Draw the header
    pygame.draw.rect(screen, DARK_GRAY, (0, 0, WIDTH, HEADER_HEIGHT)) 

    # Draw the cells 
    for row in range(ROWS):
        for col in range(COLS):
            x = col * CELL_SIZE
            y = row * CELL_SIZE + HEADER_HEIGHT  
            rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, LIGHT_GRAY, rect) 
            pygame.draw.rect(screen, BLACK, rect, 2) 

    # Event 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
