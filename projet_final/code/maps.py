
maps = { # Dico de toutes les maps du jeu. Les maps sont construites avec un cardrillage de carrés
    "map_test": {
        "dimensions": (16, 8), # Taille de la map et limites dont on ne peut pas sortir 
        "blocks": [ # Chaque bloc est un rectangle de plusieurs carrés de large
            {"x": 0,  "y": 1, "w": 4, "h": 1}, # x, y, w, l: respectivement positions x et y du coin haut gauche d'un bloc, et hauteur et longueur des blocs (tout en unités de grille)
            {"x": 4,  "y": 2, "w": 2, "h": 2},
            {"x": 6,  "y": 3, "w": 4, "h": 3},
            {"x": 10, "y": 1, "w": 2, "h": 1},
            {"x": 12, "y": 2, "w": 4, "h": 2},
            {"x": 2,  "y": 5, "w": 3, "h": 1},
            {"x": 11, "y": 5, "w": 2, "h": 1},
        ],
        "entities": [] # Entités qui apparaissent
    }
}

# Conversion des maps simplifiées pour utilisation efficace par le programme
def convert(map):
    '''
    IN: map complète provenant de maps
    OUT: liste contenant la totalité des carrés consitituée à partir des rectangles multiblocs
    '''
    raw = []
    for block in map["blocks"]:
        for x in range(block["w"]):
            for y in range(block["h"]):
                cube = {"x": block["x"]+x, "y": block["y"]-y, "type": "df"} # position x, position y, type de bloc (df pour default)
                raw.append(cube)
    return raw

maps_list = ["map_test"]
for map_name in maps_list:
    maps[map_name]["raw"] = convert(maps[map_name])
