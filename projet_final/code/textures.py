# CE FICHIER CHARGE TOUTES LES TEXTURES POUR LE JEU AU DEMARRAGE

import pygame

def frame(pic, x, frame_width=64):
    '''
    IN: pic: image contenant plusieurs frames dont on veut extraire un seul.
        x: numéro du frame qu'on veut, les frames sont en ligne à intervales réguliers sur l'image pic
        frame_width: largeur d'un frame, défaut sur 64
    OUT: le frame extrait
    '''
    frame = pic.subsurface(pygame.Rect( frame_width * (x - 1), 0, frame_width, frame_width ))
    return frame


logo = pygame.image.load('textures/misc/Logo.png')
characters = ["bouga", "chevalier", "arabe", "SUSHI"]
player = {}
for character in characters:
    player[character] = {}
    player[character]["bitmap"]  = pygame.image.load('textures/player/perso_'+character+'_run.png')
    player[character]["bitmap"]  = pygame.transform.scale(player[character]["bitmap"], (player[character]["bitmap"].get_width() * 2, player[character]["bitmap"].get_height() * 2))
    # découpage de l'image bouga en plusieurs bouga 
    player[character]["df_r"]    = frame(player[character]["bitmap"], 1)
    player[character]["walk1_r"] = frame(player[character]["bitmap"], 2)
    player[character]["walk2_r"] = frame(player[character]["bitmap"], 3)
    player[character]["hit_r"]   = frame(player[character]["bitmap"], 4)
    player[character]["df_l"]    = frame(player[character]["bitmap"], 8)
    player[character]["walk1_l"] = frame(player[character]["bitmap"], 7)
    player[character]["walk2_l"] = frame(player[character]["bitmap"], 6)
    player[character]["hit_l"]   = frame(player[character]["bitmap"], 5)