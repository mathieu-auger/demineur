import pygame

WIDTH, HEIGHT = 400, 500
BUTTON_WIDTH, BUTTON_HEIGHT = 200, 50


WHITE = (255, 255, 255)
GRAY = (150, 150, 150)
DARK_GRAY = (100, 100, 100)
BLACK = (0, 0, 0)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Minesweeper")

font = pygame.font.Font(None, 50)
button_font = pygame.font.Font(None, 40)

# Button
buttons = {
    "Play": pygame.Rect((WIDTH // 2 - BUTTON_WIDTH // 2, 200), (BUTTON_WIDTH, BUTTON_HEIGHT)),
    "Options": pygame.Rect((WIDTH // 2 - BUTTON_WIDTH // 2, 270), (BUTTON_WIDTH, BUTTON_HEIGHT)),
    "Quit": pygame.Rect((WIDTH // 2 - BUTTON_WIDTH // 2, 340), (BUTTON_WIDTH, BUTTON_HEIGHT)),
}

# main loop
running = True
while running:
    screen.fill(GRAY)

    title_text = font.render("MINESWEEPER", True, BLACK)
    screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 80))

    # Buttons
    for text, rect in buttons.items():
        pygame.draw.rect(screen, DARK_GRAY, rect) 
        pygame.draw.rect(screen, BLACK, rect, 3)  

        
        text_render = button_font.render(text, True, WHITE)
        screen.blit(text_render, (rect.x + (BUTTON_WIDTH - text_render.get_width()) // 2, rect.y + 10))

    # event management
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if buttons["Quitter"].collidepoint(event.pos):
                running = False  # Quit the game
            elif buttons["Jouer"].collidepoint(event.pos):
                print("Lancer le jeu...")  # to develope
            elif buttons["Options"].collidepoint(event.pos):
                print("Ouvrir les options...")  # to develope

    pygame.display.flip()

pygame.quit()
