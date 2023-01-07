import pygame


class Ground(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        # setup
        self.image = pygame.image.load("../sprites/tlo.png")
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect(center=pos)
        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
