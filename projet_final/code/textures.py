'''
Module qui gère l'import de toutes les textures .png du jeu, et effectue toutes les opérations de modification au démarrage pour l'utilisation efficace dans le jeu
'''
import pygame

# Fonction pour facilement récupérer des carrés d'une image
def frame(pic, x, frame_width=128):
    '''
    IN: pic: image contenant plusieurs frames dont on veut extraire un seul.
        x: numéro du frame qu'on veut, les frames sont en ligne à intervales réguliers sur l'image pic
        frame_width: largeur d'un frame, défaut sur 64
    OUT: le frame extrait
    '''
    frame = pic.subsurface(pygame.Rect( frame_width * (x - 1), 0, frame_width, pic.get_height() ))
    return frame

# Fonction pour facilement changer la taille d'une image proportionnellement
def resize(pic, scale_factor):
    '''
    IN: pic: image de départ
        scale_factor: facteur d'agrandissement
    OUT: image agrandie ou rapetissée
    '''
    resized  = pygame.transform.scale(pic, (pic.get_width() * scale_factor, pic.get_height() * scale_factor))
    return resized

# Import des textures du joueur
characters = ["bouga", "chevalier", "arabe", "SUSHI"]
player = {}
for character in characters:
    player[character] = {}
    player[character]["bitmap"]  = pygame.image.load('textures/player/perso_'+character+'_run.png')
    player[character]["bitmap"]  = resize(player[character]["bitmap"], 4)
    # découpage de l'image bouga en plusieurs bouga 
    player[character]["df_r"]    = frame(player[character]["bitmap"], 1)
    player[character]["walk1_r"] = frame(player[character]["bitmap"], 2)
    player[character]["walk2_r"] = frame(player[character]["bitmap"], 3)
    player[character]["hit_r"]   = frame(player[character]["bitmap"], 4)
    player[character]["df_l"]    = frame(player[character]["bitmap"], 8)
    player[character]["walk1_l"] = frame(player[character]["bitmap"], 7)
    player[character]["walk2_l"] = frame(player[character]["bitmap"], 6)
    player[character]["hit_l"]   = frame(player[character]["bitmap"], 5)

# Import des textures de blocs
tiles = {}
tiles["dirt"]        = pygame.image.load('textures/tiles/Dirt.png')
tiles["dirt_grass"]  = pygame.image.load('textures/tiles/Dirt_grass.png')
tiles["dirt_japan"]  = pygame.image.load('textures/tiles/Dirt_japan.png')
tiles["stone_path"]  = pygame.image.load('textures/tiles/Stone_path.png')
tiles["sand"]        = pygame.image.load('textures/tiles/Sand.png')
tiles["sand_path"]   = pygame.image.load('textures/tiles/Sand_path.png')

tiles["dirt"]        = resize(tiles["dirt"], 4)
tiles["dirt_grass"]  = resize(tiles["dirt_grass"], 4)
tiles["dirt_japan"]  = resize(tiles["dirt_japan"], 4)
tiles["stone_path"]  = resize(tiles["stone_path"], 4)
tiles["sand"]        = resize(tiles["sand"], 4)
tiles["sand_path"]   = resize(tiles["sand_path"], 4)

# Import des textures du menu

# bouton play
button_play = pygame.image.load("textures/misc/Play.png")
button_play = resize(button_play, 5)
width_button_play, height_button_play = button_play.get_size()
button_play_on = button_play.subsurface((0, 0, width_button_play // 2, height_button_play))
button_play_off = button_play.subsurface((width_button_play // 2, 0, width_button_play // 2, height_button_play))
button_play_on_rect = button_play_on.get_rect()
button_play_on_rect = button_play_on_rect.move(820, 400)

# bouton son
button_sound = pygame.image.load("textures/misc/Bouton.png")
button_sound = resize(button_sound, 4)
button_sound_on = frame(button_sound, 2, 128)
button_sound_off = frame(button_sound, 1, 128)

# sélecteur de personnages
arabe_frame = pygame.image.load("textures/misc/arabe_frame.png")
arabe_frame = resize(arabe_frame, 4)
arabe_on = frame(arabe_frame, 1, 192)
arabe_off = frame(arabe_frame, 2, 192)

bouga_frame = pygame.image.load("textures/misc/bouga_frame.png")
bouga_frame = resize(bouga_frame, 4)
bouga_on = frame(bouga_frame, 1, 192)
bouga_off = frame(bouga_frame, 2, 192)

chevalier_frame = pygame.image.load("textures/misc/chevalier_frame.png")
chevalier_frame = resize(chevalier_frame, 4)
chevalier_on = frame(chevalier_frame, 1, 192)
chevalier_off = frame(chevalier_frame, 2, 192)

SUSHI_frame = pygame.image.load("textures/misc/SUSHI_frame.png")
SUSHI_frame = resize(SUSHI_frame, 4)
SUSHI_on = frame(SUSHI_frame, 1, 192)
SUSHI_off = frame(SUSHI_frame, 2, 192)

buttons = {
    "play": {"on": button_play_on, "off": button_play_off},
    "sound": {"on": button_sound_on, "off": button_sound_off},
    "player_selector": {
        "arabe": {"on": arabe_on, "off": arabe_off},
        "bouga": {"on": bouga_on, "off": bouga_off},
        "chevalier": {"on": chevalier_on, "off": chevalier_off},
        "SUSHI": {"on": SUSHI_on, "off": SUSHI_off}
    }
}

# Import du logo
logo = pygame.image.load('textures/misc/Logo.png')

# Import de l'alphabet
alphabet_raw = pygame.image.load("textures/misc/alphabet.png")
alphabet = {}
i = 1
for letter in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!?,.:/' ":
    alphabet[letter] = frame(alphabet_raw, i, 8)
    i += 1

# Fonction de génération de texte
def text(text, alphabet, scale=1):
    picture = pygame.Surface((8 * len(text), 16), pygame.SRCALPHA)
    picture.fill((0, 0, 0, 0))
    i = 0
    for letter in text:
        if alphabet[letter]:
            picture.blit(alphabet[letter], (8*i, 0))
        i += 1
    picture  = pygame.transform.scale(picture, (picture.get_width() * scale, picture.get_height() * scale))
    return picture