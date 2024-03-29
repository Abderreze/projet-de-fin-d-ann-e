# projet-de-fin-d-ann-e

Suivi du Projet:

Idée de départ: L'idée de base est de faire un jeu en 2D pour le projet finale en NSI.

Idée du jeu: Le principe du jeu est souls like en 2D, plusieur guerrier: samourai, guerrier arabe, croisé, homme de cromagnon, maya. Le tutoriel dépend du guerrier choisi: bataille contre armée ottoman (guerrier arabe), bataille contre mongolle (samourai), guerre contre guerrier arabes (croisé), chasse de gibier (homme de cromagnon), guerre contra azteque (maya). Tout les tuto seront composé de quelque petits adversaires, suivi d'un bosse plus gros.

Lore: 




import pygame
import sys

# Définir les éléments de base du jeu
EMPTY = 0
X = 1
O = 2
BOARD_SIZE = 3

# Initialiser le jeu
def init_board():
    return [[EMPTY for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

# Concevoir l'interface utilisateur
def draw_board(screen, board):
    screen.fill((255, 255, 255))
    cell_size = 100
    for y in range(BOARD_SIZE):
        for x in range(BOARD_SIZE):
            pygame.draw.rect(screen, (0, 0, 0), (x * cell_size, y * cell_size, cell_size, cell_size), 1)
            if board[y][x] == X:
                pygame.draw.line(screen, (0, 0, 0), (x * cell_size + 10, y * cell_size + 10), 
                                 (x * cell_size + cell_size - 10, y * cell_size + cell_size - 10), 2)
                pygame.draw.line(screen, (0, 0, 0), (x * cell_size + cell_size - 10, y * cell_size + 10), 
                                 (x * cell_size + 10, y * cell_size + cell_size - 10), 2)
            elif board[y][x] == O:
                pygame.draw.circle(screen, (0, 0, 0), (x * cell_size + cell_size // 2, y * cell_size + cell_size // 2), cell_size // 2 - 10, 2)

# Gérer les événements et les entrées
def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

# Implémenter la logique du jeu
def check_winner(board):
    for i in range(BOARD_SIZE):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]
    return EMPTY

# Logique principale du jeu
def main():
    pygame.init()
    screen = pygame.display.set_mode((300, 300))
    pygame.display.set_caption("Tic Tac Toe")
    board = init_board()
    current_player = X

    while True:
        handle_events()
        draw_board(screen, board)
        pygame.display.flip()

        winner = check_winner(board)
        if winner != EMPTY:
            print("Le joueur", "X" if winner == X else "O", "a gagné !")
            pygame.quit()
            sys.exit()

if __name__ == "__main__":
    main()
