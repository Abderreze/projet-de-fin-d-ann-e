import pygame
from player import Player
from game import Game  
pygame.init()

# création de la fenêtre 
pygame.display.set_caption("BASIROUUUUUU")
screen = pygame.display.set_mode((1024, 712))
print("window loaded")

# importer l'arrière plan
background = pygame.image.load("assets/bg.jpg")

# charger le jeu
game = Game()

# importation des textures
def frame(pic, x, frame_width=64):
    frame = pic.subsurface(pygame.Rect( frame_width * (x - 1), 0, frame_width, frame_width ))
    return frame

bouga = {}
bouga["bitmap"]  = pygame.image.load('../textures/themes/perso_bouga_run.png')
bouga["bitmap"] = pygame.transform.scale(bouga["bitmap"], (bouga["bitmap"].get_width() * 2, bouga["bitmap"].get_height() * 2))
bouga["df_r"]    = frame(bouga["bitmap"], 1)
bouga["walk1_r"] = frame(bouga["bitmap"], 2)
bouga["walk2_r"] = frame(bouga["bitmap"], 3)
bouga["hit_r"]   = frame(bouga["bitmap"], 4)
bouga["df_l"]    = frame(bouga["bitmap"], 8)
bouga["walk1_l"] = frame(bouga["bitmap"], 7)
bouga["walk2_l"] = frame(bouga["bitmap"], 6)
bouga["hit_l"]   = frame(bouga["bitmap"], 5)

logo  = pygame.image.load('../textures/themes/Logo.png')
pygame.display.set_icon(logo)
print("textures loaded")

print("starting game loop...")

running = True

while running:

    # appliquer l'arrière plan
    screen.blit(background, (0, -200))

    # appliquer l'image du joueur
    screen.blit(game.player.image, game.player.rect)

    # appliquer l'ensemble des images de mon projectile 
    game.player.all_projectile.draw(screen)

    # vérifier si le joueur souhaite aller à gauche ou à droite
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True 

            # Détecter si la touche espace est enclenchée pour lancer notre projectile 
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
