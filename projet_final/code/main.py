import pygame
import settings
import time
from pygame.locals import *
'''
Fichier principal du jeu
'''
pygame.init()

# génération de la fenêtre
print("loading window...")
screen_width = settings.screen_width
screen_heigth = settings.screen_heigth
screen = pygame.display.set_mode((screen_width, screen_heigth))
pygame.display.set_caption("BASIROUUUUUUU")

# import des textures
print("loading textures...")
import textures
logo = textures.logo
buttons_textures = textures.buttons
player_textures = textures.player
pygame.display.set_icon(logo)

# import des maps
print("loading maps...")
import maps

# import du code du menu
print("loading menu algorithms...")
import menu_and_end

# import du code de partie
print("loading game algorithms...")
import game

# fonctions d'affichage
print("loading draw functions...")
def drawMenu(menu):
    global screen
    background = (94, 242, 255)
    screen.fill(background)
    for element in menu.draw_elements:
        screen.blit(element["pic"], element["pos"])
    pygame.display.flip()
def drawGame(game):
    global screen
    background = game.background
    screen.blit(background, (0, 0))
    screen.blit(game.map.picture, game.draw_pos["map"])
    screen.blit(game.player.current_frame, game.draw_pos["player"])
    pygame.display.flip() # mise à jour de l'écran
    
# Musique
print("Loading soundtracks...")
pygame.mixer.music.load("textures/misc/sound.mp3")
pygame.mixer.music.play(loops=-1)

print("starting main loop...")
running = True
while running:
    print("opened menu")
    current_menu = menu_and_end.Menu(buttons_textures, textures.alphabet)
    while not current_menu.ready:
        for event in pygame.event.get(): # fermeture de fenêtre
            if event.type == pygame.QUIT:
                running = False
                ready = True
                pygame.quit()
                print("Closed window")
        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pressed()
        current_menu.update(keys, mouse)
        if current_menu.sound:
            pygame.mixer.music.unpause()
        else:
            pygame.mixer.music.pause()
        drawMenu(current_menu)
        
    print("starting new game...")
    start_time = time.time()
    current_game = game.Game(textures, current_menu.perso, current_menu.theme, maps.maps["test_map"]) 
    print("new game started successfully!")
    # boucle de jeu
    while current_game.player.alive and not current_game.won and running:
        for event in pygame.event.get(): # fermeture de fenêtre
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                print("Closed window")
        
        # récupération des entrées clavier
        keys = pygame.key.get_pressed()
        mouse = pygame.mouse.get_pressed()
        current_game.update(keys, mouse)
        drawGame(current_game)
    end_time = time.time()
    time_played = end_time - start_time
    time_played = int(time_played * 1000) / 1000
    print("Time played: ", time_played)
    if current_game.won:
        print("Success!")
        cause = "victory"
    elif current_game.actions.suicide:
        print("Forfeited!")
        cause = "forfeit"
    elif not current_game.player.alive:
        print("Died!")
        cause = "death"
    else:
        print("Stopped game due to an unknow reason")
        cause = "unknown"
    print("game ended, opening end screen")
    go_menu = False
    current_end_screen = menu_and_end.EndScreen(time_played, cause, textures.alphabet)
    while not go_menu:
        for event in pygame.event.get(): # fermeture de fenêtre
            if event.type == pygame.QUIT:
                running = False
                go_menu = True
                pygame.quit()
                print("Closed window")
        keys = pygame.key.get_pressed()
        if keys[K_RETURN]:
            go_menu = True
        drawMenu(current_end_screen)