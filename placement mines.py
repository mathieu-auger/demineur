class Case:
    def __init__(self):
        self.revelee = False
        self.mine = False
        self.voisins_mines = 0
    
    def reveler(self):
        self.revelee = True

import random

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


