import pygame
import sys
from player import Player
from enemy import Enemy
from ground import Ground
from score import Score
from settings import *


class Level:  # klasa poziomu
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

        self.all_sprites = pygame.sprite.Group()

        self.setup()

    def setup(self):
        self.ground = Ground((640, 620), self.all_sprites)
        self.player = Player((160, 480), self.all_sprites)
        self.bee = Enemy((1400, 480), self.all_sprites, "../sprites/bee.png", 0.7)
        self.score = Score((SCREEN_WIDTH / 2, 50), self.all_sprites)

    def run(self, dt):  # funkcja odpowiadająca za działanie poziomu
        self.display_surface.fill('blue')
        self.all_sprites.draw(self.display_surface)
        if self.bee.collide(self.player.rect):
            print("COLLISION")
            self.gameover()
        self.all_sprites.update(dt)

    def gameover(self):
        while True:
            image = pygame.image.load("../sprites/gameover.png")
            image = pygame.transform.scale(image, (1280, 720))
            image.set_colorkey((0, 0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.display_surface.blit(image, (0, 0))
            pygame.display.update()
