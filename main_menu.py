import pygame
import subprocess

WIDTH, HEIGHT = 400, 500
BUTTON_WIDTH, BUTTON_HEIGHT = 200, 50

WHITE = (255, 255, 255)
GRAY = (150, 150, 150)
DARK_GRAY = (100, 100, 100)
BLACK = (0, 0, 0)

# Difficulty levels
difficulties = ["Easy", "Medium", "Hard"]


class Button:
    def __init__(self, x, y, width, height, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = pygame.font.Font(None, 40)

    def draw(self, screen):
        pygame.draw.rect(screen, DARK_GRAY, self.rect)  
        pygame.draw.rect(screen, BLACK, self.rect, 3)  

        text_render = self.font.render(self.text, True, WHITE)
        screen.blit(text_render, (self.rect.x + (self.rect.width - text_render.get_width()) // 2,
                                  self.rect.y + 10))

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)


class Menu:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Minesweeper Menu")

        self.font = pygame.font.Font(None, 50)

        # Buttons
        self.play_button = Button(WIDTH // 2 - BUTTON_WIDTH // 2, 200, BUTTON_WIDTH, BUTTON_HEIGHT, "Play")
        self.quit_button = Button(WIDTH // 2 - BUTTON_WIDTH // 2, 340, BUTTON_WIDTH, BUTTON_HEIGHT, "Quit")
        self.difficulty_button = Button(WIDTH // 2 - BUTTON_WIDTH // 2, 270, BUTTON_WIDTH, BUTTON_HEIGHT, difficulties[0])

        # Arrows for difficulty selection
        self.arrow_left = pygame.Rect(self.difficulty_button.rect.x - 50, self.difficulty_button.rect.y + 10, 40, 30)
        self.arrow_right = pygame.Rect(self.difficulty_button.rect.x + BUTTON_WIDTH + 10,
                                       self.difficulty_button.rect.y + 10, 40, 30)

        self.difficulty_index = 0
        self.running = True

    def draw(self):
        self.screen.fill(GRAY)

        title_text = self.font.render("MINESWEEPER", True, BLACK)
        self.screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 80))

        self.play_button.draw(self.screen)
        self.quit_button.draw(self.screen)
        self.difficulty_button.draw(self.screen)

        # Draw arrows
        pygame.draw.polygon(self.screen, BLACK, [(self.arrow_left.x + 30, self.arrow_left.y), 
                                                  (self.arrow_left.x + 30, self.arrow_left.y + 30),
                                                  (self.arrow_left.x, self.arrow_left.y + 15)])  # Left arrow
        pygame.draw.polygon(self.screen, BLACK, [(self.arrow_right.x, self.arrow_right.y),
                                                  (self.arrow_right.x, self.arrow_right.y + 30),
                                                  (self.arrow_right.x + 30, self.arrow_right.y + 15)])  # Right arrow

        pygame.display.flip()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.quit_button.is_clicked(event.pos):
                    self.running = False
                elif self.play_button.is_clicked(event.pos):
                    print(f"Launching game in {difficulties[self.difficulty_index]} mode...")
                    pygame.quit()
                    subprocess.run(["python", "minesweeper.py", difficulties[self.difficulty_index]])
                    exit()
                elif self.arrow_left.collidepoint(event.pos):
                    self.difficulty_index = (self.difficulty_index - 1) % len(difficulties)
                elif self.arrow_right.collidepoint(event.pos):
                    self.difficulty_index = (self.difficulty_index + 1) % len(difficulties)

                self.difficulty_button.text = difficulties[self.difficulty_index]

    def run(self):
        while self.running:
            self.handle_events()
            self.draw()

        pygame.quit()


if __name__ == "__main__":
    menu = Menu()
    menu.run()
