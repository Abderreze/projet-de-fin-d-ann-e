import pygame
from player import Player
# classe du jeu 
class Game:
    def __init__(self):
        #chargement du joueur
        self.player = Player()
        self.pressed = {}
