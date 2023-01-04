import pygame


class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, group, enemySprite):
        super().__init__(group)
        # setup
        self.image = pygame.image.load(enemySprite).convert()
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect(center=pos)

        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 200

    def import_assets(self):
        self.animations = {'up': [], 'down': [], 'left': [], 'right': []}  # tworzenie słownika animacji

    def move(self, dt):

        if self.direction.magnitude() > 0:  # jeśli długość wektora jest większa od 0
            self.direction = self.direction.normalize()
        # horizontal movement
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.centerx = self.pos.x
        # vertical movement
        self.pos.y += self.direction.y * self.speed * dt
        self.rect.centery = self.pos.y

    def update(self, dt):  # funkcja aktualizująca stan obiektu
        self.input()
        self.move(dt)
