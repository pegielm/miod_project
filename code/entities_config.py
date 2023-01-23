from settings import *


class PlayerEntity():
    def __init__(self):
        self.sprite = SPRITE_PATH + "bear.png"
        self.colorkey = (255, 255, 255)
        self.scale = 0.8 * SCALE
        self.speed = 8 * SCALE
        self.rect_inflate = (-40 * SCALE, -40 * SCALE)
        self.jumpHeight = 8000


class Ground():
    def __init__(self):
        self.sprite = SPRITE_PATH + "tlo.png"
        self.colorkey = (255, 255, 255)
        self.scale = 1 * SCALE
        self.speed = 3 * SCALE
        self.rect_inflate = (0 * SCALE, 0 * SCALE)


class Bee():
    def __init__(self):
        self.sprite = SPRITE_PATH + "bee.png"
        self.colorkey = (255, 255, 255)
        self.scale = 0.7 * SCALE
        self.speed = 5 * SCALE
        self.rect_inflate = (-10 * SCALE, -15 * SCALE)


class Honeypot():
    def __init__(self):
        self.sprite = SPRITE_PATH + "honeypot.png"
        self.colorkey = (255, 255, 255)
        self.scale = 0.3 * SCALE
        self.speed = 3 * SCALE
        self.rect_inflate = (0 * SCALE, 0 * SCALE)
