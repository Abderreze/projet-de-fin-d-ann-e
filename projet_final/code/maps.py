'''
Module qui contient toutes les maps prédéfinies du jeu en un format facilement compréhensible, et les convertit en un format plus adapté au programme pour de bonnes performances
'''
import pygame

# Import des textures de blocs
import textures
tiles_textures = textures.tiles

maps = { # Dico de toutes les maps du jeu. Les maps sont construites avec un cardrillage de carrés
    "test_map": {
        "dimensions": (48, 16), # Taille de la map et limites dont on ne peut pas sortir 
        "blocks": [ # Chaque bloc est un rectangle de plusieurs carrés de large
            {"x": 0,  "y": 1,  "w": 6,  "h": 1}, # x, y, w, l: respectivement positions x et y du coin haut gauche d'un bloc, et hauteur et longueur des blocs (tout en unités de grille)
            {"x": 6,  "y": 2,  "w": 4,  "h": 2},
            {"x": 10, "y": 3,  "w": 6,  "h": 3},
            {"x": 16, "y": 4,  "w": 5,  "h": 4},
            {"x": 21, "y": 1,  "w": 12, "h": 1},
            {"x": 23, "y": 5,  "w": 7,  "h": 2},
            {"x": 33, "y": 2,  "w": 2,  "h": 2},
            {"x": 35, "y": 3,  "w": 3,  "h": 3},
            {"x": 38, "y": 4,  "w": 4,  "h": 4},
            {"x": 42, "y": 1,  "w": 3,  "h": 1},
            {"x": 45, "y": 4,  "w": 3,  "h": 4},
        ],
        "entities": [], # Entités qui apparaissent
        "spawn": (5, 5), # Coordonnées du coin haut gauche du carré où le joueur apparaît
    }
}

# Fonction qui construit l'image de la map avec les tiles
def convert(map, theme):
    '''
    USE: convertit les maps simplifiées de maps en surfaces pygame pour affichage
    IN: map complète provenant de maps
    OUT: image de la map complète en fonction du thème
    '''
    global tiles_textures
    themes_tiles = {
        "nature": {"top": "dirt_grass", "df": "dirt"},
        "desert": {"top": "sand_path", "df": "sand"},
        "japan": {"top": "dirt_japan", "df": "dirt"},
        "stone": {"top": "stone_path", "df": "dirt"}
    }
    assert themes_tiles[theme] != None, f"theme '{theme}' is not defined!"
    
    all_tiles = []
    for block in map["blocks"]:
        for x in range(block["w"]):
            for y in range(block["h"]):
                tile = {"x": block["x"]+x, "y": block["y"]-y, "type": "df"} # position x, position y, type de bloc (df pour default)
                if y == 0:
                    tile["type"] = "top"
                all_tiles.append(tile)
    all_tiles.reverse()
    map_picture = pygame.Surface((64*map["dimensions"][0]+1, 64*map["dimensions"][1]+1), pygame.SRCALPHA)
    map_picture.fill((0, 0, 0, 0))
    for map_tile in all_tiles:
        tile_texture = tiles_textures[themes_tiles[theme][map_tile["type"]]]
        tile_x = map_tile["x"] * 64
        tile_y = (map["dimensions"][1] - map_tile["y"]) * 64
        tile_position = (tile_x, tile_y)
        map_picture.blit(tile_texture, tile_position)
    return map_picture

# Conversion de toutes les maps simplifiées en images
maps_list = ["test_map"]
themes_array = ["nature", "desert", "japan", "stone"]

for map_name in maps_list:
    maps[map_name]["raw"] = {}
    for theme in themes_array:
        maps[map_name]["raw"][theme] = convert(maps[map_name], theme)