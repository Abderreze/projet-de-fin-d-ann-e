import pygame
from pygame.locals import *

pygame.init()

# génération de la fenêtre 
screen_x = 1024
screen_y = 512
screen = pygame.display.set_mode((screen_x, screen_y))
pygame.display.set_caption("BASIROUUUUUUU")
print("window loaded")

<<<<<<< HEAD
# import des textures
import textures
logo = textures.logo
player = textures.player
=======
# importation des textures
def frame(pic, x, frame_width=64):
    frame = pic.subsurface(pygame.Rect( frame_width * (x - 1), 0, frame_width, frame_width ))
    return frame

bouga = {}
bouga["bitmap"]  = pygame.image.load('../textures/themes/perso_bouga_run.png')
bouga["bitmap"] = pygame.transform.scale(bouga["bitmap"], (bouga["bitmap"].get_width() * 2, bouga["bitmap"].get_height() * 2))
# découpage de l'image bouga en plusieurs bouga 
bouga["df_r"]    = frame(bouga["bitmap"], 1)
bouga["walk1_r"] = frame(bouga["bitmap"], 2)
bouga["walk2_r"] = frame(bouga["bitmap"], 3)
bouga["hit_r"]   = frame(bouga["bitmap"], 4)
bouga["df_l"]    = frame(bouga["bitmap"], 8)
bouga["walk1_l"] = frame(bouga["bitmap"], 7)
bouga["walk2_l"] = frame(bouga["bitmap"], 6)
bouga["hit_l"]   = frame(bouga["bitmap"], 5)

logo  = pygame.image.load('../textures/themes/Logo.png')
>>>>>>> 172eb1d0a3290d5c18ce134ea59060492fc203ac
pygame.display.set_icon(logo)
print("textures loaded")

print("starting game loop...")
# boucle principale
running = True 
player["current"] = player["df_r"]
running = {"r": ["walk1_r", "df_r", "walk2_r", "df_r"], "l": ["walk1_l", "df_l", "walk2_l", "df_l"], "adv": 0}
moving = "n"
facing = "r"
action = "hit"
background = (94, 242, 255)
while running:
    screen.fill(background) # remplissage de l'arrière plan
    for event in pygame.event.get(): # fermeture de fenêtre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Closed window")
    
    # récupération des entrées clavier
    keys = pygame.key.get_pressed()
    mouse = pygame.mouse.get_pressed()
    
    if mouse[0]:
        action = "hit"
    else:
        action = "n"
    if keys[K_LEFT]:
        facing = "l"
        moving = "l"
    elif keys[K_RIGHT]:
        facing = "r"
        moving = "r"
    else:
        moving = "n"
    
    # choix du frame adapté
    if action == "hit":
        player["current"] = player["hit_" + facing]
    elif moving != "n":
        if running["adv"] >= 3.9:
            running["adv"] = 0
        else:
            running["adv"] += 0.010
        player["current"] = player[running[facing][int(running["adv"])]]
    else:
        player["current"] = player["df_" + facing]
        running["adv"] = 0
    
    # affichage
    screen.blit(player["current"], (0, 0))
    pygame.display.flip() # mise à jour de l'écran
pygame.display.flip() # mise à jour de l'écran
