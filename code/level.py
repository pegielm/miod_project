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
        self.ground = Entity((1280, 620), self.all_sprites, Ground())
        self.score = Score()
        self.points = Score()
        self.player = Player((160, 480), self.all_sprites, PlayerEntity())
        self.bees = []
        self.bees.append(Entity((1400, 480), self.all_sprites, Bee()))
        self.honeypots = []
        self.honeypots.append(Entity((1400, 330),
                                     self.all_sprites, Honeypot()))
        self.honeypotCounter = 0
        self.gameoverEvent = pygame.event.Event(GAMEOVER, NONEDICT)
        print(self.ground.speed)

    def run(self, dt):  # funkcja odpowiadająca za działanie poziomu
        self.display_surface.fill('blue')

        diceroll = randint(1, FPS_CAP * 10)
        if diceroll == 1 or diceroll == 123:
            self.bees.append(Entity((1400, 480), self.all_sprites, Bee()))
        elif diceroll == 2:
            self.honeypots.append(Entity((1400, 330),
                                         self.all_sprites, Honeypot()))

        if self.ground.pos.x <= 0:
            self.ground.pos.x = 1280 * SCALE

        self.all_sprites.draw(self.display_surface)
        self.score.update(dt)
        self.display_surface.blit(self.score.image, (50 * SCALE, 25 * SCALE))
        self.display_surface.blit(self.points.honeypotsImage, (SCREEN_WIDTH - 150 * SCALE, 25 * SCALE))
        self.display_surface.blit(self.points.sprite, (SCREEN_WIDTH - 210 * SCALE, 40 * SCALE))
        self.all_sprites.update(dt)

        for bee in self.bees:
            if bee.collide(self.player.rect):
                pygame.event.post(self.gameoverEvent)
            if bee.pos.x < -200:
                self.bees.pop(0)
        for honeypot in self.honeypots:
            if honeypot.collide(self.player.rect):
                self.honeypotCounter += 1
                self.ground.speed += self.honeypotCounter * 10
                print(self.ground.speed)
                self.points.print_score(self.honeypotCounter)
                honeypot.pos.x = -180
            if honeypot.pos.x < -200:
                self.honeypots.pop(0)
