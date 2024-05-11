import pygame
import settings
from pygame.locals import *
'''
Fichier principal du jeu
'''
pygame.init()

# génération de la fenêtre
print("loading window...")
screen_width = settings.screen_width
screen_heigth = settings.screen_heigth
screen = pygame.display.set_mode((screen_width, screen_heigth))
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
    screen.blit(game.map.picture, game.draw_pos["map"])
    screen.blit(game.player.current_frame, game.draw_pos["player"])
    pygame.display.flip() # mise à jour de l'écran

print("preparing for game loop...")
current_game = game.Game(textures, "chevalier", "stone", maps.maps["test_map"]) 
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
    current_game.update(keys, mouse)
    drawAll(current_game)
    
pygame.display.flip() # mise à jour de l'écran