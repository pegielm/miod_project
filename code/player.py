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

        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)  # pozycja gracza
        self.speed = 1200
        self.status = "stand"

    def import_assets(self):
        self.animations = {'up': [], 'down': [], 'left': [], 'right': []}  # tworzenie słownika animacji

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] or keys[pygame.K_SPACE]:
            # self.direction.y = -1
            if self.status is "stand":
                self.status = "jump"
        # else:
        #     self.direction.y = 0

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

            self.status = "fall"
        if self.rect.bottom > 538 and self.status is "fall":
            self.status = "stand"

        if self.status is "stand":
            self.direction.y = 0
        if self.status is "jump":
            self.direction.y = -1
        if self.status is "fall":
            self.direction.y = 1


        print(self.speed, self.direction.y,self.status,dt,self.rect.bottom)

    def update(self, dt):  # funkcja aktualizująca stan obiektu
        self.input()
        self.move(dt)
