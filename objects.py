import pyxel
from math import pi, cos, sin
from util import distance


class Player:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.rotation = 0
        self.rotation_speed = 0
        self.com = None

    def update(self) -> None:
        self.rotation += self.rotation_speed
        self.x += self.vx
        self.y += self.vy

        speed = distance(0, 0, self.vx, self.vy)
        self.rotation_speed *= 0.85
        self.vx *= 1 - (speed / 300)
        self.vy *= 1 - (speed / 300)

        if pyxel.btn(pyxel.KEY_RIGHT):
            # print(0.002 / (speed + 0.001))
            self.rotation_speed = 0.09 + min(0.05, 3e-2 / (speed + 0.001))
        elif pyxel.btn(pyxel.KEY_LEFT):
            self.rotation_speed = - 0.09 - min(0.05, 3e-2 / (speed + 0.001))
        if pyxel.btn(pyxel.KEY_UP):
            self.vx += 0.2 * cos(self.rotation)
            self.vy += 0.2 * sin(self.rotation)
        if pyxel.btn(pyxel.KEY_DOWN):
            self.vx *= 0.95
            self.vy *= 0.95
        self.rotation = self.rotation % (2 * pi)
        self.compute_vertices()

    def draw(self) -> None:
        # pyxel.pset(self.x, self.y, 8)
        # pyxel.pset(*self.com, 11)
        pyxel.text(10, 10, f"{round(distance(0, 0, self.vx, self.vy), 2)}", 7)
        pyxel.text(10, 20, f"{round(self.rotation_speed, 2)}", 7)
        pyxel.trib(*self.vertices, 7)

    def compute_vertices(self) -> None:
        x1 = self.x + 8 * cos(self.rotation)
        y1 = self.y + 8 * sin(self.rotation)
        x2 = self.x + 5.4 * cos(self.rotation + (3 - 0.7) * pi / 3)
        y2 = self.y + 5.4 * sin(self.rotation + (3 - 0.7) * pi / 3)
        x3 = self.x + 5.4 * cos(self.rotation + (3 + 0.7) * pi / 3)
        y3 = self.y + 5.4 * sin(self.rotation + (3 + 0.7) * pi / 3)
        self.com = ((x1 + x2 + x3) / 3, (y1 + y2 + y3) / 3)
        self.vertices = (x1, y1, x2, y2, x3, y3)
