# CE FICHIER CHARGE TOUTES LES TEXTURES POUR LE JEU AU DEMARRAGE

import pygame

# Fonction pour facilement récupérer des carrés d'une image
def frame(pic, x, frame_width=128):
    '''
    IN: pic: image contenant plusieurs frames dont on veut extraire un seul.
        x: numéro du frame qu'on veut, les frames sont en ligne à intervales réguliers sur l'image pic
        frame_width: largeur d'un frame, défaut sur 64
    OUT: le frame extrait
    '''
    frame = pic.subsurface(pygame.Rect( frame_width * (x - 1), 0, frame_width, frame_width ))
    return frame

# Fonction pour facilement changer la taille d'une image
def resize(pic, scale_factor):
    '''
    IN: pic: image de départ
        scale_factor: facteur d'agrandissement
    OUT: image agrandie ou rapetissée
    '''
    resized  = pygame.transform.scale(pic, (pic.get_width() * scale_factor, pic.get_height() * scale_factor))
    return resized

# Import des textures du joueur
characters = ["bouga", "chevalier", "arabe", "SUSHI"]
player = {}
for character in characters:
    player[character] = {}
    player[character]["bitmap"]  = pygame.image.load('textures/player/perso_'+character+'_run.png')
    player[character]["bitmap"]  = resize(player[character]["bitmap"], 4)
    # découpage de l'image bouga en plusieurs bouga 
    player[character]["df_r"]    = frame(player[character]["bitmap"], 1)
    player[character]["walk1_r"] = frame(player[character]["bitmap"], 2)
    player[character]["walk2_r"] = frame(player[character]["bitmap"], 3)
    player[character]["hit_r"]   = frame(player[character]["bitmap"], 4)
    player[character]["df_l"]    = frame(player[character]["bitmap"], 8)
    player[character]["walk1_l"] = frame(player[character]["bitmap"], 7)
    player[character]["walk2_l"] = frame(player[character]["bitmap"], 6)
    player[character]["hit_l"]   = frame(player[character]["bitmap"], 5)

# Import des textures de blocs
tiles = {}
tiles["dirt"]        = pygame.image.load('textures/tiles/Dirt.png')
tiles["dirt_grass"]  = pygame.image.load('textures/tiles/Dirt_grass.png')
tiles["dirt_japan"]  = pygame.image.load('textures/tiles/Dirt_japan.png')
tiles["stone_path"]  = pygame.image.load('textures/tiles/Stone_path.png')
tiles["sand"]        = pygame.image.load('textures/tiles/Sand.png')
tiles["sand_path"]   = pygame.image.load('textures/tiles/Sand_path.png')

tiles["dirt"]        = resize(tiles["dirt"], 4)
tiles["dirt_grass"]  = resize(tiles["dirt_grass"], 4)
tiles["dirt_japan"]  = resize(tiles["dirt_japan"], 4)
tiles["stone_path"]  = resize(tiles["stone_path"], 4)
tiles["sand"]        = resize(tiles["sand"], 4)
tiles["sand_path"]   = resize(tiles["sand_path"], 4)

# Import des textures diverses
logo = pygame.image.load('textures/misc/Logo.png')