import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group, entity):
        super().__init__(group)
        # setup
        self.image = pygame.image.load(entity.sprite)
        size = self.image.get_size()
        size = (size[0] * entity.scale, size[1] * entity.scale)
        self.image = pygame.transform.scale(self.image, size)
        self.image.set_colorkey(entity.colorkey)
        # self.image.fill('green')
        self.rect = self.image.get_rect(center=pos)
        self.rect = self.rect.inflate(entity.rect_inflate)

        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)  # pozycja gracza
        self.speed = entity.speed
        self.jump = False
        self.jumpHeight = entity.jumpHeight

        self.properties = [pos, entity.speed]

    def import_assets(self):  # tworzenie słownika animacji
        self.animations = {'up': [], 'down': [], 'left': [], 'right': []}

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] or keys[pygame.K_SPACE]:
            self.jump = True

    def move(self, dt):

        # jeśli długość wektora jest większa od 0
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()
        # horizontal movement
        self.pos.x += self.direction.x * self.speed
        self.rect.centerx = self.pos.x
        # vertical movement
        self.pos.y += self.direction.y * self.speed
        self.rect.centery = self.pos.y

        # print(self.pos.y, dt)

        if self.jump is True:
            if self.pos.y == self.properties[0][1]:
                self.direction.y = -1
            elif self.pos.y < self.properties[0][1] - self.jumpHeight:
                self.direction.y = 1
            elif self.pos.y > self.properties[0][1]:
                self.direction.y = 0
                self.jump = False
                self.pos.y = self.properties[0][1]
                self.speed = self.properties[1]

            if self.direction.y == -1:
                self.speed -= 1.6 * dt
            elif self.direction.y == 1:
                self.speed += 1.6 * dt

    def update(self, dt):  # funkcja aktualizująca stan obiektu
        self.input()
        self.move(dt)
