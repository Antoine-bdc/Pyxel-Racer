from math import pi
from random import random
from util import linspace
from warnings import warn
from math import cos, sin
from typing import List, Tuple


def randomify(
    original_value: float,
    maximum_delta: float,
    desired_delta: float
) -> float:
    return original_value + (random() - 1 / 2) * maximum_delta * desired_delta


class Polygon:
    def __init__(
        self,
        n_sides: int,
        radius: float,
        excentricity: float = 0,
        irregularity: float = 0,
        additionnal_angle: float = 0,
    ) -> None:

        if n_sides < 3:
            warn("Attempt to create a polygon with 2 or less sides. "
                 "Defaulting to 3 sides.")
            n_sides = 3

        angles = linspace(0, 2 * pi, n_sides)
        delta_angle = 2 * pi / n_sides
        self.n_sides = n_sides
        self.angles = []
        self.radii = []
        for i in range(n_sides):
            self.radii.append(randomify(radius, radius, excentricity))
            new_angle = randomify(angles[i], delta_angle, irregularity)
            self.angles.append(new_angle % (2 * pi))

    def cartesian_coor(self) -> List[Tuple[float]]:
        cartesian_coor = []
        for i in range(self.n_sides):
            x = self.radii[i] * cos(self.angles[i])
            y = self.radii[i] * sin(self.angles[i])
            cartesian_coor.append((x, y))
        return cartesian_coor
