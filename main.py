import pygame
import random
from interface import game

win = pygame.image.load("image/win.jpg")

loose = pygame.image.load("image/looser.jpg")


ROWS, COLS = 10, 10 
CELL_SIZE = 40  
HEADER_HEIGHT = 60
WIDTH, HEIGHT = COLS * CELL_SIZE, ROWS * CELL_SIZE + HEADER_HEIGHT

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
    "Jouer": pygame.Rect((WIDTH // 2 - BUTTON_WIDTH // 2, 200), (BUTTON_WIDTH, BUTTON_HEIGHT)),
    "Options": pygame.Rect((WIDTH // 2 - BUTTON_WIDTH // 2, 270), (BUTTON_WIDTH, BUTTON_HEIGHT)),
    "Quitter": pygame.Rect((WIDTH // 2 - BUTTON_WIDTH // 2, 340), (BUTTON_WIDTH, BUTTON_HEIGHT)),
}

class Case:
    def __init__(self):
        self.revelee = False
        self.mine = False
        self.voisins_mines = 0
    
    def reveler(self):
        self.revelee = True

class Grille:
    def __init__(self, taille, nb_mines):
        self.taille = taille
        self.nb_mines = nb_mines
        self.matrice = [[Case() for _ in range(taille)] for _ in range(taille)]
        self.placer_mines()

def placer_mines(self):
        mines_placees = 0
        while mines_placees < self.nb_mines:
            x = random.randint(0, self.taille - 1)
            y = random.randint(0, self.taille - 1)
            if not self.matrice[x][y].mine:
                self.matrice[x][y].mine = True
                mines_placees += 1
                self.mettre_a_jour_voisins(x, y)    

def mettre_a_jour_voisins(self, x, y):
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.taille and 0 <= ny < self.taille:
                self.matrice[nx][ny].voisins_mines += 1

def reveler_case(self, x, y):
        if self.matrice[x][y].revelee or self.matrice[x][y].mine:
            return
        
        self.matrice[x][y].reveler()
        
        if self.matrice[x][y].voisins_mines == 0:  # Propagation récursive
            directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.taille and 0 <= ny < self.taille:
                    self.reveler_case(nx, ny)


class Jeu:
    def __init__(self, taille, nb_mines):
        self.grille = Grille(taille, nb_mines)
        self.partie_perdue = False

    def jouer_coup(self, x, y):
        if self.grille.matrice[x][y].mine:
            self.partie_perdue = True
            print("Vous avez cliqué sur une mine ! Partie perdue.")
        else:
            self.grille.reveler_case(x, y)

    def premier_clic(self, x, y):
        if self.grille.matrice[x][y].mine:
            self.grille.matrice[x][y].mine = False
            self.grille.placer_mines()    
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
        elif buttons["Jouer"].collidepoint(event.pos):# print("Lancer le jeu...")  # to develope
            game()
        elif buttons["Options"].collidepoint(event.pos):
                print("Ouvrir les options...")  # to develope
    screen.blit(win, (200,250))

    screen.blit(loose, (250, 200))
    pygame.display.flip()

pygame.quit()

