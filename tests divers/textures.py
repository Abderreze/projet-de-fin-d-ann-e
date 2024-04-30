import pygame

# importation des textures

def frame(pic, x, frame_width=64):
    frame = pic.subsurface(pygame.Rect( frame_width * (x - 1), 0, frame_width, frame_width ))
    return frame

# import du vrai bouton play
button_Play = pygame.image.load("projet_final/textures/misc/Play.png")
button_Play = pygame.transform.scale(button_Play, (button_Play.get_width() * 3, button_Play.get_height() * 3))
width_button_play, height_button_play = button_Play.get_size()
button_play_on = button_Play.subsurface((0, 0, width_button_play // 2, height_button_play))
button_play_off = button_Play.subsurface((width_button_play // 2, 0, width_button_play // 2, height_button_play))
button_play_on_rect = button_play_on.get_rect()
button_play_on_rect = button_play_on_rect.move(820, 400)

#bouton son yes
button_sound = pygame.image.load("projet_final/textures/misc/Bouton.png")
button_sound = pygame.transform.scale(button_sound, (button_sound.get_width() * 2, button_sound.get_height() * 2))
width_button_sound, height_button_sound = button_sound.get_size()
button_sound_yes_off = button_sound.subsurface((0, 0, width_button_sound // 2, height_button_sound))
button_sound_yes_on = button_sound.subsurface((width_button_sound // 2, 0, width_button_sound // 2, height_button_sound))
button_sound_yes_rect = button_sound_yes_off.get_rect()
button_sound_yes_rect = button_sound_yes_rect.move(230,420)


#bouton son no
button_sound_no = pygame.image.load("projet_final/textures/misc/Bouton.png")
button_sound_no = pygame.transform.scale(button_sound_no, (button_sound_no.get_width() * 2, button_sound_no.get_height() * 2))
width_button_sound_no, height_button_sound_no = button_sound_no.get_size()
button_sound_no_off = button_sound_no.subsurface((0, 0, width_button_sound_no // 2, height_button_sound_no))
button_sound_no_on = button_sound_no.subsurface((width_button_sound_no // 2, 0, width_button_sound_no // 2, height_button_sound_no))
button_sound_no_rect = button_sound_no_off.get_rect()
button_sound_no_rect = button_sound_no_rect.move(343, 420)


#logo
logo = pygame.image.load('projet_final/textures/misc/Logo.png')


#perso 
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
