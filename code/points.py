import pygame



class Points(pygame.sprite.Sprite):
    def __init__(self, pos, group,entity):
        super().__init__(group)
        self.image = pygame.image.load(entity.sprite).convert()
        size = self.image.get_size()
        size = (size[0] * entity.scale, size[1] * entity.scale)
        self.image = pygame.transform.scale(self.image, size)

        self.image.set_colorkey(entity.colorkey)
        self.rect = self.image.get_rect(center=pos)
        self.rect = self.rect.inflate(entity.rect_inflate)
        self.font = pygame.font.SysFont('comicsansms', 50)
        self.text = self.font.render("0", True, "black")
        self.clock = pygame.time.Clock()
        self.original_image = self.image.copy()

    def print_score(self, score):
        score = str(score)
        self.background = self.original_image.copy()
        self.text = self.font.render(score, True, "black")
        self.background.blit(self.text, (20, 0))
        self.image = self.background

    def update(self, dt):
        # get current time
        current_time = round(pygame.time.get_ticks() / 1000)
       # self.print_score(current_time)
