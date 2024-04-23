import pygame

# importation des textures

def frame(pic, x, frame_width=64):
    frame = pic.subsurface(pygame.Rect( frame_width * (x - 1), 0, frame_width, frame_width ))
    return frame
#bouton play 
button_play = pygame.image.load("projet_final/textures/misc/button_play.png")
button_play = pygame.transform.scale(button_play, (200, 100))
button_play_rect = button_play.get_rect()
button_play_rect = button_play_rect.move(820, 400)
button_play_rect = button_play.get_rect()
logo = pygame.image.load('projet_final/textures/misc/Logo.png')
theme = "SUSHI"
player = {}
player["bitmap"]  = pygame.image.load('projet_final/textures/player/perso_'+theme+'_run.png')
player["bitmap"]  = pygame.transform.scale(player["bitmap"], (player["bitmap"].get_width() * 2, player["bitmap"].get_height() * 2))
# découpage de l'image bouga en plusieurs bouga 
player["df_r"]    = frame(player["bitmap"], 1)
player["walk1_r"] = frame(player["bitmap"], 2)
player["walk2_r"] = frame(player["bitmap"], 3)
player["hit_r"]   = frame(player["bitmap"], 4)
player["df_l"]    = frame(player["bitmap"], 8)
player["walk1_l"] = frame(player["bitmap"], 7)
player["walk2_l"] = frame(player["bitmap"], 6)
player["hit_l"]   = frame(player["bitmap"], 5)
