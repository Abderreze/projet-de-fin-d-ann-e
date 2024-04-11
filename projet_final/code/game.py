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
def frame(x):
    global frame_width
    return frame_width * (x - 1)

bouga = {}
bouga["bitmap"]  = pygame.image.load('./projet_final/textures/themes/perso_bouga_run.png')
bouga["df_r"]    = bouga["bitmap"].subsurface(pygame.Rect( frame(1), 0, frame_width, frame_width ))
bouga["walk1_r"] = bouga["bitmap"].subsurface(pygame.Rect( frame(2), 0, frame_width, frame_width ))
bouga["walk2_r"] = bouga["bitmap"].subsurface(pygame.Rect( frame(3), 0, frame_width, frame_width ))
bouga["hit_r"]   = bouga["bitmap"].subsurface(pygame.Rect( frame(4), 0, frame_width, frame_width ))
bouga["df_l"]    = bouga["bitmap"].subsurface(pygame.Rect( frame(8), 0, frame_width, frame_width ))
bouga["walk1_l"] = bouga["bitmap"].subsurface(pygame.Rect( frame(7), 0, frame_width, frame_width ))
bouga["walk2_l"] = bouga["bitmap"].subsurface(pygame.Rect( frame(6), 0, frame_width, frame_width ))
bouga["hit_l"]   = bouga["bitmap"].subsurface(pygame.Rect( frame(5), 0, frame_width, frame_width ))

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
    center = 16
    pygame.display.flip() # mise à jour de l'écran
pygame.display.flip() # mise à jour de l'écran