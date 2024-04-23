import pygame
from pygame.locals import *

pygame.init()

# génération de la fenêtre .
screen_x = 1024
screen_y = 512
screen = pygame.display.set_mode((screen_x, screen_y))
pygame.display.set_caption("BASIROUUUUUUU")
print("window loaded")

# import des textures
import textures
logo = textures.logo
player = textures.player
button_play = textures.button_play
button_play_rect = textures.button_play_rect

pygame.display.set_icon(logo)
print("textures loaded")

print("starting game loop...")

player["current"] = player["df_r"]
running = {"r": ["walk1_r", "df_r", "walk2_r", "df_r"], "l": ["walk1_l", "df_l", "walk2_l", "df_l"], "adv": 0}
moving = "n"
facing = "r"
action = "hit"
background = (94, 242, 255)


# boucle principale
open = True
while open:
    run = False
    #le menu princiaple
    background = (94, 242, 255)
    screen.fill(background)
    screen.blit(button_play, button_play_rect)
    
    # si on veut quitter le jeux
    for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                open = False
                pygame.quit()
                print("Closed window")
            # lancement du jeu
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if button_play_rect.collidepoint(event.pos):
                        run = True
    while run:
       

        for event in pygame.event.get(): # fermeture de fenêtre
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                print("Closed window")
        screen.fill(background) # remplissage de l'arrière plan
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
                running["adv"] += 0.050
            player["current"] = player[running[facing][int(running["adv"])]]
        else:
            player["current"] = player["df_" + facing]
            running["adv"] = 0

        


        
        # affichage
        screen.blit(player["current"], (0, 0))
        pygame.display.flip() # mise à jour de l'écran
    pygame.display.flip() # mise à jour de l'écran
