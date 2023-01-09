import pygame


class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, group, enemySprite, spriteScale):
        super().__init__(group)
        # setup
        self.image = pygame.image.load(enemySprite).convert()
        size = self.image.get_size()
        size = (size[0] * spriteScale, size[1] * spriteScale)
        self.image = pygame.transform.scale(self.image, size)
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect(center=pos)
        self.rect = self.rect.inflate(-10, -10)


        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 400

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

        self.direction.x = -1

        # print(self.pos.x)

        if self.pos.x < -200:
            self.pos.x = 1400

    def collide(self, playerRect):
        if self.rect.colliderect(playerRect):
            return True

    def update(self, dt):  # funkcja aktualizująca stan obiektu
        self.move(dt)
