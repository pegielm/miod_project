class Bee():
    def __init__(self):
        self.sprite = "../sprites/bee.png"
        self.colorkey = (255, 255, 255)
        self.scale = 0.7
        self.speed = 5
        self.rect_inflate = (-10, -15)


class Ground():
    def __init__(self):
        self.sprite = "../sprites/tlo.png"
        self.colorkey = (255, 255, 255)
        self.scale = 1
        self.speed = 0
        self.rect_inflate = (0, 0)
