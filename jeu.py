import pygame
from pygame.locals import *
 
pygame.init()
 
#Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((200, 200))
 
#Chargement et collage du fond
fond = pygame.image.load("background.jpg").convert()
fenetre.blit(fond, (0,0))
 
#Chargement et collage du personnage
perso = pygame.image.load("dk_down.png").convert_alpha()
perso_x = 10
perso_y = 10
fenetre.blit(perso, (perso_x,perso_y))
 
#Rafraîchissement de l'écran
pygame.display.flip()
 
#BOUCLE INFINIE
continuer = 1
pygame.key.set_repeat(1,20)
while continuer:
    for event in pygame.event.get():    #Attente des événements
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            continuer = 0
 
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                perso_x = event.pos[0] - 15
                perso_y = event.pos[1] - 15
 
        if event.type == KEYDOWN:
 
            if event.key == K_UP:
                if perso_y >= 10:
                    perso = pygame.image.load("dk_up.png").convert_alpha()
                    perso_y -= 3
 
            if event.key == K_DOWN:
                if perso_y <= 160:
                    perso = pygame.image.load("dk_down.png").convert_alpha()
                    perso_y += 3
 
            if event.key == K_LEFT:
                if perso_x >= 10:
                    perso = pygame.image.load("dk_left.png").convert_alpha()
                    perso_x -= 3
 
            if event.key == K_RIGHT:
                if perso_x <= 160:
                    perso = pygame.image.load("dk_right.png").convert_alpha()
                    perso_x += 3
 
 
    #Re-collage
    fenetre.blit(fond, (0,0))
    fenetre.blit(perso, (perso_x, perso_y))
    #Rafraichissement
    pygame.display.flip()