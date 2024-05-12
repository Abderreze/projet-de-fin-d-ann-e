"""
Module qui contient les éléments de gestion du menu et de l'écran de fin de partie
"""
import random
import pygame
import textures
from pygame.locals import *

class Menu:
    # Initialisation
    def __init__(self, textures, alphabet):
        char_choices = ["arabe", "bouga", "chevalier", "SUSHI"]
        self.theme_choices = {"arabe": "desert", "bouga": "nature", "chevalier": "stone", "SUSHI": "japan"}
        self.sound = True
        self.sound_pressed = False
        self.textures = textures
        self.draw_elements = []
        self.map = "test_map"
        self.can_go = False
        self.ready = False
        self.perso = None
        self.alphabet = alphabet
    
    # Entrées
    def inputs(self, keys, mouse):
        if keys[K_a]:
            self.perso = "arabe"
        elif keys[K_z]:
            self.perso = "bouga"
        elif keys[K_e]:
            self.perso = "chevalier"
        elif keys[K_r]:
            self.perso = "SUSHI"
        
        if keys[K_1]:
            self.map = "test_map"
        
        if keys[K_s]:
            if not self.sound_pressed:
                if self.sound:
                    self.sound = False
                else:
                    self.sound = True
            self.sound_pressed = True
        else:
            self.sound_pressed = False
        
        if keys[K_p] or mouse[0] or keys[K_RETURN]:
            if self.can_go:
                self.ready = True
        
        if self.perso in ["arabe", "bouga", "chevalier", "SUSHI"]:
            self.theme = self.theme_choices[self.perso]
            self.can_go = True
        else:
            self.can_go = False           
    # Affichage
    def draw_menu(self):
        player_pos = {"arabe": (52, 48), "bouga": (295, 48), "chevalier": (538, 48), "SUSHI": (781, 48)}
        
        self.draw_elements = []
        arabe_frame     = {"pic": self.textures["player_selector"]["arabe"]["off"], "pos": player_pos["arabe"]}
        bouga_frame     = {"pic": self.textures["player_selector"]["bouga"]["off"], "pos": player_pos["bouga"]}
        chevalier_frame = {"pic": self.textures["player_selector"]["chevalier"]["off"], "pos": player_pos["chevalier"]}
        SUSHI_frame     = {"pic": self.textures["player_selector"]["SUSHI"]["off"], "pos": player_pos["SUSHI"]}
        
        if self.perso == "arabe":
            arabe_frame["pic"] = self.textures["player_selector"]["arabe"]["on"]
        elif self.perso == "bouga":
            bouga_frame["pic"] = self.textures["player_selector"]["bouga"]["on"]
        elif self.perso == "chevalier":
            chevalier_frame["pic"] = self.textures["player_selector"]["chevalier"]["on"]
        elif self.perso == "SUSHI":
            SUSHI_frame["pic"] = self.textures["player_selector"]["SUSHI"]["on"]
        
        self.draw_elements.append(arabe_frame)
        self.draw_elements.append(bouga_frame)
        self.draw_elements.append(chevalier_frame)
        self.draw_elements.append(SUSHI_frame)
        
        button_play = {"pic": self.textures["play"]["off"], "pos": (653, 300)}
        if self.can_go:
            button_play["pic"] = self.textures["play"]["on"]
        self.draw_elements.append(button_play)
        
        button_sound = {"pic": self.textures["sound"]["off"], "pos": (480, 320)}
        if self.sound:
            button_sound["pic"] = self.textures["sound"]["on"]
        self.draw_elements.append(button_sound)
        
        sound_text = "Sound [S]:"
        sound_pic = textures.text(sound_text, self.alphabet, 5)
        self.draw_elements.append({"pic": sound_pic, "pos": (50, 350)})
        
    # Fonction principale de fonctionnement
    def update(self, keys, mouse):
        self.inputs(keys, mouse)
        self.draw_menu()

class EndScreen:
    def __init__(self, time, stop_cause, alphabet):
        self.draw_elements = []
        time_played = "Time: " + str(time) + " seconds"
        pic_time = textures.text(time_played, alphabet, 3)
        self.draw_elements.append({"pic": pic_time, "pos": (50, 50)})
        
        if stop_cause == "victory":
            result = "You won!"
        elif stop_cause == "death":
            result = "You died!"
        elif stop_cause == "forfeit":
            result = "You pressed O and forfeited!"
        else:
            result = "The game has stopped due to an unknown reason"
        pic_result = textures.text(result, alphabet, 4)
        self.draw_elements.append({"pic": pic_result, "pos": (50, 150)})
        
        tip = "Press Enter to go back to main menu"
        tip_pic = textures.text(tip, alphabet, 3)
        self.draw_elements.append({"pic": tip_pic, "pos": (50, 250)})