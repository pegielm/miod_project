import pygame
from player import Player
from entity import Entity
from score import Score
from random import randint
from entities_config import *
from settings import *


class Level:  # klasa poziomu
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

        self.all_sprites = pygame.sprite.Group()

        self.setup()

    def setup(self):
        self.ground = Entity((640, 620), self.all_sprites, Ground())
        self.score = Score((SCREEN_WIDTH / 2, 50), self.all_sprites)
        self.player = Player((160, 480), self.all_sprites, PlayerEntity())
        self.bee = Entity((1400, 480), self.all_sprites, Bee())
        self.honeypot = Entity((1400, 330),
                               self.all_sprites, Honeypot())
        self.honeypotCounter = 0
        self.gameoverEvent = pygame.event.Event(GAMEOVER, NONEDICT)

    def run(self, dt):  # funkcja odpowiadająca za działanie poziomu
        self.display_surface.fill('blue')
        diceroll = randint(1, FPS_CAP * 10)
        # print(diceroll)
        if diceroll == 1 or diceroll == 3:
            self.bee = Entity((1400, 480), self.all_sprites, Bee())
        elif diceroll == 2:
            self.honeypot = Entity((1400, 330),
                                   self.all_sprites, Honeypot())
        self.all_sprites.draw(self.display_surface)
        self.all_sprites.update(dt)

        if self.bee.collide(self.player.rect):
            pygame.event.post(self.gameoverEvent)
        if self.honeypot.collide(self.player.rect):
            self.honeypotCounter += 1
