import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        # setup
        self.image = pygame.image.load("../sprites/bear.png")
        size = self.image.get_size()
        size = (size[0] * 0.8, size[1] * 0.8)
        self.image = pygame.transform.scale(self.image, size)
        self.image.set_colorkey((255, 255, 255))
        # self.image.fill('green')
        self.rect = self.image.get_rect(center=pos)
        self.rect = self.rect.inflate(-40, -40)

        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)  # pozycja gracza
        self.speed = 900
        self.jump = False

    def import_assets(self):
        self.animations = {'up': [], 'down': [], 'left': [], 'right': []}  # tworzenie słownika animacji

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] or keys[pygame.K_SPACE]:
            self.jump = True

    def move(self, dt):

        if self.direction.magnitude() > 0:  # jeśli długość wektora jest większa od 0
            self.direction = self.direction.normalize()
        # horizontal movement
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.centerx = self.pos.x
        # vertical movement
        self.pos.y += self.direction.y * self.speed * dt
        self.rect.centery = self.pos.y
        # jump
        if self.rect.bottom < 238 and self.status is "jump":

        if self.jump is True and self.direction.y == -1:
            self.speed -= 1300 * dt
        elif self.jump is True and self.direction.y == 1:
            self.speed += 1300 * dt
        if self.jump is True and self.pos.y == 480:
            self.direction.y = -1
        if self.pos.y < 180:
            self.direction.y = 1
        elif self.pos.y > 480 and self.jump is True:
            self.direction.y = 0
            self.jump = False
            self.pos.y = 480
            self.speed = 900

    def update(self, dt):  # funkcja aktualizująca stan obiektu
        self.input()
        self.move(dt)
