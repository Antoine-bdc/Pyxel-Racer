from typing import List
from warnings import warn


def linspace(
    lower_bound: float,
    upper_bound: float,
    n_steps: int = 10,
) -> List[float]:
    if n_steps <= 0:
        warn("Attempt to create linspace with 0 or less steps. "
             "Returning empty list.")
        return []
    delta = abs(upper_bound - lower_bound) / n_steps
    return [delta * i for i in range(0, n_steps)]


def distance(
    x1: float,
    y1: float,
    x2: float,
    y2: float,
) -> float:
    return ((x1 - x2)**2 + (y1 - y2)**2)**(1 / 2)
