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
button_play_on = textures.button_play_on
button_play_on_rect = textures.button_play_on_rect
button_play_off = textures.button_play_off
width_button_play = textures.width_button_play
height_button_play = textures.height_button_play 


pygame.display.set_icon(logo)
print("textures loaded")

print("starting game loop...")

#personnage
player["current"] = player["df_r"]
running = {"r": ["walk1_r", "df_r", "walk2_r", "df_r"], "l": ["walk1_l", "df_l", "walk2_l", "df_l"], "adv": 0}
moving = "n"
facing = "r"
action = "hit"
# élément, (bouton, son, ect...)
button_play_position = (820, 400)
background = (94, 242, 255)

# boucle principale
open = True
while open:
    run = False
    #le menu princiaple
    background = (94, 242, 255)
    screen.fill(background)
    screen.blit(button_play_on, (820, 400))
    mouse_x, mouse_y = pygame.mouse.get_pos()
    print(mouse_x, mouse_y)
    
    # si on veut quitter le jeux
    for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                open = False
                pygame.quit()
                print("Closed window")
            # lancement du jeu
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if button_play_on_rect.collidepoint(event.pos):
                        pygame.time.delay(1500)
                        run = True
            #test
    if button_play_position[0] <= mouse_x <= button_play_position[0] + width_button_play and button_play_position[1] <= mouse_y <= button_play_position[1] + height_button_play:
        # Si la souris est sur le bouton, afficher l'image "button_play_off"
        screen.blit(button_play_off, button_play_position)
    else:
        # Sinon, afficher l'image "button_play_on"
        screen.blit(button_play_on, button_play_position)

    # Mettre à jour l'écran
    pygame.display.flip()
       

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
