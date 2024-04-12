import pygame
from pygame.locals import *

pygame.init()

# génération de la fenêtre 
screen_x = 1024
screen_y = 512
screen = pygame.display.set_mode((screen_x, screen_y))
pygame.display.set_caption("PLATFORMOUUUUUR")

# importation des textures
frame_width = 32
def frame(pic, x):
    global frame_width
    frame = pic.subsurface(pygame.Rect( frame_width * (x - 1), 0, frame_width, frame_width ))
    return frame

bouga = {}
bouga["bitmap"]  = pygame.image.load('./projet_final/textures/themes/perso_bouga_run.png')
bouga["df_r"]    = frame(bouga["bitmap"], 1)
bouga["walk1_r"] = frame(bouga["bitmap"], 2)
bouga["walk2_r"] = frame(bouga["bitmap"], 3)
bouga["hit_r"]   = frame(bouga["bitmap"], 4)
bouga["df_l"]    = frame(bouga["bitmap"], 8)
bouga["walk1_l"] = frame(bouga["bitmap"], 7)
bouga["walk2_l"] = frame(bouga["bitmap"], 6)
bouga["hit_l"]   = frame(bouga["bitmap"], 5)

pygame.display.set_icon(bouga["df_r"])
# boucle principale
running = True 
while running:
    screen.fill((94, 242, 255)) # remplissage de l'arrière plan
    for event in pygame.event.get(): # récupération des évènements
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Closed window")
    # affichage du perso
    screen.blit(bouga["df_r"], (0, 0))
    pygame.display.flip() # mise à jour de l'écran
pygame.display.flip() # mise à jour de l'écran
