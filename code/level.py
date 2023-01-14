import pygame
import sys
from player import Player
from entity import Entity
from score import Score
from entities_config import *
from settings import *


class Level:  # klasa poziomu
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

        self.all_sprites = pygame.sprite.Group()

        self.setup()

    def setup(self):
        self.ground = Entity((640, 620), self.all_sprites, Ground())
        self.player = Player((160, 480), self.all_sprites, PlayerEntity())
        self.bee = Entity((1400, 480), self.all_sprites, Bee())
        self.score = Score((SCREEN_WIDTH / 2, 50), self.all_sprites)

    def run(self, dt):  # funkcja odpowiadająca za działanie poziomu
        self.display_surface.fill('blue')
        self.all_sprites.draw(self.display_surface)
        self.all_sprites.update(dt)
        if self.bee.collide(self.player.rect):
            noneDict = {None: None}
            gameoverEvent = pygame.event.Event(GAMEOVER, noneDict)
            pygame.event.post(gameoverEvent)
