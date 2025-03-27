import pygame
import subprocess  
# Window settings
WIDTH, HEIGHT = 400, 500
BUTTON_WIDTH, BUTTON_HEIGHT = 200, 50

WHITE = (255, 255, 255)
GRAY = (150, 150, 150)
DARK_GRAY = (100, 100, 100)
BLACK = (0, 0, 0)

difficulties = ["Easy", "Medium", "Hard"]
difficulty_index = 0  

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Minesweeper Menu")

font = pygame.font.Font(None, 50)
button_font = pygame.font.Font(None, 40)

# Create buttons
buttons = {
    "Play": pygame.Rect((WIDTH // 2 - BUTTON_WIDTH // 2, 200), (BUTTON_WIDTH, BUTTON_HEIGHT)),
    "Difficulty": pygame.Rect((WIDTH // 2 - BUTTON_WIDTH // 2, 270), (BUTTON_WIDTH, BUTTON_HEIGHT)),
    "Quit": pygame.Rect((WIDTH // 2 - BUTTON_WIDTH // 2, 340), (BUTTON_WIDTH, BUTTON_HEIGHT)),
}

# Create arrows for difficulty selection (placed outside the button)
arrow_left = pygame.Rect(buttons["Difficulty"].x - 50, buttons["Difficulty"].y + 10, 40, 30)
arrow_right = pygame.Rect(buttons["Difficulty"].x + BUTTON_WIDTH + 10, buttons["Difficulty"].y + 10, 40, 30)

# Menu loop
running = True
while running:
    screen.fill(GRAY)

    title_text = font.render("MINESWEEPER", True, BLACK)
    screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 80))

    for text, rect in buttons.items():
        pygame.draw.rect(screen, DARK_GRAY, rect)  
        pygame.draw.rect(screen, BLACK, rect, 3)  

        if text == "Difficulty":
            difficulty_text = button_font.render(difficulties[difficulty_index], True, WHITE)
            screen.blit(difficulty_text, (rect.x + (BUTTON_WIDTH - difficulty_text.get_width()) // 2, rect.y + 10))
        else:
            text_render = button_font.render(text, True, WHITE)
            screen.blit(text_render, (rect.x + (BUTTON_WIDTH - text_render.get_width()) // 2, rect.y + 10))

    # arrows
    pygame.draw.polygon(screen, BLACK, [(arrow_left.x + 30, arrow_left.y), (arrow_left.x + 30, arrow_left.y + 30), (arrow_left.x, arrow_left.y + 15)])  # Left arrow
    pygame.draw.polygon(screen, BLACK, [(arrow_right.x, arrow_right.y), (arrow_right.x, arrow_right.y + 30), (arrow_right.x + 30, arrow_right.y + 15)])  # Right arrow

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if buttons["Quit"].collidepoint(event.pos):
                running = False
            elif buttons["Play"].collidepoint(event.pos):
                print(f"Launching game in {difficulties[difficulty_index]} mode...")
                pygame.quit()  
                subprocess.run(["python", "minesweeper.py", difficulties[difficulty_index]])  # Pass the difficulty
                exit()
            elif arrow_left.collidepoint(event.pos):
                difficulty_index = (difficulty_index - 1) % len(difficulties)  # Decrease difficulty
            elif arrow_right.collidepoint(event.pos):
                difficulty_index = (difficulty_index + 1) % len(difficulties)  # Increase difficulty

    pygame.display.flip()

pygame.quit()
