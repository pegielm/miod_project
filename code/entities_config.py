SPRITE_PATH = "../sprites/"


class PlayerEntity():
    def __init__(self):
        self.sprite = SPRITE_PATH + "bear.png"
        self.colorkey = (255, 255, 255)
        self.scale = 0.8
        self.speed = 8
        self.rect_inflate = (-40, -40)
        self.jumpHeight = 8000


class Ground():
    def __init__(self):
        self.sprite = SPRITE_PATH + "tlo.png"
        self.colorkey = (255, 255, 255)
        self.scale = 1
        self.speed = 0
        self.rect_inflate = (0, 0)


class Bee():
    def __init__(self):
        self.sprite = SPRITE_PATH + "bee.png"
        self.colorkey = (255, 255, 255)
        self.scale = 0.7
        self.speed = 5
        self.rect_inflate = (-10, -15)


class Honeypot():
    def __init__(self):
        self.sprite = SPRITE_PATH + "honeypot.png"
        self.colorkey = (255, 255, 255)
        self.scale = 0.3
        self.speed = 3
        self.rect_inflate = (0, 0)
