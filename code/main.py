import pygame
import sys
from settings import *
from level import Level


class Game:  # klasa gry
    def __init__(self):  # konstruktor gry
        pygame.init()
        self.screen = pygame.display.set_mode(
            (SCREEN_WIDTH, SCREEN_HEIGHT))  # tworzenie okna gry
        pygame.display.set_caption("test_title")
        self.clock = pygame.time.Clock()
        self.level = Level()
        self.fps = 120
        self.counter = 15

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            # czas od ostatniego wywołania funkcji
            self.new_fps = self.clock.get_fps()
            if self.new_fps < self.fps and self.counter <= 0:
                self.fps = self.new_fps
            elif self.counter > 0:
                self.counter -= 1
            print(self.fps)
            dt = self.clock.tick(FPS_CAP) / 1000
            self.level.run(dt)  # wywołanie funkcji run z klasy Level
            pygame.display.update()  # aktualizacja ekranu


if __name__ == '__main__':  # pętla gry
    game = Game()
    game.run()
