import pygame
from settings import *
from player import Player
class Level: #klasa poziomu
    def __init__(self):
        self.display_surface = pygame.display.get_surface() #pobranie powierzchni ekranu


        self.all_sprites = pygame.sprite.Group() #

        self.setup()
    def setup(self):
        self.player = Player((640,360),self.all_sprites)

    def run(self,dt): #funkcja odpowiadająca za działanie poziomu
        self.display_surface.fill('blue')
        self.all_sprites.draw(self.display_surface)
        self.all_sprites.update(dt)
