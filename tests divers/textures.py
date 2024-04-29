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
# import du vrai bouton play
button_Play = pygame.image.load("projet_final/textures/misc/Play.png")
button_Play = pygame.transform.scale(button_Play, (button_Play.get_width() * 3, button_Play.get_height() * 3))
width_button_play, height_button_play = button_Play.get_size()
button_play_on = button_Play.subsurface((0, 0, width_button_play // 2, height_button_play))
button_play_off = button_Play.subsurface((width_button_play // 2, 0, width_button_play // 2, height_button_play))
button_play_on_rect = button_play_on.get_rect()
button_play_on_rect = button_play_on_rect.move(820, 400)
'''
button_Play = pygame.image.load("projet_final/textures/misc/Play.png")
height_button_Play, width_button_Play = button_Play.get_size()
button_Play_on = button_Play.subsurface(pygame.Rect(0, 0, width_button_Play // 2, height_button_Play))
button_Play_off = button_Play.subsurface(pygame.Rect(width_button_Play // 2, 0, width_button_Play // 2, height_button_Play))
button_go = {"on":button_Play_on,"off":button_Play_off}
button_Play = {}
button_Play["mms"] = pygame.image.load("projet_final/textures/misc/Play.png")
button_Play["mms"]  = pygame.transform.scale(button_Play["mms"], (button_Play["mms"].get_width() * 2, button_Play["mms"].get_height() * 2))
button_Play["off"] = frame(button_Play["mms"], 1)
button_Play["on"] = frame(button_Play["mms"], 2)
'''
#bouton son 
button_sound = pygame.image.load("projet_final/textures/misc/Bouton.png")
#logo
logo = pygame.image.load('projet_final/textures/misc/Logo.png')
#perso 
theme = "chevalier"
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
