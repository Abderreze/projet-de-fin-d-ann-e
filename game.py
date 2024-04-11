import pygame 
pygame.init()

#génération de la fenêtre 
screen = pygame.display.set_mode((1080, 720))
pygame.display.set_caption("PLATFORMOUUUUUR")

# importe le fond écran
running = True 

# condition tkt 
while running:
    # on applique le fond d'écran
    screen.fill((94, 242, 255))

    # met à jour l'écran
    pygame.display.flip()
    #si le joueur quitte la fenêtre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("f")
