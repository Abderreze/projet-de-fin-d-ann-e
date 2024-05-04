'''
Module qui contient toutes les classes et fonctions qui assurent le fonctionnement d'une partie
'''

import pygame
import settings
from pygame.locals import *

# Import des settings
run_frame_speed = 0.01 * settings.run_frame_speed

class Player:
    # initialisation
    def __init__(self, textures, coordinates=(32, 64)):
        self.coordinates = coordinates
        self.textures = textures
        self.current_frame = self.textures["df_r"]

class Actions:
    # initialisation
    def __init__(self):
        self.moving = False
        self.facing = "r"
        self.hit = False
        self.hold_hit = False
        self.actual_hit = False

class Map:
    def __init__(self, map, theme):
        self.picture = map["raw"][theme]
        self.hitboxes = map["blocks"]
        self.dimensions = map["dimensions"]

class Game:
    # initialisation
    def __init__(self, textures, player, map_theme, map):
        self.player = Player(textures.player[player])
        self.map = Map(map, map_theme)
        self.player.coordinates = (map["spawn"][0]+32, map["spawn"][1]-64)
        self.actions = Actions()
        self.hold_hit = False
        self.running = {"frames": ["walk1_", "df_", "walk2_", "df_"], "adv": 0}
    def update_inputs(self, keys, mouse):
        '''
        Récupère les entrées clavier et souris pour qu'elles soient accessibles dans l'objet Game
        '''
        if keys[K_RIGHT]:
            self.actions.facing = "r"
            self.actions.moving = True
        elif keys[K_LEFT]:
            self.actions.facing = "l"
            self.actions.moving = True
        else:
            self.actions.moving = False
            
        if mouse[0]:
            self.actions.hit = True
            if self.actions.hold_hit:
                self.actions.actual_hit = False
            else:
                self.actions.actual_hit = True
            self.actions.hold_hit = True
        else:
            self.actions.hit = False
            self.actions.hold_hit = False
            self.actions.actual_hit = False
            
    
    def update_frame(self):
        '''
        Choisit le frame adapté pour le joueur
        '''
        if self.actions.hit:
            self.running["adv"] = 0
            self.player.current_frame = self.player.textures["hit_"+self.actions.facing]
        elif self.actions.moving:
            self.running["adv"] += run_frame_speed
            self.running["adv"] %= 4
            self.player.current_frame = self.player.textures[self.running["frames"][int(self.running["adv"])]+self.actions.facing]
        else:
            self.running["adv"] = 0
            self.player.current_frame = self.player.textures["df_"+self.actions.facing]