import pygame
from pygame.locals import *
'''
Fichier principal du jeu
'''
pygame.init()

# génération de la fenêtre
print("loading window...")
screen_x = 1024
screen_y = 512
screen = pygame.display.set_mode((screen_x, screen_y))
pygame.display.set_caption("BASIROUUUUUUU")

# import des textures
print("loading textures...")
import textures
logo = textures.logo
player_textures = textures.player
pygame.display.set_icon(logo)

# import des maps
print("loading maps...")
import maps

# import du code de partie
print("loading game algorithms...")
import game

# fonction d'affichage
print("loading draw function...")
def drawAll(game):
    global screen
    background = (94, 242, 255)
    screen.fill(background)
    screen.blit(game.map.picture, (0, 0))
    screen.blit(game.player.current_frame, (0, 0))
    pygame.display.flip() # mise à jour de l'écran

print("preparing for game loop...")
current_game = game.Game(textures, "chevalier", "nature", maps.maps["test_map"]) 
running = True
print("loaded game successfully, starting game loop!")
# boucle principale
while running:
    for event in pygame.event.get(): # fermeture de fenêtre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Closed window")
    
    # récupération des entrées clavier
    keys = pygame.key.get_pressed()
    mouse = pygame.mouse.get_pressed()
    current_game.update_inputs(keys, mouse)
    current_game.update_frame()
    drawAll(current_game)
    
pygame.display.flip() # mise à jour de l'écran