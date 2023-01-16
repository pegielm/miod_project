import pygame
from player import Player
from entity import Entity
from score import Score
from random import randint
from entities_config import *
from settings import *
from points import Points


class Level:  # klasa poziomu
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

        self.all_sprites = pygame.sprite.Group()

        self.setup()

    def setup(self):
        self.ground = Entity((640, 620), self.all_sprites, Ground())
        self.score = Score((100, 50), self.all_sprites)
        self.points = Points((SCREEN_WIDTH -100 , 50), self.all_sprites , PointsEntity())
        self.player = Player((160, 480), self.all_sprites, PlayerEntity())
        self.bees = []
        self.bees.append(Entity((1400, 480), self.all_sprites, Bee()))
        self.honeypots = []
        self.honeypots.append(Entity((1400, 330),
                                    self.all_sprites, Honeypot()))
        self.honeypotCounter = 0
        self.gameoverEvent = pygame.event.Event(GAMEOVER, NONEDICT)

    def run(self, dt):  # funkcja odpowiadająca za działanie poziomu
        self.display_surface.fill('blue')
        diceroll = randint(1, FPS_CAP * 10)
        # print(diceroll)
        if diceroll == 1 or diceroll == 100:
            self.bees.append(Entity((1400, 480), self.all_sprites, Bee()))
        elif diceroll == 2:
            self.honeypots.append(Entity((1400, 330),
                                   self.all_sprites, Honeypot()))
        self.all_sprites.draw(self.display_surface)
        self.all_sprites.update(dt)

        print(self.honeypots)
        for bee in self.bees:
            if bee.collide(self.player.rect):
                pygame.event.post(self.gameoverEvent)
            if bee.pos.x < -200:
                self.bees.pop(0)
        for honeypot in self.honeypots:
            if honeypot.collide(self.player.rect):
                self.honeypotCounter += 1
                self.points.print_score(self.honeypotCounter)
                honeypot.pos.x = -180
            if honeypot.pos.x < -200:
                self.honeypots.pop(0)
