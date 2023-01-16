import pygame
import sys
from settings import *
from level import Level


class Game:  # klasa gry
    def __init__(self):  # konstruktor gry
        pygame.init()
        self.screen = pygame.display.set_mode(
            (SCREEN_WIDTH, SCREEN_HEIGHT),
            pygame.DOUBLEBUF)  # tworzenie okna gry
        pygame.display.set_caption("test_title")
        self.clock = pygame.time.Clock()
        self.level = Level()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == GAMEOVER:
                    self.gameover()

            dt = self.clock.tick(FPS_CAP) / 1000
            self.level.run(dt)  # wywołanie funkcji run z klasy Level
            pygame.display.update()  # aktualizacja ekranu

    def gameover(self):
        image = pygame.image.load("../sprites/gameover.png")
        image = pygame.transform.scale(image, (1280, 720))
        image.set_colorkey((0, 0, 0))
        self.screen.blit(image, (0, 0))
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()


if __name__ == '__main__':  # pętla gry
    game = Game()
    game.run()
