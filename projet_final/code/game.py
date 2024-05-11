'''
Module qui contient toutes les classes et fonctions qui assurent le fonctionnement d'une partie
'''

import pygame
import settings
from pygame.locals import *

# Import des settings
screen_width = settings.screen_width
screen_heigth = settings.screen_heigth
run_frame_speed = 0.03

class Player:
    # initialisation
    def __init__(self, textures, spawn):
        self.coordinates = spawn
        self.textures = textures
        self.current_frame = self.textures["df_r"]
        self.hitbox = (24, 92)
        self.vertical_speed = 0
        self.falling = False

class Actions:
    # initialisation
    def __init__(self):
        self.moving = False
        self.facing = "r"
        self.hit = False
        self.hold_hit = False
        self.actual_hit = False
        self.jump = False

class Map:
    def __init__(self, map, theme):
        self.picture = map["raw"][theme]
        self.hitboxes = []
        for block in map["blocks"]:
            hitbox = {
                "left": 64 * block["x"],
                "right": 64 * (block["x"] + block["w"]),
                "top": 64 * block["y"],
                "bottom": 64 * (block["y"] - block["h"])
            }
            self.hitboxes.append(hitbox)
        dim_x = 64 * map["dimensions"][0]
        dim_y = 64 * map["dimensions"][1]
        self.dimensions = (dim_x, dim_y)

class Game:
    # initialisation
    def __init__(self, textures, player, map_theme, map):
        spawn = [64 * map["spawn"][0] + 32, 64 * map["spawn"][1] - 64]
        self.player = Player(textures.player[player], spawn)
        self.map = Map(map, map_theme)
        self.actions = Actions()
        self.hold_hit = False
        self.running = {"frames": ["walk1_", "df_", "walk2_", "df_"], "adv": 0}
        self.draw_pos = {"map": (0, 0), "player": (0, 0)}
    
    def update_inputs(self, keys, mouse):
        '''
        Récupère les entrées clavier et souris pour qu'elles soient accessibles dans l'objet Game
        '''
        # mouvements horizontaux
        if keys[K_RIGHT]:
            self.actions.facing = "r"
            self.actions.moving = True
        elif keys[K_LEFT]:
            self.actions.facing = "l"
            self.actions.moving = True
        else:
            self.actions.moving = False
        
        # souris (attaque)
        if mouse[0]:
            self.actions.hit = True
            if self.actions.hold_hit:
                self.actions.actual_hit = False
            else:
                self.actions.actual_hit = True
            self.actions.hold_hit = True
            self.actions.moving = False
        else:
            self.actions.hit = False
            self.actions.hold_hit = False
            self.actions.actual_hit = False
            
        if keys[K_UP]:
            self.actions.jump = True
        else:
            self.actions.jump = False
            
    def hit(self):
        falling = True
        for hitbox in self.map.hitboxes:
            # test pour savoir si le joueur touche le bloc
            hit_test_a = self.player.coordinates[0] + self.player.hitbox[0] > hitbox["left"]
            hit_test_b = self.player.coordinates[0] - self.player.hitbox[0] < hitbox["right"]
            hit_test_c = self.player.coordinates[1] + self.player.hitbox[1] > hitbox["bottom"]
            hit_test_d = self.player.coordinates[1] <= hitbox["top"]
            # tests pour savoir où déplacer le joueur s'il touche le bloc
            if hit_test_a and hit_test_b and hit_test_c and hit_test_d:
                if self.player.coordinates[1] > hitbox["top"] - 16:
                    self.player.coordinates[1] = hitbox["top"]
                    falling = False
                    self.player.vertical_speed = 0
                elif self.player.coordinates[0] + self.player.hitbox[0] < hitbox["left"] + 16:
                    self.player.coordinates[0] = hitbox["left"] - self.player.hitbox[0]
                elif self.player.coordinates[0] - self.player.hitbox[0] > hitbox["right"] - 16:
                    self.player.coordinates[0] = hitbox["right"] + self.player.hitbox[0]
                elif self.player.coordinates[1] + self.player.hitbox[1] < hitbox["bottom"] + 16:
                    self.player.coordinates[1] = hitbox["bottom"] - self.player.hitbox[1]
                    self.player.vertical_speed = 0
                else:
                    self.player.coordinates[1] = hitbox["top"]
                    falling = False
                    self.player.vertical_speed = 0
        if falling: 
            self.player.falling = True
        else: self.player.falling = False
    
    def move(self):
        # déplacements horizontaux
        speed = 0.5
        if self.actions.moving:
            if self.actions.facing == "r":
                self.player.coordinates[0] += speed
            else:
                self.player.coordinates[0] -= speed
        
        # gravité
        if self.player.falling:
            self.player.vertical_speed -= 0.01
        if self.player.vertical_speed < -1.5:
                self.player.vertical_speed = -1.5
        if self.actions.jump and not self.player.falling:
            self.player.vertical_speed = 1.5
        self.player.coordinates[1] += self.player.vertical_speed
        
        # limites de la map
        if self.player.coordinates[0] < self.player.hitbox[0]:
            self.player.coordinates[0] = self.player.hitbox[0]
            self.actions.moving = False
        elif self.player.coordinates[0] > self.map.dimensions[0] - self.player.hitbox[0]:
            self.player.coordinates[0] = self.map.dimensions[0] - self.player.hitbox[0]
            self.actions.moving = False
        if self.player.coordinates[1] < 0:
            self.player.coordinates[1] = 0
        elif self.player.coordinates[1] > self.map.dimensions[1] - self.player.hitbox[1]:
            self.player.coordinates[1] = self.map.dimensions[1] - self.player.hitbox[1]
    
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
    
    def update_drawpos(self):
        map_x = 0.5 * screen_width - self.player.coordinates[0]
        map_y = 0.5 * screen_heigth + self.player.coordinates[1] - self.map.dimensions[1]
        
        if map_x > 0:
            map_x = 0
        elif map_x < screen_width - self.map.dimensions[0]:
            map_x = screen_width - self.map.dimensions[0]
        
        if map_y > 0:
            map_y = 0
        elif map_y < screen_heigth - self.map.dimensions[1]:
            map_y = screen_heigth - self.map.dimensions[1]
        
        self.draw_pos["map"] = (map_x, map_y)
        
        player_x = map_x + self.player.coordinates[0] - 64
        player_y = map_y + self.map.dimensions[1] - self.player.coordinates[1] - 128
        
        self.draw_pos["player"] = (player_x, player_y)
    
    def update(self, keys, mouse):
        self.update_inputs(keys, mouse)
        self.hit()
        self.move()
        self.update_frame()
        self.update_drawpos()