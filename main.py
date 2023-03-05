import pyxel
from objects import Player
from math import sin, cos, pi
from util import distance


WIDTH = 700
HEIGHT = 400
MAX_PARTICLES = 200


def add_particle(particles, particle):
    particles.insert(0, particle)
    if len(particles) > MAX_PARTICLES:
        particles.pop(MAX_PARTICLES)
    return particles


class App:
    def __init__(self) -> None:
        pyxel.init(WIDTH, HEIGHT, fps=60)
        self.player = Player(WIDTH // 16, HEIGHT // 2)
        self.particles = []
        pyxel.run(self.update, self.draw)

    def update(self) -> None:
        self.player.update()
        self.player.x = self.player.x % WIDTH
        self.player.y = self.player.y % HEIGHT

        vx = self.player.vx
        vy = self.player.vy
        if abs(self.player.rotation_speed ** 0.5 * distance(0, 0, vx, vy)) > 1.75:
            x1 = self.player.x + 5.4 * cos(self.player.rotation + (3 - 0.7) * pi / 3)
            y1 = self.player.y + 5.4 * sin(self.player.rotation + (3 - 0.7) * pi / 3)

            x2 = self.player.x + 5.4 * cos(self.player.rotation + (3 + 0.7) * pi / 3)
            y2 = self.player.y + 5.4 * sin(self.player.rotation + (3 + 0.7) * pi / 3)

            self.particles = add_particle(self.particles, (x1, y1))
            self.particles = add_particle(self.particles, (x2, y2))

    def draw(self) -> None:
        pyxel.cls(0)
        for i in range(0, len(self.particles) - 2, 2):
            p1, p2 = self.particles[i], self.particles[i + 2]
            p3, p4 = self.particles[i + 1], self.particles[i + 3]
            # pyxel.pset(p, 13)
            if distance(*p1, *p2) < 10:
                pyxel.line(*p1, *p2, 13)
            if distance(*p3, *p4) < 10:
                pyxel.line(*p3, *p4, 13)
        pyxel.circb(WIDTH * 1 / 5, 2.5 * HEIGHT / 5, 15, 7)
        pyxel.circb(WIDTH * 2 / 5, 2.5 * HEIGHT / 5, 15, 7)
        pyxel.circb(WIDTH * 3 / 5, 2.5 * HEIGHT / 5, 15, 7)
        pyxel.circb(WIDTH * 4 / 5, 2.5 * HEIGHT / 5, 15, 7)
        self.player.draw()


if __name__ == "__main__":
    App()
