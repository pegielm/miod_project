import pygame
from settings import *
class Score(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.font = pygame.font.SysFont('comicsansms',50)
        self.image = self.font.render(str(000), True,"pink")
        self.rect = self.image.get_rect(center=pos)
        self.clock = pygame.time.Clock()

    def print_score(self,score):
        score = str(score)
        self.image = self.font.render(score, True, "pink")
    def update(self,dt):
        #get current time
        current_time = round(pygame.time.get_ticks()/1000)
        self.print_score(current_time)








