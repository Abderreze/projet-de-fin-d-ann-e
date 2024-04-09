import pygame 
pygame.init()

#génération de la fenêtre 
screen = pygame.display.set_mode((1080, 720))
pygame.display.set_caption("PLATFORMOUUUUUR")

# importe le fond écran
background = pygame.image.load("Tiles/Tiles/Assets/pxfuel.jpg")
running = True 

# condition tkt 
while running:
    # on applique le fond d'écran
    screen.blit(background, (0, 0))

    # met à jour l'écran
    pygame.display.flip()
    #si le joueur quitte la fenêtre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("f")

