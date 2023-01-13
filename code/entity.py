import pygame


class Entity(pygame.sprite.Sprite):
    def __init__(self, pos, group, entity):
        super().__init__(group)
        # setup
        self.image = pygame.image.load(entity.sprite).convert()
        size = self.image.get_size()
        size = (size[0] * entity.scale, size[1] * entity.scale)
        self.image = pygame.transform.scale(self.image, size)
        self.image.set_colorkey(entity.colorkey)
        self.rect = self.image.get_rect(center=pos)
        self.rect = self.rect.inflate(entity.rect_inflate)

        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = entity.speed

    def import_assets(self):
        # tworzenie słownika animacji
        self.animations = {'up': [], 'down': [], 'left': [], 'right': []}

    def move(self, dt):

        # jeśli długość wektora jest większa od 0
        if self.direction.magnitude() > 0:
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
